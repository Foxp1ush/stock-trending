"""Mania Index — 6 팩터 OLS 회귀의 '통계적 불안정성'을 광기 시그널로 정량화.

정통 FF5(weekly_run.py)와 정반대 관점:
  - 정통: 팩터로 설명되는 부분 → 학술적 risk-return 해석
  - Mania: 팩터로 설명 안 되는 부분 + 모멘텀 추종성 → 신생 테마주·밈주식 포착

점수 3지표 (각 풀 내 quantile rank, 가중합 100점):
  1. (1 - R²)       : 팩터로 설명 안 되는 분산 비율
  2. |UMD beta|     : 모멘텀 추종성 (방향 무관)
  3. mean bse       : 5팩터 베타의 평균 표준오차 (계수 불안정성)
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

import pandas as pd
import statsmodels.api as sm

from src.ff5.factor_loader import load_ff5_plus_umd_daily
from src.ff5.price_loader import load_prices
from src.ff5.weekly_selector import DEFAULT_SOURCE, select_top_tickers

MIN_OBS_FOR_REGRESSION = 60
DEFAULT_POOL_SIZE = 50
DEFAULT_TOP_K = 20
DEFAULT_WINDOW_DAYS = 252
MIN_OK_FOR_SCORING = 5

FF5_FACTOR_COLS = ["Mkt-RF", "SMB", "HML", "RMW", "CMA"]
SIX_FACTOR_COLS = FF5_FACTOR_COLS + ["Mom"]


@dataclass
class ManiaResult:
    ticker: str
    status: str               # 'ok' | 'price_unavailable' | 'insufficient_data'
    note: str
    nobs: int
    rsquared: float
    idio_vol: float           # 참고용 (점수에서 제외)
    umd_beta: float           # raw — 방향 식별용
    umd_beta_abs: float       # 점수 계산용
    mean_bse: float           # 5팩터 베타의 평균 표준오차


def _empty(ticker: str, status: str, note: str) -> ManiaResult:
    nan = float("nan")
    return ManiaResult(
        ticker=ticker, status=status, note=note,
        nobs=0, rsquared=nan, idio_vol=nan,
        umd_beta=nan, umd_beta_abs=nan, mean_bse=nan,
    )


def run_six_factor(
    ticker: str,
    window_days: int = DEFAULT_WINDOW_DAYS,
) -> ManiaResult:
    """1년 일별 6팩터 OLS. 광기 지표 3종 추출."""
    ticker = ticker.upper()

    try:
        prices = load_prices(ticker, years=1)
    except Exception as exc:
        return _empty(ticker, "price_unavailable", str(exc))

    if prices.empty or len(prices) < MIN_OBS_FOR_REGRESSION:
        return _empty(
            ticker, "insufficient_data",
            f"price history only {len(prices)} days",
        )

    returns = prices["Close"].pct_change().dropna()
    returns.name = "Ri"

    factors = load_ff5_plus_umd_daily()
    df = pd.concat([returns, factors], axis=1, join="inner").dropna()
    df = df.iloc[-window_days:]

    if len(df) < MIN_OBS_FOR_REGRESSION:
        return _empty(
            ticker, "insufficient_data",
            f"only {len(df)} overlapping days after factor join",
        )

    y = df["Ri"] - df["RF"]
    X = sm.add_constant(df[SIX_FACTOR_COLS])
    model = sm.OLS(y, X).fit()

    umd_beta = float(model.params["Mom"])
    bse_5factors = [float(model.bse[k]) for k in FF5_FACTOR_COLS]
    mean_bse = sum(bse_5factors) / len(bse_5factors)

    return ManiaResult(
        ticker=ticker,
        status="ok",
        note="",
        nobs=int(model.nobs),
        rsquared=float(model.rsquared),
        idio_vol=float(model.resid.std()),
        umd_beta=umd_beta,
        umd_beta_abs=abs(umd_beta),
        mean_bse=mean_bse,
    )


def compute_mania_scores(
    results: list[ManiaResult],
    weights: tuple[float, float, float] = (1.0, 1.0, 1.0),
    use_abs_umd: bool = False,
) -> pd.DataFrame:
    """status=='ok'만 모아 quantile rank 후 가중합 mania_score 산출.

    weights = (w_invR², w_UMD, w_bse). 기본 균등. 합계 100점.
    use_abs_umd=False: UMD raw 값 사용 (양수만 광기 = FOMO 광기 해석, 기본값)
    use_abs_umd=True : |UMD| 절대값 사용 (방향 무관 모멘텀 강도, 패닉 셀링도 포함)
    """
    ok = [r for r in results if r.status == "ok"]
    if len(ok) < MIN_OK_FOR_SCORING:
        raise RuntimeError(
            f"Too few successful regressions ({len(ok)}) — need >= {MIN_OK_FOR_SCORING}."
        )

    df = pd.DataFrame([asdict(r) for r in ok])
    df["inv_rsq"] = 1.0 - df["rsquared"]

    umd_col = "umd_beta_abs" if use_abs_umd else "umd_beta"

    w_sum = sum(weights)
    scale = 100.0 / w_sum  # 합계가 100점이 되도록 정규화

    df["inv_rsq_score"] = df["inv_rsq"].rank(pct=True) * weights[0] * scale
    df["umd_score"]     = df[umd_col].rank(pct=True) * weights[1] * scale
    df["bse_score"]     = df["mean_bse"].rank(pct=True) * weights[2] * scale
    df["mania_score"]   = (
        df["inv_rsq_score"] + df["umd_score"] + df["bse_score"]
    )

    return df.sort_values("mania_score", ascending=False).reset_index(drop=True)


def select_top_mania(
    pool_size: int = DEFAULT_POOL_SIZE,
    top_k: int = DEFAULT_TOP_K,
    weights: tuple[float, float, float] = (1.0, 1.0, 1.0),
    use_abs_umd: bool = False,
    source: str = DEFAULT_SOURCE,
) -> pd.DataFrame:
    """ApeWisdom Top pool_size → 6팩터 회귀 → mania 점수 → Top K DataFrame.

    source: 'apewisdom:all-stocks' (기본) 또는 'apewisdom:wallstreetbets',
            'apewisdom:pennystocks', 'apewisdom:Shortsqueeze' 등 서브레딧별 호출 가능.
    """
    pool = select_top_tickers(top_k=pool_size, source=source)
    if pool.empty:
        raise RuntimeError(f"No trending tickers found for source={source}.")

    tickers = pool["ticker"].tolist()
    print(f"[1/2] Running 6-factor regressions on {len(tickers)} tickers ({source}) ...")
    results: list[ManiaResult] = []
    for tk in tickers:
        r = run_six_factor(tk)
        flag = "OK  " if r.status == "ok" else "SKIP"
        extra = (
            f"  R^2={r.rsquared:.3f}  |UMD|={r.umd_beta_abs:.3f}  bse={r.mean_bse:.4f}"
            if r.status == "ok"
            else f"  ({r.note})"
        )
        print(f"  [{flag}] {tk:6s}{extra}")
        results.append(r)

    print("\n[2/2] Computing mania scores (quantile rank) ...")
    scored = compute_mania_scores(results, weights=weights, use_abs_umd=use_abs_umd)
    return scored.head(top_k)


def main(argv: list[str]) -> None:
    pool = int(argv[1]) if len(argv) > 1 else DEFAULT_POOL_SIZE
    topk = int(argv[2]) if len(argv) > 2 else DEFAULT_TOP_K

    print(f"=== Mania Index Run (pool={pool}, top_k={topk}) ===\n")
    df = select_top_mania(pool_size=pool, top_k=topk)

    print(f"\n=== Top {len(df)} by Mania Index Score ===")
    cols_show = [
        "ticker", "mania_score", "inv_rsq_score", "umd_score", "bse_score",
        "rsquared", "umd_beta", "mean_bse", "idio_vol", "nobs",
    ]
    show = df[cols_show].copy()
    show["mania_score"]   = show["mania_score"].round(2)
    show["inv_rsq_score"] = show["inv_rsq_score"].round(2)
    show["umd_score"]     = show["umd_score"].round(2)
    show["bse_score"]     = show["bse_score"].round(2)
    show["rsquared"]      = show["rsquared"].round(3)
    show["umd_beta"]      = show["umd_beta"].round(3)
    show["mean_bse"]      = show["mean_bse"].round(4)
    show["idio_vol"]      = show["idio_vol"].round(4)
    print(show.to_string(index=False))


if __name__ == "__main__":
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    main(sys.argv)
