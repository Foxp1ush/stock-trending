# Weekly Report — `wallstreetbets` — 2026-W34

Generated: 2026-08-23  ·  Source: `apewisdom:wallstreetbets`  ·  Lookback: 7 days

[← Back to dashboard](2026-W34.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MRNA | -28.88% | +0.670 | +0.870 | -0.171 | -2.043 | +1.607 | 0.243 | 401 | Small-cap tilt; Weak profitability; Conservative investment |
| MU | +66.20% | +1.945 | -0.280 | -0.167 | -0.988 | +0.314 | 0.388 | 401 | Weak profitability |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| NVDA | +20.06% | +1.677 | -0.825 | -1.155 | -0.321 | +1.362 | 0.671 | 401 | Large-cap tilt; Growth tilt; Conservative investment |
| RDDT | +63.30% | +1.588 | -0.151 | -0.741 | -1.289 | -0.437 | 0.247 | 401 | Growth tilt; Weak profitability |
| META | +2.22% | +1.381 | -0.031 | -0.533 | +0.458 | -0.586 | 0.508 | 401 | Growth tilt; Aggressive investment |
| NBIS | +171.20% | +1.642 | +0.745 | -2.284 | -2.007 | -0.014 | 0.295 | 360 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| DTE | +1.54% | +0.291 | -0.195 | +0.554 | -0.226 | +0.072 | 0.146 | 401 | Value tilt; Modest factor fit |
| TSLA | +28.35% | +2.215 | +0.046 | -0.022 | -0.215 | -1.254 | 0.445 | 401 | Aggressive investment |
| GOOG | +34.22% | +1.018 | +0.235 | -0.533 | +0.499 | -0.704 | 0.449 | 401 | Growth tilt; Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **86.67** | 20.00 | 33.33 | 33.33 | 0.319 | +2.212 | 1.1385 | 0.0584 | 151 |
| NBIS | **83.33** | 23.33 | 30.00 | 30.00 | 0.311 | +1.217 | 1.1353 | 0.0582 | 151 |
| MU | **63.33** | 16.67 | 26.67 | 20.00 | 0.338 | +0.762 | 0.6652 | 0.0341 | 151 |
| MRNA | **60.00** | 26.67 | 6.67 | 26.67 | 0.288 | -0.231 | 0.7312 | 0.0375 | 151 |
| RDDT | **56.67** | 30.00 | 3.33 | 23.33 | 0.256 | -0.741 | 0.6847 | 0.0351 | 151 |
| DTE | **50.00** | 33.33 | 13.33 | 3.33 | 0.061 | +0.043 | 0.1832 | 0.0094 | 151 |
| META | **43.33** | 13.33 | 16.67 | 13.33 | 0.349 | +0.066 | 0.3467 | 0.0178 | 151 |
| GOOG | **40.00** | 10.00 | 20.00 | 10.00 | 0.375 | +0.176 | 0.2789 | 0.0143 | 151 |
| TSLA | **33.33** | 6.67 | 10.00 | 16.67 | 0.410 | -0.119 | 0.4047 | 0.0208 | 151 |
| NVDA | **33.33** | 3.33 | 23.33 | 6.67 | 0.665 | +0.586 | 0.2541 | 0.0130 | 151 |

## Per-ticker FF5 Detail

### MRNA

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.2432 (adjusted = 0.2337)
- Alpha (annualized): **-28.88%** (daily = -0.001146, t = -0.61, p = 0.5425)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6700 | +3.36 | 0.0009 *** |
| SMB | +0.8697 | +2.56 | 0.0108 * |
| HML | -0.1711 | -0.55 | 0.5799  |
| RMW | -2.0431 | -5.39 | 0.0000 *** |
| CMA | +1.6075 | +4.04 | 0.0001 *** |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment_

### MU

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.3882 (adjusted = 0.3804)
- Alpha (annualized): **+66.20%** (daily = +0.002627, t = +1.67, p = 0.0966)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9446 | +11.61 | 0.0000 *** |
| SMB | -0.2797 | -0.98 | 0.3269  |
| HML | -0.1666 | -0.64 | 0.5205  |
| RMW | -0.9876 | -3.11 | 0.0020 ** |
| CMA | +0.3135 | +0.94 | 0.3486  |

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

### NVDA

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.6714 (adjusted = 0.6673)
- Alpha (annualized): **+20.06%** (daily = +0.000796, t = +0.94, p = 0.3491)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6769 | +18.60 | 0.0000 *** |
| SMB | -0.8248 | -5.38 | 0.0000 *** |
| HML | -1.1554 | -8.28 | 0.0000 *** |
| RMW | -0.3208 | -1.88 | 0.0615  |
| CMA | +1.3617 | +7.57 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### RDDT

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.2471 (adjusted = 0.2376)
- Alpha (annualized): **+63.30%** (daily = +0.002512, t = +1.13, p = 0.2589)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5882 | +6.73 | 0.0000 *** |
| SMB | -0.1512 | -0.38 | 0.7067  |
| HML | -0.7412 | -2.03 | 0.0430 * |
| RMW | -1.2893 | -2.88 | 0.0042 ** |
| CMA | -0.4369 | -0.93 | 0.3538  |

_Interpretation: Growth tilt; Weak profitability_

### META

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.5077 (adjusted = 0.5015)
- Alpha (annualized): **+2.22%** (daily = +0.000088, t = +0.11, p = 0.9132)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3815 | +16.12 | 0.0000 *** |
| SMB | -0.0311 | -0.21 | 0.8312  |
| HML | -0.5333 | -4.02 | 0.0001 *** |
| RMW | +0.4580 | +2.82 | 0.0051 ** |
| CMA | -0.5855 | -3.43 | 0.0007 *** |

_Interpretation: Growth tilt; Aggressive investment_

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

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.1460 (adjusted = 0.1352)
- Alpha (annualized): **+1.54%** (daily = +0.000061, t = +0.12, p = 0.9033)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2907 | +5.46 | 0.0000 *** |
| SMB | -0.1954 | -2.16 | 0.0316 * |
| HML | +0.5545 | +6.73 | 0.0000 *** |
| RMW | -0.2260 | -2.24 | 0.0258 * |
| CMA | +0.0719 | +0.68 | 0.4986  |

_Interpretation: Value tilt; Modest factor fit_

### TSLA

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.4451 (adjusted = 0.4381)
- Alpha (annualized): **+28.35%** (daily = +0.001125, t = +0.76, p = 0.4467)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2154 | +14.13 | 0.0000 *** |
| SMB | +0.0463 | +0.17 | 0.8623  |
| HML | -0.0217 | -0.09 | 0.9288  |
| RMW | -0.2150 | -0.72 | 0.4705  |
| CMA | -1.2544 | -4.01 | 0.0001 *** |

_Interpretation: Aggressive investment_

### GOOG

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.4494 (adjusted = 0.4425)
- Alpha (annualized): **+34.22%** (daily = +0.001358, t = +1.91, p = 0.0563)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0177 | +13.51 | 0.0000 *** |
| SMB | +0.2349 | +1.83 | 0.0676  |
| HML | -0.5335 | -4.58 | 0.0000 *** |
| RMW | +0.4985 | +3.49 | 0.0005 *** |
| CMA | -0.7040 | -4.68 | 0.0000 *** |

_Interpretation: Growth tilt; Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._