# Weekly Report — `Shortsqueeze` — 2026-W25

Generated: 2026-06-21  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W25.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| LFVN | -3.92% | +0.795 | +1.184 | -0.690 | +0.675 | +0.094 | 0.085 | 445 | Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit |
| SPCE | -63.54% | +0.971 | +2.054 | -0.709 | -2.020 | -0.247 | 0.300 | 445 | Small-cap tilt; Growth tilt; Weak profitability |
| GRPN | -3.03% | +0.677 | +1.136 | -0.348 | -1.807 | +0.592 | 0.162 | 445 | Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit |
| ALL | +3.65% | +0.683 | -0.286 | +0.805 | +0.331 | -0.155 | 0.211 | 445 | Value tilt |
| AAPL | +4.89% | +1.310 | -0.114 | -0.058 | +0.758 | +0.075 | 0.537 | 445 | Robust profitability |
| CRM | -20.61% | +0.797 | +0.258 | -0.361 | -0.441 | -0.061 | 0.326 | 445 | Neutral profile |
| IBM | +12.27% | +0.810 | +0.081 | +0.201 | -0.015 | -0.045 | 0.202 | 445 | Neutral profile |
| HAS | +23.05% | +0.924 | +0.674 | -0.063 | +0.457 | +0.498 | 0.321 | 445 | Small-cap tilt |
| GL | +13.59% | +0.892 | -0.142 | +0.805 | -0.007 | -0.096 | 0.375 | 445 | Value tilt |
| ES | +4.53% | +0.341 | -0.075 | +0.499 | -0.114 | +0.268 | 0.087 | 445 | Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| ALL | **70.00** | 30.00 | 26.67 | 13.33 | 0.140 | -0.001 | 0.2281 | 0.0139 | 195 |
| SPCE | **66.67** | 13.33 | 20.00 | 33.33 | 0.271 | -0.064 | 0.6356 | 0.0386 | 195 |
| GL | **66.67** | 26.67 | 33.33 | 6.67 | 0.141 | +0.153 | 0.2052 | 0.0125 | 195 |
| ES | **66.67** | 33.33 | 16.67 | 16.67 | 0.064 | -0.131 | 0.2541 | 0.0155 | 195 |
| LFVN | **56.67** | 23.33 | 6.67 | 26.67 | 0.165 | -0.736 | 0.5344 | 0.0325 | 195 |
| GRPN | **56.67** | 16.67 | 10.00 | 30.00 | 0.234 | -0.713 | 0.5572 | 0.0339 | 195 |
| IBM | **56.67** | 20.00 | 13.33 | 23.33 | 0.225 | -0.553 | 0.3106 | 0.0189 | 195 |
| AAPL | **43.33** | 10.00 | 30.00 | 3.33 | 0.327 | +0.029 | 0.1906 | 0.0116 | 195 |
| HAS | **40.00** | 6.67 | 23.33 | 10.00 | 0.382 | -0.062 | 0.2099 | 0.0128 | 195 |
| CRM | **26.67** | 3.33 | 3.33 | 20.00 | 0.423 | -1.410 | 0.2698 | 0.0164 | 195 |

## Per-ticker FF5 Detail

### LFVN

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.0853 (adjusted = 0.0749)
- Alpha (annualized): **-3.92%** (daily = -0.000156, t = -0.08, p = 0.9370)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7949 | +3.77 | 0.0002 *** |
| SMB | +1.1843 | +3.47 | 0.0006 *** |
| HML | -0.6898 | -2.14 | 0.0331 * |
| RMW | +0.6753 | +1.66 | 0.0967  |
| CMA | +0.0938 | +0.23 | 0.8176  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit_

### SPCE

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.2996 (adjusted = 0.2916)
- Alpha (annualized): **-63.54%** (daily = -0.002521, t = -1.18, p = 0.2378)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9706 | +4.25 | 0.0000 *** |
| SMB | +2.0538 | +5.55 | 0.0000 *** |
| HML | -0.7088 | -2.03 | 0.0433 * |
| RMW | -2.0204 | -4.60 | 0.0000 *** |
| CMA | -0.2468 | -0.56 | 0.5755  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### GRPN

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.1618 (adjusted = 0.1522)
- Alpha (annualized): **-3.03%** (daily = -0.000120, t = -0.05, p = 0.9576)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6773 | +2.80 | 0.0054 ** |
| SMB | +1.1358 | +2.90 | 0.0040 ** |
| HML | -0.3483 | -0.94 | 0.3481  |
| RMW | -1.8067 | -3.88 | 0.0001 *** |
| CMA | +0.5918 | +1.27 | 0.2057  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit_

### ALL

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.2109 (adjusted = 0.2019)
- Alpha (annualized): **+3.65%** (daily = +0.000145, t = +0.22, p = 0.8297)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6835 | +9.50 | 0.0000 *** |
| SMB | -0.2864 | -2.46 | 0.0144 * |
| HML | +0.8048 | +7.30 | 0.0000 *** |
| RMW | +0.3312 | +2.39 | 0.0173 * |
| CMA | -0.1548 | -1.11 | 0.2655  |

_Interpretation: Value tilt_

### AAPL

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.5371 (adjusted = 0.5318)
- Alpha (annualized): **+4.89%** (daily = +0.000194, t = +0.33, p = 0.7390)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3105 | +21.02 | 0.0000 *** |
| SMB | -0.1141 | -1.13 | 0.2594  |
| HML | -0.0579 | -0.61 | 0.5446  |
| RMW | +0.7580 | +6.31 | 0.0000 *** |
| CMA | +0.0753 | +0.63 | 0.5315  |

_Interpretation: Robust profitability_

### CRM

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.3264 (adjusted = 0.3187)
- Alpha (annualized): **-20.61%** (daily = -0.000818, t = -0.99, p = 0.3240)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7974 | +8.99 | 0.0000 *** |
| SMB | +0.2581 | +1.80 | 0.0731  |
| HML | -0.3606 | -2.66 | 0.0082 ** |
| RMW | -0.4413 | -2.58 | 0.0101 * |
| CMA | -0.0611 | -0.36 | 0.7209  |

_Interpretation: Neutral profile_

### IBM

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.2017 (adjusted = 0.1926)
- Alpha (annualized): **+12.27%** (daily = +0.000487, t = +0.59, p = 0.5580)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8102 | +9.11 | 0.0000 *** |
| SMB | +0.0812 | +0.56 | 0.5731  |
| HML | +0.2013 | +1.48 | 0.1401  |
| RMW | -0.0154 | -0.09 | 0.9284  |
| CMA | -0.0446 | -0.26 | 0.7949  |

_Interpretation: Neutral profile_

### HAS

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.3215 (adjusted = 0.3137)
- Alpha (annualized): **+23.05%** (daily = +0.000915, t = +1.15, p = 0.2519)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9240 | +10.83 | 0.0000 *** |
| SMB | +0.6740 | +4.87 | 0.0000 *** |
| HML | -0.0631 | -0.48 | 0.6294  |
| RMW | +0.4570 | +2.78 | 0.0056 ** |
| CMA | +0.4981 | +3.03 | 0.0026 ** |

_Interpretation: Small-cap tilt_

### GL

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.3745 (adjusted = 0.3674)
- Alpha (annualized): **+13.59%** (daily = +0.000539, t = +0.94, p = 0.3458)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8916 | +14.58 | 0.0000 *** |
| SMB | -0.1423 | -1.44 | 0.1516  |
| HML | +0.8052 | +8.60 | 0.0000 *** |
| RMW | -0.0071 | -0.06 | 0.9519  |
| CMA | -0.0958 | -0.81 | 0.4173  |

_Interpretation: Value tilt_

### ES

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.0870 (adjusted = 0.0766)
- Alpha (annualized): **+4.53%** (daily = +0.000180, t = +0.25, p = 0.8011)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3413 | +4.47 | 0.0000 *** |
| SMB | -0.0750 | -0.61 | 0.5444  |
| HML | +0.4989 | +4.27 | 0.0000 *** |
| RMW | -0.1142 | -0.78 | 0.4378  |
| CMA | +0.2682 | +1.82 | 0.0692  |

_Interpretation: Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._