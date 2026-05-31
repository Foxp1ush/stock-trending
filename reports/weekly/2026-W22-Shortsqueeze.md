# Weekly Report — `Shortsqueeze` — 2026-W22

Generated: 2026-05-31  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W22.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| LFVN | -8.17% | +0.773 | +1.189 | -0.697 | +0.651 | +0.139 | 0.084 | 459 | Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit |
| GRPN | -0.74% | +0.689 | +1.221 | -0.399 | -1.683 | +0.588 | 0.160 | 459 | Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit |
| HUBC | -298.22% | +2.108 | -1.061 | +0.826 | -0.360 | -0.159 | 0.044 | 459 | Large-cap tilt; Value tilt; Significant negative alpha; Low explanatory power — likely sentiment-driven |
| OI | -13.95% | +1.160 | +1.260 | +0.237 | +0.544 | +1.113 | 0.373 | 459 | Small-cap tilt; Robust profitability; Conservative investment |
| CC | -6.66% | +1.784 | +1.802 | +0.254 | +0.258 | +1.163 | 0.436 | 459 | Small-cap tilt; Conservative investment |
| AMZN | -1.77% | +1.328 | +0.007 | -0.330 | +0.191 | -0.564 | 0.549 | 459 | Aggressive investment |
| AAPL | +6.45% | +1.306 | -0.071 | -0.110 | +0.806 | +0.059 | 0.520 | 459 | Robust profitability |
| EDIT | -7.05% | +1.184 | +1.984 | -0.430 | -2.861 | +1.090 | 0.221 | 459 | Small-cap tilt; Weak profitability; Conservative investment |
| ES | +4.88% | +0.333 | -0.088 | +0.490 | -0.121 | +0.287 | 0.084 | 459 | Modest factor fit |
| IBKR | +17.79% | +1.569 | -0.532 | +0.575 | -0.990 | -0.271 | 0.510 | 459 | Large-cap tilt; Value tilt; Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| HUBC | **100.00** | 33.33 | 33.33 | 33.33 | 0.053 | +1.047 | 1.6366 | 0.1029 | 209 |
| GRPN | **56.67** | 23.33 | 6.67 | 26.67 | 0.213 | -0.719 | 0.5502 | 0.0346 | 209 |
| ES | **56.67** | 30.00 | 16.67 | 10.00 | 0.061 | -0.138 | 0.2401 | 0.0151 | 209 |
| OI | **56.67** | 13.33 | 26.67 | 16.67 | 0.385 | +0.221 | 0.3393 | 0.0213 | 209 |
| EDIT | **56.67** | 16.67 | 10.00 | 30.00 | 0.377 | -0.686 | 0.7528 | 0.0473 | 209 |
| LFVN | **53.33** | 26.67 | 3.33 | 23.33 | 0.166 | -0.720 | 0.5049 | 0.0318 | 209 |
| IBKR | **46.67** | 3.33 | 30.00 | 13.33 | 0.489 | +0.304 | 0.2675 | 0.0168 | 209 |
| CC | **46.67** | 6.67 | 20.00 | 20.00 | 0.414 | -0.032 | 0.4915 | 0.0309 | 209 |
| AAPL | **46.67** | 20.00 | 23.33 | 3.33 | 0.337 | +0.046 | 0.1814 | 0.0114 | 209 |
| AMZN | **30.00** | 10.00 | 13.33 | 6.67 | 0.392 | -0.399 | 0.2360 | 0.0148 | 209 |

## Per-ticker FF5 Detail

### LFVN

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.0839 (adjusted = 0.0738)
- Alpha (annualized): **-8.17%** (daily = -0.000324, t = -0.17, p = 0.8665)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7729 | +3.72 | 0.0002 *** |
| SMB | +1.1887 | +3.56 | 0.0004 *** |
| HML | -0.6973 | -2.19 | 0.0290 * |
| RMW | +0.6512 | +1.64 | 0.1013  |
| CMA | +0.1392 | +0.35 | 0.7288  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit_

### GRPN

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.1603 (adjusted = 0.1510)
- Alpha (annualized): **-0.74%** (daily = -0.000030, t = -0.01, p = 0.9894)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6892 | +2.89 | 0.0041 ** |
| SMB | +1.2210 | +3.18 | 0.0016 ** |
| HML | -0.3986 | -1.09 | 0.2761  |
| RMW | -1.6833 | -3.70 | 0.0002 *** |
| CMA | +0.5880 | +1.28 | 0.2024  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit_

### HUBC

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.0436 (adjusted = 0.0331)
- Alpha (annualized): **-298.22%** (daily = -0.011834, t = -2.52, p = 0.0120)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.1077 | +4.16 | 0.0000 *** |
| SMB | -1.0613 | -1.30 | 0.1929  |
| HML | +0.8260 | +1.07 | 0.2870  |
| RMW | -0.3605 | -0.37 | 0.7090  |
| CMA | -0.1593 | -0.16 | 0.8705  |

_Interpretation: Large-cap tilt; Value tilt; Significant negative alpha; Low explanatory power — likely sentiment-driven_

### OI

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.3729 (adjusted = 0.3659)
- Alpha (annualized): **-13.95%** (daily = -0.000554, t = -0.53, p = 0.5961)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1599 | +10.31 | 0.0000 *** |
| SMB | +1.2605 | +6.96 | 0.0000 *** |
| HML | +0.2367 | +1.37 | 0.1703  |
| RMW | +0.5438 | +2.53 | 0.0116 * |
| CMA | +1.1130 | +5.13 | 0.0000 *** |

_Interpretation: Small-cap tilt; Robust profitability; Conservative investment_

### CC

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.4361 (adjusted = 0.4299)
- Alpha (annualized): **-6.66%** (daily = -0.000264, t = -0.19, p = 0.8474)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7836 | +12.05 | 0.0000 *** |
| SMB | +1.8020 | +7.57 | 0.0000 *** |
| HML | +0.2544 | +1.12 | 0.2624  |
| RMW | +0.2583 | +0.91 | 0.3610  |
| CMA | +1.1629 | +4.07 | 0.0001 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### AMZN

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.5495 (adjusted = 0.5445)
- Alpha (annualized): **-1.77%** (daily = -0.000070, t = -0.11, p = 0.9144)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3279 | +18.88 | 0.0000 *** |
| SMB | +0.0069 | +0.06 | 0.9515  |
| HML | -0.3297 | -3.06 | 0.0023 ** |
| RMW | +0.1912 | +1.43 | 0.1547  |
| CMA | -0.5640 | -4.16 | 0.0000 *** |

_Interpretation: Aggressive investment_

### AAPL

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.5204 (adjusted = 0.5151)
- Alpha (annualized): **+6.45%** (daily = +0.000256, t = +0.43, p = 0.6648)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3061 | +20.52 | 0.0000 *** |
| SMB | -0.0712 | -0.70 | 0.4869  |
| HML | -0.1097 | -1.13 | 0.2606  |
| RMW | +0.8056 | +6.64 | 0.0000 *** |
| CMA | +0.0595 | +0.48 | 0.6283  |

_Interpretation: Robust profitability_

### EDIT

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.2213 (adjusted = 0.2127)
- Alpha (annualized): **-7.05%** (daily = -0.000280, t = -0.09, p = 0.9262)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1844 | +3.64 | 0.0003 *** |
| SMB | +1.9845 | +3.79 | 0.0002 *** |
| HML | -0.4298 | -0.86 | 0.3890  |
| RMW | -2.8608 | -4.61 | 0.0000 *** |
| CMA | +1.0899 | +1.74 | 0.0834  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment_

### ES

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.0838 (adjusted = 0.0736)
- Alpha (annualized): **+4.88%** (daily = +0.000194, t = +0.28, p = 0.7824)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3330 | +4.41 | 0.0000 *** |
| SMB | -0.0879 | -0.72 | 0.4696  |
| HML | +0.4905 | +4.24 | 0.0000 *** |
| RMW | -0.1211 | -0.84 | 0.4012  |
| CMA | +0.2868 | +1.97 | 0.0498 * |

_Interpretation: Modest factor fit_

### IBKR

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.5101 (adjusted = 0.5047)
- Alpha (annualized): **+17.79%** (daily = +0.000706, t = +0.84, p = 0.4038)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5694 | +17.23 | 0.0000 *** |
| SMB | -0.5324 | -3.64 | 0.0003 *** |
| HML | +0.5746 | +4.12 | 0.0000 *** |
| RMW | -0.9904 | -5.70 | 0.0000 *** |
| CMA | -0.2707 | -1.54 | 0.1242  |

_Interpretation: Large-cap tilt; Value tilt; Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._