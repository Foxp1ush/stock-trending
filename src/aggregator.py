"""수집기들의 표준 출력을 받아 통합/소스별 Top N 산출.

설계 메모:
- count 단위가 소스마다 다를 수 있음 (ApeWisdom=실 멘션 수, Stocktwits=인버스 랭크).
  Phase 3는 단순 합산으로 가고, Phase 3.5에서 정규화/가중치 도입 여부 결정.
- 통합 Top N에는 'sources_count'(몇 개 소스에 등장했는가)를 함께 노출해
  매일 결과를 보며 "여러 커뮤니티 동시 화제" 종목을 식별할 수 있게 한다.
"""
from collections import Counter, defaultdict
from datetime import date, datetime, timezone
from typing import Iterable

from src.collector_base import CollectorResult


def aggregate(
    results: Iterable[CollectorResult],
    whitelist: set[str],
    blacklist: set[str],
    top_n: int = 10,
) -> dict:
    by_source: dict[str, list[dict]] = {}
    source_stats: dict[str, dict[str, int]] = {}
    counters: dict[str, Counter] = {}

    for result in results:
        source = result["source"]
        counter: Counter = Counter()
        raw_count = len(result["items"])
        for item in result["items"]:
            ticker = item["ticker"].upper()
            if ticker not in whitelist or ticker in blacklist:
                continue
            counter[ticker] += int(item.get("count", 0))
        counters[source] = counter
        by_source[source] = _top(counter, top_n)
        source_stats[source] = {
            "raw_items": raw_count,
            "valid_items": len(counter),
        }

    # 통합 집계
    combined_counter: Counter = Counter()
    sources_per_ticker: dict[str, set[str]] = defaultdict(set)
    for source, counter in counters.items():
        combined_counter.update(counter)
        for ticker in counter:
            sources_per_ticker[ticker].add(source)

    combined_top = _top(combined_counter, top_n, sources_per_ticker)

    return {
        "date": date.today().isoformat(),
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "combined_top10": combined_top,
        "by_source": by_source,
        "source_stats": source_stats,
    }


def _top(
    counter: Counter,
    n: int,
    sources_per_ticker: dict[str, set[str]] | None = None,
) -> list[dict]:
    # 동률 시 알파벳 순으로 결정성 확보 (테스트 안정성용)
    items = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
    out: list[dict] = []
    for ticker, count in items:
        entry: dict = {"ticker": ticker, "count": count}
        if sources_per_ticker is not None:
            entry["sources_count"] = len(sources_per_ticker[ticker])
        out.append(entry)
    return out
