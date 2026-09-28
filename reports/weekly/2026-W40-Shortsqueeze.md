# Weekly Report — `Shortsqueeze` — 2026-W40

Generated: 2026-09-28  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W40.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **9 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| UA | -10.80% | +1.147 | +1.246 | -0.498 | +0.566 | +1.335 | 0.255 | 377 | Small-cap tilt; Robust profitability; Conservative investment |
| ANY | — | — | — | — | — | — | — | — | _insufficient_data_ |
| API | +77.07% | +0.081 | +0.742 | -1.408 | -1.552 | +0.752 | 0.063 | 377 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| ASTS | +108.17% | +1.320 | +1.137 | -1.140 | -2.923 | -0.267 | 0.313 | 377 | Small-cap tilt; Growth tilt; Weak profitability |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| AMC | -97.43% | +0.886 | +0.579 | -0.199 | -0.126 | +0.336 | 0.128 | 377 | Small-cap tilt; Significant negative alpha; Modest factor fit |
| HTZ | +55.83% | +1.023 | +2.106 | +0.644 | +0.352 | +0.277 | 0.100 | 377 | Small-cap tilt; Value tilt; Modest factor fit |
| LOT | -82.13% | +1.022 | +0.767 | +0.035 | -0.442 | +0.400 | 0.095 | 377 | Small-cap tilt; Modest factor fit |
| LINK | +56.99% | -0.026 | +1.221 | -0.266 | -1.947 | +0.112 | 0.060 | 377 | Small-cap tilt; Weak profitability; Modest factor fit |
| META | +1.49% | +1.379 | -0.013 | -0.553 | +0.445 | -0.542 | 0.505 | 377 | Growth tilt; Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| LINK | **88.89** | 33.33 | 29.63 | 25.93 | 0.095 | +0.430 | 1.1304 | 0.0535 | 127 |
| SNDK | **77.78** | 11.11 | 33.33 | 33.33 | 0.333 | +2.363 | 1.2718 | 0.0602 | 127 |
| HTZ | **74.07** | 29.63 | 22.22 | 22.22 | 0.108 | +0.035 | 1.0047 | 0.0475 | 127 |
| LOT | **55.56** | 25.93 | 11.11 | 18.52 | 0.134 | -0.191 | 0.7335 | 0.0347 | 127 |
| ASTS | **51.85** | 7.41 | 14.81 | 29.63 | 0.377 | -0.028 | 1.2060 | 0.0571 | 127 |
| UA | **44.44** | 14.81 | 18.52 | 11.11 | 0.313 | +0.012 | 0.5952 | 0.0282 | 127 |
| API | **37.04** | 22.22 | 7.41 | 7.41 | 0.142 | -0.388 | 0.5706 | 0.0270 | 127 |
| AMC | **37.04** | 18.52 | 3.70 | 14.81 | 0.162 | -0.692 | 0.6516 | 0.0308 | 127 |
| META | **33.33** | 3.70 | 25.93 | 3.70 | 0.383 | +0.122 | 0.3914 | 0.0185 | 127 |

## Per-ticker FF5 Detail

### UA

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.2546 (adjusted = 0.2445)
- Alpha (annualized): **-10.80%** (daily = -0.000429, t = -0.28, p = 0.7798)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1472 | +7.16 | 0.0000 *** |
| SMB | +1.2464 | +4.44 | 0.0000 *** |
| HML | -0.4978 | -1.98 | 0.0481 * |
| RMW | +0.5660 | +1.86 | 0.0641  |
| CMA | +1.3354 | +4.09 | 0.0001 *** |

_Interpretation: Small-cap tilt; Robust profitability; Conservative investment_

### ANY

Status: `insufficient_data` — price history only 50 days


### API

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.0635 (adjusted = 0.0508)
- Alpha (annualized): **+77.07%** (daily = +0.003058, t = +0.87, p = 0.3850)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.0808 | +0.22 | 0.8260  |
| SMB | +0.7417 | +1.15 | 0.2507  |
| HML | -1.4079 | -2.44 | 0.0150 * |
| RMW | -1.5515 | -2.22 | 0.0271 * |
| CMA | +0.7515 | +1.00 | 0.3162  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### ASTS

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.3126 (adjusted = 0.3033)
- Alpha (annualized): **+108.17%** (daily = +0.004293, t = +1.57, p = 0.1163)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3205 | +4.63 | 0.0000 *** |
| SMB | +1.1368 | +2.27 | 0.0235 * |
| HML | -1.1402 | -2.55 | 0.0111 * |
| RMW | -2.9235 | -5.39 | 0.0000 *** |
| CMA | -0.2665 | -0.46 | 0.6465  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

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

### AMC

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.1284 (adjusted = 0.1167)
- Alpha (annualized): **-97.43%** (daily = -0.003866, t = -2.33, p = 0.0204)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8855 | +5.11 | 0.0000 *** |
| SMB | +0.5790 | +1.90 | 0.0578  |
| HML | -0.1994 | -0.73 | 0.4637  |
| RMW | -0.1261 | -0.38 | 0.7025  |
| CMA | +0.3360 | +0.95 | 0.3423  |

_Interpretation: Small-cap tilt; Significant negative alpha; Modest factor fit_

### HTZ

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.0995 (adjusted = 0.0874)
- Alpha (annualized): **+55.83%** (daily = +0.002216, t = +0.71, p = 0.4764)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0228 | +3.15 | 0.0018 ** |
| SMB | +2.1059 | +3.70 | 0.0003 *** |
| HML | +0.6443 | +1.27 | 0.2065  |
| RMW | +0.3521 | +0.57 | 0.5693  |
| CMA | +0.2775 | +0.42 | 0.6753  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### LOT

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.0951 (adjusted = 0.0829)
- Alpha (annualized): **-82.13%** (daily = -0.003259, t = -1.34, p = 0.1796)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0225 | +4.04 | 0.0001 *** |
| SMB | +0.7666 | +1.73 | 0.0853  |
| HML | +0.0354 | +0.09 | 0.9291  |
| RMW | -0.4421 | -0.92 | 0.3596  |
| CMA | +0.3998 | +0.77 | 0.4390  |

_Interpretation: Small-cap tilt; Modest factor fit_

### LINK

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.0596 (adjusted = 0.0469)
- Alpha (annualized): **+56.99%** (daily = +0.002262, t = +0.65, p = 0.5172)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.0261 | -0.07 | 0.9430  |
| SMB | +1.2208 | +1.91 | 0.0570  |
| HML | -0.2656 | -0.46 | 0.6423  |
| RMW | -1.9475 | -2.81 | 0.0053 ** |
| CMA | +0.1124 | +0.15 | 0.8798  |

_Interpretation: Small-cap tilt; Weak profitability; Modest factor fit_

### META

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.5045 (adjusted = 0.4979)
- Alpha (annualized): **+1.49%** (daily = +0.000059, t = +0.07, p = 0.9446)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3792 | +15.49 | 0.0000 *** |
| SMB | -0.0128 | -0.08 | 0.9350  |
| HML | -0.5535 | -3.97 | 0.0001 *** |
| RMW | +0.4453 | +2.63 | 0.0089 ** |
| CMA | -0.5418 | -2.99 | 0.0030 ** |

_Interpretation: Growth tilt; Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._