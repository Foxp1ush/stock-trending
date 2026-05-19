"""ApeWisdom 공개 API에서 주식 멘션 카운트 수집.

ApeWisdom은 r/wallstreetbets, r/stocks 등 11개 주식 서브레딧을 30분마다
크롤링해 멘션 카운트를 집계한다. 인증 불필요, 무료.

Endpoint: GET https://apewisdom.io/api/v1.0/filter/{filter}/page/1
필터별로 호출해 소스별 분리된 결과를 반환한다 (통합용 'all-stocks' 포함).
"""
import time

import requests

from src.collector_base import CollectorItem, CollectorResult, now_iso

API_BASE = "https://apewisdom.io/api/v1.0/filter"
FILTERS = [
    "all-stocks",
    "wallstreetbets",
    "stocks",
    "investing",
    "Daytrading",
    "Shortsqueeze",
    "pennystocks",
]
USER_AGENT = "stock-trending-bot/0.1 (research)"
REQUEST_DELAY_SEC = 0.5
TIMEOUT_SEC = 10
TOP_N_PER_FILTER = 50  # 응답은 100개까지 오지만 상위 50개만 보관


def _fetch_filter(filter_name: str) -> CollectorResult:
    url = f"{API_BASE}/{filter_name}/page/1"
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT_SEC)
    response.raise_for_status()
    data = response.json()

    items: list[CollectorItem] = []
    for entry in data.get("results", [])[:TOP_N_PER_FILTER]:
        items.append({
            "ticker": str(entry["ticker"]).upper(),
            "count": int(entry["mentions"]),
            "extra": {
                "name": entry.get("name"),
                "upvotes": int(entry.get("upvotes", 0) or 0),
                "rank_24h_ago": entry.get("rank_24h_ago"),
                "mentions_24h_ago": entry.get("mentions_24h_ago"),
            },
        })

    return {
        "source": f"apewisdom:{filter_name}",
        "items": items,
        "fetched_at": now_iso(),
    }


def collect() -> list[CollectorResult]:
    """모든 필터를 순차 호출해 필터별 CollectorResult 리스트로 반환.

    개별 필터 실패는 무시(스킵)하고 나머지를 계속 진행한다.
    """
    results: list[CollectorResult] = []
    for filter_name in FILTERS:
        try:
            results.append(_fetch_filter(filter_name))
        except requests.RequestException as exc:
            print(f"[apewisdom] {filter_name} 실패: {exc}")
        time.sleep(REQUEST_DELAY_SEC)
    return results


if __name__ == "__main__":
    import json
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    output = collect()
    print(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"\n총 {len(output)}개 필터, {sum(len(r['items']) for r in output)}개 종목 항목.")
