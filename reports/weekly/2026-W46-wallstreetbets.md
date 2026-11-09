# Weekly Report — `wallstreetbets` — 2026-W46

Generated: 2026-11-09  ·  Source: `apewisdom:wallstreetbets`  ·  Lookback: 7 days

[← Back to dashboard](2026-W46.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +79.66% | +1.967 | -0.322 | -0.160 | -0.967 | +0.200 | 0.401 | 347 | Weak profitability |
| NVDA | +18.38% | +1.551 | -0.926 | -1.353 | -0.333 | +1.310 | 0.679 | 347 | Large-cap tilt; Growth tilt; Conservative investment |
| AMD | +16.37% | +1.602 | -0.581 | -0.396 | -1.646 | -0.297 | 0.482 | 347 | Large-cap tilt; Weak profitability |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| AAPL | +5.75% | +1.403 | -0.092 | +0.075 | +0.795 | +0.076 | 0.568 | 347 | Robust profitability |
| TSLA | +16.19% | +2.124 | -0.018 | -0.048 | -0.390 | -1.016 | 0.481 | 347 | Aggressive investment |
| GOOG | +38.03% | +0.996 | +0.147 | -0.564 | +0.458 | -0.670 | 0.446 | 347 | Growth tilt; Aggressive investment |
| DTE | +6.65% | +0.335 | -0.180 | +0.571 | -0.203 | +0.058 | 0.165 | 347 | Value tilt; Modest factor fit |
| INTC | +15.42% | +1.567 | -0.439 | +1.485 | -1.802 | +0.313 | 0.282 | 347 | Value tilt; Weak profitability |
| NBIS | +178.07% | +1.650 | +0.621 | -2.394 | -1.985 | +0.083 | 0.306 | 347 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **96.67** | 30.00 | 33.33 | 33.33 | 0.344 | +2.464 | 1.4811 | 0.0582 | 97 |
| NBIS | **76.67** | 16.67 | 30.00 | 30.00 | 0.463 | +1.292 | 1.1791 | 0.0463 | 97 |
| MU | **73.33** | 20.00 | 26.67 | 26.67 | 0.395 | +1.033 | 0.8978 | 0.0353 | 97 |
| INTC | **70.00** | 26.67 | 20.00 | 23.33 | 0.388 | +0.888 | 0.8762 | 0.0344 | 97 |
| AMD | **50.00** | 6.67 | 23.33 | 20.00 | 0.557 | +0.950 | 0.6477 | 0.0254 | 97 |
| AAPL | **43.33** | 23.33 | 13.33 | 6.67 | 0.392 | +0.147 | 0.2699 | 0.0106 | 97 |
| DTE | **43.33** | 33.33 | 6.67 | 3.33 | 0.061 | +0.046 | 0.2547 | 0.0100 | 97 |
| TSLA | **33.33** | 13.33 | 3.33 | 16.67 | 0.469 | -0.007 | 0.4488 | 0.0176 | 97 |
| NVDA | **33.33** | 3.33 | 16.67 | 13.33 | 0.697 | +0.684 | 0.3221 | 0.0127 | 97 |
| GOOG | **30.00** | 10.00 | 10.00 | 10.00 | 0.492 | +0.130 | 0.3165 | 0.0124 | 97 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.4006 (adjusted = 0.3919)
- Alpha (annualized): **+79.66%** (daily = +0.003161, t = +1.84, p = 0.0666)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9667 | +11.03 | 0.0000 *** |
| SMB | -0.3220 | -1.03 | 0.3053  |
| HML | -0.1600 | -0.54 | 0.5869  |
| RMW | -0.9670 | -2.91 | 0.0039 ** |
| CMA | +0.2001 | +0.54 | 0.5889  |

_Interpretation: Weak profitability_

### NVDA

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.6790 (adjusted = 0.6743)
- Alpha (annualized): **+18.38%** (daily = +0.000729, t = +0.81, p = 0.4178)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5509 | +16.62 | 0.0000 *** |
| SMB | -0.9256 | -5.64 | 0.0000 *** |
| HML | -1.3533 | -8.79 | 0.0000 *** |
| RMW | -0.3326 | -1.91 | 0.0571  |
| CMA | +1.3097 | +6.76 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### AMD

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.4820 (adjusted = 0.4744)
- Alpha (annualized): **+16.37%** (daily = +0.000650, t = +0.44, p = 0.6572)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6020 | +10.55 | 0.0000 *** |
| SMB | -0.5808 | -2.17 | 0.0304 * |
| HML | -0.3962 | -1.58 | 0.1148  |
| RMW | -1.6456 | -5.80 | 0.0000 *** |
| CMA | -0.2967 | -0.94 | 0.3470  |

_Interpretation: Large-cap tilt; Weak profitability_

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

### AAPL

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.5681 (adjusted = 0.5618)
- Alpha (annualized): **+5.75%** (daily = +0.000228, t = +0.34, p = 0.7352)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4029 | +20.04 | 0.0000 *** |
| SMB | -0.0915 | -0.74 | 0.4578  |
| HML | +0.0747 | +0.65 | 0.5181  |
| RMW | +0.7949 | +6.08 | 0.0000 *** |
| CMA | +0.0760 | +0.52 | 0.6009  |

_Interpretation: Robust profitability_

### TSLA

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.4810 (adjusted = 0.4734)
- Alpha (annualized): **+16.19%** (daily = +0.000643, t = +0.43, p = 0.6662)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.1242 | +13.75 | 0.0000 *** |
| SMB | -0.0176 | -0.06 | 0.9484  |
| HML | -0.0478 | -0.19 | 0.8513  |
| RMW | -0.3896 | -1.35 | 0.1777  |
| CMA | -1.0165 | -3.17 | 0.0017 ** |

_Interpretation: Aggressive investment_

### GOOG

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.4457 (adjusted = 0.4376)
- Alpha (annualized): **+38.03%** (daily = +0.001509, t = +1.91, p = 0.0573)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9961 | +12.13 | 0.0000 *** |
| SMB | +0.1475 | +1.02 | 0.3080  |
| HML | -0.5644 | -4.16 | 0.0000 *** |
| RMW | +0.4585 | +2.99 | 0.0030 ** |
| CMA | -0.6700 | -3.93 | 0.0001 *** |

_Interpretation: Growth tilt; Aggressive investment_

### DTE

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.1650 (adjusted = 0.1527)
- Alpha (annualized): **+6.65%** (daily = +0.000264, t = +0.50, p = 0.6200)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3354 | +6.08 | 0.0000 *** |
| SMB | -0.1796 | -1.85 | 0.0652  |
| HML | +0.5715 | +6.28 | 0.0000 *** |
| RMW | -0.2026 | -1.97 | 0.0501  |
| CMA | +0.0583 | +0.51 | 0.6110  |

_Interpretation: Value tilt; Modest factor fit_

### INTC

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.2824 (adjusted = 0.2719)
- Alpha (annualized): **+15.42%** (daily = +0.000612, t = +0.32, p = 0.7457)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5667 | +8.01 | 0.0000 *** |
| SMB | -0.4387 | -1.27 | 0.2032  |
| HML | +1.4849 | +4.60 | 0.0000 *** |
| RMW | -1.8022 | -4.93 | 0.0000 *** |
| CMA | +0.3129 | +0.77 | 0.4413  |

_Interpretation: Value tilt; Weak profitability_

### NBIS

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.3064 (adjusted = 0.2963)
- Alpha (annualized): **+178.07%** (daily = +0.007066, t = +2.23, p = 0.0264)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6497 | +5.01 | 0.0000 *** |
| SMB | +0.6206 | +1.07 | 0.2842  |
| HML | -2.3945 | -4.41 | 0.0000 *** |
| RMW | -1.9853 | -3.23 | 0.0013 ** |
| CMA | +0.0827 | +0.12 | 0.9036  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._