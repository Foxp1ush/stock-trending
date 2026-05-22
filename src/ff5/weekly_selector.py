"""주간 Top K 트렌딩 티커 선정.

지난 N일(기본 7일) ApeWisdom all-stocks raw CSV를 누적해
mentions 합산 Top K(기본 10)를 반환.

필터링:
- ApeWisdom all-stocks 소스 행만 사용 (서브레딧별 중복 합산 회피)
- valid_tickers.csv 화이트리스트 통과
- is_etf == 'Y' 제외 (개별 종목 FF5 회귀가 목적이라 ETF는 의미 작음)
"""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / "raw"
WHITELIST_PATH = ROOT / "data" / "valid_tickers.csv"

DEFAULT_LOOKBACK_DAYS = 7
DEFAULT_TOP_K = 10
DEFAULT_SOURCE = "apewisdom:all-stocks"


def _load_whitelist_non_etf() -> set[str]:
    """valid_tickers.csv에서 is_etf == 'N' 인 symbol만 set으로 반환."""
    if not WHITELIST_PATH.exists():
        return set()
    df = pd.read_csv(WHITELIST_PATH, dtype={"symbol": str, "is_etf": str})
    df = df[df["is_etf"].str.upper() == "N"]
    return set(df["symbol"].str.upper())


def _load_recent_raw(end_date: date, lookback_days: int) -> pd.DataFrame:
    """end_date 포함 직전 lookback_days 일의 raw CSV를 모두 읽어 concat."""
    dfs: list[pd.DataFrame] = []
    for delta in range(lookback_days):
        d = end_date - timedelta(days=delta)
        path = RAW_DIR / f"{d.isoformat()}.csv"
        if path.exists():
            dfs.append(pd.read_csv(path))
    if not dfs:
        return pd.DataFrame()
    return pd.concat(dfs, ignore_index=True)


def select_top_tickers(
    end_date: date | None = None,
    lookback_days: int = DEFAULT_LOOKBACK_DAYS,
    top_k: int = DEFAULT_TOP_K,
    source: str = DEFAULT_SOURCE,
) -> pd.DataFrame:
    """주간 Top K 티커를 mentions 합산 기준으로 반환.

    반환 컬럼: ticker, total_mentions, days_present
    데이터 없으면 빈 DataFrame.
    """
    end_date = end_date or date.today()
    df = _load_recent_raw(end_date, lookback_days)
    if df.empty:
        return pd.DataFrame(columns=["ticker", "total_mentions", "days_present"])

    df = df[df["source"] == source].copy()
    df = df.dropna(subset=["mentions"])
    df["ticker"] = df["ticker"].astype(str).str.upper()
    df["mentions"] = pd.to_numeric(df["mentions"], errors="coerce").fillna(0).astype(int)

    whitelist = _load_whitelist_non_etf()
    if whitelist:
        df = df[df["ticker"].isin(whitelist)]

    if df.empty:
        return pd.DataFrame(columns=["ticker", "total_mentions", "days_present"])

    agg = (
        df.groupby("ticker", as_index=False)
        .agg(total_mentions=("mentions", "sum"), days_present=("date", "nunique"))
        .sort_values("total_mentions", ascending=False)
        .head(top_k)
        .reset_index(drop=True)
    )
    return agg


if __name__ == "__main__":
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    df = select_top_tickers()
    if df.empty:
        print("No raw data found for the recent 7-day window.")
        sys.exit(0)
    print(
        f"=== Weekly Top {len(df)} Trending Tickers "
        f"(last 7 days, ApeWisdom all-stocks, non-ETF) ==="
    )
    for i, row in df.iterrows():
        print(
            f"  {i+1:2d}. {row['ticker']:6s}  "
            f"mentions={int(row['total_mentions']):6d}  "
            f"days={int(row['days_present'])}"
        )
