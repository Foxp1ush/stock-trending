"""주간 FF5 리포트 생성 통합 진입점.

실행: python -m src.ff5.weekly_run
파이프라인:
  weekly_selector.select_top_tickers()
  → regression.run_single() per ticker
  → report_builder.write_reports()
  → reports/weekly/YYYY-Www.md + .json
"""

from __future__ import annotations

import sys
from datetime import date

from src.ff5.regression import run_single
from src.ff5.report_builder import write_reports
from src.ff5.weekly_selector import (
    DEFAULT_LOOKBACK_DAYS,
    DEFAULT_SOURCE,
    DEFAULT_TOP_K,
    select_top_tickers,
)


def _week_id(d: date) -> str:
    """ISO 주차 형식: YYYY-Www (예: 2026-W21)."""
    iso_year, iso_week, _ = d.isocalendar()
    return f"{iso_year}-W{iso_week:02d}"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    today = date.today()
    week_id = _week_id(today)

    print(f"=== Weekly FF5 Run: {week_id} ===\n")

    print("[1/3] Selecting top tickers ...")
    top = select_top_tickers()
    if top.empty:
        print("No trending tickers found — aborting.")
        sys.exit(1)
    tickers = top["ticker"].tolist()
    print(f"  -> {len(tickers)} tickers: {', '.join(tickers)}\n")

    print(f"[2/3] Running FF5 regressions ({len(tickers)} tickers) ...")
    results = []
    for tk in tickers:
        r = run_single(tk)
        flag = "OK  " if r.status == "ok" else "SKIP"
        extra = f"  R^2={r.rsquared:.3f}" if r.status == "ok" else f"  ({r.note})"
        print(f"  [{flag}] {tk:6s}{extra}")
        results.append(r)
    print()

    print("[3/3] Writing report files ...")
    selection_meta = {
        "source": DEFAULT_SOURCE,
        "lookback_days": DEFAULT_LOOKBACK_DAYS,
        "top_k": DEFAULT_TOP_K,
        "end_date": today.isoformat(),
    }
    md_path, json_path = write_reports(results, week_id, selection_meta)
    print(f"  -> Markdown: {md_path}")
    print(f"  -> JSON    : {json_path}")
    print("\nDone.")


if __name__ == "__main__":
    main()
