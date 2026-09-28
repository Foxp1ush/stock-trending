# Weekly Report — `pennystocks` — 2026-W40

Generated: 2026-09-28  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W40.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **9 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| JAGX | -213.81% | +1.500 | +0.429 | -0.594 | -1.465 | +0.180 | 0.080 | 377 | Growth tilt; Weak profitability; Modest factor fit |
| GLND | — | — | — | — | — | — | — | — | _insufficient_data_ |
| MSS | -100.92% | +0.124 | +0.793 | -1.139 | -0.900 | +0.686 | 0.048 | 377 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| WHLR | -611.38% | +1.030 | -0.514 | +0.985 | -2.111 | +1.065 | 0.020 | 377 | Large-cap tilt; Value tilt; Weak profitability; Conservative investment; Significant negative alpha; Low explanatory power — likely sentiment-driven |
| ORBS | +1794.98% | -1.743 | -1.041 | -6.413 | -10.493 | +0.636 | 0.003 | 377 | Large-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| CTNT | +35.79% | +0.573 | +1.387 | -0.809 | +0.362 | +0.561 | 0.015 | 377 | Small-cap tilt; Growth tilt; Conservative investment; Low explanatory power — likely sentiment-driven |
| BFRG | +30.04% | +1.635 | +1.685 | -1.386 | -1.584 | -0.158 | 0.139 | 377 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| NCPL | -27.01% | +0.934 | +0.369 | +0.339 | -0.855 | +0.623 | 0.021 | 377 | Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| AVGO | +48.51% | +1.612 | -0.135 | -1.277 | +0.086 | -0.214 | 0.459 | 377 | Growth tilt |
| AMD | +2.99% | +1.591 | -0.599 | -0.403 | -1.670 | -0.267 | 0.472 | 377 | Large-cap tilt; Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| NCPL | **74.07** | 29.63 | 11.11 | 33.33 | 0.043 | -1.222 | 2.6790 | 0.1268 | 127 |
| MSS | **70.37** | 33.33 | 22.22 | 14.81 | 0.037 | +0.175 | 1.3818 | 0.0654 | 127 |
| ORBS | **66.67** | 14.81 | 33.33 | 18.52 | 0.162 | +2.014 | 1.7145 | 0.0811 | 127 |
| WHLR | **62.96** | 25.93 | 7.41 | 29.63 | 0.047 | -1.326 | 2.6128 | 0.1236 | 127 |
| JAGX | **59.26** | 22.22 | 14.81 | 22.22 | 0.082 | -0.348 | 2.2714 | 0.1075 | 127 |
| CTNT | **48.15** | 18.52 | 18.52 | 11.11 | 0.128 | +0.063 | 0.9040 | 0.0428 | 127 |
| AMD | **44.44** | 7.41 | 29.63 | 7.41 | 0.516 | +0.649 | 0.6504 | 0.0308 | 127 |
| BFRG | **40.74** | 11.11 | 3.70 | 25.93 | 0.164 | -3.590 | 2.4068 | 0.1139 | 127 |
| AVGO | **33.33** | 3.70 | 25.93 | 3.70 | 0.576 | +0.495 | 0.3979 | 0.0188 | 127 |

## Per-ticker FF5 Detail

### JAGX

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.0800 (adjusted = 0.0676)
- Alpha (annualized): **-213.81%** (daily = -0.008484, t = -1.90, p = 0.0582)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5002 | +3.22 | 0.0014 ** |
| SMB | +0.4291 | +0.52 | 0.6005  |
| HML | -0.5937 | -0.81 | 0.4174  |
| RMW | -1.4647 | -1.65 | 0.0998  |
| CMA | +0.1797 | +0.19 | 0.8502  |

_Interpretation: Growth tilt; Weak profitability; Modest factor fit_

### GLND

Status: `insufficient_data` — only 6 overlapping days after factor join


### MSS

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.0484 (adjusted = 0.0355)
- Alpha (annualized): **-100.92%** (daily = -0.004005, t = -1.31, p = 0.1915)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.1243 | +0.39 | 0.6977  |
| SMB | +0.7929 | +1.41 | 0.1584  |
| HML | -1.1390 | -2.27 | 0.0236 * |
| RMW | -0.8995 | -1.48 | 0.1402  |
| CMA | +0.6859 | +1.05 | 0.2932  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### WHLR

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.0197 (adjusted = 0.0065)
- Alpha (annualized): **-611.38%** (daily = -0.024261, t = -3.58, p = 0.0004)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0303 | +1.46 | 0.1463  |
| SMB | -0.5137 | -0.41 | 0.6794  |
| HML | +0.9849 | +0.89 | 0.3753  |
| RMW | -2.1109 | -1.57 | 0.1180  |
| CMA | +1.0646 | +0.74 | 0.4610  |

_Interpretation: Large-cap tilt; Value tilt; Weak profitability; Conservative investment; Significant negative alpha; Low explanatory power — likely sentiment-driven_

### ORBS

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.0031 (adjusted = -0.0104)
- Alpha (annualized): **+1794.98%** (daily = +0.071230, t = +0.88, p = 0.3794)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -1.7429 | -0.21 | 0.8368  |
| SMB | -1.0411 | -0.07 | 0.9441  |
| HML | -6.4133 | -0.48 | 0.6288  |
| RMW | -10.4925 | -0.65 | 0.5148  |
| CMA | +0.6364 | +0.04 | 0.9706  |

_Interpretation: Large-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### CTNT

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.0154 (adjusted = 0.0021)
- Alpha (annualized): **+35.79%** (daily = +0.001420, t = +0.27, p = 0.7865)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5734 | +1.05 | 0.2956  |
| SMB | +1.3871 | +1.44 | 0.1496  |
| HML | -0.8088 | -0.94 | 0.3466  |
| RMW | +0.3621 | +0.35 | 0.7284  |
| CMA | +0.5605 | +0.50 | 0.6157  |

_Interpretation: Small-cap tilt; Growth tilt; Conservative investment; Low explanatory power — likely sentiment-driven_

### BFRG

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.1391 (adjusted = 0.1274)
- Alpha (annualized): **+30.04%** (daily = +0.001192, t = +0.27, p = 0.7849)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6354 | +3.59 | 0.0004 *** |
| SMB | +1.6849 | +2.11 | 0.0359 * |
| HML | -1.3862 | -1.94 | 0.0532  |
| RMW | -1.5839 | -1.83 | 0.0688  |
| CMA | -0.1584 | -0.17 | 0.8647  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### NCPL

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.0215 (adjusted = 0.0083)
- Alpha (annualized): **-27.01%** (daily = -0.001072, t = -0.21, p = 0.8306)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9343 | +1.79 | 0.0748  |
| SMB | +0.3689 | +0.40 | 0.6879  |
| HML | +0.3390 | +0.41 | 0.6795  |
| RMW | -0.8550 | -0.86 | 0.3909  |
| CMA | +0.6233 | +0.58 | 0.5591  |

_Interpretation: Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### AVGO

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.4592 (adjusted = 0.4519)
- Alpha (annualized): **+48.51%** (daily = +0.001925, t = +1.48, p = 0.1389)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6119 | +11.89 | 0.0000 *** |
| SMB | -0.1350 | -0.57 | 0.5708  |
| HML | -1.2770 | -6.01 | 0.0000 *** |
| RMW | +0.0861 | +0.33 | 0.7388  |
| CMA | -0.2142 | -0.77 | 0.4389  |

_Interpretation: Growth tilt_

### AMD

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.4723 (adjusted = 0.4652)
- Alpha (annualized): **+2.99%** (daily = +0.000119, t = +0.09, p = 0.9322)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5910 | +10.92 | 0.0000 *** |
| SMB | -0.5994 | -2.34 | 0.0196 * |
| HML | -0.4032 | -1.77 | 0.0783  |
| RMW | -1.6700 | -6.02 | 0.0000 *** |
| CMA | -0.2667 | -0.90 | 0.3697  |

_Interpretation: Large-cap tilt; Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._