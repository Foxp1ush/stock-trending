"""Kenneth French Data Library에서 FF5 일별 팩터 다운로드 + parquet 캐시.

데이터셋: F-F_Research_Data_5_Factors_2x3_daily
컬럼: Mkt-RF, SMB, HML, RMW, CMA, RF  (모두 일별 수익률, 원본은 % 단위 → /100 환산 적용)
캐시: data/ff5/F-F_5_Factors_daily.parquet (mtime 기준 7일 룰)
"""

from __future__ import annotations

import time
from pathlib import Path

import pandas as pd
from pandas_datareader import data as pdr

ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = ROOT / "data" / "ff5"
CACHE_PATH = CACHE_DIR / "F-F_5_Factors_daily.parquet"

DATASET_ID = "F-F_Research_Data_5_Factors_2x3_daily"
UMD_DATASET_ID = "F-F_Momentum_Factor_daily"
UMD_CACHE_PATH = CACHE_DIR / "F-F_Momentum_daily.parquet"
CACHE_TTL_DAYS = 7


def _is_cache_fresh(path: Path, ttl_days: int) -> bool:
    if not path.exists():
        return False
    age_sec = time.time() - path.stat().st_mtime
    return age_sec < ttl_days * 86400


def _download_factors() -> pd.DataFrame:
    """pandas_datareader로 FF5 일별 팩터를 다운로드해 비율 단위 DataFrame 반환."""
    # start 미지정 시 기본값이 약 5년 전 → 풀 히스토리(1963년 7월부터) 확보 위해 명시
    result = pdr.DataReader(DATASET_ID, "famafrench", start="1900-01-01")
    # famafrench 반환 형식: {0: DataFrame(daily), 'DESCR': str}
    df = result[0].copy()
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index.astype(str))
    df.index.name = "Date"
    # 원본은 % 단위 → 비율로 환산 (회귀 전 필수)
    return df / 100.0


def load_ff5_daily(force_refresh: bool = False) -> pd.DataFrame:
    """FF5 일별 팩터 DataFrame 반환.

    캐시 파일이 7일 이내면 재사용, 아니면 재다운로드 후 캐시 갱신.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    if not force_refresh and _is_cache_fresh(CACHE_PATH, CACHE_TTL_DAYS):
        return pd.read_parquet(CACHE_PATH)

    df = _download_factors()
    df.to_parquet(CACHE_PATH)
    return df


def _download_momentum() -> pd.DataFrame:
    """Carhart Momentum(UMD) 일별 팩터 다운로드. 비율 단위 환산."""
    result = pdr.DataReader(UMD_DATASET_ID, "famafrench", start="1900-01-01")
    df = result[0].copy()
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index.astype(str))
    df.index.name = "Date"
    # Kenneth French 데이터셋이 컬럼명에 공백을 포함하는 경우가 있어 정리
    df.columns = [c.strip() for c in df.columns]
    return df / 100.0


def load_momentum_daily(force_refresh: bool = False) -> pd.DataFrame:
    """Carhart UMD 일별 팩터 DataFrame 반환. 컬럼: 'Mom' (또는 'UMD'). 7일 캐시."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    if not force_refresh and _is_cache_fresh(UMD_CACHE_PATH, CACHE_TTL_DAYS):
        return pd.read_parquet(UMD_CACHE_PATH)

    df = _download_momentum()
    df.to_parquet(UMD_CACHE_PATH)
    return df


def load_ff5_plus_umd_daily(force_refresh: bool = False) -> pd.DataFrame:
    """FF5 + UMD inner-join. 컬럼: Mkt-RF, SMB, HML, RMW, CMA, Mom, RF (7개)."""
    ff5 = load_ff5_daily(force_refresh=force_refresh)
    umd = load_momentum_daily(force_refresh=force_refresh)
    # 'Mom' 컬럼 1개만 추가 (RF는 FF5에 이미 있어 중복 회피)
    mom_col = "Mom" if "Mom" in umd.columns else umd.columns[0]
    return ff5.join(umd[[mom_col]].rename(columns={mom_col: "Mom"}), how="inner")


if __name__ == "__main__":
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    df = load_ff5_daily()
    print(f"FF5 일별 팩터 로드 완료: {len(df):,}행")
    print(f"기간: {df.index.min().date()} ~ {df.index.max().date()}")
    print(f"컬럼: {list(df.columns)}")
    print(f"캐시 경로: {CACHE_PATH}")
    print("\n최근 5거래일 샘플 (비율 단위):")
    print(df.tail())

    print("\n--- 6 팩터 통합 (FF5 + UMD) ---")
    df6 = load_ff5_plus_umd_daily()
    print(f"6 팩터 로드 완료: {len(df6):,}행, 컬럼: {list(df6.columns)}")
    print(f"기간: {df6.index.min().date()} ~ {df6.index.max().date()}")
    print("\n최근 5거래일 샘플:")
    print(df6.tail())
