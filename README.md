# stock-trending-bot

[![Daily Collection](https://github.com/Foxp1ush/stock-trending/actions/workflows/daily.yml/badge.svg)](https://github.com/Foxp1ush/stock-trending/actions/workflows/daily.yml)
[![Weekly Reports](https://github.com/Foxp1ush/stock-trending/actions/workflows/weekly.yml/badge.svg)](https://github.com/Foxp1ush/stock-trending/actions/workflows/weekly.yml)
![Python](https://img.shields.io/badge/python-3.13-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> **⚙️ One-line summary** — A hands-off **data pipeline**: pulls data from public APIs → transforms & caches (parquet) → auto-generates weekly reports → runs itself on **free GitHub Actions** cron. No servers, no manual steps.
>
> **⚙️ 한 줄 요약** — 외부 API 데이터 수집 → 가공·캐싱(parquet) → 리포트 자동 생성 → **GitHub Actions 무료 cron**으로 무인 자동 실행되는 데이터 파이프라인. 서버·수작업 없음.

A self-running bot that pulls trending US stock tickers from ApeWisdom (which aggregates 11 major stock subreddits) and runs **two complementary factor analyses** every week — orthodox Fama-French 5-factor and a custom **Mania Index** — across four subreddit tracks. Reports auto-publish to this repo. Built entirely on free tiers (GitHub Actions + public data APIs).

> 🇰🇷 **한국어 요약**: 매일 미국 주식 커뮤니티(Reddit 11개 서브 통합 사이트 ApeWisdom)에서 가장 화제인 종목을 수집하고, 매주 일요일에 두 가지 분석을 자동 실행합니다. **정통 Fama-French 5팩터**로 학술적 위험-수익 프로파일을 보고, 직접 설계한 **광기 지수(Mania Index)**로 행동재무학 관점에서 "팩터로 설명 안 되는 광기 종목"을 점수화합니다. 4개 서브레딧(all-stocks / wallstreetbets / pennystocks / Shortsqueeze) 각각 별도 트랙 출력. 모든 결과는 GitHub Actions로 자동 생성·커밋되어 [`reports/weekly/`](reports/weekly/)에 누적됩니다. 단계별 개발 로드맵은 [`docs/ROADMAP.md`](docs/ROADMAP.md) (한국어).

---

## What it does

Two scheduled jobs run on free GitHub Actions:

- **Daily, 06:30 KST** — Calls ApeWisdom's free API for 7 subreddit filters, flattens the raw mention counts into a single CSV (`data/raw/YYYY-MM-DD.csv`), and auto-commits the snapshot. Builds up a time series for trend analysis.
- **Weekly, Monday 07:00 KST** — Loads the last 7 days of raw CSVs, picks the top tickers per subreddit, downloads 1–2 years of daily prices from Yahoo Finance, runs OLS regressions against Fama-French factors, and produces **both** an orthodox FF5 report and a Mania Index ranking — written as a dashboard plus per-subreddit Markdown files in [`reports/weekly/`](reports/weekly/).

The whole system is hands-off after initial setup. No paid services, no secrets required for the analysis pipeline (all data sources are unauthenticated public APIs).

---

## Two analytical lenses

The same regression machinery is intentionally read in opposite directions, producing complementary views:

| | **Orthodox FF5** | **Mania Index** |
|---|---|---|
| Question | *"What systematic risks explain this stock's returns?"* | *"How much of this stock's behavior evades factor explanation, and how strongly does it ride momentum?"* |
| Model | 5-factor OLS (Mkt-RF, SMB, HML, RMW, CMA), 2y daily | 6-factor OLS (FF5 + Carhart UMD), 1y daily |
| What's a "good" R² | Higher = clearer factor exposure | Lower = stronger mania signal |
| Score | alpha, 5 betas, t-stats, p-values, R² | Quantile rank of (1−R²) + \|UMD beta\| + mean BSE → 0–100 |
| Best use | Understand large-cap thematic exposures | Surface microcap / meme / retail-driven names |
| Output | Per-ticker breakdown with significance stars | Ranked Top 10 within each subreddit |

The two views are deliberately separated — they answer different questions and would muddle each other if mixed in one report.

---

## Architecture

```
┌─ ApeWisdom API (free, no auth, 7 subreddit filters) ─┐
│                                                       │
▼                                                       │
data/raw/YYYY-MM-DD.csv   ◄── daily.yml (06:30 KST)    │
                                                        │
┌─ weekly.yml (Mon 07:00 KST) ───────────────────────────┴────────────┐
│                                                                      │
│  weekly_selector (per source, top-N from last-7d cumulative)         │
│        │                                                             │
│        ▼                                                             │
│   ┌──── Orthodox FF5 ────────┐    ┌─── Mania Index ────────────┐    │
│   │  yfinance prices (2y)    │    │  yfinance prices (1y)      │    │
│   │  + Kenneth French FF5    │    │  + FF5 + Carhart UMD       │    │
│   │  → OLS, alpha + 5 betas  │    │  → 3 metrics → quantile    │    │
│   └────────────┬─────────────┘    └────────────┬───────────────┘    │
│                └───────────────┬────────────────┘                    │
│                                ▼                                     │
│   reports/weekly/YYYY-Www.md            (dashboard)                  │
│   reports/weekly/YYYY-Www-{source}.md   (per-subreddit, 4 files)     │
│   reports/weekly/YYYY-Www.json          (integrated machine-read)    │
│                                │                                     │
│                                └──► auto-commit + push               │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Subreddit tracks

Four parallel tracks per weekly run:

| Track | Character | Why include |
|---|---|---|
| `all-stocks` | Aggregate of 11 subreddits, large-cap-dominated | Big picture |
| `wallstreetbets` | FOMO / options / volatility | Classic retail mania |
| `pennystocks` | Microcap, often near OTC | Where FF5 breaks down — pure mania signal |
| `Shortsqueeze` | Short interest plays | Extreme tail events |

> ⚠️ Mania scores are quantile-ranked **within each track's pool** — they are NOT directly comparable across subreddits.

---

## Latest reports

The most recent set lives in [`reports/weekly/`](reports/weekly/). Open the weekly dashboard (`YYYY-Www.md`) for a summary and navigation links to the four per-subreddit detail files.

---

## Tech stack

- **Python 3.13** — modern type syntax (`list[T]`), dataclasses
- **statsmodels 0.14.6** — OLS regression with t-stats and p-values
- **yfinance 1.3.0** — daily auto-adjusted price data from Yahoo Finance
- **pandas-datareader 0.10.0** — Kenneth R. French Data Library access (FF5 + UMD)
- **pandas 2.3.0 + pyarrow 18.1.0** — parquet caching
- **GitHub Actions** — fully automated scheduling on free tier

---

## Automation schedule

Both workflows can also be triggered manually via the Actions tab (`workflow_dispatch`).

| Workflow | Cron (UTC) | KST | What it does |
|---|---|---|---|
| `daily.yml` | `30 21 * * *` | 06:30 next day | Collects ApeWisdom snapshot, commits raw CSV |
| `weekly.yml` | `0 22 * * 0` | Mon 07:00 | Runs 4 tracks × (FF5 + Mania), commits 6 report files |

Estimated monthly Actions usage: ~80 / 2000 min free tier = 4%.

---

## Local run

```bash
git clone https://github.com/Foxp1ush/stock-trending.git
cd stock-trending
python -m venv .venv
.venv\Scripts\activate         # Windows
# source .venv/bin/activate    # macOS / Linux
pip install -r requirements.txt
```

Then one of:

```bash
python run.py                       # daily collection (one-shot)
python -m src.ff5.weekly_run        # weekly multi-track reports (one-shot)
python -m src.ff5.mania_index       # Mania Index on all-stocks pool (debug view)
python scripts/compare_umd_modes.py # |UMD| vs raw UMD comparison
```

Output files land in `data/raw/`, `data/runs/`, and `reports/weekly/`.

---

## Lessons learned (technical)

A handful of non-obvious things that surfaced during development:

- **Python 3.13 removed `distutils`.** `pandas_datareader 0.10.0` still imports it. Fix: pin `setuptools<70` to keep the distutils shim alive. Caught only in CI (local Windows had the shim incidentally).
- **`yfinance 0.2.40` broke against Yahoo's 2026 API shape** — silently returned "possibly delisted" for active tickers like NVDA. Library moved past 1.0 in 2025; bumped to `yfinance==1.3.0`.
- **`statsmodels 0.14.4` ↔ `scipy 1.15` incompatibility.** scipy removed the internal `_lazywhere` helper; statsmodels 0.14.5+ patches the import. Pin: `statsmodels==0.14.6`.
- **`pyarrow 15.0.0` has no cp313 wheel** → forces source build → setuptools chain break. Move to `pyarrow==18.1.0` which ships cp313 wheels.
- **`git pull --no-rebase -X ours` resolves auto-commit conflicts.** When local-run reports collided with workflow-generated reports (same filename, different content), the strategy kept the local (newer multi-track) version automatically.

---

## Disclaimer

This project is for **research and educational use only**. The numerical outputs are statistical estimates from a finite window — they are **not investment advice**. Statistical significance does not imply economic significance. Past factor exposures do not predict future returns.

---

## License

MIT
