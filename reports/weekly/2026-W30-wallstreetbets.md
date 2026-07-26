# Weekly Report — `wallstreetbets` — 2026-W30

Generated: 2026-07-26  ·  Source: `apewisdom:wallstreetbets`  ·  Lookback: 7 days

[← Back to dashboard](2026-W30.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +58.19% | +1.960 | -0.293 | -0.156 | -1.030 | +0.381 | 0.403 | 421 | Weak profitability |
| GOOG | +28.80% | +1.019 | +0.224 | -0.494 | +0.479 | -0.737 | 0.452 | 421 | Aggressive investment |
| TSLA | +23.84% | +2.202 | +0.057 | -0.123 | -0.254 | -1.040 | 0.450 | 421 | Aggressive investment |
| MSFT | -14.65% | +0.880 | -0.256 | -0.411 | +0.133 | -0.504 | 0.513 | 421 | Aggressive investment |
| GOOGL | +29.78% | +1.025 | +0.212 | -0.501 | +0.497 | -0.754 | 0.445 | 421 | Growth tilt; Aggressive investment |
| NVDA | +16.15% | +1.723 | -0.854 | -1.178 | -0.369 | +1.595 | 0.691 | 421 | Large-cap tilt; Growth tilt; Conservative investment |
| INTC | +2.01% | +1.715 | -0.363 | +1.225 | -1.746 | +0.310 | 0.303 | 421 | Value tilt; Weak profitability |
| NOW | -36.85% | +0.997 | -0.258 | -0.400 | -0.591 | -0.028 | 0.335 | 421 | Weak profitability |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| NBIS | +171.20% | +1.642 | +0.745 | -2.284 | -2.007 | -0.014 | 0.295 | 360 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| NBIS | **93.33** | 30.00 | 30.00 | 33.33 | 0.294 | +1.271 | 1.0246 | 0.0578 | 171 |
| SNDK | **90.00** | 26.67 | 33.33 | 30.00 | 0.311 | +2.038 | 0.9959 | 0.0561 | 171 |
| INTC | **80.00** | 33.33 | 20.00 | 26.67 | 0.284 | +0.381 | 0.6426 | 0.0362 | 171 |
| MU | **73.33** | 23.33 | 26.67 | 23.33 | 0.328 | +0.673 | 0.5913 | 0.0333 | 171 |
| GOOGL | **46.67** | 20.00 | 13.33 | 13.33 | 0.371 | +0.089 | 0.2531 | 0.0143 | 171 |
| GOOG | **43.33** | 16.67 | 16.67 | 10.00 | 0.373 | +0.090 | 0.2477 | 0.0140 | 171 |
| TSLA | **43.33** | 13.33 | 10.00 | 20.00 | 0.412 | -0.151 | 0.3618 | 0.0204 | 171 |
| NVDA | **33.33** | 3.33 | 23.33 | 6.67 | 0.649 | +0.498 | 0.2294 | 0.0129 | 171 |
| NOW | **26.67** | 6.67 | 3.33 | 16.67 | 0.444 | -1.718 | 0.3263 | 0.0184 | 171 |
| MSFT | **20.00** | 10.00 | 6.67 | 3.33 | 0.421 | -0.478 | 0.2097 | 0.0118 | 171 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.4035 (adjusted = 0.3963)
- Alpha (annualized): **+58.19%** (daily = +0.002309, t = +1.52, p = 0.1299)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9598 | +12.17 | 0.0000 *** |
| SMB | -0.2930 | -1.06 | 0.2891  |
| HML | -0.1563 | -0.63 | 0.5309  |
| RMW | -1.0295 | -3.33 | 0.0010 *** |
| CMA | +0.3813 | +1.21 | 0.2260  |

_Interpretation: Weak profitability_

### GOOG

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.4521 (adjusted = 0.4455)
- Alpha (annualized): **+28.80%** (daily = +0.001143, t = +1.67, p = 0.0962)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0191 | +14.05 | 0.0000 *** |
| SMB | +0.2240 | +1.80 | 0.0723  |
| HML | -0.4943 | -4.40 | 0.0000 *** |
| RMW | +0.4788 | +3.44 | 0.0007 *** |
| CMA | -0.7369 | -5.20 | 0.0000 *** |

_Interpretation: Aggressive investment_

### TSLA

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.4496 (adjusted = 0.4429)
- Alpha (annualized): **+23.84%** (daily = +0.000946, t = +0.66, p = 0.5097)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2017 | +14.51 | 0.0000 *** |
| SMB | +0.0568 | +0.22 | 0.8272  |
| HML | -0.1234 | -0.53 | 0.5997  |
| RMW | -0.2535 | -0.87 | 0.3851  |
| CMA | -1.0403 | -3.51 | 0.0005 *** |

_Interpretation: Aggressive investment_

### MSFT

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.5133 (adjusted = 0.5074)
- Alpha (annualized): **-14.65%** (daily = -0.000581, t = -1.08, p = 0.2805)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8801 | +15.46 | 0.0000 *** |
| SMB | -0.2558 | -2.62 | 0.0091 ** |
| HML | -0.4105 | -4.66 | 0.0000 *** |
| RMW | +0.1333 | +1.22 | 0.2238  |
| CMA | -0.5038 | -4.53 | 0.0000 *** |

_Interpretation: Aggressive investment_

### GOOGL

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.4451 (adjusted = 0.4384)
- Alpha (annualized): **+29.78%** (daily = +0.001182, t = +1.69, p = 0.0916)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0249 | +13.86 | 0.0000 *** |
| SMB | +0.2120 | +1.67 | 0.0951  |
| HML | -0.5012 | -4.38 | 0.0000 *** |
| RMW | +0.4973 | +3.50 | 0.0005 *** |
| CMA | -0.7542 | -5.22 | 0.0000 *** |

_Interpretation: Growth tilt; Aggressive investment_

### NVDA

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.6909 (adjusted = 0.6871)
- Alpha (annualized): **+16.15%** (daily = +0.000641, t = +0.76, p = 0.4449)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7235 | +19.43 | 0.0000 *** |
| SMB | -0.8537 | -5.61 | 0.0000 *** |
| HML | -1.1785 | -8.58 | 0.0000 *** |
| RMW | -0.3687 | -2.16 | 0.0311 * |
| CMA | +1.5950 | +9.21 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### INTC

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.3025 (adjusted = 0.2941)
- Alpha (annualized): **+2.01%** (daily = +0.000080, t = +0.05, p = 0.9630)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7148 | +9.43 | 0.0000 *** |
| SMB | -0.3626 | -1.16 | 0.2454  |
| HML | +1.2249 | +4.35 | 0.0000 *** |
| RMW | -1.7464 | -5.00 | 0.0000 *** |
| CMA | +0.3096 | +0.87 | 0.3838  |

_Interpretation: Value tilt; Weak profitability_

### NOW

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.3354 (adjusted = 0.3274)
- Alpha (annualized): **-36.85%** (daily = -0.001462, t = -1.47, p = 0.1425)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9970 | +9.47 | 0.0000 *** |
| SMB | -0.2580 | -1.43 | 0.1536  |
| HML | -0.3999 | -2.45 | 0.0146 * |
| RMW | -0.5908 | -2.92 | 0.0037 ** |
| CMA | -0.0284 | -0.14 | 0.8902  |

_Interpretation: Weak profitability_

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

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._