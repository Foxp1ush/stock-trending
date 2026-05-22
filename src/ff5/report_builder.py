"""주간 FF5 리포트 빌더 (영어 Markdown + JSON).

요약 표 + 종목별 상세 + 자동 해석 코멘트 + 방법론·면책.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from src.ff5.regression import FACTOR_NAMES, FF5Result

ROOT = Path(__file__).resolve().parents[2]
REPORTS_DIR = ROOT / "reports" / "weekly"

BETA_TILT_THRESHOLD = 0.5
LOW_R2_THRESHOLD = 0.05
MODEST_R2_THRESHOLD = 0.20
ALPHA_SIGNIFICANCE_P = 0.05


def _interpret(r: FF5Result) -> str:
    """베타·R²·alpha 유의성을 자연어 태그 한 줄로 요약."""
    if r.status != "ok":
        return f"_{r.status}: {r.note}_"

    tags: list[str] = []

    smb = r.betas.get("SMB", 0)
    if smb > BETA_TILT_THRESHOLD:
        tags.append("Small-cap tilt")
    elif smb < -BETA_TILT_THRESHOLD:
        tags.append("Large-cap tilt")

    hml = r.betas.get("HML", 0)
    if hml > BETA_TILT_THRESHOLD:
        tags.append("Value tilt")
    elif hml < -BETA_TILT_THRESHOLD:
        tags.append("Growth tilt")

    rmw = r.betas.get("RMW", 0)
    if rmw > BETA_TILT_THRESHOLD:
        tags.append("Robust profitability")
    elif rmw < -BETA_TILT_THRESHOLD:
        tags.append("Weak profitability")

    cma = r.betas.get("CMA", 0)
    if cma > BETA_TILT_THRESHOLD:
        tags.append("Conservative investment")
    elif cma < -BETA_TILT_THRESHOLD:
        tags.append("Aggressive investment")

    if r.alpha_pvalue < ALPHA_SIGNIFICANCE_P:
        sign = "positive" if r.alpha_daily > 0 else "negative"
        tags.append(f"Significant {sign} alpha")

    if r.rsquared < LOW_R2_THRESHOLD:
        tags.append("Low explanatory power — likely sentiment-driven")
    elif r.rsquared < MODEST_R2_THRESHOLD:
        tags.append("Modest factor fit")

    return "; ".join(tags) if tags else "Neutral profile"


def _format_summary_table(results: list[FF5Result]) -> str:
    header = (
        "| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |\n"
        "|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|"
    )
    rows = []
    for r in results:
        if r.status != "ok":
            rows.append(
                f"| {r.ticker} | — | — | — | — | — | — | — | — | _{r.status}_ |"
            )
            continue
        rows.append(
            "| {tk} | {alpha:+.2f}% | {mkt:+.3f} | {smb:+.3f} | {hml:+.3f} "
            "| {rmw:+.3f} | {cma:+.3f} | {r2:.3f} | {n} | {note} |".format(
                tk=r.ticker,
                alpha=r.alpha_annualized * 100,
                mkt=r.betas["Mkt-RF"],
                smb=r.betas["SMB"],
                hml=r.betas["HML"],
                rmw=r.betas["RMW"],
                cma=r.betas["CMA"],
                r2=r.rsquared,
                n=r.nobs,
                note=_interpret(r),
            )
        )
    return header + "\n" + "\n".join(rows)


def _format_detail_section(r: FF5Result) -> str:
    if r.status != "ok":
        return f"### {r.ticker}\n\nStatus: `{r.status}` — {r.note}\n"

    lines = [
        f"### {r.ticker}",
        "",
        f"- Period: `{r.period_start}` to `{r.period_end}` ({r.nobs} obs)",
        f"- R² = {r.rsquared:.4f} (adjusted = {r.rsquared_adj:.4f})",
        f"- Alpha (annualized): **{r.alpha_annualized * 100:+.2f}%** "
        f"(daily = {r.alpha_daily:+.6f}, t = {r.alpha_tstat:+.2f}, p = {r.alpha_pvalue:.4f})",
        "",
        "Factor loadings:",
        "",
        "| Factor | β | t-stat | p-value |",
        "|--------|---|--------|---------|",
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
        lines.append(f"| {k} | {beta:+.4f} | {t:+.2f} | {p:.4f} {sig} |")
    lines.append("")
    lines.append(f"_Interpretation: {_interpret(r)}_")
    return "\n".join(lines)


def build_markdown(
    results: list[FF5Result],
    week_id: str,
    selection_meta: dict,
) -> str:
    today = date.today().isoformat()
    n_total = len(results)
    n_ok = sum(1 for r in results if r.status == "ok")

    sections = [
        f"# Weekly FF5 Factor Report — {week_id}",
        "",
        f"Generated: {today}",
        "",
        "## Selection",
        "",
        f"- Top {n_total} tickers by accumulated mentions on ApeWisdom "
        f"`{selection_meta.get('source', '?')}` over the last "
        f"{selection_meta.get('lookback_days', '?')} days.",
        "- Whitelisted, non-ETF only.",
        f"- Successful regressions: {n_ok} / {n_total}.",
        "",
        "## Summary",
        "",
        _format_summary_table(results),
        "",
        "## Per-ticker Detail",
        "",
    ]

    for r in results:
        sections.append(_format_detail_section(r))
        sections.append("")

    sections.extend([
        "---",
        "",
        "### Methodology",
        "",
        "- Dependent variable: stock daily excess return (R_i - RF).",
        "- Independent variables: Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA), daily.",
        "- Estimator: Ordinary Least Squares (statsmodels).",
        "- Window: up to ~2 years of overlapping daily observations.",
        "- Factor data: Kenneth R. French Data Library "
        "(F-F_Research_Data_5_Factors_2x3_daily).",
        "- Price data: Yahoo Finance via yfinance (auto-adjusted close).",
        "",
        "### Disclaimer",
        "",
        "_This report is generated for research and educational purposes only. "
        "It is not investment advice. Past performance does not predict future returns. "
        "Statistical significance does not imply economic significance._",
    ])

    return "\n".join(sections)


def build_json(
    results: list[FF5Result],
    week_id: str,
    selection_meta: dict,
) -> dict:
    return {
        "week_id": week_id,
        "generated_at": date.today().isoformat(),
        "selection": selection_meta,
        "results": [asdict(r) for r in results],
    }


def _format_mania_table(df) -> str:
    """Mania DataFrame을 Markdown 표로 포맷. df는 compute_mania_scores 출력."""
    header = (
        "| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |\n"
        "|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|"
    )
    rows = []
    for _, r in df.iterrows():
        rows.append(
            f"| {r['ticker']} | **{r['mania_score']:.2f}** | "
            f"{r['inv_rsq_score']:.2f} | {r['umd_score']:.2f} | {r['bse_score']:.2f} | "
            f"{r['rsquared']:.3f} | {r['umd_beta']:+.3f} | "
            f"{r['mean_bse']:.4f} | {r['idio_vol']:.4f} | {int(r['nobs'])} |"
        )
    return header + "\n" + "\n".join(rows)


def build_subreddit_report(
    source: str,
    ff5_results: list[FF5Result],
    mania_top,
    week_id: str,
    selection_meta: dict,
) -> str:
    """단일 서브레딧 리포트: Orthodox FF5 + Mania Index 통합 단일 .md."""
    sub_name = source.split(":", 1)[-1]
    today = date.today().isoformat()
    n_ff5 = len(ff5_results)
    n_ff5_ok = sum(1 for r in ff5_results if r.status == "ok")

    sections = [
        f"# Weekly Report — `{sub_name}` — {week_id}",
        "",
        f"Generated: {today}  ·  Source: `{source}`  ·  "
        f"Lookback: {selection_meta.get('lookback_days', '?')} days",
        "",
        f"[← Back to dashboard]({week_id}.md)",
        "",
        "## Part 1 — Orthodox FF5 Regression",
        "",
        f"Successful regressions: **{n_ff5_ok} / {n_ff5}**",
        "",
        _format_summary_table(ff5_results),
        "",
        "## Part 2 — Mania Index (within-subreddit ranking)",
        "",
    ]

    if mania_top is None or len(mania_top) == 0:
        sections.append(
            "_Insufficient successful regressions in this subreddit for Mania scoring. "
            "See Part 1 for available FF5 data._"
        )
    else:
        sections.extend([
            "Quantile rank within this subreddit's pool (0~100). "
            "Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).",
            "",
            _format_mania_table(mania_top),
        ])

    sections.extend([
        "",
        "## Per-ticker FF5 Detail",
        "",
    ])
    for r in ff5_results:
        sections.append(_format_detail_section(r))
        sections.append("")

    sections.extend([
        "---",
        "### Methodology",
        "",
        "- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). "
        "Excess return = R_i - RF.",
        "- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. "
        "Three instability metrics quantile-ranked within this subreddit pool: "
        "(1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.",
        "- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.",
        "",
        "### Disclaimer",
        "",
        "_Research and educational use only. Not investment advice. Past performance does not "
        "predict future returns._",
    ])

    return "\n".join(sections)


def build_dashboard(per_source_summary: dict, week_id: str) -> str:
    """메인 대시보드 — 각 서브레딧 Top 3 요약 표 + 아이 파일 링크."""
    today = date.today().isoformat()

    sections = [
        f"# Weekly Reports Dashboard — {week_id}",
        "",
        f"Generated: {today}",
        "",
        "Two analyses run per ApeWisdom subreddit, in parallel:",
        "",
        "- **Orthodox FF5** — Fama-French 5-factor risk decomposition (2y daily OLS).",
        "- **Mania Index** — 6-factor (FF5 + Carhart UMD) instability score: "
        "(1-R²) + |UMD beta| + mean BSE, each quantile-ranked within the subreddit's pool. "
        "Higher = more retail-mania-like.",
        "",
        "> ⚠ **Mania scores are quantile ranks within each subreddit's pool** — "
        "they are NOT directly comparable across subreddits.",
        "",
        "## Subreddit Tracks",
        "",
    ]

    for source, data in per_source_summary.items():
        sub_name = source.split(":", 1)[-1]
        link = f"{week_id}-{sub_name}.md"
        n_pool = data.get("n_pool", 0)
        n_ok = data.get("n_ok", 0)

        sections.extend([
            f"### `{sub_name}`  ·  [→ details]({link})",
            "",
            f"Pool: **{n_pool}** tickers  ·  FF5 OK: **{n_ok}**",
            "",
        ])

        ff5_top = data.get("ff5_top3", [])
        if ff5_top:
            sections.extend([
                "**FF5 — Top 3 by R²** (best explained by factors):",
                "",
                "| Ticker | R² | Mkt-RF β | SMB β | HML β | Tag |",
                "|--------|------|----------|-------|-------|-----|",
            ])
            for r in ff5_top:
                sections.append(
                    f"| {r['ticker']} | {r['rsquared']:.3f} | {r['mkt']:+.2f} | "
                    f"{r['smb']:+.2f} | {r['hml']:+.2f} | {r['tag']} |"
                )
            sections.append("")

        mania_top = data.get("mania_top3", [])
        if mania_top:
            sections.extend([
                "**Mania Index — Top 3** (most mania-like in this pool):",
                "",
                "| Ticker | Mania | R² | UMD β | mean_bse |",
                "|--------|-------|------|-------|----------|",
            ])
            for r in mania_top:
                sections.append(
                    f"| {r['ticker']} | **{r['mania_score']:.2f}** | {r['rsquared']:.3f} | "
                    f"{r['umd_beta']:+.3f} | {r['mean_bse']:.4f} |"
                )
            sections.append("")
        else:
            sections.append("_Mania scoring unavailable (insufficient OK regressions)._")
            sections.append("")

    sections.extend([
        "---",
        "### Methodology",
        "",
        "- Trending tickers from ApeWisdom (https://apewisdom.io), 7-day accumulated mentions.",
        "- Price data: yfinance (auto-adjusted close). Factor data: Kenneth R. French Data Library.",
        "- Statistical estimation: OLS via statsmodels. Whitelisted, non-ETF tickers only.",
        "",
        "_Research and educational use only. Not investment advice._",
    ])

    return "\n".join(sections)


def write_reports(
    results: list[FF5Result],
    week_id: str,
    selection_meta: dict,
) -> tuple[Path, Path]:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    md_path = REPORTS_DIR / f"{week_id}.md"
    json_path = REPORTS_DIR / f"{week_id}.json"

    md_path.write_text(
        build_markdown(results, week_id, selection_meta),
        encoding="utf-8",
    )
    json_path.write_text(
        json.dumps(
            build_json(results, week_id, selection_meta),
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return md_path, json_path
