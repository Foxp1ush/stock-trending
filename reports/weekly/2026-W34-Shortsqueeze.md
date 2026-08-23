# Weekly Report — `Shortsqueeze` — 2026-W34

Generated: 2026-08-23  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W34.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +54.76% | +1.023 | +2.130 | +0.661 | +0.368 | +0.342 | 0.104 | 401 | Small-cap tilt; Value tilt; Modest factor fit |
| BYND | -37.65% | +0.986 | +0.777 | +0.274 | -1.312 | +1.909 | 0.029 | 401 | Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| ALL | -2.22% | +0.687 | -0.245 | +0.776 | +0.313 | -0.116 | 0.217 | 401 | Value tilt |
| AMD | +6.36% | +1.615 | -0.571 | -0.459 | -1.653 | -0.187 | 0.483 | 401 | Large-cap tilt; Weak profitability |
| BB | +14.86% | +1.030 | +0.219 | -0.410 | -1.274 | +0.802 | 0.286 | 401 | Weak profitability; Conservative investment |
| AMZN | +4.56% | +1.332 | +0.026 | -0.370 | +0.289 | -0.509 | 0.555 | 401 | Aggressive investment |
| AAPL | +1.73% | +1.331 | -0.111 | -0.063 | +0.751 | +0.168 | 0.539 | 401 | Robust profitability |
| ES | -2.85% | +0.378 | -0.075 | +0.454 | -0.121 | +0.313 | 0.092 | 401 | Modest factor fit |
| ET | +4.81% | +0.742 | -0.213 | +0.355 | -0.296 | +0.356 | 0.317 | 401 | Neutral profile |
| GOOG | +34.22% | +1.018 | +0.235 | -0.533 | +0.499 | -0.704 | 0.449 | 401 | Growth tilt; Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| HTZ | **76.67** | 23.33 | 23.33 | 30.00 | 0.111 | +0.079 | 0.8911 | 0.0457 | 151 |
| BYND | **70.00** | 33.33 | 3.33 | 33.33 | 0.047 | -2.601 | 3.5132 | 0.1801 | 151 |
| ES | **66.67** | 30.00 | 16.67 | 20.00 | 0.056 | -0.157 | 0.3280 | 0.0168 | 151 |
| AMD | **63.33** | 3.33 | 33.33 | 26.67 | 0.490 | +0.694 | 0.5763 | 0.0295 | 151 |
| GOOG | **53.33** | 10.00 | 30.00 | 13.33 | 0.375 | +0.176 | 0.2789 | 0.0143 | 151 |
| ET | **50.00** | 26.67 | 20.00 | 3.33 | 0.080 | +0.070 | 0.1884 | 0.0097 | 151 |
| BB | **46.67** | 16.67 | 6.67 | 23.33 | 0.230 | -0.492 | 0.4355 | 0.0223 | 151 |
| AAPL | **46.67** | 13.33 | 26.67 | 6.67 | 0.318 | +0.087 | 0.2263 | 0.0116 | 151 |
| ALL | **43.33** | 20.00 | 13.33 | 10.00 | 0.220 | -0.238 | 0.2463 | 0.0126 | 151 |
| AMZN | **33.33** | 6.67 | 10.00 | 16.67 | 0.419 | -0.463 | 0.2903 | 0.0149 | 151 |

## Per-ticker FF5 Detail

### HTZ

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.1043 (adjusted = 0.0929)
- Alpha (annualized): **+54.76%** (daily = +0.002173, t = +0.73, p = 0.4663)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0226 | +3.23 | 0.0013 ** |
| SMB | +2.1298 | +3.95 | 0.0001 *** |
| HML | +0.6608 | +1.35 | 0.1779  |
| RMW | +0.3678 | +0.61 | 0.5406  |
| CMA | +0.3423 | +0.54 | 0.5880  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### BYND

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.0291 (adjusted = 0.0168)
- Alpha (annualized): **-37.65%** (daily = -0.001494, t = -0.26, p = 0.7987)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9864 | +1.59 | 0.1135  |
| SMB | +0.7773 | +0.73 | 0.4630  |
| HML | +0.2737 | +0.28 | 0.7762  |
| RMW | -1.3122 | -1.11 | 0.2668  |
| CMA | +1.9094 | +1.54 | 0.1246  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### ALL

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.2175 (adjusted = 0.2075)
- Alpha (annualized): **-2.22%** (daily = -0.000088, t = -0.13, p = 0.8999)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6869 | +9.25 | 0.0000 *** |
| SMB | -0.2453 | -1.94 | 0.0529  |
| HML | +0.7764 | +6.76 | 0.0000 *** |
| RMW | +0.3135 | +2.23 | 0.0266 * |
| CMA | -0.1155 | -0.78 | 0.4359  |

_Interpretation: Value tilt_

### AMD

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.4832 (adjusted = 0.4766)
- Alpha (annualized): **+6.36%** (daily = +0.000252, t = +0.19, p = 0.8487)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6147 | +11.50 | 0.0000 *** |
| SMB | -0.5712 | -2.39 | 0.0173 * |
| HML | -0.4590 | -2.11 | 0.0352 * |
| RMW | -1.6533 | -6.21 | 0.0000 *** |
| CMA | -0.1870 | -0.67 | 0.5047  |

_Interpretation: Large-cap tilt; Weak profitability_

### BB

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.2864 (adjusted = 0.2774)
- Alpha (annualized): **+14.86%** (daily = +0.000590, t = +0.40, p = 0.6868)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0299 | +6.64 | 0.0000 *** |
| SMB | +0.2188 | +0.83 | 0.4078  |
| HML | -0.4097 | -1.71 | 0.0887  |
| RMW | -1.2743 | -4.33 | 0.0000 *** |
| CMA | +0.8024 | +2.59 | 0.0099 ** |

_Interpretation: Weak profitability; Conservative investment_

### AMZN

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.5548 (adjusted = 0.5492)
- Alpha (annualized): **+4.56%** (daily = +0.000181, t = +0.26, p = 0.7956)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3320 | +17.98 | 0.0000 *** |
| SMB | +0.0256 | +0.20 | 0.8392  |
| HML | -0.3696 | -3.23 | 0.0014 ** |
| RMW | +0.2894 | +2.06 | 0.0402 * |
| CMA | -0.5093 | -3.45 | 0.0006 *** |

_Interpretation: Aggressive investment_

### AAPL

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.5387 (adjusted = 0.5328)
- Alpha (annualized): **+1.73%** (daily = +0.000069, t = +0.11, p = 0.9122)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3307 | +20.10 | 0.0000 *** |
| SMB | -0.1108 | -0.98 | 0.3258  |
| HML | -0.0634 | -0.62 | 0.5364  |
| RMW | +0.7512 | +5.98 | 0.0000 *** |
| CMA | +0.1684 | +1.28 | 0.2030  |

_Interpretation: Robust profitability_

### ES

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.0921 (adjusted = 0.0806)
- Alpha (annualized): **-2.85%** (daily = -0.000113, t = -0.15, p = 0.8816)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3778 | +4.68 | 0.0000 *** |
| SMB | -0.0753 | -0.55 | 0.5834  |
| HML | +0.4537 | +3.63 | 0.0003 *** |
| RMW | -0.1208 | -0.79 | 0.4306  |
| CMA | +0.3133 | +1.95 | 0.0523  |

_Interpretation: Modest factor fit_

### ET

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.3173 (adjusted = 0.3086)
- Alpha (annualized): **+4.81%** (daily = +0.000191, t = +0.31, p = 0.7569)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7422 | +11.36 | 0.0000 *** |
| SMB | -0.2127 | -1.91 | 0.0566  |
| HML | +0.3555 | +3.52 | 0.0005 *** |
| RMW | -0.2963 | -2.39 | 0.0174 * |
| CMA | +0.3562 | +2.73 | 0.0066 ** |

_Interpretation: Neutral profile_

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