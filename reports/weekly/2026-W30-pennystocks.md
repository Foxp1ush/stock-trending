# Weekly Report — `pennystocks` — 2026-W30

Generated: 2026-07-26  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W30.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| BATL | +264.54% | +0.013 | +0.765 | -1.809 | +2.658 | -0.382 | 0.008 | 421 | Small-cap tilt; Growth tilt; Robust profitability; Low explanatory power — likely sentiment-driven |
| OTLK | -113.31% | +0.400 | +1.516 | -1.539 | -0.185 | +0.049 | 0.044 | 421 | Small-cap tilt; Growth tilt; Low explanatory power — likely sentiment-driven |
| VIVK | -145.71% | -0.033 | +0.387 | -0.064 | -1.513 | +0.376 | 0.008 | 421 | Weak profitability; Low explanatory power — likely sentiment-driven |
| LASE | +112.97% | +1.243 | +0.944 | -0.096 | -0.279 | -1.261 | 0.025 | 421 | Small-cap tilt; Aggressive investment; Low explanatory power — likely sentiment-driven |
| HMR | -109.85% | +0.254 | +0.514 | +0.107 | +0.096 | +1.182 | 0.010 | 278 | Small-cap tilt; Conservative investment; Low explanatory power — likely sentiment-driven |
| AMC | -95.32% | +0.831 | +0.599 | -0.265 | -0.172 | +0.387 | 0.136 | 421 | Small-cap tilt; Significant negative alpha; Modest factor fit |
| WBUY | +93.81% | -0.189 | +0.747 | -0.616 | -3.112 | -0.472 | 0.019 | 421 | Small-cap tilt; Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven |
| ES | +0.81% | +0.364 | -0.094 | +0.460 | -0.090 | +0.254 | 0.084 | 421 | Modest factor fit |
| CSAI | -101.47% | +1.371 | +1.782 | -3.936 | +0.257 | +1.093 | 0.065 | 292 | Small-cap tilt; Growth tilt; Conservative investment; Modest factor fit |
| GOOG | +28.80% | +1.019 | +0.224 | -0.494 | +0.479 | -0.737 | 0.452 | 421 | Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| BATL | **76.67** | 33.33 | 10.00 | 33.33 | 0.018 | -1.084 | 4.0331 | 0.2274 | 171 |
| VIVK | **70.00** | 23.33 | 16.67 | 30.00 | 0.044 | -0.713 | 2.7272 | 0.1538 | 171 |
| WBUY | **66.67** | 26.67 | 13.33 | 26.67 | 0.038 | -0.796 | 2.0004 | 0.1128 | 171 |
| HMR | **66.67** | 30.00 | 23.33 | 13.33 | 0.020 | -0.359 | 0.7518 | 0.0424 | 171 |
| CSAI | **56.67** | 10.00 | 30.00 | 16.67 | 0.091 | -0.076 | 1.2419 | 0.0700 | 171 |
| ES | **50.00** | 16.67 | 26.67 | 6.67 | 0.064 | -0.126 | 0.2871 | 0.0162 | 171 |
| OTLK | **46.67** | 20.00 | 6.67 | 20.00 | 0.058 | -1.471 | 1.5969 | 0.0900 | 171 |
| GOOG | **40.00** | 3.33 | 33.33 | 3.33 | 0.373 | +0.090 | 0.2477 | 0.0140 | 171 |
| LASE | **40.00** | 13.33 | 3.33 | 23.33 | 0.071 | -1.997 | 1.9630 | 0.1107 | 171 |
| AMC | **36.67** | 6.67 | 20.00 | 10.00 | 0.160 | -0.496 | 0.5076 | 0.0286 | 171 |

## Per-ticker FF5 Detail

### BATL

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.0083 (adjusted = -0.0037)
- Alpha (annualized): **+264.54%** (daily = +0.010498, t = +1.26, p = 0.2083)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.0125 | +0.01 | 0.9887  |
| SMB | +0.7651 | +0.51 | 0.6129  |
| HML | -1.8094 | -1.33 | 0.1855  |
| RMW | +2.6579 | +1.57 | 0.1174  |
| CMA | -0.3816 | -0.22 | 0.8247  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Low explanatory power — likely sentiment-driven_

### OTLK

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.0441 (adjusted = 0.0326)
- Alpha (annualized): **-113.31%** (daily = -0.004497, t = -1.20, p = 0.2318)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3998 | +1.01 | 0.3148  |
| SMB | +1.5156 | +2.23 | 0.0266 * |
| HML | -1.5395 | -2.50 | 0.0127 * |
| RMW | -0.1847 | -0.24 | 0.8089  |
| CMA | +0.0486 | +0.06 | 0.9501  |

_Interpretation: Small-cap tilt; Growth tilt; Low explanatory power — likely sentiment-driven_

### VIVK

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.0085 (adjusted = -0.0035)
- Alpha (annualized): **-145.71%** (daily = -0.005782, t = -1.05, p = 0.2955)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.0332 | -0.06 | 0.9548  |
| SMB | +0.3871 | +0.39 | 0.6993  |
| HML | -0.0639 | -0.07 | 0.9437  |
| RMW | -1.5126 | -1.35 | 0.1785  |
| CMA | +0.3760 | +0.33 | 0.7418  |

_Interpretation: Weak profitability; Low explanatory power — likely sentiment-driven_

### LASE

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.0246 (adjusted = 0.0129)
- Alpha (annualized): **+112.97%** (daily = +0.004483, t = +0.78, p = 0.4358)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2432 | +2.04 | 0.0415 * |
| SMB | +0.9445 | +0.91 | 0.3654  |
| HML | -0.0959 | -0.10 | 0.9189  |
| RMW | -0.2788 | -0.24 | 0.8115  |
| CMA | -1.2611 | -1.06 | 0.2888  |

_Interpretation: Small-cap tilt; Aggressive investment; Low explanatory power — likely sentiment-driven_

### HMR

- Period: `2025-02-21` to `2026-03-31` (278 obs)
- R² = 0.0104 (adjusted = -0.0078)
- Alpha (annualized): **-109.85%** (daily = -0.004359, t = -0.87, p = 0.3843)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2541 | +0.52 | 0.6045  |
| SMB | +0.5144 | +0.56 | 0.5753  |
| HML | +0.1071 | +0.12 | 0.9053  |
| RMW | +0.0965 | +0.10 | 0.9197  |
| CMA | +1.1819 | +0.99 | 0.3233  |

_Interpretation: Small-cap tilt; Conservative investment; Low explanatory power — likely sentiment-driven_

### AMC

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.1356 (adjusted = 0.1252)
- Alpha (annualized): **-95.32%** (daily = -0.003783, t = -2.49, p = 0.0132)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8305 | +5.17 | 0.0000 *** |
| SMB | +0.5994 | +2.17 | 0.0302 * |
| HML | -0.2654 | -1.07 | 0.2867  |
| RMW | -0.1720 | -0.56 | 0.5780  |
| CMA | +0.3871 | +1.23 | 0.2182  |

_Interpretation: Small-cap tilt; Significant negative alpha; Modest factor fit_

### WBUY

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.0190 (adjusted = 0.0072)
- Alpha (annualized): **+93.81%** (daily = +0.003723, t = +0.47, p = 0.6369)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.1888 | -0.23 | 0.8209  |
| SMB | +0.7468 | +0.52 | 0.6017  |
| HML | -0.6163 | -0.48 | 0.6333  |
| RMW | -3.1116 | -1.94 | 0.0528  |
| CMA | -0.4719 | -0.29 | 0.7721  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

### ES

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.0841 (adjusted = 0.0731)
- Alpha (annualized): **+0.81%** (daily = +0.000032, t = +0.04, p = 0.9651)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3638 | +4.65 | 0.0000 *** |
| SMB | -0.0937 | -0.70 | 0.4847  |
| HML | +0.4598 | +3.80 | 0.0002 *** |
| RMW | -0.0900 | -0.60 | 0.5496  |
| CMA | +0.2544 | +1.67 | 0.0964  |

_Interpretation: Modest factor fit_

### CSAI

- Period: `2025-01-31` to `2026-03-31` (292 obs)
- R² = 0.0652 (adjusted = 0.0488)
- Alpha (annualized): **-101.47%** (daily = -0.004027, t = -0.50, p = 0.6204)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3705 | +1.71 | 0.0893  |
| SMB | +1.7821 | +1.19 | 0.2344  |
| HML | -3.9362 | -2.68 | 0.0078 ** |
| RMW | +0.2571 | +0.17 | 0.8679  |
| CMA | +1.0929 | +0.57 | 0.5684  |

_Interpretation: Small-cap tilt; Growth tilt; Conservative investment; Modest factor fit_

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

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._