# 주식 커뮤니티 인기 종목 X 자동 포스팅 봇 — 개발 로드맵 (단계적 접근)

## Context (왜 이 프로젝트인가, 왜 이 순서인가)

- **목표:** Reddit(r/wallstreetbets, r/stocks, r/pennystocks 등)과 Stocktwits에서 당일 가장 많이 언급된 주식 종목을 크롤링·집계해서, 최종적으로 매일 미국 장 마감 후(한국 시간 06:30) X에 자동 포스팅하는 봇.
- **제약:** 사용자는 비개발자, 유료 서버 사용 안 함 → **GitHub Actions 무료 티어**로 자동 실행.
- **보안:** API 키는 처음부터 **GitHub Secrets**(환경변수)로 관리. 추후 퍼블릭 저장소 공개해도 안전.
- **확정된 결정 사항(사용자 응답 기준):**
  1. 집계 방식: **통합 Top 10 + 커뮤니티별 Top 10** 둘 다 트윗
  2. 트윗 형식: **텍스트 전용** (이미지/차트 X)
  3. 포스팅 시각: **미국 장 마감 후** — UTC 21:30 = 한국 시간 06:30
  4. **개발 전략: 단계적 접근(Stage A → Stage B)** — 먼저 수집·정제 파이프라인만 완성하고 1~2주간 매일 본인 눈으로 결과를 검증하며 데이터 품질을 끌어올린 뒤, 안정화되면 X 자동 포스팅을 붙임. 이유: 정제가 덜 된 결과("$THE 142회 언급" 같은 오탐)가 본인 X 계정에 자동으로 올라가는 사고 방지 + 비개발자 학습 부담 분산.
  5. **Reddit 데이터 소스 변경 (2026 정책 대응):** 2024~2025년 Reddit API 사전 심사제 도입으로 직접 PRAW 접근은 티켓 승인 대기 중. **대기 시간 동안 ApeWisdom 무료 공개 API**(WSB/stocks/investing/Daytrading 등 11개 주식 서브레딧 30분마다 자체 집계)로 Stage A를 진행. **티켓 승인 시 `reddit_collector.py` 모듈을 추가**해 r/pennystocks 등 ApeWisdom 미커버 서브레딧 보강. 수집기를 공통 인터페이스로 추상화해 swap-in 용이하게 설계 — 이 자체가 포트폴리오 어필 포인트.

---

## 1. 전체 아키텍처

### 기술 스택 (모두 무료)

| 영역 | 선택 | Stage |
|---|---|---|
| 언어 | Python 3.11+ | A |
| **Reddit 집계 (1차)** | **ApeWisdom 공개 API + `requests`** (인증 불필요) | A |
| Reddit 직접 수집 (2차, 옵션) | `praw` — **티켓 승인 후 추가**. r/pennystocks 등 ApeWisdom 미커버 서브 보강용 | A 후반 또는 별도 |
| Stocktwits 수집 | `requests` + 공개 `trending` 엔드포인트 | A |
| **수집기 인터페이스** | 각 수집기는 `collect() -> dict` 동일 시그니처 | A |
| 종목 추출 | 정규식 `\$[A-Z]{1,5}` (Stocktwits 텍스트용) + ApeWisdom은 티커 직접 제공 | A |
| 티커 검증 | 화이트리스트 CSV (NASDAQ + NYSE) | A |
| 집계 | `collections.Counter` (표준 라이브러리) | A |
| 집계 결과 저장 | JSON 파일 (`data/runs/YYYY-MM-DD.json`) | A |
| **Raw 시계열 저장** | **일별 CSV (`data/raw/YYYY-MM-DD.csv`)** — 정제 전 API 응답 평탄화 | A |
| 시계열 분석 헬퍼 | `scripts/analyze_timeseries.py` + `pandas` | A |
| 수동 검증 | 매일 콘솔 출력 확인 + 메모 | A |
| X 포스팅 | `tweepy` v4+ (X API v2) | B |
| 자동 실행 | GitHub Actions (cron) | B |
| 비밀 키 관리 | `.env` (로컬) → GitHub Secrets (Actions) | A부터 패턴 확립 |

### Stage A 데이터 흐름 (수집·정제 완성)

```
[로컬에서 매일 수동 실행 또는 Actions 수동 트리거]
        ↓
   ┌────────────────────┬──────────────────┬─ (선택) ──────────────┐
   │ ApeWisdom 집계 API │ Stocktwits 수집   │ Reddit 직접 수집(PRAW)│
   │ (필터별 + all-stocks)│ (trending+messages)│ 티켓 승인 후 추가      │
   └─────────┬──────────┴────────┬─────────┴──────────┬───────────┘
             ↓ 동일한 collect() 시그니처로 반환            ↓
     [raw CSV 평탄화 저장 → data/raw/YYYY-MM-DD.csv]   ← Phase 3.6 (시계열 보존)
             ↓
     [티커 정규화 + 화이트리스트 + 블랙리스트 필터링]
             ↓
     [Counter 집계: 통합 + 소스별 Top 10]
             ↓
     [콘솔 출력 + JSON 스냅샷 저장]
             ↓
     [사용자 육안 검증 → 정제 로직 반복 개선]
             ↓
     [시계열 누적 후 scripts/analyze_timeseries.py 로 트렌드 확인]
```

### Stage B 추가 흐름 (자동 포스팅 연결)

```
... (Stage A 결과) ...
          ↓
     [트윗 본문 생성 (텍스트, 스레드)]
          ↓
     [X API로 트윗 게시 (tweepy)]
          ↓
     [실행 로그 → Actions UI에 기록]
```

---

## 2. 단계별 마일스톤

각 Phase 끝에 **다음 단계용 클로드 질문 템플릿**을 명시. 비개발자가 복붙해 그대로 의뢰 가능.

---

## ━━━ Stage A: 데이터 파이프라인 (1~2주) ━━━

### Phase 0 — 계정/환경 (Stage A에 필요한 최소한만)

이 단계는 사용자 본인만 가능한 행정 작업.

1. **GitHub 계정** → github.com
2. **Reddit 공식 API 티켓** — 이미 신청 완료, 승인 대기 중. **Stage A를 막지 않음.** 승인은 백그라운드로 기다리고, 도착하면 Phase 2.5(아래)에서 PRAW 추가.
3. **ApeWisdom** — 인증 불필요. 회원가입 불필요. 즉시 사용 가능.
4. **Stocktwits** — trending 엔드포인트 공개 무인증, 별도 키 불필요.
5. **로컬 개발 환경**
   - Windows: Python 3.11 (설치 시 "Add to PATH" 체크) — https://www.python.org
   - VS Code — https://code.visualstudio.com
   - Git for Windows — https://git-scm.com/download/win
6. **X 개발자 계정**은 Stage B 시작 시점에 신청 — 승인 대기 며칠. Stage A 중반에 미리 신청 걸어두면 좋음.

> **클로드에게 물어볼 다음 질문:**
> "Python, VS Code, Git 설치 끝. Reddit 티켓은 대기 중이지만 ApeWisdom으로 시작하기로 했어. 다음으로 GitHub 레포지토리를 만들고 폴더 구조 + .env/.gitignore 보안 패턴까지 잡는 Phase 1을 도와줘."

---

### Phase 1 — 프로젝트 초기화 + 비밀 키 안전 패턴 (1시간)

**목표:** 폴더 구조 만들고 `.env`+`.gitignore` 패턴으로 비밀 키가 절대 깃에 올라가지 않는 구조 확립. **이 패턴은 Stage A부터 적용**해서 Stage B에서 X 키 추가 시 그대로 확장.

생성할 구조:
```
stock-trending-bot/
├── src/
│   ├── __init__.py
│   ├── collector_base.py            # 공통 인터페이스 정의 (Phase 2)
│   ├── apewisdom_collector.py       # Phase 2 (1차 Reddit 소스)
│   ├── stocktwits_collector.py      # Phase 2
│   ├── reddit_collector.py          # Phase 2.5 (티켓 승인 후)
│   ├── ticker_extractor.py          # Phase 3
│   ├── aggregator.py                # Phase 3
│   ├── tweet_formatter.py           # Phase B-1 (나중에)
│   └── x_publisher.py               # Phase B-1 (나중에)
├── data/
│   ├── valid_tickers.csv            # 화이트리스트 (Phase 3)
│   ├── blacklist.txt                # 오탐 단어 (Phase 3.5에서 점진적 추가)
│   └── runs/                        # 일별 결과 스냅샷 JSON
├── tests/
│   └── test_ticker_extractor.py
├── run.py                           # Stage A: 수집~집계~저장. Stage B에서 포스팅 추가
├── requirements.txt
├── .env.example                     # 키 이름만 (커밋 OK)
├── .env                             # 실제 키 (커밋 X)
├── .gitignore                       # .env, data/runs/, __pycache__/
└── README.md
```

`.env.example`:
```
# Stage A — ApeWisdom과 Stocktwits는 키 불필요
# (Phase 2.5에서 Reddit 티켓 승인 시 아래 키 채움)
# REDDIT_CLIENT_ID=
# REDDIT_CLIENT_SECRET=
# REDDIT_USER_AGENT=stock-trending-bot/0.1 by yourname

# Stage B (나중에 채움)
# X_API_KEY=
# X_API_SECRET=
# X_ACCESS_TOKEN=
# X_ACCESS_TOKEN_SECRET=
```

`requirements.txt` (Stage A):
```
requests==2.31.0
python-dotenv==1.0.0
```
(`praw`는 Phase 2.5에서, `tweepy`는 Stage B에서 추가)

> **클로드에게 물어볼 다음 질문:**
> "폴더 구조랑 .gitignore까지 만들었어. Phase 2 — Reddit과 Stocktwits에서 데이터를 가져오는 두 수집기 모듈을 작성해줘. PRAW 사용법과 Stocktwits trending 엔드포인트 호출 코드 단계별로."

---

### Phase 2 — 데이터 수집기 (2~3시간)

**목표:** ApeWisdom + Stocktwits에서 티커별 멘션 카운트를 표준화된 형식으로 수집.

- **`collector_base.py`** — 공통 인터페이스(클래스 또는 함수 시그니처):
  ```python
  # 각 수집기는 다음 형식을 반환
  {
    "source": "apewisdom:all-stocks",   # 또는 "stocktwits:trending", "reddit:pennystocks"
    "items": [
      {"ticker": "TSLA", "count": 142, "extra": {"upvotes": 3210, "sentiment": 0.62}},
      ...
    ],
    "fetched_at": "2026-05-19T21:30:00Z",
  }
  ```
  - 이렇게 표준화해두면 나중에 `reddit_collector.py`, 다른 소스 추가해도 aggregator 코드 손 안 댐. **인터뷰/포트폴리오에서 "왜 이렇게 설계했나" 설명하기 좋은 부분.**

- **`apewisdom_collector.py`**
  - 엔드포인트: `https://apewisdom.io/api/v1.0/filter/{filter}/page/1`
  - 호출 필터(여러 번 호출해 소스별 분리):
    - `all-stocks` (통합 Top 10용)
    - `wallstreetbets`, `stocks`, `investing`, `Daytrading`, `Shortsqueeze` (개별)
  - 응답 `results` 배열의 `ticker`, `mentions`, `upvotes`, `sentiment`를 위 표준 형식으로 매핑
  - 호출 간 `time.sleep(0.5)` (예의상)

- **`stocktwits_collector.py`**
  - `https://api.stocktwits.com/api/2/trending/symbols.json` → trending 30개
  - Stocktwits는 자체 멘션 카운트를 안 줘서, 보강용으로 각 종목의 메시지 스트림(`/api/2/streams/symbol/{ticker}.json`)을 호출해 메시지 수를 카운트로 사용 — 또는 단순히 trending 순위 그대로 사용(더 빠름)
  - 1차 구현은 trending 순위 그대로 사용, Phase 3.5에서 필요 시 보강

**검증:** `python -m src.apewisdom_collector` 와 `python -m src.stocktwits_collector` 각각 실행해 표준 형식 dict가 출력되는지 육안 확인.

> **클로드에게 물어볼 다음 질문:**
> "수집기 두 개 모두 로컬에서 실행 성공. Phase 3 — 화이트리스트 검증, 통합 + 커뮤니티별 Top 10 집계, JSON 파일 저장까지 작성해줘. (ApeWisdom은 티커를 이미 깔끔히 주니까 정규식 추출은 Stocktwits 텍스트 보강 시점에만 필요)."

---

### Phase 2.5 — Reddit 직접 수집기 추가 (티켓 승인 후, 옵션)

**언제:** Reddit 공식 API 티켓이 승인되면. Stage A 진행을 막지 않는 별도 트랙.

**목표:** ApeWisdom이 커버 안 하는 r/pennystocks(+추가 서브)를 PRAW로 직접 수집.

- `requirements.txt`에 `praw==7.7.1` 추가
- `.env`에 Reddit 키 3종 활성화
- `reddit_collector.py`:
  - 대상: `pennystocks` (그리고 ApeWisdom 커버리지가 약한 다른 서브 자유 추가)
  - 각 서브 `hot` 상위 50 게시글 + 상위 코멘트 50 본문 수집
  - 본문 텍스트에서 정규식 `\$[A-Z]{1,5}` + 화이트리스트로 티커 추출 → 카운트
  - **반환 형식은 Phase 2의 표준 형식과 동일** → `run.py`에 한 줄 추가만으로 파이프라인 합류
- 보안: `client_id`, `client_secret`, `user_agent` 전부 환경변수에서 로드. `.env.example`에서 주석 해제 + GitHub Secrets에도 추가

> **클로드에게 물어볼 다음 질문:**
> "Reddit 티켓 승인됐어! Phase 2.5 — PRAW로 r/pennystocks를 수집하는 모듈을 기존 표준 인터페이스에 맞춰 추가해줘. .env와 GitHub Secrets에 키 추가하는 절차도."

---

### Phase 3 — 티커 정제 + 집계 + JSON 저장 (2시간)

**목표:** 수집기들의 표준 형식 출력을 검증·정제·집계해 Top 10 산출, 결과를 일자별 JSON 파일로 저장.

- `ticker_extractor.py`
  - **두 가지 모드 지원:**
    - 텍스트 모드(Stocktwits 본문 등): 정규식 `\$([A-Z]{1,5})\b` 로 후보 추출
    - 사전 추출된 티커 검증 모드(ApeWisdom 출력): 정규식 건너뛰고 검증만
  - 공통: 화이트리스트(`data/valid_tickers.csv`)에 있는 것만 통과, 블랙리스트(`data/blacklist.txt`) 제거
  - 화이트리스트는 NASDAQ Trader의 `nasdaqtraded.txt`에서 한 번 수동 다운로드 후 CSV 정리
- `aggregator.py`
  - 입력: `list[수집기_표준_dict]` (수집기 N개 출력을 그대로 받음)
  - 출력:
    ```python
    {
      "date": "2026-05-19",
      "combined_top10":  [{"ticker": "TSLA", "count": 142}, ...],
      "by_source": {
        "apewisdom:all-stocks":    [{"ticker": "TSLA", "count": 142}, ...],
        "apewisdom:wallstreetbets":[...],
        "apewisdom:stocks":        [...],
        "stocktwits:trending":     [...],
        # 티켓 승인 후 추가:
        # "reddit:pennystocks":    [...],
      },
      "source_counts": {"apewisdom:all-stocks": 100, "stocktwits:trending": 30, ...},
    }
    ```
  - 동률 시 알파벳 순 정렬로 결정성 확보
- `run.py` (Stage A 버전):
  - 수집기들을 리스트로 호출 → 정제 → 집계 → 콘솔 출력 + `data/runs/2026-05-19.json` 저장
  - 트윗 게시는 아직 없음
- `tests/test_ticker_extractor.py` — 최소 1개: `"$TSLA to the moon $LOL"` → `["TSLA"]` (LOL 블랙리스트)

> **클로드에게 물어볼 다음 질문:**
> "Phase 3까지 완성. 첫 실행 결과 JSON 보냈어. Phase 3.6 — raw API 데이터를 CSV로 별도 저장해 시계열 분석 기반 마련하고, 간단한 분석 헬퍼 스크립트도 함께 만들어줘."

---

### Phase 3.6 — Raw 데이터 시계열 저장 + 기본 분석 헬퍼 (1시간)

**왜:** 현재 `run.py`는 정제·집계 후 결과(combined_top10, by_source)만 JSON으로 저장한다. ApeWisdom의 `rank_24h_ago` / `mentions_24h_ago` 같은 필드는 매일 누적해야 "급상승 종목", "지속 화제 종목" 같은 시계열 신호로 활용 가능. 데이터 분석 친화 형식(CSV)으로 raw API 응답을 별도 보존 → Phase 3.5 정제 사이클과 추후 트윗 콘텐츠 풍부화(예: "오늘 가장 가파르게 순위 오른 종목") 양쪽에서 활용.

**구현 사항:**

- **새 모듈 `src/raw_saver.py`** — 표준 `CollectorResult` 리스트를 받아 평탄화 후 CSV로 저장.
  - 컬럼 스키마: `date, fetched_at, source, rank, ticker, name, mentions, upvotes, rank_24h_ago, mentions_24h_ago`
  - 모든 8개 소스(ApeWisdom 7 + Stocktwits 1)를 한 파일에 `source` 컬럼으로 구분
  - `rank`는 응답 순서(1-indexed)로 복원 (collector가 50개로 자른 이후 인덱스 기준)
  - Stocktwits처럼 일부 필드(mentions, upvotes, rank_24h_ago) 없는 소스는 빈 값으로 둠 — CSV에서 NaN으로 자연스럽게 처리됨
  - 저장 위치: `data/raw/YYYY-MM-DD.csv`

- **`run.py` 흐름 한 단계 추가** — 수집 직후, 정제 전에 raw 저장:
  ```
  수집 → raw_saver.save_csv(raw_results)   ← 새 단계
        → 화이트/블랙 필터 → aggregator → JSON 저장
  ```
  raw 저장이 필터링 전이라야 "필터로 잘려나간 종목도 보존"되어 추후 분석 가치 ↑.

- **새 스크립트 `scripts/analyze_timeseries.py`** — pandas 기반 분석 예시 1개:
  - `data/raw/*.csv` 전체를 glob → 단일 DataFrame
  - 출력 분석: **"지난 N일간 통합 mentions 변동 폭이 큰 종목 Top 5"** (N=7 기본, 데이터 적은 날엔 "데이터 부족" 친절 메시지)
  - 한 번 돌려보면 시계열 활용 감각이 잡히고, 데이터 누적되면 더 정교한 분석 의뢰 시 base가 됨
  - 출력은 콘솔만 (시각화는 jupyter 도입 시점에)

- **`requirements.txt` 에 `pandas==2.2.0` 추가** — 의존성 1개 늘어남(~50MB). 분석 스크립트뿐 아니라 Phase 3.5 정제 사이클에서도 ad-hoc 분석에 자주 쓸 도구라 추가 합리적.

**검증:**
1. `python run.py` → `data/raw/2026-05-19.csv` 생성, Excel에서 열어 컬럼/행 구조 확인
2. `python -m scripts.analyze_timeseries` → 단일 일자에선 "데이터 부족, 최소 2일치 필요" 메시지가 정상
3. 며칠 누적 후 같은 명령으로 Top 5 변동 종목 출력

**파일 변경 요약:**
- 추가: `src/raw_saver.py`
- 추가: `scripts/analyze_timeseries.py`
- 수정: `run.py` (raw_saver 호출 단계 추가)
- 수정: `requirements.txt` (pandas 추가)
- 자동 생성: `data/raw/YYYY-MM-DD.csv` (매 실행마다)

> **클로드에게 물어볼 다음 질문:**
> "Phase 3.6 완성, 첫 CSV 생성됐어. Phase 3.5 — 매일 결과를 보면서 정제 로직을 어떻게 개선할지, 어떤 패턴이 있을 때 어떤 필터를 추가해야 할지 가이드해줘."

> **데이터 누적 후 분석 의뢰 시 질문 템플릿:**
> "오늘로 N일치 raw CSV 모였어. analyze_timeseries.py 출력 확인 부탁하고, 추가로 봐볼 만한 패턴/분석 아이디어 있으면 제안해줘."

---

### Phase 3.5 — **매일 수동 검증 + 정제 로직 반복 개선 (1~2주, 이 프로젝트의 핵심)**

**이 단계가 단계적 접근의 가장 큰 가치.** Stage B로 넘어가기 전 데이터 품질을 끌어올림.

**일일 루틴 (하루 5~10분):**
1. 미 장 마감 후 `python run.py` 실행
2. 콘솔 Top 10 출력 + `data/runs/YYYY-MM-DD.json` 저장 확인
3. 결과를 보고 다음 질문에 답:
   - 1위 종목이 상식적으로 말이 되는가? (메이저 뉴스가 있었는지 구글 30초 검색)
   - Top 10 중 "이건 가짜 같다" 싶은 종목이 있는가? → **블랙리스트에 추가**
   - 같은 종목이 여러 표기로 분산되는가? (예: `$BRK.B` vs `$BRK`) → 정규화 규칙 추가
   - 한 게시글이 같은 티커를 10번 반복해서 순위 왜곡? → **게시글당 티커 unique 카운트로 변경**
   - 봇 글로 보이는 패턴 발견? → 작성자 차단 리스트, 또는 최소 게시글 길이 필터
4. 발견한 이슈는 `data/issues.md`에 기록 (포트폴리오 README에 "Lessons learned" 섹션으로 활용 가능)

**예상 개선 사이클 (반드시 이 순서일 필요는 없음, 실제 보이는 패턴에 따라):**

| 라운드 | 흔히 발견되는 문제 | 추가할 정제 로직 |
|---|---|---|
| 1 | `$A`, `$I`, `$BE`, `$SO`, `$ALL`, `$THE`, `$IT` 같은 일반 단어가 티커처럼 잡힘 | 블랙리스트 확장 |
| 2 | "TSLA TSLA TSLA TSLA" 같은 도배 글이 순위 왜곡 | 게시글당 unique 티커 카운트 |
| 3 | 같은 봇 작성자가 매일 동일 종목 도배 | 작성자별 가중치 캡(상위 N개 게시글만) |
| 4 | 종목명 풀텍스트("Tesla")는 잡히는데 티커 미언급으로 누락 | 회사명 → 티커 매핑 사전 추가 (TOP 200 한정) |
| 5 | 새 상장/티커 변경 반영 안 됨 | 화이트리스트 월 1회 갱신 스크립트 |
| 6 | 코멘트보다 본문 비중 너무 작음 (또는 반대) | 본문/코멘트 가중치 분리 |

**Stage B 진입 조건 (사용자가 스스로 판단):**
- 최소 7~10일 연속 실행
- 그 중 80% 이상의 날에 Top 10 결과가 "내가 X에 올려도 부끄럽지 않다"고 느낌
- 새 블랙리스트 추가가 거의 안 나오는 안정 상태

> **클로드에게 물어볼 다음 질문 (각 사이클마다):**
> "오늘 결과 JSON을 첨부해. 이 결과에서 어떤 이상한 패턴이 보이는지, 어떤 필터를 추가하면 좋을지 분석해줘. 그리고 그 필터를 ticker_extractor.py에 추가하는 코드를 알려줘."

> **Stage B 진입할 때 질문:**
> "10일간 결과가 안정적이야. 이제 Stage B 시작 — Phase B-0의 X 개발자 계정 신청 준비부터 안내해줘."

---

## ━━━ Stage B: X 자동 포스팅 + 자동화 (3~5일) ━━━

### Phase B-0 — X 개발자 계정 + 키 발급 (대기 시간 포함 1~3일)

- https://developer.x.com → Free tier 신청 (월 500 쓰기 = 일 1회 + 스레드 충분)
- 앱 생성 → **User authentication settings: Read and Write** 활성화 (이거 빼먹으면 401, 토큰 재발급 필수)
- 발급물: `API Key`, `API Secret`, `Access Token`, `Access Token Secret` → `.env`에 추가

> **클로드에게 물어볼 다음 질문:**
> "X 키 4개 다 받아서 .env에 넣었어. Phase B-1 — 트윗 포매터와 tweepy로 X에 게시하는 모듈, 그리고 DRY_RUN 플래그 작성해줘."

---

### Phase B-1 — 트윗 포매터 + X 게시 (dry-run 우선) (2시간)

- `tweet_formatter.py` 출력 예시:
  ```
  📊 Today's Top Stocks on Social (2026-05-19)

  🔥 Combined Top 10
  1. $TSLA (142)
  2. $NVDA (98)
  ...

  📱 Reddit: $GME, $AMC, $TSLA...
  💬 Stocktwits: $NVDA, $TSLA, $AAPL...
  ```
  - 280자 초과 시 스레드 2~3개로 분리
- `x_publisher.py`
  - `tweepy.Client(...)` + `create_tweet(text=..., in_reply_to_tweet_id=prev_id)`
  - **환경변수 `DRY_RUN=true`면 콘솔 print만 하고 실제 게시 안 함** — Stage A의 안전망을 Stage B에도 유지
- `run.py`에 포매터+퍼블리셔 단계 추가

**검증 순서:**
1. `DRY_RUN=true python run.py` → 콘솔 미리보기
2. `DRY_RUN=false python run.py` → 본인 X 타임라인에 첫 실제 트윗 (며칠은 수동 실행)

> **클로드에게 물어볼 다음 질문:**
> "로컬 dry-run 통과, 수동 실제 게시도 성공. Phase B-2 — GitHub Actions로 매일 UTC 21:30 자동 실행되게 설정해줘. Secrets 등록부터 워크플로우 YAML까지."

---

### Phase B-2 — GitHub Actions 자동화 (1시간)

- GitHub 레포 → Settings → Secrets and variables → Actions → 7개 키 전부 Secret으로 등록
- `.github/workflows/daily-tweet.yml`:
  ```yaml
  name: Daily Stock Trending Tweet
  on:
    schedule:
      - cron: '30 21 * * *'   # UTC 21:30
    workflow_dispatch:         # 수동 실행 버튼
  jobs:
    post:
      runs-on: ubuntu-latest
      timeout-minutes: 10
      steps:
        - uses: actions/checkout@v4
        - uses: actions/setup-python@v5
          with: { python-version: '3.11' }
        - run: pip install -r requirements.txt
        - run: python run.py
          env:
            REDDIT_CLIENT_ID: ${{ secrets.REDDIT_CLIENT_ID }}
            REDDIT_CLIENT_SECRET: ${{ secrets.REDDIT_CLIENT_SECRET }}
            REDDIT_USER_AGENT: ${{ secrets.REDDIT_USER_AGENT }}
            X_API_KEY: ${{ secrets.X_API_KEY }}
            X_API_SECRET: ${{ secrets.X_API_SECRET }}
            X_ACCESS_TOKEN: ${{ secrets.X_ACCESS_TOKEN }}
            X_ACCESS_TOKEN_SECRET: ${{ secrets.X_ACCESS_TOKEN_SECRET }}
            DRY_RUN: 'false'
  ```
- **안전한 점진 활성화:**
  1. 먼저 `DRY_RUN: 'true'`로 워크플로우 등록 → 며칠간 Actions 로그만 확인
  2. `workflow_dispatch`로 수동 트리거 1~2회 → 정상이면 `DRY_RUN: 'false'`로 변경
  3. cron 자동 실행 모니터링

> **클로드에게 물어볼 다음 질문:**
> "자동 포스팅 성공! Phase B-3 — README, 아키텍처 다이어그램, Lessons Learned(Phase 3.5의 issues.md 활용) 정리해서 포트폴리오로 다듬어줘."

---

### Phase B-3 — 포트폴리오화 (1시간)

- README 구성:
  - 프로젝트 소개 / 동기
  - 아키텍처 다이어그램 (mermaid 또는 ASCII)
  - 기술 스택 배지
  - 자동 포스팅된 트윗 스크린샷
  - **"Lessons Learned" 섹션** — Phase 3.5에서 발견한 정제 이슈와 해결 과정 정리. **이게 비개발자 포트폴리오의 가장 강력한 차별점**(단순 코드가 아닌 "데이터 품질에 대한 반복적 개선 사고" 증명)
  - 로컬 실행법 (`.env.example` 참고)
  - 라이선스 MIT
- **퍼블릭 전환 전 보안 점검:**
  - `git log -p` 에 키 문자열 grep
  - GitHub Settings → Security → Secret scanning, Push protection 활성화
  - `.env` 가 한 번이라도 커밋된 적 있다면 즉시 키 4종 전부 재발급 + `git filter-repo`

---

## 3. 비개발자가 마주칠 예상 문제점과 해결책

| 문제 | 발생 시점 | 해결책 |
|---|---|---|
| **Reddit 공식 API 사전 심사제 (2024~2025 정책)** | Phase 0 | 티켓 신청 후 ApeWisdom으로 Stage A 우선 진행. 승인 시 Phase 2.5에서 PRAW 추가 |
| **r/pennystocks가 ApeWisdom에 없음** | Phase 2 | Reddit 티켓 승인 전까지는 r/Shortsqueeze + r/SqueezePlays가 일부 저가주 화제 커버. 승인 후 Phase 2.5에서 직접 수집 |
| ApeWisdom 응답 지연/일시 다운 | Phase 2 | `try/except` + 짧은 재시도. 다운되면 그날만 Stocktwits 단독 결과로 폴백 |
| ApeWisdom 정책 변경/유료화 가능성 | 향후 | 수집기 인터페이스 추상화 덕분에 다른 서드파티(SentiSense, Quiver 등)로 swap 용이 |
| Stocktwits 429 차단 | Phase 2 | `User-Agent` 설정 + `time.sleep(1)`. 막히면 trending만 사용 |
| 가짜 티커 (`$A`, `$THE`) | Phase 3 | 화이트리스트 + 블랙리스트, **Phase 3.5에서 점진적 강화 (단계적 접근의 핵심 가치)** |
| 도배 글로 인한 순위 왜곡 | Phase 3.5 | ApeWisdom은 이미 "게시글당 1회" 카운트라 완화됨. 직접 Reddit 수집(2.5) 시엔 동일 정책 적용 |
| 종목 표기 분산 (`BRK.B` vs `BRK`) | Phase 3.5 | 정규화 규칙 추가 |
| Reddit PRAW rate limit (티켓 승인 후) | Phase 2.5 | PRAW 자동 throttle. 부족하면 서브레딧/게시글 수 축소 |
| PRAW user_agent 형식 위반 | Phase 2.5 | `platform:appname:version (by /u/yourname)` 형식 강제 |
| X Free tier 한도 (월 500 쓰기) | Phase B-1 | 일 1회 + 스레드 ≤4 → 월 ~120회로 여유 |
| X "Read and Write" 권한 미설정 | Phase B-1 | 401 발생. 권한 변경 후 Access Token **반드시 재발급** |
| GitHub Actions cron 지연 | Phase B-2 | 정시 보장 X, 5~15분 지연. 데이터 누적엔 오히려 유리 |
| 서머타임(DST) 시간 어긋남 | Phase B-2 | cron은 항상 UTC. 21:30 UTC 고정이면 EDT 시 마감 1.5h 후 / EST 시 30m 후 — 데이터 충분히 누적 |
| 로컬에선 되는데 Actions 실패 | Phase B-2 | 99%는 Secret 이름 오타. `env:` 키와 `os.environ.get()` 정확히 일치 확인 |
| 퍼블릭 공개 시 키 노출 사고 | Phase B-3 | 공개 전 `git log --all --full-history -- .env` 확인. 노출됐다면 즉시 재발급 + 히스토리 삭제 |

---

## 4. 핵심 파일 경로 요약

작업 루트: `C:\Users\kotar\Desktop\claude\주식 종목 추천\stock-trending-bot\`

**Stage A에서 생성:**
- `run.py`
- `src/collector_base.py`, `src/apewisdom_collector.py`, `src/stocktwits_collector.py`
- `src/ticker_extractor.py`, `src/aggregator.py`
- `src/raw_saver.py` (Phase 3.6)
- `scripts/analyze_timeseries.py` (Phase 3.6)
- `data/valid_tickers.csv`, `data/blacklist.txt`
- `data/runs/*.json` (집계 결과)
- `data/raw/*.csv` (raw 시계열 — Phase 3.6)
- `data/issues.md` (Phase 3.5 학습 기록, 포트폴리오용)
- `.env`, `.env.example`, `.gitignore`, `requirements.txt`

**Phase 2.5에서 추가 (Reddit 티켓 승인 시):**
- `src/reddit_collector.py`
- `requirements.txt`에 `praw` 추가
- `.env`에 Reddit 키 활성화

**Stage B에서 추가:**
- `src/tweet_formatter.py`, `src/x_publisher.py`
- `.github/workflows/daily-tweet.yml`
- README.md 본격 작성

---

## 5. 검증 (End-to-end)

**Stage A 완료 시점:**
1. `python run.py` 실행 → 콘솔 Top 10 + `data/runs/YYYY-MM-DD.json` 생성
2. 최소 7~10일치 JSON 스냅샷 누적, 본인 기준 "결과가 그럴듯하다" 충족
3. `data/issues.md` 에 발견·해결한 정제 이슈 ≥5건 기록

**Stage B 완료 시점:**
1. 로컬 `DRY_RUN=true python run.py` → 트윗 미리보기 OK
2. 로컬 `DRY_RUN=false python run.py` → 실제 X 게시 OK
3. Actions 수동 트리거(`workflow_dispatch`) 게시 OK
4. cron 자동 실행 3일 연속 성공
5. 퍼블릭 전환 후 Secret scanning 알림 0건

---

## 6. 예상 총 소요 시간

- **Stage A:** 셋업 1일 + 매일 5~10분 × 7~14일 = **1~2주**
- **Stage B:** 3~5일 (X 계정 승인 대기 포함)
- **합계: 약 2~3주**
