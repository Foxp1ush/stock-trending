"""단일 티커에 대한 Fama-French 5-Factor OLS 회귀.

종속변수: 종목 일별 초과수익률 (R_i - RF)
독립변수: Mkt-RF, SMB, HML, RMW, CMA  (모두 비율 단위, factor_loader가 환산 완료)
출력: alpha + 5 베타 + t-stat + p-value + R²
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
import statsmodels.api as sm

from src.ff5.factor_loader import load_ff5_daily
from src.ff5.price_loader import load_prices

MIN_OBS_FOR_REGRESSION = 60       # 60거래일(약 3개월) 미만이면 회귀 스킵
TRADING_DAYS_PER_YEAR = 252

FACTOR_NAMES = ["Mkt-RF", "SMB", "HML", "RMW", "CMA"]


@dataclass
class FF5Result:
    ticker: str
    status: str                       # 'ok' | 'insufficient_data' | 'price_unavailable'
    note: str
    nobs: int
    period_start: str
    period_end: str
    alpha_daily: float
    alpha_annualized: float
    alpha_tstat: float
    alpha_pvalue: float
    betas: dict[str, float]
    beta_tstats: dict[str, float]
    beta_pvalues: dict[str, float]
    rsquared: float
    rsquared_adj: float


def _empty(ticker: str, status: str, note: str) -> FF5Result:
    nan = float("nan")
    return FF5Result(
        ticker=ticker, status=status, note=note,
        nobs=0, period_start="", period_end="",
        alpha_daily=nan, alpha_annualized=nan, alpha_tstat=nan, alpha_pvalue=nan,
        betas={}, beta_tstats={}, beta_pvalues={},
        rsquared=nan, rsquared_adj=nan,
    )


def run_single(ticker: str) -> FF5Result:
    """단일 티커에 대한 FF5 회귀 결과 반환. 데이터 부족이면 status로 신호."""
    ticker = ticker.upper()

    try:
        prices = load_prices(ticker)
    except Exception as exc:
        return _empty(ticker, "price_unavailable", str(exc))

    if prices.empty or len(prices) < MIN_OBS_FOR_REGRESSION:
        return _empty(
            ticker,
            "insufficient_data",
            f"price history only {len(prices)} days",
        )

    returns = prices["Close"].pct_change().dropna()
    returns.name = "Ri"

    factors = load_ff5_daily()
    df = pd.concat([returns, factors], axis=1, join="inner").dropna()

    if len(df) < MIN_OBS_FOR_REGRESSION:
        return _empty(
            ticker,
            "insufficient_data",
            f"only {len(df)} overlapping days after factor join",
        )

    y = df["Ri"] - df["RF"]
    X = sm.add_constant(df[FACTOR_NAMES])
    model = sm.OLS(y, X).fit()

    return FF5Result(
        ticker=ticker,
        status="ok",
        note="",
        nobs=int(model.nobs),
        period_start=str(df.index.min().date()),
        period_end=str(df.index.max().date()),
        alpha_daily=float(model.params["const"]),
        alpha_annualized=float(model.params["const"] * TRADING_DAYS_PER_YEAR),
        alpha_tstat=float(model.tvalues["const"]),
        alpha_pvalue=float(model.pvalues["const"]),
        betas={k: float(model.params[k]) for k in FACTOR_NAMES},
        beta_tstats={k: float(model.tvalues[k]) for k in FACTOR_NAMES},
        beta_pvalues={k: float(model.pvalues[k]) for k in FACTOR_NAMES},
        rsquared=float(model.rsquared),
        rsquared_adj=float(model.rsquared_adj),
    )


def format_result(r: FF5Result) -> str:
    """콘솔 출력용 사람-가독 포맷."""
    if r.status != "ok":
        return f"[{r.ticker}] status={r.status} — {r.note}"

    lines = [
        f"=== FF5 Regression: {r.ticker} ===",
        f"Period: {r.period_start} ~ {r.period_end}  (N obs = {r.nobs})",
        f"R^2 = {r.rsquared:.4f}   (adjusted = {r.rsquared_adj:.4f})",
        "",
        f"Alpha (daily)      : {r.alpha_daily:+.6f}",
        f"Alpha (annualized) : {r.alpha_annualized * 100:+.2f}%",
        f"   t-stat = {r.alpha_tstat:+.2f}   p-value = {r.alpha_pvalue:.4f}",
        "",
        "Factor loadings:",
    ]
    for k in FACTOR_NAMES:
        beta = r.betas[k]
        t = r.beta_tstats[k]
        p = r.beta_pvalues[k]
        if p < 0.001:
            sig = "***"
        elif p < 0.01:
            sig = "**"
        elif p < 0.05:
            sig = "*"
        else:
            sig = ""
        lines.append(
            f"   {k:7s}  beta = {beta:+.4f}   t = {t:+6.2f}   p = {p:.4f}  {sig}"
        )
    lines.append("")
    lines.append("Significance: * p<0.05, ** p<0.01, *** p<0.001")
    return "\n".join(lines)


if __name__ == "__main__":
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    sample = sys.argv[1] if len(sys.argv) > 1 else "NVDA"
    result = run_single(sample)
    print(format_result(result))
