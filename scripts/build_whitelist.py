"""NASDAQ Trader에서 현재 상장 종목 목록을 받아 data/valid_tickers.csv 로 저장.

매월 한 번 정도 다시 실행해 신규 상장/상폐를 반영. (Phase 3.5 라운드 5 참고)

실행:
    python -m scripts.build_whitelist
"""
import csv
import re
import sys
from pathlib import Path

import requests

URL = "https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqtraded.txt"
OUT = Path(__file__).resolve().parent.parent / "data" / "valid_tickers.csv"
SYMBOL_RE = re.compile(r"^[A-Z][A-Z0-9.\-]{0,9}$")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print(f"다운로드 중: {URL}")
    response = requests.get(URL, timeout=30)
    response.raise_for_status()
    lines = response.text.splitlines()
    if not lines:
        sys.exit("응답이 비어있음")

    header = lines[0].split("|")
    print(f"헤더 컬럼: {header}")

    rows = []
    for line in lines[1:]:
        if not line or line.startswith("File Creation Time"):
            continue
        fields = line.split("|")
        if len(fields) < len(header):
            continue
        row = dict(zip(header, fields))
        if row.get("Test Issue", "").strip() == "Y":
            continue
        symbol = row.get("Symbol", "").strip().upper()
        if not SYMBOL_RE.match(symbol):
            continue
        rows.append({
            "symbol": symbol,
            "name": row.get("Security Name", "").strip(),
            "exchange": row.get("Listing Exchange", "").strip(),
            "is_etf": row.get("ETF", "").strip(),
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["symbol", "name", "exchange", "is_etf"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n저장 완료: {OUT}")
    print(f"총 {len(rows)}개 종목.")
    print(f"미리보기 (앞 5개): {[r['symbol'] for r in rows[:5]]}")


if __name__ == "__main__":
    main()
