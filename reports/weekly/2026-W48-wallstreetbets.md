# Weekly Report — `wallstreetbets` — 2026-W48

Generated: 2026-11-23  ·  Source: `apewisdom:wallstreetbets`  ·  Lookback: 7 days

[← Back to dashboard](2026-W48.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| NVDA | +18.85% | +1.559 | -0.917 | -1.364 | -0.319 | +1.287 | 0.679 | 337 | Large-cap tilt; Growth tilt; Conservative investment |
| AMD | +24.24% | +1.595 | -0.567 | -0.428 | -1.664 | -0.275 | 0.485 | 337 | Large-cap tilt; Weak profitability |
| MU | +88.99% | +1.967 | -0.363 | -0.148 | -0.995 | +0.174 | 0.404 | 337 | Weak profitability; Significant positive alpha |
| GOOG | +43.88% | +1.001 | +0.181 | -0.569 | +0.470 | -0.661 | 0.457 | 337 | Growth tilt; Aggressive investment; Significant positive alpha |
| NBIS | +175.82% | +1.664 | +0.558 | -2.433 | -1.913 | +0.068 | 0.303 | 337 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| SLS | +115.98% | +0.321 | +1.040 | +0.540 | -1.809 | -1.505 | 0.091 | 337 | Small-cap tilt; Value tilt; Weak profitability; Aggressive investment; Modest factor fit |
| GOOGL | +45.15% | +1.011 | +0.178 | -0.580 | +0.497 | -0.678 | 0.452 | 337 | Growth tilt; Aggressive investment; Significant positive alpha |
| DTE | +3.27% | +0.341 | -0.210 | +0.588 | -0.192 | +0.055 | 0.168 | 337 | Value tilt; Modest factor fit |
| IT | -81.94% | +0.816 | +0.386 | -0.232 | +0.202 | +0.089 | 0.131 | 337 | Significant negative alpha; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **90.00** | 26.67 | 33.33 | 30.00 | 0.294 | +2.436 | 1.5736 | 0.0575 | 87 |
| SLS | **83.33** | 30.00 | 20.00 | 33.33 | 0.245 | +0.812 | 1.7059 | 0.0623 | 87 |
| MU | **73.33** | 23.33 | 26.67 | 23.33 | 0.365 | +1.105 | 0.9690 | 0.0354 | 87 |
| NBIS | **70.00** | 13.33 | 30.00 | 26.67 | 0.498 | +1.148 | 1.2292 | 0.0449 | 87 |
| AMD | **46.67** | 6.67 | 23.33 | 16.67 | 0.591 | +1.053 | 0.6484 | 0.0237 | 87 |
| IT | **43.33** | 20.00 | 3.33 | 20.00 | 0.423 | -2.135 | 0.6937 | 0.0253 | 87 |
| DTE | **43.33** | 33.33 | 6.67 | 3.33 | 0.072 | +0.036 | 0.2736 | 0.0100 | 87 |
| GOOGL | **36.67** | 16.67 | 10.00 | 10.00 | 0.491 | +0.100 | 0.3293 | 0.0120 | 87 |
| NVDA | **33.33** | 3.33 | 16.67 | 13.33 | 0.661 | +0.685 | 0.3516 | 0.0128 | 87 |
| GOOG | **30.00** | 10.00 | 13.33 | 6.67 | 0.502 | +0.106 | 0.3202 | 0.0117 | 87 |

## Per-ticker FF5 Detail

### NVDA

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.6792 (adjusted = 0.6744)
- Alpha (annualized): **+18.85%** (daily = +0.000748, t = +0.82, p = 0.4153)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5587 | +16.55 | 0.0000 *** |
| SMB | -0.9166 | -5.44 | 0.0000 *** |
| HML | -1.3635 | -8.57 | 0.0000 *** |
| RMW | -0.3185 | -1.81 | 0.0713  |
| CMA | +1.2868 | +6.45 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### AMD

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.4853 (adjusted = 0.4776)
- Alpha (annualized): **+24.24%** (daily = +0.000962, t = +0.64, p = 0.5203)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5954 | +10.39 | 0.0000 *** |
| SMB | -0.5671 | -2.07 | 0.0397 * |
| HML | -0.4280 | -1.65 | 0.0998  |
| RMW | -1.6636 | -5.80 | 0.0000 *** |
| CMA | -0.2755 | -0.85 | 0.3970  |

_Interpretation: Large-cap tilt; Weak profitability_

### MU

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.4037 (adjusted = 0.3947)
- Alpha (annualized): **+88.99%** (daily = +0.003531, t = +2.02, p = 0.0444)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9667 | +10.94 | 0.0000 *** |
| SMB | -0.3629 | -1.13 | 0.2598  |
| HML | -0.1481 | -0.49 | 0.6260  |
| RMW | -0.9950 | -2.96 | 0.0033 ** |
| CMA | +0.1740 | +0.46 | 0.6477  |

_Interpretation: Weak profitability; Significant positive alpha_

### GOOG

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.4573 (adjusted = 0.4492)
- Alpha (annualized): **+43.88%** (daily = +0.001741, t = +2.20, p = 0.0286)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0005 | +12.30 | 0.0000 *** |
| SMB | +0.1812 | +1.25 | 0.2140  |
| HML | -0.5691 | -4.14 | 0.0000 *** |
| RMW | +0.4698 | +3.09 | 0.0022 ** |
| CMA | -0.6613 | -3.84 | 0.0001 *** |

_Interpretation: Growth tilt; Aggressive investment; Significant positive alpha_

### NBIS

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.3029 (adjusted = 0.2923)
- Alpha (annualized): **+175.82%** (daily = +0.006977, t = +2.16, p = 0.0319)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6637 | +5.00 | 0.0000 *** |
| SMB | +0.5585 | +0.94 | 0.3485  |
| HML | -2.4331 | -4.33 | 0.0000 *** |
| RMW | -1.9129 | -3.08 | 0.0023 ** |
| CMA | +0.0681 | +0.10 | 0.9230  |

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

### SLS

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.0915 (adjusted = 0.0778)
- Alpha (annualized): **+115.98%** (daily = +0.004602, t = +1.46, p = 0.1460)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3205 | +0.99 | 0.3239  |
| SMB | +1.0403 | +1.79 | 0.0740  |
| HML | +0.5405 | +0.99 | 0.3248  |
| RMW | -1.8089 | -2.98 | 0.0031 ** |
| CMA | -1.5055 | -2.19 | 0.0290 * |

_Interpretation: Small-cap tilt; Value tilt; Weak profitability; Aggressive investment; Modest factor fit_

### GOOGL

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.4517 (adjusted = 0.4434)
- Alpha (annualized): **+45.15%** (daily = +0.001792, t = +2.22, p = 0.0274)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0109 | +12.17 | 0.0000 *** |
| SMB | +0.1775 | +1.19 | 0.2331  |
| HML | -0.5801 | -4.13 | 0.0000 *** |
| RMW | +0.4971 | +3.20 | 0.0015 ** |
| CMA | -0.6785 | -3.86 | 0.0001 *** |

_Interpretation: Growth tilt; Aggressive investment; Significant positive alpha_

### DTE

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.1683 (adjusted = 0.1558)
- Alpha (annualized): **+3.27%** (daily = +0.000130, t = +0.24, p = 0.8106)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3410 | +6.14 | 0.0000 *** |
| SMB | -0.2101 | -2.12 | 0.0351 * |
| HML | +0.5880 | +6.27 | 0.0000 *** |
| RMW | -0.1924 | -1.86 | 0.0644  |
| CMA | +0.0552 | +0.47 | 0.6390  |

_Interpretation: Value tilt; Modest factor fit_

### IT

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.1312 (adjusted = 0.1181)
- Alpha (annualized): **-81.94%** (daily = -0.003252, t = -2.25, p = 0.0249)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8163 | +5.51 | 0.0000 *** |
| SMB | +0.3863 | +1.46 | 0.1460  |
| HML | -0.2322 | -0.93 | 0.3543  |
| RMW | +0.2017 | +0.73 | 0.4669  |
| CMA | +0.0892 | +0.28 | 0.7764  |

_Interpretation: Significant negative alpha; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._