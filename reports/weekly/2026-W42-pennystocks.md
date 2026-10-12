# Weekly Report — `pennystocks` — 2026-W42

Generated: 2026-10-12  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W42.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| ALEC | -12.60% | +1.005 | +2.061 | -0.472 | -1.171 | +0.525 | 0.148 | 367 | Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit |
| BEAT | -6.78% | +0.944 | +0.010 | +1.193 | -2.192 | -0.007 | 0.057 | 367 | Value tilt; Weak profitability; Modest factor fit |
| HTZ | +55.53% | +1.035 | +2.082 | +0.641 | +0.339 | +0.288 | 0.098 | 367 | Small-cap tilt; Value tilt; Modest factor fit |
| OLB | +35.79% | +0.650 | +1.417 | -0.333 | -0.788 | +0.587 | 0.012 | 367 | Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| WHLR | -674.59% | +1.167 | +0.031 | +0.893 | -1.457 | +0.188 | 0.022 | 367 | Value tilt; Weak profitability; Significant negative alpha; Low explanatory power — likely sentiment-driven |
| NKE | -22.78% | +1.051 | +1.030 | -0.118 | +1.043 | +0.687 | 0.335 | 367 | Small-cap tilt; Robust profitability; Conservative investment |
| NVDA | +20.50% | +1.657 | -0.834 | -1.101 | -0.299 | +1.121 | 0.664 | 367 | Large-cap tilt; Growth tilt; Conservative investment |
| ON | -12.31% | +1.812 | +0.608 | -0.027 | -0.155 | +0.978 | 0.423 | 367 | Small-cap tilt; Conservative investment |
| AAPL | +4.23% | +1.345 | -0.149 | -0.051 | +0.762 | +0.181 | 0.549 | 367 | Robust profitability |
| AVGO | +47.69% | +1.607 | -0.103 | -1.288 | +0.121 | -0.253 | 0.458 | 367 | Growth tilt |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| OLB | **86.67** | 33.33 | 20.00 | 33.33 | 0.011 | +0.039 | 5.4850 | 0.2496 | 117 |
| WHLR | **63.33** | 30.00 | 3.33 | 30.00 | 0.048 | -1.537 | 2.7930 | 0.1271 | 117 |
| ON | **60.00** | 16.67 | 26.67 | 16.67 | 0.358 | +0.423 | 0.5445 | 0.0248 | 117 |
| BEAT | **60.00** | 26.67 | 6.67 | 26.67 | 0.057 | -0.905 | 2.6764 | 0.1218 | 117 |
| ALEC | **60.00** | 20.00 | 16.67 | 23.33 | 0.164 | -0.035 | 1.2647 | 0.0575 | 117 |
| HTZ | **56.67** | 23.33 | 13.33 | 20.00 | 0.108 | -0.201 | 1.0600 | 0.0482 | 117 |
| AVGO | **50.00** | 6.67 | 30.00 | 13.33 | 0.578 | +0.539 | 0.4200 | 0.0191 | 117 |
| NVDA | **43.33** | 3.33 | 33.33 | 6.67 | 0.709 | +0.676 | 0.2753 | 0.0125 | 117 |
| AAPL | **40.00** | 13.33 | 23.33 | 3.33 | 0.360 | +0.080 | 0.2364 | 0.0108 | 117 |
| NKE | **30.00** | 10.00 | 10.00 | 10.00 | 0.428 | -0.527 | 0.3544 | 0.0161 | 117 |

## Per-ticker FF5 Detail

### ALEC

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.1478 (adjusted = 0.1360)
- Alpha (annualized): **-12.60%** (daily = -0.000500, t = -0.16, p = 0.8732)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0052 | +3.10 | 0.0021 ** |
| SMB | +2.0611 | +3.61 | 0.0003 *** |
| HML | -0.4716 | -0.93 | 0.3534  |
| RMW | -1.1708 | -1.89 | 0.0590  |
| CMA | +0.5251 | +0.79 | 0.4303  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit_

### BEAT

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.0566 (adjusted = 0.0436)
- Alpha (annualized): **-6.78%** (daily = -0.000269, t = -0.06, p = 0.9485)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9441 | +2.19 | 0.0293 * |
| SMB | +0.0102 | +0.01 | 0.9892  |
| HML | +1.1932 | +1.77 | 0.0780  |
| RMW | -2.1922 | -2.67 | 0.0080 ** |
| CMA | -0.0072 | -0.01 | 0.9935  |

_Interpretation: Value tilt; Weak profitability; Modest factor fit_

### HTZ

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.0985 (adjusted = 0.0860)
- Alpha (annualized): **+55.53%** (daily = +0.002204, t = +0.69, p = 0.4897)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0353 | +3.14 | 0.0019 ** |
| SMB | +2.0815 | +3.58 | 0.0004 *** |
| HML | +0.6405 | +1.24 | 0.2159  |
| RMW | +0.3386 | +0.54 | 0.5909  |
| CMA | +0.2878 | +0.43 | 0.6710  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### OLB

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.0121 (adjusted = -0.0016)
- Alpha (annualized): **+35.79%** (daily = +0.001420, t = +0.18, p = 0.8585)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6499 | +0.79 | 0.4313  |
| SMB | +1.4169 | +0.98 | 0.3294  |
| HML | -0.3333 | -0.26 | 0.7964  |
| RMW | -0.7883 | -0.50 | 0.6164  |
| CMA | +0.5874 | +0.35 | 0.7286  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### WHLR

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.0223 (adjusted = 0.0088)
- Alpha (annualized): **-674.59%** (daily = -0.026769, t = -4.31, p = 0.0000)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1673 | +1.82 | 0.0702  |
| SMB | +0.0310 | +0.03 | 0.9781  |
| HML | +0.8930 | +0.89 | 0.3753  |
| RMW | -1.4573 | -1.19 | 0.2350  |
| CMA | +0.1880 | +0.14 | 0.8867  |

_Interpretation: Value tilt; Weak profitability; Significant negative alpha; Low explanatory power — likely sentiment-driven_

### NKE

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.3347 (adjusted = 0.3255)
- Alpha (annualized): **-22.78%** (daily = -0.000904, t = -0.88, p = 0.3773)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0512 | +9.92 | 0.0000 *** |
| SMB | +1.0300 | +5.53 | 0.0000 *** |
| HML | -0.1179 | -0.71 | 0.4775  |
| RMW | +1.0429 | +5.16 | 0.0000 *** |
| CMA | +0.6867 | +3.16 | 0.0017 ** |

_Interpretation: Small-cap tilt; Robust profitability; Conservative investment_

### NVDA

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.6639 (adjusted = 0.6593)
- Alpha (annualized): **+20.50%** (daily = +0.000813, t = +0.92, p = 0.3592)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6566 | +18.05 | 0.0000 *** |
| SMB | -0.8343 | -5.17 | 0.0000 *** |
| HML | -1.1007 | -7.66 | 0.0000 *** |
| RMW | -0.2993 | -1.71 | 0.0880  |
| CMA | +1.1209 | +5.95 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### ON

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.4235 (adjusted = 0.4155)
- Alpha (annualized): **-12.31%** (daily = -0.000489, t = -0.35, p = 0.7258)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.8123 | +12.57 | 0.0000 *** |
| SMB | +0.6082 | +2.40 | 0.0170 * |
| HML | -0.0271 | -0.12 | 0.9047  |
| RMW | -0.1548 | -0.56 | 0.5737  |
| CMA | +0.9780 | +3.31 | 0.0010 ** |

_Interpretation: Small-cap tilt; Conservative investment_

### AAPL

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.5490 (adjusted = 0.5427)
- Alpha (annualized): **+4.23%** (daily = +0.000168, t = +0.26, p = 0.7985)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3448 | +19.75 | 0.0000 *** |
| SMB | -0.1489 | -1.24 | 0.2144  |
| HML | -0.0505 | -0.47 | 0.6356  |
| RMW | +0.7623 | +5.87 | 0.0000 *** |
| CMA | +0.1809 | +1.30 | 0.1958  |

_Interpretation: Robust profitability_

### AVGO

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.4576 (adjusted = 0.4500)
- Alpha (annualized): **+47.69%** (daily = +0.001893, t = +1.43, p = 0.1549)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6067 | +11.68 | 0.0000 *** |
| SMB | -0.1031 | -0.43 | 0.6704  |
| HML | -1.2876 | -5.98 | 0.0000 *** |
| RMW | +0.1211 | +0.46 | 0.6446  |
| CMA | -0.2527 | -0.90 | 0.3710  |

_Interpretation: Growth tilt_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._