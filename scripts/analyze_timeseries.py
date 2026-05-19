"""시계열 분석 예시 — '최근 N일 vs 그 이전 N일'의 mentions 변동 폭 Top.

data/raw/*.csv 전체를 pandas로 로드해 source/ticker 기준 그룹핑 후,
최근 윈도 vs 이전 윈도의 평균 mentions 차이가 큰 종목을 출력한다.
누적이 짧을 땐 친절한 안내. ApeWisdom 소스만 mentions 값이 있으므로
기본 분석 대상은 'apewisdom:all-stocks'.

실행:
    python -m scripts.analyze_timeseries
    python -m scripts.analyze_timeseries --days 7
    python -m scripts.analyze_timeseries --source apewisdom:wallstreetbets
"""
import argparse
import sys
from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="시계열 mentions 변동 분석")
    parser.add_argument("--days", type=int, default=7, help="비교 윈도 크기(일) (기본 7)")
    parser.add_argument("--top", type=int, default=5, help="출력 Top N (기본 5)")
    parser.add_argument(
        "--source",
        default="apewisdom:all-stocks",
        help="분석 대상 소스 (기본: apewisdom:all-stocks)",
    )
    args = parser.parse_args()

    csv_files = sorted(RAW_DIR.glob("*.csv"))
    if not csv_files:
        print(f"⚠️  {RAW_DIR}에 CSV 없음. 먼저 `python run.py` 를 실행하세요.")
        return

    df = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)
    df["date"] = pd.to_datetime(df["date"])

    print(f"=== 시계열 분석 ({len(csv_files)}일치 데이터) ===")
    print(f"기간: {df['date'].min().date()} ~ {df['date'].max().date()}")
    print(f"분석 소스: {args.source}\n")

    df_src = df[df["source"] == args.source].copy()
    if df_src.empty:
        print(f"⚠️  source='{args.source}' 데이터 없음.")
        print("사용 가능한 source 목록:")
        for s in sorted(df["source"].unique()):
            print(f"  - {s}")
        return

    unique_days = df_src["date"].nunique()
    if unique_days < 2:
        print(
            f"⚠️  데이터가 {unique_days}일치라 시계열 변동 분석 불가.\n"
            f"   최소 2일치 누적 후 다시 실행하세요. "
            f"(매일 한 번 `python run.py` 하면 됨)"
        )
        return

    # 윈도 크기를 데이터 양에 맞춰 자동 축소
    window_days = max(1, min(args.days, unique_days // 2))
    latest = df_src["date"].max()
    recent_start = latest - pd.Timedelta(days=window_days - 1)
    past_end = recent_start - pd.Timedelta(days=1)
    past_start = past_end - pd.Timedelta(days=window_days - 1)

    recent = df_src[df_src["date"] >= recent_start]
    past = df_src[(df_src["date"] >= past_start) & (df_src["date"] <= past_end)]

    print(
        f"비교: 최근 {window_days}일 ({recent_start.date()} ~ {latest.date()}) "
        f"vs 이전 {window_days}일 ({past_start.date()} ~ {past_end.date()})\n"
    )

    if past.empty:
        print("⚠️  비교용 '이전 윈도' 데이터가 비어있음. 단일 윈도 평균만 출력:\n")
        avg = (
            recent.groupby("ticker")["mentions"]
            .mean()
            .dropna()
            .sort_values(ascending=False)
            .head(args.top)
        )
        print(avg.to_string())
        return

    recent_avg = recent.groupby("ticker")["mentions"].mean()
    past_avg = past.groupby("ticker")["mentions"].mean()
    delta = (recent_avg - past_avg).dropna()

    if delta.empty:
        print("⚠️  두 윈도에 공통 출현 종목 없음.")
        return

    print(f"📈 mentions 증가 Top {args.top}")
    for ticker, change in delta.sort_values(ascending=False).head(args.top).items():
        prev = past_avg.get(ticker, 0)
        cur = recent_avg[ticker]
        print(f"  {ticker:6s}  Δ {change:+9.1f}   ({prev:.0f}  →  {cur:.0f})")

    print(f"\n📉 mentions 감소 Top {args.top}")
    for ticker, change in delta.sort_values().head(args.top).items():
        prev = past_avg.get(ticker, 0)
        cur = recent_avg[ticker]
        print(f"  {ticker:6s}  Δ {change:+9.1f}   ({prev:.0f}  →  {cur:.0f})")


if __name__ == "__main__":
    main()
