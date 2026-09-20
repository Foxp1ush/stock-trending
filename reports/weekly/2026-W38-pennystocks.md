# Weekly Report — `pennystocks` — 2026-W38

Generated: 2026-09-20  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W38.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| CTNT | +30.39% | +0.594 | +1.419 | -0.759 | +0.369 | +0.547 | 0.016 | 382 | Small-cap tilt; Growth tilt; Conservative investment; Low explanatory power — likely sentiment-driven |
| CMG | -43.08% | +0.939 | +0.395 | +0.053 | +0.063 | +0.266 | 0.230 | 382 | Neutral profile |
| TPST | -135.24% | +1.058 | +0.745 | -0.087 | -1.915 | +0.056 | 0.145 | 382 | Small-cap tilt; Weak profitability; Modest factor fit |
| AVGO | +50.10% | +1.613 | -0.141 | -1.275 | +0.083 | -0.212 | 0.459 | 382 | Growth tilt |
| AAPL | +2.16% | +1.351 | -0.139 | -0.050 | +0.751 | +0.193 | 0.549 | 382 | Robust profitability |
| AMD | +5.35% | +1.591 | -0.615 | -0.399 | -1.688 | -0.243 | 0.472 | 382 | Large-cap tilt; Weak profitability |
| BP | +17.65% | +0.686 | -0.236 | +0.607 | +0.031 | +0.263 | 0.158 | 382 | Value tilt; Modest factor fit |
| CC | +19.52% | +1.747 | +2.027 | +0.220 | +0.166 | +1.460 | 0.432 | 382 | Small-cap tilt; Conservative investment |
| NVDA | +22.78% | +1.647 | -0.855 | -1.103 | -0.337 | +1.213 | 0.661 | 382 | Large-cap tilt; Growth tilt; Conservative investment |
| NOW | -42.98% | +1.008 | -0.248 | -0.439 | -0.581 | +0.082 | 0.326 | 382 | Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| CC | **73.33** | 16.67 | 30.00 | 26.67 | 0.377 | +0.621 | 0.6632 | 0.0320 | 132 |
| TPST | **73.33** | 30.00 | 10.00 | 33.33 | 0.119 | -0.119 | 1.3654 | 0.0659 | 132 |
| CTNT | **70.00** | 26.67 | 13.33 | 30.00 | 0.128 | +0.087 | 0.8700 | 0.0420 | 132 |
| AMD | **66.67** | 10.00 | 33.33 | 23.33 | 0.513 | +0.670 | 0.6274 | 0.0303 | 132 |
| BP | **63.33** | 33.33 | 20.00 | 10.00 | 0.118 | +0.142 | 0.3412 | 0.0165 | 132 |
| CMG | **50.00** | 23.33 | 6.67 | 20.00 | 0.285 | -0.625 | 0.4620 | 0.0223 | 132 |
| AVGO | **46.67** | 6.67 | 23.33 | 16.67 | 0.556 | +0.493 | 0.3920 | 0.0189 | 132 |
| AAPL | **40.00** | 20.00 | 16.67 | 3.33 | 0.356 | +0.087 | 0.2290 | 0.0111 | 132 |
| NVDA | **36.67** | 3.33 | 26.67 | 6.67 | 0.696 | +0.615 | 0.2633 | 0.0127 | 132 |
| NOW | **30.00** | 13.33 | 3.33 | 13.33 | 0.506 | -1.900 | 0.3791 | 0.0183 | 132 |

## Per-ticker FF5 Detail

### CTNT

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.0158 (adjusted = 0.0027)
- Alpha (annualized): **+30.39%** (daily = +0.001206, t = +0.23, p = 0.8160)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5939 | +1.09 | 0.2757  |
| SMB | +1.4187 | +1.49 | 0.1370  |
| HML | -0.7593 | -0.89 | 0.3730  |
| RMW | +0.3692 | +0.36 | 0.7211  |
| CMA | +0.5466 | +0.50 | 0.6198  |

_Interpretation: Small-cap tilt; Growth tilt; Conservative investment; Low explanatory power — likely sentiment-driven_

### CMG

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.2297 (adjusted = 0.2195)
- Alpha (annualized): **-43.08%** (daily = -0.001709, t = -1.62, p = 0.1051)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9393 | +8.50 | 0.0000 *** |
| SMB | +0.3951 | +2.04 | 0.0417 * |
| HML | +0.0532 | +0.31 | 0.7586  |
| RMW | +0.0632 | +0.30 | 0.7637  |
| CMA | +0.2656 | +1.19 | 0.2357  |

_Interpretation: Neutral profile_

### TPST

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.1453 (adjusted = 0.1339)
- Alpha (annualized): **-135.24%** (daily = -0.005367, t = -1.90, p = 0.0581)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0584 | +3.57 | 0.0004 *** |
| SMB | +0.7452 | +1.44 | 0.1518  |
| HML | -0.0869 | -0.19 | 0.8515  |
| RMW | -1.9152 | -3.40 | 0.0007 *** |
| CMA | +0.0556 | +0.09 | 0.9262  |

_Interpretation: Small-cap tilt; Weak profitability; Modest factor fit_

### AVGO

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.4592 (adjusted = 0.4520)
- Alpha (annualized): **+50.10%** (daily = +0.001988, t = +1.55, p = 0.1219)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6128 | +11.97 | 0.0000 *** |
| SMB | -0.1409 | -0.60 | 0.5502  |
| HML | -1.2753 | -6.05 | 0.0000 *** |
| RMW | +0.0829 | +0.32 | 0.7460  |
| CMA | -0.2119 | -0.78 | 0.4375  |

_Interpretation: Growth tilt_

### AAPL

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.5486 (adjusted = 0.5426)
- Alpha (annualized): **+2.16%** (daily = +0.000086, t = +0.13, p = 0.8932)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3508 | +20.14 | 0.0000 *** |
| SMB | -0.1388 | -1.18 | 0.2379  |
| HML | -0.0499 | -0.48 | 0.6350  |
| RMW | +0.7505 | +5.89 | 0.0000 *** |
| CMA | +0.1927 | +1.42 | 0.1565  |

_Interpretation: Robust profitability_

### AMD

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.4723 (adjusted = 0.4653)
- Alpha (annualized): **+5.35%** (daily = +0.000212, t = +0.15, p = 0.8777)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5911 | +10.99 | 0.0000 *** |
| SMB | -0.6149 | -2.43 | 0.0157 * |
| HML | -0.3991 | -1.76 | 0.0790  |
| RMW | -1.6875 | -6.13 | 0.0000 *** |
| CMA | -0.2435 | -0.83 | 0.4066  |

_Interpretation: Large-cap tilt; Weak profitability_

### BP

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.1582 (adjusted = 0.1470)
- Alpha (annualized): **+17.65%** (daily = +0.000700, t = +0.81, p = 0.4164)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6858 | +7.58 | 0.0000 *** |
| SMB | -0.2358 | -1.49 | 0.1370  |
| HML | +0.6071 | +4.29 | 0.0000 *** |
| RMW | +0.0307 | +0.18 | 0.8581  |
| CMA | +0.2635 | +1.44 | 0.1508  |

_Interpretation: Value tilt; Modest factor fit_

### CC

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.4315 (adjusted = 0.4240)
- Alpha (annualized): **+19.52%** (daily = +0.000774, t = +0.49, p = 0.6244)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7472 | +10.52 | 0.0000 *** |
| SMB | +2.0271 | +6.98 | 0.0000 *** |
| HML | +0.2202 | +0.85 | 0.3971  |
| RMW | +0.1659 | +0.53 | 0.5992  |
| CMA | +1.4604 | +4.35 | 0.0000 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### NVDA

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.6609 (adjusted = 0.6564)
- Alpha (annualized): **+22.78%** (daily = +0.000904, t = +1.04, p = 0.2973)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6467 | +18.10 | 0.0000 *** |
| SMB | -0.8553 | -5.37 | 0.0000 *** |
| HML | -1.1035 | -7.75 | 0.0000 *** |
| RMW | -0.3374 | -1.95 | 0.0517  |
| CMA | +1.2133 | +6.59 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### NOW

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.3255 (adjusted = 0.3166)
- Alpha (annualized): **-42.98%** (daily = -0.001706, t = -1.57, p = 0.1162)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0085 | +8.86 | 0.0000 *** |
| SMB | -0.2480 | -1.25 | 0.2136  |
| HML | -0.4388 | -2.47 | 0.0141 * |
| RMW | -0.5813 | -2.69 | 0.0075 ** |
| CMA | +0.0818 | +0.36 | 0.7224  |

_Interpretation: Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._