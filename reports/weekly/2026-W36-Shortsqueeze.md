# Weekly Report — `Shortsqueeze` — 2026-W36

Generated: 2026-09-06  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W36.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +62.67% | +1.036 | +2.140 | +0.688 | +0.369 | +0.269 | 0.103 | 392 | Small-cap tilt; Value tilt; Modest factor fit |
| GPRO | -6.53% | +1.154 | +2.027 | -0.639 | -1.498 | -0.007 | 0.200 | 392 | Small-cap tilt; Growth tilt; Weak profitability |
| SLS | +97.45% | +0.219 | +0.660 | +0.178 | -1.896 | -0.978 | 0.078 | 392 | Small-cap tilt; Weak profitability; Aggressive investment; Modest factor fit |
| MSTR | -0.77% | +1.666 | +0.584 | -0.099 | -2.714 | -0.582 | 0.345 | 392 | Small-cap tilt; Weak profitability; Aggressive investment |
| API | +82.91% | +0.076 | +0.664 | -1.340 | -1.614 | +0.770 | 0.063 | 392 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| ARR | -7.54% | +0.629 | +0.090 | +0.211 | -0.295 | +0.382 | 0.271 | 392 | Neutral profile |
| FCF | -9.78% | +0.992 | +0.965 | +1.206 | +0.201 | -0.260 | 0.708 | 392 | Small-cap tilt; Value tilt |
| GRRR | +120.81% | +1.428 | +0.109 | -0.796 | -2.535 | +1.171 | 0.139 | 392 | Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| OPEN | +121.93% | +1.271 | +1.961 | -0.644 | -1.320 | +1.405 | 0.098 | 392 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| HOOD | +61.21% | +2.262 | -0.172 | +0.022 | -2.495 | -0.589 | 0.561 | 392 | Weak profitability; Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| HTZ | **83.33** | 33.33 | 26.67 | 23.33 | 0.108 | +0.106 | 0.9289 | 0.0468 | 142 |
| SLS | **83.33** | 20.00 | 33.33 | 30.00 | 0.160 | +0.827 | 1.1310 | 0.0570 | 142 |
| OPEN | **70.00** | 23.33 | 13.33 | 33.33 | 0.155 | -0.245 | 1.6795 | 0.0847 | 142 |
| GPRO | **63.33** | 16.67 | 20.00 | 26.67 | 0.307 | -0.068 | 1.0414 | 0.0525 | 142 |
| ARR | **63.33** | 26.67 | 30.00 | 6.67 | 0.150 | +0.137 | 0.2831 | 0.0143 | 142 |
| GRRR | **56.67** | 13.33 | 23.33 | 20.00 | 0.346 | +0.020 | 0.7781 | 0.0392 | 142 |
| API | **50.00** | 30.00 | 10.00 | 10.00 | 0.127 | -0.268 | 0.5432 | 0.0274 | 142 |
| MSTR | **30.00** | 10.00 | 3.33 | 16.67 | 0.408 | -0.556 | 0.7364 | 0.0371 | 142 |
| HOOD | **26.67** | 6.67 | 6.67 | 13.33 | 0.556 | -0.360 | 0.6008 | 0.0303 | 142 |
| FCF | **23.33** | 3.33 | 16.67 | 3.33 | 0.696 | -0.120 | 0.1652 | 0.0083 | 142 |

## Per-ticker FF5 Detail

### HTZ

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.1032 (adjusted = 0.0916)
- Alpha (annualized): **+62.67%** (daily = +0.002487, t = +0.82, p = 0.4133)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0355 | +3.23 | 0.0013 ** |
| SMB | +2.1398 | +3.88 | 0.0001 *** |
| HML | +0.6880 | +1.38 | 0.1689  |
| RMW | +0.3695 | +0.61 | 0.5423  |
| CMA | +0.2690 | +0.42 | 0.6778  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### GPRO

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.2005 (adjusted = 0.1901)
- Alpha (annualized): **-6.53%** (daily = -0.000259, t = -0.09, p = 0.9259)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1543 | +3.92 | 0.0001 *** |
| SMB | +2.0270 | +4.01 | 0.0001 *** |
| HML | -0.6389 | -1.40 | 0.1635  |
| RMW | -1.4985 | -2.70 | 0.0073 ** |
| CMA | -0.0069 | -0.01 | 0.9907  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### SLS

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.0781 (adjusted = 0.0662)
- Alpha (annualized): **+97.45%** (daily = +0.003867, t = +1.38, p = 0.1672)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2191 | +0.74 | 0.4585  |
| SMB | +0.6602 | +1.30 | 0.1937  |
| HML | +0.1777 | +0.39 | 0.6990  |
| RMW | -1.8955 | -3.40 | 0.0007 *** |
| CMA | -0.9780 | -1.64 | 0.1013  |

_Interpretation: Small-cap tilt; Weak profitability; Aggressive investment; Modest factor fit_

### MSTR

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.3446 (adjusted = 0.3362)
- Alpha (annualized): **-0.77%** (daily = -0.000030, t = -0.01, p = 0.9893)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6661 | +6.95 | 0.0000 *** |
| SMB | +0.5840 | +1.42 | 0.1569  |
| HML | -0.0990 | -0.27 | 0.7909  |
| RMW | -2.7137 | -5.99 | 0.0000 *** |
| CMA | -0.5822 | -1.20 | 0.2293  |

_Interpretation: Small-cap tilt; Weak profitability; Aggressive investment_

### API

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.0632 (adjusted = 0.0511)
- Alpha (annualized): **+82.91%** (daily = +0.003290, t = +0.97, p = 0.3323)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.0764 | +0.21 | 0.8311  |
| SMB | +0.6643 | +1.08 | 0.2808  |
| HML | -1.3398 | -2.40 | 0.0166 * |
| RMW | -1.6137 | -2.39 | 0.0175 * |
| CMA | +0.7697 | +1.07 | 0.2871  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### ARR

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.2712 (adjusted = 0.2617)
- Alpha (annualized): **-7.54%** (daily = -0.000299, t = -0.45, p = 0.6520)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6288 | +8.98 | 0.0000 *** |
| SMB | +0.0899 | +0.75 | 0.4553  |
| HML | +0.2108 | +1.93 | 0.0537  |
| RMW | -0.2953 | -2.23 | 0.0261 * |
| CMA | +0.3818 | +2.70 | 0.0072 ** |

_Interpretation: Neutral profile_

### FCF

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.7077 (adjusted = 0.7039)
- Alpha (annualized): **-9.78%** (daily = -0.000388, t = -0.79, p = 0.4328)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9921 | +19.01 | 0.0000 *** |
| SMB | +0.9653 | +10.77 | 0.0000 *** |
| HML | +1.2061 | +14.85 | 0.0000 *** |
| RMW | +0.2008 | +2.04 | 0.0424 * |
| CMA | -0.2598 | -2.47 | 0.0141 * |

_Interpretation: Small-cap tilt; Value tilt_

### GRRR

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.1390 (adjusted = 0.1278)
- Alpha (annualized): **+120.81%** (daily = +0.004794, t = +1.27, p = 0.2040)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4280 | +3.59 | 0.0004 *** |
| SMB | +0.1089 | +0.16 | 0.8735  |
| HML | -0.7957 | -1.28 | 0.1997  |
| RMW | -2.5351 | -3.37 | 0.0008 *** |
| CMA | +1.1715 | +1.46 | 0.1453  |

_Interpretation: Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### OPEN

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.0982 (adjusted = 0.0865)
- Alpha (annualized): **+121.93%** (daily = +0.004838, t = +1.13, p = 0.2598)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2711 | +2.81 | 0.0053 ** |
| SMB | +1.9613 | +2.52 | 0.0121 * |
| HML | -0.6435 | -0.91 | 0.3617  |
| RMW | -1.3201 | -1.54 | 0.1235  |
| CMA | +1.4049 | +1.54 | 0.1249  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### HOOD

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.5611 (adjusted = 0.5554)
- Alpha (annualized): **+61.21%** (daily = +0.002429, t = +1.54, p = 0.1253)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2616 | +13.54 | 0.0000 *** |
| SMB | -0.1720 | -0.60 | 0.5491  |
| HML | +0.0223 | +0.09 | 0.9317  |
| RMW | -2.4949 | -7.91 | 0.0000 *** |
| CMA | -0.5885 | -1.75 | 0.0814  |

_Interpretation: Weak profitability; Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._