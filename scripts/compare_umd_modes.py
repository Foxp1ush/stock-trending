"""UMD 절대값 vs raw 모드로 Mania Index Top K 비교.

한 번의 회귀로 두 모드 점수를 모두 계산해 순위 변동을 시각화.
캐시(yfinance + Kenneth French)가 이미 있으면 거의 즉시 결과 출력.

실행 (프로젝트 루트에서):
  python -m scripts.compare_umd_modes
  python -m scripts.compare_umd_modes 50 20
"""

from __future__ import annotations

import sys
from pathlib import Path

# 단독 스크립트로 실행될 때를 대비해 프로젝트 루트를 sys.path에 추가
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pandas as pd

from src.ff5.mania_index import (
    DEFAULT_POOL_SIZE,
    DEFAULT_TOP_K,
    compute_mania_scores,
    run_six_factor,
)
from src.ff5.weekly_selector import select_top_tickers


def main(argv: list[str]) -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    pool_size = int(argv[1]) if len(argv) > 1 else DEFAULT_POOL_SIZE
    top_k = int(argv[2]) if len(argv) > 2 else DEFAULT_TOP_K

    print(f"=== UMD Mode Comparison (pool={pool_size}, top_k={top_k}) ===\n")

    pool = select_top_tickers(top_k=pool_size)
    if pool.empty:
        print("No trending tickers found.")
        sys.exit(1)
    tickers = pool["ticker"].tolist()

    print(f"[1/3] Running 6-factor regressions on {len(tickers)} tickers (cache hits will be fast) ...")
    results = []
    for tk in tickers:
        r = run_six_factor(tk)
        flag = "OK  " if r.status == "ok" else "SKIP"
        print(f"  [{flag}] {tk}")
        results.append(r)
    n_ok = sum(1 for r in results if r.status == "ok")
    print(f"  -> {n_ok} OK, {len(results) - n_ok} skipped\n")

    print("[2/3] Scoring with |UMD| (absolute, current default) ...")
    scored_abs = compute_mania_scores(results, use_abs_umd=True)
    abs_index = scored_abs.set_index("ticker")
    abs_ranks = {tk: i + 1 for i, tk in enumerate(scored_abs["ticker"])}

    print("[3/3] Scoring with raw UMD (positive only counts) ...")
    scored_raw = compute_mania_scores(results, use_abs_umd=False)
    raw_index = scored_raw.set_index("ticker")
    raw_ranks = {tk: i + 1 for i, tk in enumerate(scored_raw["ticker"])}

    top_abs_set = set(scored_abs.head(top_k)["ticker"])
    top_raw_set = set(scored_raw.head(top_k)["ticker"])
    union_top = top_abs_set | top_raw_set

    rows = []
    for tk in union_top:
        umd_beta = abs_index.loc[tk, "umd_beta"]
        rows.append({
            "ticker": tk,
            "umd_beta": round(float(umd_beta), 3),
            "abs_rank": abs_ranks[tk],
            "raw_rank": raw_ranks[tk],
            "abs_score": round(float(abs_index.loc[tk, "mania_score"]), 2),
            "raw_score": round(float(raw_index.loc[tk, "mania_score"]), 2),
            "in_abs_top": "Y" if tk in top_abs_set else "-",
            "in_raw_top": "Y" if tk in top_raw_set else "-",
        })
    cmp = pd.DataFrame(rows)
    cmp["delta_rank"] = cmp["raw_rank"] - cmp["abs_rank"]
    cmp["delta_score"] = (cmp["raw_score"] - cmp["abs_score"]).round(2)
    cmp = cmp.sort_values("abs_rank").reset_index(drop=True)

    print(f"\n=== Side-by-side comparison (union of two Top {top_k}s, sorted by abs rank) ===")
    print(cmp.to_string(index=False))

    only_in_abs = sorted(top_abs_set - top_raw_set)
    only_in_raw = sorted(top_raw_set - top_abs_set)
    stable      = sorted(top_abs_set & top_raw_set)

    print(f"\n=== Top {top_k} membership delta ===")
    print(f"In |UMD| top but NOT in raw top ({len(only_in_abs)}):  {only_in_abs}")
    print(f"In raw top but NOT in |UMD| top ({len(only_in_raw)}):  {only_in_raw}")
    print(f"Stable in both ({len(stable)}):  {stable}")

    # 가장 큰 변동 종목 강조
    biggest_drops = cmp.nlargest(5, "delta_rank")
    biggest_gains = cmp.nsmallest(5, "delta_rank")
    print("\n=== Biggest rank movers (raw vs |UMD|) ===")
    print("Top 5 DROPS in raw mode (rank ↑ means worse):")
    print(biggest_drops[["ticker", "umd_beta", "abs_rank", "raw_rank", "delta_rank"]].to_string(index=False))
    print("\nTop 5 GAINS in raw mode (rank ↓ means better):")
    print(biggest_gains[["ticker", "umd_beta", "abs_rank", "raw_rank", "delta_rank"]].to_string(index=False))


if __name__ == "__main__":
    main(sys.argv)
