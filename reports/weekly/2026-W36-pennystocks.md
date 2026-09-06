# Weekly Report — `pennystocks` — 2026-W36

Generated: 2026-09-06  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W36.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| GPRO | -6.53% | +1.154 | +2.027 | -0.639 | -1.498 | -0.007 | 0.200 | 392 | Small-cap tilt; Growth tilt; Weak profitability |
| VIVK | -144.78% | -0.058 | +0.520 | -0.162 | -1.544 | +0.425 | 0.009 | 392 | Small-cap tilt; Weak profitability; Low explanatory power — likely sentiment-driven |
| FAMI | -30.40% | +0.482 | +0.819 | +0.886 | -0.928 | -0.792 | 0.063 | 392 | Small-cap tilt; Value tilt; Weak profitability; Aggressive investment; Modest factor fit |
| AKAN | -210.46% | +0.164 | +0.179 | -0.723 | -1.892 | +1.412 | 0.054 | 392 | Growth tilt; Weak profitability; Conservative investment; Significant negative alpha; Modest factor fit |
| AIM | -152.91% | +1.084 | +0.323 | +0.554 | -1.169 | +0.931 | 0.028 | 392 | Value tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| IP | -24.58% | +1.145 | +0.472 | +0.583 | +0.332 | +0.929 | 0.323 | 392 | Value tilt; Conservative investment |
| GME | +12.47% | +0.497 | +0.891 | -0.608 | -0.174 | -0.054 | 0.097 | 392 | Small-cap tilt; Growth tilt; Modest factor fit |
| GELS | +96.79% | +1.724 | +3.357 | -0.130 | +1.297 | -1.579 | 0.033 | 354 | Small-cap tilt; Robust profitability; Aggressive investment; Low explanatory power — likely sentiment-driven |
| OPTT | +141.76% | +1.278 | +1.454 | -0.858 | -1.766 | +0.956 | 0.075 | 392 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| SOUN | +56.17% | +1.832 | +1.409 | -1.793 | -2.092 | +0.498 | 0.338 | 392 | Small-cap tilt; Growth tilt; Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| AIM | **93.33** | 33.33 | 33.33 | 26.67 | 0.049 | +0.956 | 1.6870 | 0.0850 | 142 |
| FAMI | **66.67** | 26.67 | 26.67 | 13.33 | 0.081 | -0.000 | 0.8208 | 0.0414 | 142 |
| OPTT | **66.67** | 13.33 | 30.00 | 23.33 | 0.194 | +0.242 | 1.3357 | 0.0673 | 142 |
| VIVK | **66.67** | 30.00 | 3.33 | 33.33 | 0.070 | -1.257 | 3.2527 | 0.1640 | 142 |
| AKAN | **60.00** | 23.33 | 6.67 | 30.00 | 0.094 | -1.078 | 1.6948 | 0.0854 | 142 |
| GPRO | **50.00** | 10.00 | 23.33 | 16.67 | 0.307 | -0.068 | 1.0414 | 0.0525 | 142 |
| GELS | **50.00** | 20.00 | 10.00 | 20.00 | 0.098 | -0.575 | 1.1757 | 0.0593 | 142 |
| GME | **43.33** | 16.67 | 20.00 | 6.67 | 0.179 | -0.090 | 0.4089 | 0.0206 | 142 |
| IP | **26.67** | 6.67 | 16.67 | 3.33 | 0.375 | -0.297 | 0.4038 | 0.0204 | 142 |
| SOUN | **26.67** | 3.33 | 13.33 | 10.00 | 0.532 | -0.366 | 0.6264 | 0.0316 | 142 |

## Per-ticker FF5 Detail

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

### VIVK

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.0091 (adjusted = -0.0037)
- Alpha (annualized): **-144.78%** (daily = -0.005745, t = -0.97, p = 0.3322)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.0584 | -0.09 | 0.9257  |
| SMB | +0.5203 | +0.48 | 0.6283  |
| HML | -0.1621 | -0.17 | 0.8677  |
| RMW | -1.5438 | -1.31 | 0.1918  |
| CMA | +0.4254 | +0.34 | 0.7360  |

_Interpretation: Small-cap tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

### FAMI

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.0632 (adjusted = 0.0510)
- Alpha (annualized): **-30.40%** (daily = -0.001206, t = -0.47, p = 0.6405)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.4821 | +1.77 | 0.0778  |
| SMB | +0.8193 | +1.75 | 0.0810  |
| HML | +0.8858 | +2.09 | 0.0374 * |
| RMW | -0.9285 | -1.80 | 0.0721  |
| CMA | -0.7919 | -1.44 | 0.1507  |

_Interpretation: Small-cap tilt; Value tilt; Weak profitability; Aggressive investment; Modest factor fit_

### AKAN

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.0540 (adjusted = 0.0418)
- Alpha (annualized): **-210.46%** (daily = -0.008352, t = -2.46, p = 0.0144)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.1640 | +0.46 | 0.6482  |
| SMB | +0.1786 | +0.29 | 0.7723  |
| HML | -0.7229 | -1.29 | 0.1964  |
| RMW | -1.8924 | -2.79 | 0.0055 ** |
| CMA | +1.4119 | +1.95 | 0.0520  |

_Interpretation: Growth tilt; Weak profitability; Conservative investment; Significant negative alpha; Modest factor fit_

### AIM

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.0276 (adjusted = 0.0150)
- Alpha (annualized): **-152.91%** (daily = -0.006068, t = -1.19, p = 0.2362)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0842 | +2.01 | 0.0454 * |
| SMB | +0.3235 | +0.35 | 0.7276  |
| HML | +0.5542 | +0.66 | 0.5102  |
| RMW | -1.1690 | -1.15 | 0.2526  |
| CMA | +0.9310 | +0.85 | 0.3934  |

_Interpretation: Value tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### IP

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.3230 (adjusted = 0.3142)
- Alpha (annualized): **-24.58%** (daily = -0.000975, t = -0.95, p = 0.3413)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1452 | +10.59 | 0.0000 *** |
| SMB | +0.4715 | +2.54 | 0.0115 * |
| HML | +0.5832 | +3.47 | 0.0006 *** |
| RMW | +0.3324 | +1.63 | 0.1044  |
| CMA | +0.9288 | +4.26 | 0.0000 *** |

_Interpretation: Value tilt; Conservative investment_

### GME

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.0968 (adjusted = 0.0851)
- Alpha (annualized): **+12.47%** (daily = +0.000495, t = +0.29, p = 0.7682)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.4973 | +2.81 | 0.0053 ** |
| SMB | +0.8908 | +2.93 | 0.0036 ** |
| HML | -0.6078 | -2.20 | 0.0281 * |
| RMW | -0.1744 | -0.52 | 0.6025  |
| CMA | -0.0536 | -0.15 | 0.8808  |

_Interpretation: Small-cap tilt; Growth tilt; Modest factor fit_

### GELS

- Period: `2024-10-30` to `2026-03-31` (354 obs)
- R² = 0.0333 (adjusted = 0.0194)
- Alpha (annualized): **+96.79%** (daily = +0.003841, t = +0.45, p = 0.6544)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7243 | +1.97 | 0.0495 * |
| SMB | +3.3569 | +2.15 | 0.0320 * |
| HML | -0.1298 | -0.09 | 0.9252  |
| RMW | +1.2968 | +0.78 | 0.4385  |
| CMA | -1.5787 | -0.87 | 0.3839  |

_Interpretation: Small-cap tilt; Robust profitability; Aggressive investment; Low explanatory power — likely sentiment-driven_

### OPTT

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.0746 (adjusted = 0.0626)
- Alpha (annualized): **+141.76%** (daily = +0.005625, t = +1.11, p = 0.2663)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2784 | +2.40 | 0.0171 * |
| SMB | +1.4537 | +1.59 | 0.1137  |
| HML | -0.8584 | -1.03 | 0.3020  |
| RMW | -1.7662 | -1.75 | 0.0806  |
| CMA | +0.9559 | +0.89 | 0.3752  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### SOUN

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.3377 (adjusted = 0.3291)
- Alpha (annualized): **+56.17%** (daily = +0.002229, t = +0.82, p = 0.4149)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.8322 | +6.35 | 0.0000 *** |
| SMB | +1.4092 | +2.84 | 0.0047 ** |
| HML | -1.7929 | -3.99 | 0.0001 *** |
| RMW | -2.0916 | -3.84 | 0.0001 *** |
| CMA | +0.4983 | +0.86 | 0.3923  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._