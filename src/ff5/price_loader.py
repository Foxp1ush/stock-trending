"""yfinance에서 종목 일별 가격 다운로드 + parquet 캐시.

캐시 정책: 마지막 데이터 날짜가 오늘 이전이면 풀 재다운로드.
2년치는 약 500행에 불과해 증분 다운로드 대비 단순함을 우선.
Close는 auto_adjust=True 로 배당·분할 조정된 값.
"""

from __future__ import annotations

import time
from datetime import date
from pathlib import Path

import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = ROOT / "data" / "prices"

DEFAULT_PERIOD_YEARS = 2
RETRY_COUNT = 3
RETRY_SLEEP_SEC = 1.0


def _cache_path(ticker: str) -> Path:
    return CACHE_DIR / f"{ticker.upper()}.parquet"


def _is_cache_current(path: Path) -> bool:
    """캐시의 마지막 데이터 날짜가 오늘 이상이면 True."""
    if not path.exists():
        return False
    df = pd.read_parquet(path)
    if df.empty:
        return False
    last_date = df.index.max().date()
    return last_date >= date.today()


def _download_history(ticker: str, years: int) -> pd.DataFrame:
    """yfinance 일별 가격 다운로드. 빈 응답 / 네트워크 에러 시 3회 재시도."""
    period = f"{years}y"
    last_err: Exception | None = None
    for attempt in range(RETRY_COUNT):
        try:
            df = yf.Ticker(ticker).history(period=period, auto_adjust=True)
            if df.empty:
                raise ValueError(f"yfinance returned empty data for {ticker}")
            return df
        except Exception as exc:
            last_err = exc
            if attempt < RETRY_COUNT - 1:
                time.sleep(RETRY_SLEEP_SEC)
    raise RuntimeError(
        f"Failed to download {ticker} after {RETRY_COUNT} retries: {last_err}"
    )


def load_prices(
    ticker: str,
    years: int = DEFAULT_PERIOD_YEARS,
    force_refresh: bool = False,
) -> pd.DataFrame:
    """종목 일별 가격 DataFrame 반환.

    Close 컬럼은 배당·분할 조정된 가격. 인덱스는 timezone-naive DatetimeIndex.
    캐시 마지막 날짜가 오늘 이상이면 재사용, 아니면 풀 재다운로드.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = _cache_path(ticker)

    if not force_refresh and _is_cache_current(path):
        return pd.read_parquet(path)

    df = _download_history(ticker, years)
    if df.index.tz is not None:
        df.index = df.index.tz_localize(None)
    df.index.name = "Date"
    df.to_parquet(path)
    return df


if __name__ == "__main__":
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    sample = sys.argv[1].upper() if len(sys.argv) > 1 else "NVDA"
    df = load_prices(sample)
    print(f"[{sample}] 가격 로드 완료: {len(df)}행")
    print(f"기간: {df.index.min().date()} ~ {df.index.max().date()}")
    print(f"컬럼: {list(df.columns)}")
    print(f"캐시 경로: {_cache_path(sample)}")
    print("\n최근 5거래일 Close:")
    print(df[["Close"]].tail())
