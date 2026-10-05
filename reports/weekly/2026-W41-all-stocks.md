# Weekly Report — `all-stocks` — 2026-W41

Generated: 2026-10-05  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W41.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +73.89% | +1.974 | -0.272 | -0.131 | -0.917 | +0.204 | 0.399 | 372 | Weak profitability |
| NKE | -22.67% | +1.058 | +1.024 | -0.113 | +1.050 | +0.672 | 0.335 | 372 | Small-cap tilt; Robust profitability; Conservative investment |
| NVDA | +23.28% | +1.646 | -0.841 | -1.104 | -0.314 | +1.157 | 0.662 | 372 | Large-cap tilt; Growth tilt; Conservative investment |
| DTE | -0.81% | +0.294 | -0.206 | +0.557 | -0.243 | +0.110 | 0.152 | 372 | Value tilt; Modest factor fit |
| META | -1.06% | +1.378 | -0.004 | -0.555 | +0.431 | -0.537 | 0.507 | 372 | Growth tilt; Aggressive investment |
| GOOG | +37.69% | +1.009 | +0.173 | -0.508 | +0.462 | -0.733 | 0.445 | 372 | Growth tilt; Aggressive investment; Significant positive alpha |
| GOOGL | +38.85% | +1.017 | +0.167 | -0.523 | +0.489 | -0.748 | 0.440 | 372 | Growth tilt; Aggressive investment; Significant positive alpha |
| TSLA | +24.11% | +2.202 | +0.049 | +0.009 | -0.205 | -1.267 | 0.446 | 372 | Aggressive investment |
| AMD | +2.77% | +1.588 | -0.585 | -0.406 | -1.674 | -0.276 | 0.473 | 372 | Large-cap tilt; Weak profitability |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **96.67** | 30.00 | 33.33 | 33.33 | 0.351 | +2.702 | 1.2711 | 0.0593 | 122 |
| MU | **86.67** | 26.67 | 30.00 | 30.00 | 0.385 | +1.183 | 0.7394 | 0.0345 | 122 |
| AMD | **56.67** | 6.67 | 23.33 | 26.67 | 0.519 | +0.652 | 0.6673 | 0.0311 | 122 |
| META | **56.67** | 23.33 | 13.33 | 20.00 | 0.392 | +0.050 | 0.3984 | 0.0186 | 122 |
| GOOGL | **50.00** | 20.00 | 16.67 | 13.33 | 0.432 | +0.162 | 0.2897 | 0.0135 | 122 |
| DTE | **46.67** | 33.33 | 10.00 | 3.33 | 0.067 | +0.041 | 0.2080 | 0.0097 | 122 |
| GOOG | **46.67** | 16.67 | 20.00 | 10.00 | 0.437 | +0.165 | 0.2823 | 0.0132 | 122 |
| TSLA | **40.00** | 10.00 | 6.67 | 23.33 | 0.492 | -0.024 | 0.4013 | 0.0187 | 122 |
| NVDA | **36.67** | 3.33 | 26.67 | 6.67 | 0.707 | +0.671 | 0.2705 | 0.0126 | 122 |
| NKE | **33.33** | 13.33 | 3.33 | 16.67 | 0.449 | -0.541 | 0.3407 | 0.0159 | 122 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.3989 (adjusted = 0.3907)
- Alpha (annualized): **+73.89%** (daily = +0.002932, t = +1.80, p = 0.0721)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9745 | +11.69 | 0.0000 *** |
| SMB | -0.2723 | -0.92 | 0.3600  |
| HML | -0.1308 | -0.49 | 0.6211  |
| RMW | -0.9167 | -2.84 | 0.0047 ** |
| CMA | +0.2045 | +0.59 | 0.5543  |

_Interpretation: Weak profitability_

### NKE

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.3347 (adjusted = 0.3256)
- Alpha (annualized): **-22.67%** (daily = -0.000900, t = -0.89, p = 0.3742)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0582 | +10.07 | 0.0000 *** |
| SMB | +1.0236 | +5.54 | 0.0000 *** |
| HML | -0.1129 | -0.69 | 0.4930  |
| RMW | +1.0504 | +5.23 | 0.0000 *** |
| CMA | +0.6723 | +3.13 | 0.0019 ** |

_Interpretation: Small-cap tilt; Robust profitability; Conservative investment_

### NVDA

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.6622 (adjusted = 0.6576)
- Alpha (annualized): **+23.28%** (daily = +0.000924, t = +1.05, p = 0.2946)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6464 | +18.01 | 0.0000 *** |
| SMB | -0.8405 | -5.22 | 0.0000 *** |
| HML | -1.1037 | -7.71 | 0.0000 *** |
| RMW | -0.3142 | -1.80 | 0.0730  |
| CMA | +1.1575 | +6.19 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### DTE

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.1522 (adjusted = 0.1406)
- Alpha (annualized): **-0.81%** (daily = -0.000032, t = -0.06, p = 0.9517)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2943 | +5.37 | 0.0000 *** |
| SMB | -0.2060 | -2.14 | 0.0331 * |
| HML | +0.5571 | +6.50 | 0.0000 *** |
| RMW | -0.2433 | -2.33 | 0.0206 * |
| CMA | +0.1100 | +0.98 | 0.3268  |

_Interpretation: Value tilt; Modest factor fit_

### META

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.5066 (adjusted = 0.4999)
- Alpha (annualized): **-1.06%** (daily = -0.000042, t = -0.05, p = 0.9609)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3781 | +15.41 | 0.0000 *** |
| SMB | -0.0042 | -0.03 | 0.9786  |
| HML | -0.5549 | -3.96 | 0.0001 *** |
| RMW | +0.4308 | +2.52 | 0.0121 * |
| CMA | -0.5367 | -2.93 | 0.0036 ** |

_Interpretation: Growth tilt; Aggressive investment_

### GOOG

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.4453 (adjusted = 0.4377)
- Alpha (annualized): **+37.69%** (daily = +0.001495, t = +1.99, p = 0.0476)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0087 | +12.91 | 0.0000 *** |
| SMB | +0.1729 | +1.26 | 0.2094  |
| HML | -0.5084 | -4.15 | 0.0000 *** |
| RMW | +0.4622 | +3.09 | 0.0021 ** |
| CMA | -0.7326 | -4.58 | 0.0000 *** |

_Interpretation: Growth tilt; Aggressive investment; Significant positive alpha_

### GOOGL

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.4398 (adjusted = 0.4322)
- Alpha (annualized): **+38.85%** (daily = +0.001542, t = +2.01, p = 0.0453)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0169 | +12.76 | 0.0000 *** |
| SMB | +0.1669 | +1.19 | 0.2348  |
| HML | -0.5232 | -4.19 | 0.0000 *** |
| RMW | +0.4888 | +3.21 | 0.0014 ** |
| CMA | -0.7484 | -4.59 | 0.0000 *** |

_Interpretation: Growth tilt; Aggressive investment; Significant positive alpha_

### TSLA

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.4461 (adjusted = 0.4386)
- Alpha (annualized): **+24.11%** (daily = +0.000957, t = +0.62, p = 0.5379)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2020 | +13.66 | 0.0000 *** |
| SMB | +0.0490 | +0.17 | 0.8630  |
| HML | +0.0085 | +0.03 | 0.9732  |
| RMW | -0.2048 | -0.66 | 0.5065  |
| CMA | -1.2670 | -3.84 | 0.0001 *** |

_Interpretation: Aggressive investment_

### AMD

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.4727 (adjusted = 0.4655)
- Alpha (annualized): **+2.77%** (daily = +0.000110, t = +0.08, p = 0.9379)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5876 | +10.83 | 0.0000 *** |
| SMB | -0.5849 | -2.27 | 0.0239 * |
| HML | -0.4064 | -1.77 | 0.0775  |
| RMW | -1.6742 | -5.98 | 0.0000 *** |
| CMA | -0.2761 | -0.92 | 0.3578  |

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

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._