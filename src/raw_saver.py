"""정제 전 API raw 데이터를 일별 CSV로 평탄화 저장 — 시계열 분석용.

표준 CollectorResult 리스트를 받아 한 파일로 컬럼화한다. 컬럼 스키마:
  date, fetched_at, source, rank, ticker, name, mentions, upvotes,
  rank_24h_ago, mentions_24h_ago

소스마다 일부 필드가 없을 수 있음 (예: Stocktwits는 mentions 미제공).
빈 값은 CSV에서 빈 셀로 저장되며 pandas 로드 시 NaN으로 처리되어 분석에 자연스럽다.

화이트/블랙리스트 필터링 *이전* 시점에 저장해야 잘려나간 종목까지 보존된다.
"""
import csv
from datetime import date as _date
from pathlib import Path
from typing import Iterable

from src.collector_base import CollectorResult

CSV_COLUMNS = [
    "date",
    "fetched_at",
    "source",
    "rank",
    "ticker",
    "name",
    "mentions",
    "upvotes",
    "rank_24h_ago",
    "mentions_24h_ago",
]


def _flatten(results: Iterable[CollectorResult]) -> list[dict]:
    today = _date.today().isoformat()
    rows: list[dict] = []
    for result in results:
        source = result["source"]
        fetched_at = result["fetched_at"]
        is_apewisdom = source.startswith("apewisdom:")
        for rank, item in enumerate(result["items"], start=1):
            extra = item.get("extra", {}) or {}
            rows.append({
                "date": today,
                "fetched_at": fetched_at,
                "source": source,
                "rank": rank,
                "ticker": item.get("ticker"),
                "name": extra.get("name"),
                # ApeWisdom: count == 실제 mentions. Stocktwits: count == 인버스랭크
                # 이므로 mentions 의미가 아니라 빈 값으로 둔다(rank 컬럼으로 충분).
                "mentions": item.get("count") if is_apewisdom else None,
                "upvotes": extra.get("upvotes"),
                "rank_24h_ago": extra.get("rank_24h_ago"),
                "mentions_24h_ago": extra.get("mentions_24h_ago"),
            })
    return rows


def save_csv(results: Iterable[CollectorResult], out_dir: Path) -> Path:
    """results 를 out_dir/YYYY-MM-DD.csv 에 저장 후 경로 반환.

    같은 날 재실행 시 덮어쓴다 (가장 최신 호출 결과 보존).
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{_date.today().isoformat()}.csv"
    rows = _flatten(results)
    with out_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return out_path
