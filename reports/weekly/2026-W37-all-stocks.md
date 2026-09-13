# Weekly Report — `all-stocks` — 2026-W37

Generated: 2026-09-13  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W37.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| AGI | +50.66% | +0.211 | -0.315 | -0.314 | -1.079 | +0.246 | 0.093 | 387 | Weak profitability; Modest factor fit |
| MU | +79.89% | +1.964 | -0.285 | -0.134 | -0.992 | +0.324 | 0.388 | 387 | Weak profitability |
| ORCL | -2.32% | +1.295 | -0.303 | -0.790 | -0.360 | -0.576 | 0.293 | 387 | Growth tilt; Aggressive investment |
| NVDA | +22.88% | +1.650 | -0.853 | -1.107 | -0.335 | +1.217 | 0.663 | 387 | Large-cap tilt; Growth tilt; Conservative investment |
| AAPL | +2.15% | +1.349 | -0.138 | -0.063 | +0.746 | +0.202 | 0.544 | 387 | Robust profitability |
| DTE | +1.03% | +0.292 | -0.195 | +0.550 | -0.224 | +0.086 | 0.145 | 387 | Value tilt; Modest factor fit |
| META | +3.77% | +1.388 | -0.025 | -0.541 | +0.451 | -0.560 | 0.506 | 387 | Growth tilt; Aggressive investment |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| NBIS | +171.20% | +1.642 | +0.745 | -2.284 | -2.007 | -0.014 | 0.295 | 360 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| TSLA | +24.24% | +2.216 | +0.049 | -0.009 | -0.180 | -1.272 | 0.445 | 387 | Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **93.33** | 26.67 | 33.33 | 33.33 | 0.333 | +2.309 | 1.1839 | 0.0585 | 137 |
| MU | **76.67** | 23.33 | 26.67 | 26.67 | 0.345 | +0.827 | 0.7016 | 0.0347 | 137 |
| AGI | **73.33** | 30.00 | 20.00 | 23.33 | 0.212 | +0.574 | 0.6545 | 0.0324 | 137 |
| NBIS | **70.00** | 10.00 | 30.00 | 30.00 | 0.419 | +1.352 | 0.9230 | 0.0456 | 137 |
| DTE | **46.67** | 33.33 | 10.00 | 3.33 | 0.061 | +0.057 | 0.1942 | 0.0096 | 137 |
| AAPL | **43.33** | 20.00 | 16.67 | 6.67 | 0.358 | +0.105 | 0.2243 | 0.0111 | 137 |
| META | **43.33** | 16.67 | 13.33 | 13.33 | 0.364 | +0.095 | 0.3693 | 0.0183 | 137 |
| ORCL | **40.00** | 13.33 | 6.67 | 20.00 | 0.386 | -0.109 | 0.5172 | 0.0256 | 137 |
| NVDA | **36.67** | 3.33 | 23.33 | 10.00 | 0.668 | +0.577 | 0.2675 | 0.0132 | 137 |
| TSLA | **26.67** | 6.67 | 3.33 | 16.67 | 0.448 | -0.129 | 0.4005 | 0.0198 | 137 |

## Per-ticker FF5 Detail

### AGI

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.0926 (adjusted = 0.0807)
- Alpha (annualized): **+50.66%** (daily = +0.002010, t = +1.42, p = 0.1568)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2115 | +1.42 | 0.1575  |
| SMB | -0.3149 | -1.22 | 0.2232  |
| HML | -0.3143 | -1.35 | 0.1791  |
| RMW | -1.0786 | -3.80 | 0.0002 *** |
| CMA | +0.2460 | +0.82 | 0.4155  |

_Interpretation: Weak profitability; Modest factor fit_

### MU

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.3879 (adjusted = 0.3798)
- Alpha (annualized): **+79.89%** (daily = +0.003170, t = +1.96, p = 0.0505)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9644 | +11.54 | 0.0000 *** |
| SMB | -0.2849 | -0.97 | 0.3336  |
| HML | -0.1336 | -0.50 | 0.6160  |
| RMW | -0.9915 | -3.07 | 0.0023 ** |
| CMA | +0.3241 | +0.94 | 0.3469  |

_Interpretation: Weak profitability_

### ORCL

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.2929 (adjusted = 0.2836)
- Alpha (annualized): **-2.32%** (daily = -0.000092, t = -0.06, p = 0.9514)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2953 | +8.13 | 0.0000 *** |
| SMB | -0.3026 | -1.10 | 0.2726  |
| HML | -0.7896 | -3.17 | 0.0016 ** |
| RMW | -0.3605 | -1.19 | 0.2343  |
| CMA | -0.5759 | -1.79 | 0.0745  |

_Interpretation: Growth tilt; Aggressive investment_

### NVDA

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.6629 (adjusted = 0.6585)
- Alpha (annualized): **+22.88%** (daily = +0.000908, t = +1.06, p = 0.2891)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6501 | +18.31 | 0.0000 *** |
| SMB | -0.8531 | -5.47 | 0.0000 *** |
| HML | -1.1068 | -7.85 | 0.0000 *** |
| RMW | -0.3346 | -1.95 | 0.0514  |
| CMA | +1.2170 | +6.68 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### AAPL

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.5437 (adjusted = 0.5377)
- Alpha (annualized): **+2.15%** (daily = +0.000085, t = +0.13, p = 0.8938)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3491 | +20.03 | 0.0000 *** |
| SMB | -0.1378 | -1.18 | 0.2374  |
| HML | -0.0632 | -0.60 | 0.5491  |
| RMW | +0.7461 | +5.83 | 0.0000 *** |
| CMA | +0.2016 | +1.48 | 0.1396  |

_Interpretation: Robust profitability_

### DTE

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.1449 (adjusted = 0.1336)
- Alpha (annualized): **+1.03%** (daily = +0.000041, t = +0.08, p = 0.9366)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2916 | +5.37 | 0.0000 *** |
| SMB | -0.1949 | -2.08 | 0.0384 * |
| HML | +0.5499 | +6.48 | 0.0000 *** |
| RMW | -0.2240 | -2.17 | 0.0304 * |
| CMA | +0.0858 | +0.78 | 0.4344  |

_Interpretation: Value tilt; Modest factor fit_

### META

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.5060 (adjusted = 0.4995)
- Alpha (annualized): **+3.77%** (daily = +0.000150, t = +0.18, p = 0.8575)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3879 | +15.82 | 0.0000 *** |
| SMB | -0.0253 | -0.17 | 0.8676  |
| HML | -0.5411 | -3.94 | 0.0001 *** |
| RMW | +0.4509 | +2.71 | 0.0071 ** |
| CMA | -0.5598 | -3.16 | 0.0017 ** |

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

### TSLA

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.4453 (adjusted = 0.4380)
- Alpha (annualized): **+24.24%** (daily = +0.000962, t = +0.64, p = 0.5237)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2157 | +13.96 | 0.0000 *** |
| SMB | +0.0494 | +0.18 | 0.8574  |
| HML | -0.0094 | -0.04 | 0.9697  |
| RMW | -0.1795 | -0.60 | 0.5520  |
| CMA | -1.2721 | -3.96 | 0.0001 *** |

_Interpretation: Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._