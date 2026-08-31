# Weekly Report — `all-stocks` — 2026-W36

Generated: 2026-08-31  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W36.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| NVDA | +20.73% | +1.669 | -0.830 | -1.160 | -0.309 | +1.279 | 0.674 | 396 | Large-cap tilt; Growth tilt; Conservative investment |
| MU | +72.15% | +1.952 | -0.246 | -0.155 | -0.981 | +0.345 | 0.390 | 396 | Weak profitability |
| MRVL | +17.29% | +1.974 | -0.563 | -0.701 | -1.219 | +0.861 | 0.437 | 396 | Large-cap tilt; Growth tilt; Weak profitability; Conservative investment |
| META | +3.79% | +1.383 | -0.014 | -0.535 | +0.460 | -0.579 | 0.509 | 396 | Growth tilt; Aggressive investment |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| IREN | +99.47% | +1.659 | +0.670 | -0.108 | -3.405 | -1.018 | 0.307 | 396 | Small-cap tilt; Weak profitability; Aggressive investment |
| CRM | -25.69% | +0.795 | +0.210 | -0.375 | -0.437 | -0.022 | 0.311 | 396 | Neutral profile |
| AVGO | +49.64% | +1.663 | -0.143 | -1.319 | +0.104 | -0.162 | 0.473 | 396 | Growth tilt |
| NBIS | +171.20% | +1.642 | +0.745 | -2.284 | -2.007 | -0.014 | 0.295 | 360 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| DTE | +1.56% | +0.293 | -0.201 | +0.557 | -0.228 | +0.079 | 0.147 | 396 | Value tilt; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **90.00** | 23.33 | 33.33 | 33.33 | 0.324 | +2.276 | 1.1587 | 0.0591 | 146 |
| NBIS | **83.33** | 26.67 | 26.67 | 30.00 | 0.310 | +1.201 | 1.1584 | 0.0591 | 146 |
| IREN | **70.00** | 13.33 | 30.00 | 26.67 | 0.365 | +1.675 | 1.0929 | 0.0557 | 146 |
| MU | **66.67** | 20.00 | 23.33 | 23.33 | 0.336 | +0.777 | 0.6781 | 0.0346 | 146 |
| MRVL | **63.33** | 30.00 | 13.33 | 20.00 | 0.308 | +0.138 | 0.5858 | 0.0299 | 146 |
| DTE | **43.33** | 33.33 | 6.67 | 3.33 | 0.059 | +0.051 | 0.1852 | 0.0094 | 146 |
| AVGO | **40.00** | 6.67 | 16.67 | 16.67 | 0.469 | +0.462 | 0.4254 | 0.0217 | 146 |
| META | **40.00** | 16.67 | 10.00 | 13.33 | 0.348 | +0.061 | 0.3537 | 0.0180 | 146 |
| NVDA | **30.00** | 3.33 | 20.00 | 6.67 | 0.667 | +0.578 | 0.2566 | 0.0131 | 146 |
| CRM | **23.33** | 10.00 | 3.33 | 10.00 | 0.465 | -1.597 | 0.3340 | 0.0170 | 146 |

## Per-ticker FF5 Detail

### NVDA

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.6740 (adjusted = 0.6698)
- Alpha (annualized): **+20.73%** (daily = +0.000822, t = +0.97, p = 0.3321)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6688 | +18.65 | 0.0000 *** |
| SMB | -0.8296 | -5.40 | 0.0000 *** |
| HML | -1.1603 | -8.36 | 0.0000 *** |
| RMW | -0.3085 | -1.82 | 0.0699  |
| CMA | +1.2791 | +7.09 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### MU

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.3900 (adjusted = 0.3822)
- Alpha (annualized): **+72.15%** (daily = +0.002863, t = +1.80, p = 0.0725)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9516 | +11.62 | 0.0000 *** |
| SMB | -0.2460 | -0.85 | 0.3947  |
| HML | -0.1546 | -0.59 | 0.5532  |
| RMW | -0.9809 | -3.08 | 0.0022 ** |
| CMA | +0.3447 | +1.02 | 0.3097  |

_Interpretation: Weak profitability_

### MRVL

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.4374 (adjusted = 0.4302)
- Alpha (annualized): **+17.29%** (daily = +0.000686, t = +0.43, p = 0.6700)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9742 | +11.62 | 0.0000 *** |
| SMB | -0.5631 | -1.93 | 0.0546  |
| HML | -0.7015 | -2.66 | 0.0081 ** |
| RMW | -1.2191 | -3.78 | 0.0002 *** |
| CMA | +0.8607 | +2.51 | 0.0124 * |

_Interpretation: Large-cap tilt; Growth tilt; Weak profitability; Conservative investment_

### META

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.5087 (adjusted = 0.5024)
- Alpha (annualized): **+3.79%** (daily = +0.000150, t = +0.18, p = 0.8538)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3834 | +16.05 | 0.0000 *** |
| SMB | -0.0144 | -0.10 | 0.9224  |
| HML | -0.5351 | -4.01 | 0.0001 *** |
| RMW | +0.4597 | +2.81 | 0.0052 ** |
| CMA | -0.5794 | -3.33 | 0.0009 *** |

_Interpretation: Growth tilt; Aggressive investment_

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

### IREN

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.3066 (adjusted = 0.2977)
- Alpha (annualized): **+99.47%** (daily = +0.003947, t = +1.41, p = 0.1582)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6594 | +5.63 | 0.0000 *** |
| SMB | +0.6700 | +1.32 | 0.1870  |
| HML | -0.1078 | -0.24 | 0.8137  |
| RMW | -3.4046 | -6.08 | 0.0000 *** |
| CMA | -1.0176 | -1.71 | 0.0879  |

_Interpretation: Small-cap tilt; Weak profitability; Aggressive investment_

### CRM

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.3107 (adjusted = 0.3019)
- Alpha (annualized): **-25.69%** (daily = -0.001019, t = -1.12, p = 0.2631)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7946 | +8.27 | 0.0000 *** |
| SMB | +0.2101 | +1.27 | 0.2041  |
| HML | -0.3748 | -2.52 | 0.0123 * |
| RMW | -0.4371 | -2.40 | 0.0170 * |
| CMA | -0.0223 | -0.12 | 0.9084  |

_Interpretation: Neutral profile_

### AVGO

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.4731 (adjusted = 0.4663)
- Alpha (annualized): **+49.64%** (daily = +0.001970, t = +1.57, p = 0.1183)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6627 | +12.51 | 0.0000 *** |
| SMB | -0.1428 | -0.62 | 0.5325  |
| HML | -1.3187 | -6.40 | 0.0000 *** |
| RMW | +0.1044 | +0.41 | 0.6792  |
| CMA | -0.1623 | -0.61 | 0.5454  |

_Interpretation: Growth tilt_

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

### DTE

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.1469 (adjusted = 0.1359)
- Alpha (annualized): **+1.56%** (daily = +0.000062, t = +0.12, p = 0.9027)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2928 | +5.47 | 0.0000 *** |
| SMB | -0.2013 | -2.19 | 0.0293 * |
| HML | +0.5565 | +6.70 | 0.0000 *** |
| RMW | -0.2281 | -2.25 | 0.0253 * |
| CMA | +0.0790 | +0.73 | 0.4646  |

_Interpretation: Value tilt; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._