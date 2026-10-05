# Weekly Report — `Shortsqueeze` — 2026-W41

Generated: 2026-10-05  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W41.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| BE | +186.14% | +1.346 | -0.279 | +0.064 | -2.698 | -2.046 | 0.197 | 372 | Weak profitability; Aggressive investment; Significant positive alpha; Modest factor fit |
| API | +13.51% | +0.170 | +1.050 | -1.405 | -1.166 | +0.356 | 0.091 | 372 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| BB | +17.85% | +1.017 | +0.224 | -0.443 | -1.236 | +0.807 | 0.278 | 372 | Weak profitability; Conservative investment |
| ASTS | +106.40% | +1.308 | +1.088 | -1.150 | -2.949 | -0.258 | 0.312 | 372 | Small-cap tilt; Growth tilt; Weak profitability |
| ES | -2.00% | +0.384 | -0.072 | +0.447 | -0.129 | +0.356 | 0.095 | 372 | Modest factor fit |
| EU | -25.89% | +0.859 | +1.552 | -1.207 | -0.997 | -0.112 | 0.176 | 372 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| GME | +17.74% | +0.553 | +0.923 | -0.703 | -0.137 | +0.069 | 0.118 | 372 | Small-cap tilt; Growth tilt; Modest factor fit |
| HTZ | +54.93% | +1.021 | +2.101 | +0.648 | +0.323 | +0.309 | 0.099 | 372 | Small-cap tilt; Value tilt; Modest factor fit |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| TTD | -90.38% | +1.183 | +0.345 | -0.776 | -0.203 | +0.099 | 0.162 | 372 | Growth tilt; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **73.33** | 10.00 | 30.00 | 33.33 | 0.351 | +2.702 | 1.2711 | 0.0593 | 122 |
| HTZ | **73.33** | 30.00 | 20.00 | 23.33 | 0.112 | -0.091 | 1.0303 | 0.0481 | 122 |
| EU | **63.33** | 16.67 | 26.67 | 20.00 | 0.325 | +1.403 | 0.9027 | 0.0421 | 122 |
| BE | **63.33** | 3.33 | 33.33 | 26.67 | 0.506 | +3.229 | 1.0948 | 0.0511 | 122 |
| ASTS | **60.00** | 6.67 | 23.33 | 30.00 | 0.395 | +0.374 | 1.1833 | 0.0552 | 122 |
| API | **53.33** | 26.67 | 10.00 | 16.67 | 0.147 | -0.483 | 0.5844 | 0.0273 | 122 |
| ES | **50.00** | 33.33 | 13.33 | 3.33 | 0.066 | -0.167 | 0.3582 | 0.0167 | 122 |
| GME | **46.67** | 23.33 | 16.67 | 6.67 | 0.180 | -0.129 | 0.4250 | 0.0198 | 122 |
| BB | **36.67** | 20.00 | 6.67 | 10.00 | 0.309 | -0.687 | 0.4347 | 0.0203 | 122 |
| TTD | **30.00** | 13.33 | 3.33 | 13.33 | 0.337 | -1.848 | 0.5634 | 0.0263 | 122 |

## Per-ticker FF5 Detail

### BE

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.1974 (adjusted = 0.1865)
- Alpha (annualized): **+186.14%** (daily = +0.007387, t = +2.32, p = 0.0206)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3463 | +4.08 | 0.0001 *** |
| SMB | -0.2787 | -0.48 | 0.6315  |
| HML | +0.0643 | +0.12 | 0.9010  |
| RMW | -2.6975 | -4.28 | 0.0000 *** |
| CMA | -2.0460 | -3.03 | 0.0026 ** |

_Interpretation: Weak profitability; Aggressive investment; Significant positive alpha; Modest factor fit_

### API

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.0914 (adjusted = 0.0790)
- Alpha (annualized): **+13.51%** (daily = +0.000536, t = +0.19, p = 0.8491)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.1704 | +0.58 | 0.5605  |
| SMB | +1.0496 | +2.04 | 0.0420 * |
| HML | -1.4051 | -3.07 | 0.0023 ** |
| RMW | -1.1661 | -2.09 | 0.0376 * |
| CMA | +0.3564 | +0.60 | 0.5518  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### BB

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.2782 (adjusted = 0.2684)
- Alpha (annualized): **+17.85%** (daily = +0.000708, t = +0.46, p = 0.6474)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0170 | +6.33 | 0.0000 *** |
| SMB | +0.2244 | +0.79 | 0.4278  |
| HML | -0.4432 | -1.76 | 0.0791  |
| RMW | -1.2362 | -4.03 | 0.0001 *** |
| CMA | +0.8071 | +2.45 | 0.0146 * |

_Interpretation: Weak profitability; Conservative investment_

### ASTS

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.3121 (adjusted = 0.3027)
- Alpha (annualized): **+106.40%** (daily = +0.004222, t = +1.53, p = 0.1261)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3081 | +4.57 | 0.0000 *** |
| SMB | +1.0882 | +2.16 | 0.0312 * |
| HML | -1.1500 | -2.57 | 0.0107 * |
| RMW | -2.9486 | -5.39 | 0.0000 *** |
| CMA | -0.2575 | -0.44 | 0.6602  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### ES

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.0947 (adjusted = 0.0824)
- Alpha (annualized): **-2.00%** (daily = -0.000079, t = -0.10, p = 0.9223)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3843 | +4.56 | 0.0000 *** |
| SMB | -0.0720 | -0.49 | 0.6271  |
| HML | +0.4465 | +3.38 | 0.0008 *** |
| RMW | -0.1293 | -0.80 | 0.4223  |
| CMA | +0.3563 | +2.07 | 0.0395 * |

_Interpretation: Modest factor fit_

### EU

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.1756 (adjusted = 0.1644)
- Alpha (annualized): **-25.89%** (daily = -0.001027, t = -0.40, p = 0.6895)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8590 | +3.22 | 0.0014 ** |
| SMB | +1.5521 | +3.31 | 0.0010 ** |
| HML | -1.2074 | -2.89 | 0.0041 ** |
| RMW | -0.9973 | -1.96 | 0.0513  |
| CMA | -0.1124 | -0.21 | 0.8370  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### GME

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.1184 (adjusted = 0.1064)
- Alpha (annualized): **+17.74%** (daily = +0.000704, t = +0.42, p = 0.6739)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5529 | +3.18 | 0.0016 ** |
| SMB | +0.9231 | +3.02 | 0.0027 ** |
| HML | -0.7028 | -2.58 | 0.0101 * |
| RMW | -0.1371 | -0.41 | 0.6797  |
| CMA | +0.0693 | +0.20 | 0.8455  |

_Interpretation: Small-cap tilt; Growth tilt; Modest factor fit_

### HTZ

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.0994 (adjusted = 0.0871)
- Alpha (annualized): **+54.93%** (daily = +0.002180, t = +0.69, p = 0.4893)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0215 | +3.12 | 0.0019 ** |
| SMB | +2.1006 | +3.65 | 0.0003 *** |
| HML | +0.6480 | +1.26 | 0.2069  |
| RMW | +0.3235 | +0.52 | 0.6052  |
| CMA | +0.3087 | +0.46 | 0.6450  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

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

### TTD

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.1618 (adjusted = 0.1504)
- Alpha (annualized): **-90.38%** (daily = -0.003586, t = -1.74, p = 0.0821)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1830 | +5.54 | 0.0000 *** |
| SMB | +0.3454 | +0.92 | 0.3589  |
| HML | -0.7760 | -2.32 | 0.0210 * |
| RMW | -0.2035 | -0.50 | 0.6186  |
| CMA | +0.0992 | +0.23 | 0.8207  |

_Interpretation: Growth tilt; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._