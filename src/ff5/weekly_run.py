"""주간 통합 진입점 — 4개 서브레딧 트랙 × (Orthodox FF5 + Mania Index).

실행: python -m src.ff5.weekly_run
출력:
  reports/weekly/YYYY-Www.md                  # 메인 대시보드
  reports/weekly/YYYY-Www-all-stocks.md       # 트랙별 아이 파일
  reports/weekly/YYYY-Www-wallstreetbets.md
  reports/weekly/YYYY-Www-pennystocks.md
  reports/weekly/YYYY-Www-Shortsqueeze.md
  reports/weekly/YYYY-Www.json                # 통합 JSON

회귀 결과는 ticker별 전역 캐시로 memoize — 같은 종목이 여러 서브레딧에 등장해도 한 번만 실행.
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from datetime import date

import pandas as pd

from src.ff5.mania_index import (
    MIN_OK_FOR_SCORING,
    ManiaResult,
    compute_mania_scores,
    run_six_factor,
)
from src.ff5.regression import FF5Result, run_single
from src.ff5.report_builder import (
    REPORTS_DIR,
    build_dashboard,
    build_subreddit_report,
)
from src.ff5.weekly_selector import DEFAULT_LOOKBACK_DAYS, select_top_tickers

TRACKS = [
    "apewisdom:all-stocks",
    "apewisdom:wallstreetbets",
    "apewisdom:pennystocks",
    "apewisdom:Shortsqueeze",
]
TOP_K_PER_TRACK = 10


def _week_id(d: date) -> str:
    iso_year, iso_week, _ = d.isocalendar()
    return f"{iso_year}-W{iso_week:02d}"


def _get_or_run_ff5(ticker: str, cache: dict[str, FF5Result]) -> FF5Result:
    if ticker not in cache:
        cache[ticker] = run_single(ticker)
    return cache[ticker]


def _get_or_run_mania(ticker: str, cache: dict[str, ManiaResult]) -> ManiaResult:
    if ticker not in cache:
        cache[ticker] = run_six_factor(ticker)
    return cache[ticker]


def _quick_tag(r: FF5Result) -> str:
    tags = []
    smb = r.betas.get("SMB", 0)
    if smb > 0.5:
        tags.append("Small")
    elif smb < -0.5:
        tags.append("Large")
    hml = r.betas.get("HML", 0)
    if hml > 0.5:
        tags.append("Value")
    elif hml < -0.5:
        tags.append("Growth")
    return "/".join(tags) if tags else "Neutral"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    today = date.today()
    week_id = _week_id(today)

    print(f"=== Weekly Multi-Track Run: {week_id} ===")
    print(f"Tracks: {TRACKS}\n")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    ff5_cache: dict[str, FF5Result] = {}
    mania_cache: dict[str, ManiaResult] = {}
    per_source_summary: dict[str, dict] = {}
    per_source_json: dict[str, dict] = {}

    for idx, source in enumerate(TRACKS, start=1):
        sub_name = source.split(":", 1)[-1]
        print(f"--- [{idx}/{len(TRACKS)}] {sub_name} ---")

        pool = select_top_tickers(top_k=TOP_K_PER_TRACK, source=source)
        if pool.empty:
            print(f"  (no data for {source} in recent lookback — skipping)\n")
            per_source_summary[source] = {
                "n_pool": 0, "n_ok": 0, "ff5_top3": [], "mania_top3": [],
            }
            per_source_json[source] = {"pool": [], "ff5": [], "mania_top": []}
            continue

        tickers = pool["ticker"].tolist()
        print(f"  Pool ({len(tickers)}): {', '.join(tickers)}")

        ff5_results: list[FF5Result] = []
        for tk in tickers:
            r = _get_or_run_ff5(tk, ff5_cache)
            flag = "OK  " if r.status == "ok" else "SKIP"
            extra = f"  R^2={r.rsquared:.3f}" if r.status == "ok" else f"  ({r.note})"
            print(f"    [FF5  {flag}] {tk:6s}{extra}")
            ff5_results.append(r)

        mania_results: list[ManiaResult] = []
        for tk in tickers:
            r = _get_or_run_mania(tk, mania_cache)
            flag = "OK  " if r.status == "ok" else "SKIP"
            print(f"    [Mani {flag}] {tk:6s}")
            mania_results.append(r)

        n_mania_ok = sum(1 for r in mania_results if r.status == "ok")
        if n_mania_ok >= MIN_OK_FOR_SCORING:
            mania_scored = compute_mania_scores(mania_results)
            mania_top = mania_scored.head(TOP_K_PER_TRACK)
        else:
            print(
                f"  ⚠ Mania scoring skipped — only {n_mania_ok} OK results "
                f"(need >= {MIN_OK_FOR_SCORING})"
            )
            mania_top = pd.DataFrame()

        selection_meta = {
            "source": source,
            "lookback_days": DEFAULT_LOOKBACK_DAYS,
            "top_k": TOP_K_PER_TRACK,
            "end_date": today.isoformat(),
        }
        report_path = REPORTS_DIR / f"{week_id}-{sub_name}.md"
        report_path.write_text(
            build_subreddit_report(source, ff5_results, mania_top, week_id, selection_meta),
            encoding="utf-8",
        )
        print(f"  → {report_path.name}\n")

        ff5_ok = [r for r in ff5_results if r.status == "ok"]
        ff5_top3 = sorted(ff5_ok, key=lambda r: -r.rsquared)[:3]
        per_source_summary[source] = {
            "n_pool": len(tickers),
            "n_ok": len(ff5_ok),
            "ff5_top3": [
                {
                    "ticker": r.ticker,
                    "rsquared": r.rsquared,
                    "mkt": r.betas["Mkt-RF"],
                    "smb": r.betas["SMB"],
                    "hml": r.betas["HML"],
                    "tag": _quick_tag(r),
                }
                for r in ff5_top3
            ],
            "mania_top3": (
                [
                    {
                        "ticker": row["ticker"],
                        "mania_score": float(row["mania_score"]),
                        "rsquared": float(row["rsquared"]),
                        "umd_beta": float(row["umd_beta"]),
                        "mean_bse": float(row["mean_bse"]),
                    }
                    for _, row in mania_top.head(3).iterrows()
                ]
                if not mania_top.empty
                else []
            ),
        }
        per_source_json[source] = {
            "pool": tickers,
            "ff5": [asdict(r) for r in ff5_results],
            "mania_top": mania_top.to_dict(orient="records") if not mania_top.empty else [],
        }

    print("--- Writing dashboard + integrated JSON ---")
    dash_path = REPORTS_DIR / f"{week_id}.md"
    dash_path.write_text(build_dashboard(per_source_summary, week_id), encoding="utf-8")
    print(f"  → {dash_path.name}")

    json_path = REPORTS_DIR / f"{week_id}.json"
    json_path.write_text(
        json.dumps(
            {
                "week_id": week_id,
                "generated_at": today.isoformat(),
                "tracks": per_source_json,
            },
            indent=2,
            ensure_ascii=False,
            default=str,
        ),
        encoding="utf-8",
    )
    print(f"  → {json_path.name}")

    print(f"\nDone. FF5 cache hits: {len(ff5_cache)} unique tickers, "
          f"Mania cache hits: {len(mania_cache)} unique tickers.")


if __name__ == "__main__":
    main()
