# Weekly Report — `Shortsqueeze` — 2026-W42

Generated: 2026-10-12  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W42.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +55.53% | +1.035 | +2.082 | +0.641 | +0.339 | +0.288 | 0.098 | 367 | Small-cap tilt; Value tilt; Modest factor fit |
| ALL | -2.53% | +0.681 | -0.250 | +0.786 | +0.294 | -0.052 | 0.220 | 367 | Value tilt |
| ASTS | +109.46% | +1.310 | +1.024 | -1.181 | -2.937 | -0.204 | 0.313 | 367 | Small-cap tilt; Growth tilt; Weak profitability |
| AM | +19.63% | +0.612 | -0.356 | +0.389 | -0.296 | +0.126 | 0.196 | 367 | Modest factor fit |
| GME | +18.91% | +0.554 | +0.915 | -0.709 | -0.143 | +0.085 | 0.119 | 367 | Small-cap tilt; Growth tilt; Modest factor fit |
| EU | -21.01% | +0.865 | +1.521 | -1.209 | -1.005 | -0.086 | 0.175 | 367 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| BB | +17.14% | +1.012 | +0.228 | -0.463 | -1.243 | +0.826 | 0.279 | 367 | Weak profitability; Conservative investment |
| BE | +192.83% | +1.346 | -0.304 | +0.054 | -2.719 | -2.001 | 0.197 | 367 | Weak profitability; Aggressive investment; Significant positive alpha; Modest factor fit |
| ES | +0.63% | +0.385 | -0.080 | +0.450 | -0.139 | +0.372 | 0.097 | 367 | Modest factor fit |
| DTE | +1.72% | +0.296 | -0.214 | +0.565 | -0.249 | +0.118 | 0.156 | 367 | Value tilt; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| ASTS | **66.67** | 6.67 | 26.67 | 33.33 | 0.385 | +0.417 | 1.2294 | 0.0559 | 117 |
| BE | **66.67** | 3.33 | 33.33 | 30.00 | 0.524 | +3.020 | 1.1238 | 0.0511 | 117 |
| AM | **63.33** | 33.33 | 23.33 | 6.67 | 0.047 | +0.125 | 0.2651 | 0.0121 | 117 |
| EU | **63.33** | 10.00 | 30.00 | 23.33 | 0.329 | +1.375 | 0.9389 | 0.0427 | 117 |
| HTZ | **60.00** | 23.33 | 10.00 | 26.67 | 0.108 | -0.201 | 1.0600 | 0.0482 | 117 |
| ES | **56.67** | 30.00 | 13.33 | 13.33 | 0.064 | -0.175 | 0.3740 | 0.0170 | 117 |
| GME | **56.67** | 20.00 | 16.67 | 20.00 | 0.163 | -0.154 | 0.4414 | 0.0201 | 117 |
| DTE | **50.00** | 26.67 | 20.00 | 3.33 | 0.069 | +0.041 | 0.2148 | 0.0098 | 117 |
| BB | **33.33** | 13.33 | 3.33 | 16.67 | 0.259 | -0.561 | 0.4299 | 0.0196 | 117 |
| ALL | **33.33** | 16.67 | 6.67 | 10.00 | 0.246 | -0.249 | 0.2782 | 0.0127 | 117 |

## Per-ticker FF5 Detail

### HTZ

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.0985 (adjusted = 0.0860)
- Alpha (annualized): **+55.53%** (daily = +0.002204, t = +0.69, p = 0.4897)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0353 | +3.14 | 0.0019 ** |
| SMB | +2.0815 | +3.58 | 0.0004 *** |
| HML | +0.6405 | +1.24 | 0.2159  |
| RMW | +0.3386 | +0.54 | 0.5909  |
| CMA | +0.2878 | +0.43 | 0.6710  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### ALL

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.2197 (adjusted = 0.2089)
- Alpha (annualized): **-2.53%** (daily = -0.000100, t = -0.13, p = 0.8929)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6807 | +8.84 | 0.0000 *** |
| SMB | -0.2496 | -1.84 | 0.0662  |
| HML | +0.7860 | +6.52 | 0.0000 *** |
| RMW | +0.2939 | +2.00 | 0.0461 * |
| CMA | -0.0524 | -0.33 | 0.7403  |

_Interpretation: Value tilt_

### ASTS

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.3131 (adjusted = 0.3036)
- Alpha (annualized): **+109.46%** (daily = +0.004344, t = +1.57, p = 0.1172)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3102 | +4.57 | 0.0000 *** |
| SMB | +1.0236 | +2.03 | 0.0430 * |
| HML | -1.1808 | -2.63 | 0.0088 ** |
| RMW | -2.9371 | -5.38 | 0.0000 *** |
| CMA | -0.2043 | -0.35 | 0.7283  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### AM

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.1958 (adjusted = 0.1847)
- Alpha (annualized): **+19.63%** (daily = +0.000779, t = +1.07, p = 0.2836)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6121 | +8.14 | 0.0000 *** |
| SMB | -0.3563 | -2.70 | 0.0074 ** |
| HML | +0.3894 | +3.31 | 0.0010 ** |
| RMW | -0.2958 | -2.06 | 0.0397 * |
| CMA | +0.1263 | +0.82 | 0.4130  |

_Interpretation: Modest factor fit_

### GME

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.1186 (adjusted = 0.1064)
- Alpha (annualized): **+18.91%** (daily = +0.000750, t = +0.44, p = 0.6575)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5537 | +3.16 | 0.0017 ** |
| SMB | +0.9148 | +2.97 | 0.0032 ** |
| HML | -0.7087 | -2.59 | 0.0101 * |
| RMW | -0.1429 | -0.43 | 0.6688  |
| CMA | +0.0852 | +0.24 | 0.8125  |

_Interpretation: Small-cap tilt; Growth tilt; Modest factor fit_

### EU

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.1750 (adjusted = 0.1636)
- Alpha (annualized): **-21.01%** (daily = -0.000834, t = -0.32, p = 0.7487)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8652 | +3.21 | 0.0014 ** |
| SMB | +1.5209 | +3.21 | 0.0014 ** |
| HML | -1.2094 | -2.87 | 0.0044 ** |
| RMW | -1.0047 | -1.96 | 0.0511  |
| CMA | -0.0856 | -0.15 | 0.8770  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### BB

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.2794 (adjusted = 0.2695)
- Alpha (annualized): **+17.14%** (daily = +0.000680, t = +0.43, p = 0.6640)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0117 | +6.24 | 0.0000 *** |
| SMB | +0.2275 | +0.80 | 0.4252  |
| HML | -0.4628 | -1.82 | 0.0688  |
| RMW | -1.2426 | -4.02 | 0.0001 *** |
| CMA | +0.8256 | +2.48 | 0.0134 * |

_Interpretation: Weak profitability; Conservative investment_

### BE

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.1969 (adjusted = 0.1858)
- Alpha (annualized): **+192.83%** (daily = +0.007652, t = +2.38, p = 0.0178)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3461 | +4.04 | 0.0001 *** |
| SMB | -0.3037 | -0.52 | 0.6044  |
| HML | +0.0539 | +0.10 | 0.9178  |
| RMW | -2.7190 | -4.28 | 0.0000 *** |
| CMA | -2.0008 | -2.93 | 0.0036 ** |

_Interpretation: Weak profitability; Aggressive investment; Significant positive alpha; Modest factor fit_

### ES

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.0967 (adjusted = 0.0841)
- Alpha (annualized): **+0.63%** (daily = +0.000025, t = +0.03, p = 0.9755)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3849 | +4.54 | 0.0000 *** |
| SMB | -0.0799 | -0.54 | 0.5924  |
| HML | +0.4498 | +3.39 | 0.0008 *** |
| RMW | -0.1390 | -0.86 | 0.3900  |
| CMA | +0.3722 | +2.14 | 0.0329 * |

_Interpretation: Modest factor fit_

### DTE

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.1560 (adjusted = 0.1443)
- Alpha (annualized): **+1.72%** (daily = +0.000068, t = +0.13, p = 0.8979)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2958 | +5.38 | 0.0000 *** |
| SMB | -0.2142 | -2.21 | 0.0274 * |
| HML | +0.5650 | +6.57 | 0.0000 *** |
| RMW | -0.2488 | -2.37 | 0.0181 * |
| CMA | +0.1176 | +1.04 | 0.2975  |

_Interpretation: Value tilt; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._