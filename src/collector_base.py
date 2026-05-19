"""모든 수집기가 따르는 공통 출력 스키마.

각 수집기 모듈은 `collect() -> list[CollectorResult]` 함수를 노출한다.
이 표준화 덕분에 run.py와 aggregator는 소스 종류와 무관하게 동작한다
(새로운 수집기 추가 시 aggregator 코드 수정 불필요).
"""
from datetime import datetime, timezone
from typing import TypedDict


class CollectorItem(TypedDict, total=False):
    ticker: str   # 티커 심볼 (대문자)
    count: int    # 멘션/언급 수치 — 소스마다 의미가 다를 수 있음 (Phase 3에서 정규화)
    extra: dict   # 소스별 부가 정보 (upvotes, sentiment, rank 등). 옵셔널.


class CollectorResult(TypedDict):
    source: str               # 식별자. 예: "apewisdom:all-stocks", "stocktwits:trending"
    items: list[CollectorItem]
    fetched_at: str           # ISO 8601 UTC 타임스탬프


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
