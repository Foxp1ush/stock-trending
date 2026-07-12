# Weekly Report — `Shortsqueeze` — 2026-W28

Generated: 2026-07-12  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W28.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| LFVN | +6.36% | +0.751 | +1.312 | -0.750 | +0.669 | +0.172 | 0.090 | 431 | Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit |
| IQ | -64.82% | +0.992 | +0.085 | +0.127 | -0.742 | +0.296 | 0.128 | 431 | Weak profitability; Modest factor fit |
| AAPL | +0.58% | +1.303 | -0.095 | -0.050 | +0.748 | +0.097 | 0.536 | 431 | Robust profitability |
| ALL | +4.04% | +0.703 | -0.339 | +0.812 | +0.353 | -0.164 | 0.216 | 431 | Value tilt |
| CC | -3.13% | +1.767 | +1.858 | +0.308 | +0.192 | +1.249 | 0.444 | 431 | Small-cap tilt; Conservative investment |
| AMZN | -1.06% | +1.352 | +0.048 | -0.336 | +0.271 | -0.564 | 0.564 | 431 | Aggressive investment |
| BB | +11.83% | +1.018 | +0.290 | -0.380 | -1.281 | +0.723 | 0.305 | 431 | Weak profitability; Conservative investment |
| BE | +155.05% | +1.432 | -0.089 | -0.047 | -2.660 | -1.759 | 0.208 | 431 | Weak profitability; Aggressive investment; Significant positive alpha |
| CRM | -21.68% | +0.801 | +0.260 | -0.345 | -0.436 | -0.052 | 0.329 | 431 | Neutral profile |
| MSFT | -15.14% | +0.885 | -0.265 | -0.406 | +0.137 | -0.504 | 0.520 | 431 | Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| BE | **83.33** | 16.67 | 33.33 | 33.33 | 0.367 | +2.005 | 0.9422 | 0.0542 | 181 |
| IQ | **76.67** | 33.33 | 20.00 | 23.33 | 0.126 | -0.154 | 0.4924 | 0.0283 | 181 |
| CC | **66.67** | 10.00 | 30.00 | 26.67 | 0.418 | +0.209 | 0.5395 | 0.0311 | 181 |
| LFVN | **63.33** | 26.67 | 6.67 | 30.00 | 0.185 | -0.744 | 0.5602 | 0.0322 | 181 |
| ALL | **63.33** | 30.00 | 23.33 | 10.00 | 0.164 | -0.071 | 0.2359 | 0.0136 | 181 |
| BB | **56.67** | 23.33 | 13.33 | 20.00 | 0.262 | -0.456 | 0.3673 | 0.0211 | 181 |
| AAPL | **53.33** | 20.00 | 26.67 | 6.67 | 0.336 | +0.058 | 0.2038 | 0.0117 | 181 |
| AMZN | **43.33** | 13.33 | 16.67 | 13.33 | 0.398 | -0.429 | 0.2656 | 0.0153 | 181 |
| CRM | **23.33** | 3.33 | 3.33 | 16.67 | 0.447 | -1.506 | 0.2845 | 0.0164 | 181 |
| MSFT | **20.00** | 6.67 | 10.00 | 3.33 | 0.424 | -0.469 | 0.2003 | 0.0115 | 181 |

## Per-ticker FF5 Detail

### LFVN

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.0902 (adjusted = 0.0795)
- Alpha (annualized): **+6.36%** (daily = +0.000252, t = +0.13, p = 0.9001)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7505 | +3.51 | 0.0005 *** |
| SMB | +1.3124 | +3.67 | 0.0003 *** |
| HML | -0.7496 | -2.29 | 0.0228 * |
| RMW | +0.6686 | +1.62 | 0.1053  |
| CMA | +0.1722 | +0.41 | 0.6801  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit_

### IQ

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.1276 (adjusted = 0.1173)
- Alpha (annualized): **-64.82%** (daily = -0.002572, t = -1.48, p = 0.1398)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9916 | +5.36 | 0.0000 *** |
| SMB | +0.0853 | +0.28 | 0.7829  |
| HML | +0.1275 | +0.45 | 0.6538  |
| RMW | -0.7420 | -2.08 | 0.0381 * |
| CMA | +0.2963 | +0.82 | 0.4127  |

_Interpretation: Weak profitability; Modest factor fit_

### AAPL

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.5356 (adjusted = 0.5301)
- Alpha (annualized): **+0.58%** (daily = +0.000023, t = +0.04, p = 0.9692)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3027 | +20.54 | 0.0000 *** |
| SMB | -0.0951 | -0.90 | 0.3699  |
| HML | -0.0497 | -0.51 | 0.6097  |
| RMW | +0.7481 | +6.12 | 0.0000 *** |
| CMA | +0.0967 | +0.78 | 0.4351  |

_Interpretation: Robust profitability_

### ALL

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.2165 (adjusted = 0.2072)
- Alpha (annualized): **+4.04%** (daily = +0.000160, t = +0.23, p = 0.8160)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7025 | +9.59 | 0.0000 *** |
| SMB | -0.3392 | -2.77 | 0.0059 ** |
| HML | +0.8124 | +7.23 | 0.0000 *** |
| RMW | +0.3526 | +2.50 | 0.0129 * |
| CMA | -0.1643 | -1.15 | 0.2513  |

_Interpretation: Value tilt_

### CC

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.4439 (adjusted = 0.4374)
- Alpha (annualized): **-3.13%** (daily = -0.000124, t = -0.09, p = 0.9310)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7674 | +11.58 | 0.0000 *** |
| SMB | +1.8583 | +7.28 | 0.0000 *** |
| HML | +0.3083 | +1.32 | 0.1887  |
| RMW | +0.1922 | +0.65 | 0.5137  |
| CMA | +1.2485 | +4.19 | 0.0000 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### AMZN

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.5637 (adjusted = 0.5585)
- Alpha (annualized): **-1.06%** (daily = -0.000042, t = -0.06, p = 0.9500)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3519 | +18.88 | 0.0000 *** |
| SMB | +0.0477 | +0.40 | 0.6904  |
| HML | -0.3357 | -3.06 | 0.0024 ** |
| RMW | +0.2712 | +1.97 | 0.0500 * |
| CMA | -0.5642 | -4.04 | 0.0001 *** |

_Interpretation: Aggressive investment_

### BB

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.3046 (adjusted = 0.2964)
- Alpha (annualized): **+11.83%** (daily = +0.000469, t = +0.34, p = 0.7311)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0185 | +7.01 | 0.0000 *** |
| SMB | +0.2897 | +1.19 | 0.2337  |
| HML | -0.3803 | -1.71 | 0.0888  |
| RMW | -1.2815 | -4.58 | 0.0000 *** |
| CMA | +0.7229 | +2.55 | 0.0112 * |

_Interpretation: Weak profitability; Conservative investment_

### BE

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.2078 (adjusted = 0.1985)
- Alpha (annualized): **+155.05%** (daily = +0.006153, t = +2.19, p = 0.0288)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4321 | +4.79 | 0.0000 *** |
| SMB | -0.0892 | -0.18 | 0.8583  |
| HML | -0.0468 | -0.10 | 0.9188  |
| RMW | -2.6599 | -4.62 | 0.0000 *** |
| CMA | -1.7594 | -3.02 | 0.0027 ** |

_Interpretation: Weak profitability; Aggressive investment; Significant positive alpha_

### CRM

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.3288 (adjusted = 0.3209)
- Alpha (annualized): **-21.68%** (daily = -0.000860, t = -1.02, p = 0.3095)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8006 | +8.89 | 0.0000 *** |
| SMB | +0.2605 | +1.73 | 0.0842  |
| HML | -0.3453 | -2.50 | 0.0128 * |
| RMW | -0.4356 | -2.51 | 0.0124 * |
| CMA | -0.0518 | -0.29 | 0.7685  |

_Interpretation: Neutral profile_

### MSFT

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.5197 (adjusted = 0.5141)
- Alpha (annualized): **-15.14%** (daily = -0.000601, t = -1.14, p = 0.2556)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8854 | +15.75 | 0.0000 *** |
| SMB | -0.2654 | -2.82 | 0.0050 ** |
| HML | -0.4064 | -4.71 | 0.0000 *** |
| RMW | +0.1367 | +1.26 | 0.2074  |
| CMA | -0.5042 | -4.60 | 0.0000 *** |

_Interpretation: Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._