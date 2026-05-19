"""Stocktwits 공개 trending 엔드포인트에서 인기 종목 수집.

Stocktwits는 멘션 카운트를 직접 노출하지 않으므로, trending 순위를
인버스 랭크(1위가 가장 큰 값)로 변환해 'count'로 사용한다.
Phase 3.5에서 정확도 부족하다고 판단되면 종목별 메시지 스트림 호출로 보강.

Endpoint: GET https://api.stocktwits.com/api/2/trending/symbols.json
"""

import requests

from src.collector_base import CollectorItem, CollectorResult, now_iso

API_URL = "https://api.stocktwits.com/api/2/trending/symbols.json"
USER_AGENT = "stock-trending-bot/0.1 (research)"
TIMEOUT_SEC = 10


def collect() -> list[CollectorResult]:
    """Stocktwits trending을 1회 호출해 단일 CollectorResult 리스트로 반환."""
    try:
        response = requests.get(
            API_URL,
            headers={"User-Agent": USER_AGENT},
            timeout=TIMEOUT_SEC,
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        print(f"[stocktwits] trending 실패: {exc}")
        return []

    symbols = data.get("symbols", [])
    total = len(symbols)
    items: list[CollectorItem] = []
    for rank, entry in enumerate(symbols, start=1):
        ticker = str(entry.get("symbol", "")).upper()
        if not ticker:
            continue
        items.append({
            "ticker": ticker,
            "count": total - rank + 1,   # 인버스 랭크
            "extra": {
                "name": entry.get("title"),
                "rank": rank,
                "watchlist_count": entry.get("watchlist_count"),
            },
        })

    return [{
        "source": "stocktwits:trending",
        "items": items,
        "fetched_at": now_iso(),
    }]


if __name__ == "__main__":
    import json
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    output = collect()
    print(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"\n수집된 종목 수: {sum(len(r['items']) for r in output)}")
