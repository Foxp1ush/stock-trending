# Weekly Report — `wallstreetbets` — 2026-W33

Generated: 2026-08-16  ·  Source: `apewisdom:wallstreetbets`  ·  Lookback: 7 days

[← Back to dashboard](2026-W33.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +47.67% | +1.023 | +2.142 | +0.598 | +0.383 | +0.351 | 0.104 | 406 | Small-cap tilt; Value tilt; Modest factor fit |
| MU | +62.99% | +1.945 | -0.279 | -0.171 | -0.968 | +0.299 | 0.388 | 406 | Weak profitability |
| NBIS | +171.20% | +1.642 | +0.745 | -2.284 | -2.007 | -0.014 | 0.295 | 360 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| NVDA | +19.60% | +1.680 | -0.831 | -1.142 | -0.346 | +1.390 | 0.673 | 406 | Large-cap tilt; Growth tilt; Conservative investment |
| RKLB | +153.72% | +1.426 | +0.705 | -0.825 | -3.444 | +0.076 | 0.391 | 406 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| RDDT | +63.24% | +1.583 | -0.135 | -0.749 | -1.245 | -0.482 | 0.246 | 406 | Growth tilt; Weak profitability |
| SMCI | -22.83% | +1.191 | +0.273 | -2.107 | -2.034 | +1.929 | 0.252 | 406 | Growth tilt; Weak profitability; Conservative investment |
| ONDS | +216.37% | +1.576 | +1.469 | -0.590 | -2.351 | -1.076 | 0.165 | 406 | Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Significant positive alpha; Modest factor fit |
| ASTS | +82.56% | +1.287 | +1.238 | -1.102 | -3.061 | -0.302 | 0.303 | 406 | Small-cap tilt; Growth tilt; Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| ONDS | **86.67** | 26.67 | 26.67 | 33.33 | 0.299 | +1.051 | 1.3029 | 0.0684 | 156 |
| SNDK | **83.33** | 20.00 | 33.33 | 30.00 | 0.316 | +2.187 | 1.0973 | 0.0576 | 156 |
| NBIS | **80.00** | 23.33 | 30.00 | 26.67 | 0.316 | +1.175 | 1.0929 | 0.0574 | 156 |
| HTZ | **63.33** | 33.33 | 10.00 | 20.00 | 0.119 | +0.090 | 0.8662 | 0.0455 | 156 |
| ASTS | **53.33** | 16.67 | 13.33 | 23.33 | 0.324 | +0.126 | 1.0790 | 0.0567 | 156 |
| RDDT | **43.33** | 30.00 | 3.33 | 10.00 | 0.256 | -0.705 | 0.6640 | 0.0349 | 156 |
| MU | **40.00** | 10.00 | 23.33 | 6.67 | 0.334 | +0.720 | 0.6451 | 0.0339 | 156 |
| RKLB | **40.00** | 6.67 | 16.67 | 16.67 | 0.434 | +0.434 | 0.8095 | 0.0425 | 156 |
| SMCI | **33.33** | 13.33 | 6.67 | 13.33 | 0.328 | -0.045 | 0.7484 | 0.0393 | 156 |
| NVDA | **26.67** | 3.33 | 20.00 | 3.33 | 0.671 | +0.587 | 0.2446 | 0.0128 | 156 |

## Per-ticker FF5 Detail

### HTZ

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.1036 (adjusted = 0.0924)
- Alpha (annualized): **+47.67%** (daily = +0.001892, t = +0.64, p = 0.5224)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0232 | +3.24 | 0.0013 ** |
| SMB | +2.1423 | +4.01 | 0.0001 *** |
| HML | +0.5982 | +1.24 | 0.2170  |
| RMW | +0.3825 | +0.64 | 0.5212  |
| CMA | +0.3506 | +0.56 | 0.5757  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### MU

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.3882 (adjusted = 0.3805)
- Alpha (annualized): **+62.99%** (daily = +0.002500, t = +1.60, p = 0.1099)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9448 | +11.67 | 0.0000 *** |
| SMB | -0.2789 | -0.99 | 0.3235  |
| HML | -0.1713 | -0.67 | 0.5029  |
| RMW | -0.9677 | -3.08 | 0.0022 ** |
| CMA | +0.2988 | +0.90 | 0.3666  |

_Interpretation: Weak profitability_

### NBIS

- Period: `2024-10-22` to `2026-03-31` (360 obs)
- R² = 0.2953 (adjusted = 0.2854)
- Alpha (annualized): **+171.20%** (daily = +0.006794, t = +2.15, p = 0.0320)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6416 | +5.06 | 0.0000 *** |
| SMB | +0.7454 | +1.29 | 0.1966  |
| HML | -2.2842 | -4.49 | 0.0000 *** |
| RMW | -2.0070 | -3.24 | 0.0013 ** |
| CMA | -0.0135 | -0.02 | 0.9839  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### SNDK

- Period: `2025-02-14` to `2026-03-31` (282 obs)
- R² = 0.2490 (adjusted = 0.2354)
- Alpha (annualized): **+277.05%** (daily = +0.010994, t = +3.31, p = 0.0011)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.3574 | +7.20 | 0.0000 *** |
| SMB | -0.0193 | -0.03 | 0.9748  |
| HML | +0.8466 | +1.41 | 0.1591  |
| RMW | -1.2601 | -1.98 | 0.0485 * |
| CMA | -1.2831 | -1.62 | 0.1062  |

_Interpretation: Value tilt; Weak profitability; Aggressive investment; Significant positive alpha_

### NVDA

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.6729 (adjusted = 0.6688)
- Alpha (annualized): **+19.60%** (daily = +0.000778, t = +0.92, p = 0.3559)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6796 | +18.69 | 0.0000 *** |
| SMB | -0.8308 | -5.46 | 0.0000 *** |
| HML | -1.1422 | -8.29 | 0.0000 *** |
| RMW | -0.3464 | -2.04 | 0.0419 * |
| CMA | +1.3904 | +7.80 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### RKLB

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.3912 (adjusted = 0.3835)
- Alpha (annualized): **+153.72%** (daily = +0.006100, t = +2.70, p = 0.0072)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4264 | +5.92 | 0.0000 *** |
| SMB | +0.7046 | +1.72 | 0.0853  |
| HML | -0.8245 | -2.23 | 0.0263 * |
| RMW | -3.4435 | -7.56 | 0.0000 *** |
| CMA | +0.0762 | +0.16 | 0.8736  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### RDDT

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.2458 (adjusted = 0.2363)
- Alpha (annualized): **+63.24%** (daily = +0.002509, t = +1.14, p = 0.2544)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5834 | +6.75 | 0.0000 *** |
| SMB | -0.1349 | -0.34 | 0.7346  |
| HML | -0.7486 | -2.08 | 0.0382 * |
| RMW | -1.2450 | -2.81 | 0.0052 ** |
| CMA | -0.4818 | -1.03 | 0.3015  |

_Interpretation: Growth tilt; Weak profitability_

### SMCI

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.2521 (adjusted = 0.2427)
- Alpha (annualized): **-22.83%** (daily = -0.000906, t = -0.33, p = 0.7418)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1913 | +4.06 | 0.0001 *** |
| SMB | +0.2731 | +0.55 | 0.5829  |
| HML | -2.1066 | -4.68 | 0.0000 *** |
| RMW | -2.0340 | -3.67 | 0.0003 *** |
| CMA | +1.9291 | +3.31 | 0.0010 ** |

_Interpretation: Growth tilt; Weak profitability; Conservative investment_

### ONDS

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.1651 (adjusted = 0.1547)
- Alpha (annualized): **+216.37%** (daily = +0.008586, t = +2.25, p = 0.0252)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5759 | +3.86 | 0.0001 *** |
| SMB | +1.4686 | +2.12 | 0.0342 * |
| HML | -0.5905 | -0.94 | 0.3459  |
| RMW | -2.3509 | -3.05 | 0.0024 ** |
| CMA | -1.0758 | -1.33 | 0.1846  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Significant positive alpha; Modest factor fit_

### ASTS

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.3032 (adjusted = 0.2945)
- Alpha (annualized): **+82.56%** (daily = +0.003276, t = +1.22, p = 0.2250)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2873 | +4.47 | 0.0000 *** |
| SMB | +1.2382 | +2.54 | 0.0115 * |
| HML | -1.1020 | -2.50 | 0.0129 * |
| RMW | -3.0605 | -5.63 | 0.0000 *** |
| CMA | -0.3024 | -0.53 | 0.5967  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._