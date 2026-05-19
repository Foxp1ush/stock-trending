"""Entry point — 수집 → 정제 → 집계 → JSON 저장."""
import json
import sys
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()

from src import (
    aggregator,
    apewisdom_collector,
    raw_saver,
    stocktwits_collector,
    ticker_extractor,
)

ROOT = Path(__file__).resolve().parent
RUNS_DIR = ROOT / "data" / "runs"
RAW_DIR = ROOT / "data" / "raw"


def main() -> None:
    print("=== Stock Trending Bot — Daily Run ===\n")

    print("[수집] 외부 API 호출 중...")
    raw_results = apewisdom_collector.collect() + stocktwits_collector.collect()
    print(f"  → {len(raw_results)}개 소스 수집 완료\n")

    print("[Raw 저장] 시계열 분석용 CSV 평탄화 중...")
    raw_csv_path = raw_saver.save_csv(raw_results, RAW_DIR)
    print(f"  → {raw_csv_path}\n")

    print("[정제] 화이트/블랙리스트 로드 중...")
    whitelist = ticker_extractor.load_whitelist()
    blacklist = ticker_extractor.load_blacklist()
    print(f"  → 화이트리스트 {len(whitelist)}개, 블랙리스트 {len(blacklist)}개\n")

    print("[집계] 통합/소스별 Top 10 계산 중...")
    result = aggregator.aggregate(raw_results, whitelist, blacklist)

    _print_results(result)

    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RUNS_DIR / f"{date.today().isoformat()}.json"
    out_path.write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\n[저장] {out_path}")


def _print_results(result: dict) -> None:
    print("\n📊 Combined Top 10")
    for i, item in enumerate(result["combined_top10"], 1):
        print(
            f"  {i:2d}. ${item['ticker']:6s} count={item['count']:6d}  "
            f"({item['sources_count']}개 소스)"
        )

    print("\n📊 By Source (Top 5 each)")
    for source, items in result["by_source"].items():
        top5 = ", ".join(f"${i['ticker']}({i['count']})" for i in items[:5])
        print(f"  {source}")
        print(f"    {top5}")

    print("\n📈 Source Stats")
    for source, stats in result["source_stats"].items():
        print(
            f"  {source:32s} 원본 {stats['raw_items']:3d}  →  유효 {stats['valid_items']:3d}"
        )


if __name__ == "__main__":
    main()
