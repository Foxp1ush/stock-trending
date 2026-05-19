"""티커 추출/검증 유틸.

두 가지 모드를 지원한다:
  1) 텍스트 모드: 자유 텍스트(Stocktwits 게시글 본문 등)에서 `$TICKER` 패턴 추출
  2) 검증 모드: 이미 추출된 티커 목록을 화이트리스트/블랙리스트로 거름

화이트리스트는 scripts/build_whitelist.py 로 생성된 data/valid_tickers.csv,
블랙리스트는 data/blacklist.txt (한 줄당 하나).
"""
import csv
import re
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TICKER_REGEX = re.compile(r"\$([A-Z]{1,5})\b")


def load_whitelist() -> set[str]:
    csv_path = _DATA_DIR / "valid_tickers.csv"
    if not csv_path.exists():
        raise FileNotFoundError(
            f"화이트리스트 없음: {csv_path}\n"
            f"먼저 'python -m scripts.build_whitelist' 를 실행해 생성하세요."
        )
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return {row["symbol"].upper() for row in reader if row.get("symbol")}


def load_blacklist() -> set[str]:
    blk_path = _DATA_DIR / "blacklist.txt"
    if not blk_path.exists():
        return set()
    return {
        line.strip().upper()
        for line in blk_path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    }


def extract_from_text(text: str) -> list[str]:
    """텍스트에서 $TICKER 패턴을 등장 순서대로 추출 (검증 전 raw 후보)."""
    return [m.group(1).upper() for m in TICKER_REGEX.finditer(text)]


def is_valid_ticker(ticker: str, whitelist: set[str], blacklist: set[str]) -> bool:
    ticker = ticker.upper()
    return ticker in whitelist and ticker not in blacklist


def filter_tickers(
    tickers: list[str], whitelist: set[str], blacklist: set[str]
) -> list[str]:
    """등장 순서를 유지하며 유효한 티커만 남김."""
    return [t for t in tickers if is_valid_ticker(t, whitelist, blacklist)]
