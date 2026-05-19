# stock-trending-bot

Reddit + Stocktwits 인기 종목 Top 10 집계 → 매일 X(Twitter) 자동 포스팅 봇.

> 현재 Phase 1 (환경 셋업) 완료. 본격적인 README는 Phase B-3에서 작성 예정.

## 로컬 실행 (개발 중)

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
python run.py
```

## 구조

- `src/` — 수집기/추출기/집계기/포스터 모듈
- `data/` — 화이트리스트, 블랙리스트, 일별 결과 스냅샷
- `tests/` — 단위 테스트
- `run.py` — 전체 파이프라인 진입점
