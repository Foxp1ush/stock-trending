# Weekly Report — `pennystocks` — 2026-W37

Generated: 2026-09-13  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W37.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **9 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| BATL | +303.02% | -0.122 | +0.462 | -1.783 | +2.697 | -0.547 | 0.009 | 387 | Growth tilt; Robust profitability; Aggressive investment; Low explanatory power — likely sentiment-driven |
| ASTS | +96.11% | +1.316 | +1.252 | -1.132 | -2.889 | -0.320 | 0.311 | 387 | Small-cap tilt; Growth tilt; Weak profitability |
| SUNE | -195.44% | +1.589 | +2.016 | -1.691 | +0.697 | +3.503 | 0.053 | 387 | Small-cap tilt; Growth tilt; Robust profitability; Conservative investment; Modest factor fit |
| LABT | — | — | — | — | — | — | — | — | _insufficient_data_ |
| PR | +21.04% | +1.385 | +0.133 | +0.809 | +0.354 | +0.388 | 0.328 | 387 | Value tilt |
| BAOS | +168.67% | +1.767 | -0.500 | -0.022 | -0.660 | -1.588 | 0.017 | 387 | Large-cap tilt; Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven |
| SLS | +92.44% | +0.199 | +0.675 | +0.240 | -1.911 | -1.037 | 0.079 | 387 | Small-cap tilt; Weak profitability; Aggressive investment; Modest factor fit |
| TPET | +66.92% | -0.871 | +0.682 | -0.200 | +0.476 | -2.107 | 0.010 | 387 | Small-cap tilt; Aggressive investment; Low explanatory power — likely sentiment-driven |
| RS | -3.41% | +0.917 | +0.674 | +0.573 | +0.353 | +0.290 | 0.455 | 387 | Small-cap tilt; Value tilt |
| RKLB | +153.33% | +1.420 | +0.737 | -0.908 | -3.356 | +0.013 | 0.391 | 387 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| BATL | **81.48** | 33.33 | 14.81 | 33.33 | 0.021 | -1.040 | 5.1112 | 0.2527 | 137 |
| SLS | **62.96** | 14.81 | 33.33 | 14.81 | 0.165 | +0.829 | 1.1689 | 0.0578 | 137 |
| TPET | **62.96** | 29.63 | 3.70 | 29.63 | 0.052 | -2.541 | 3.7887 | 0.1873 | 137 |
| SUNE | **59.26** | 22.22 | 11.11 | 25.93 | 0.106 | -1.040 | 1.8378 | 0.0909 | 137 |
| BAOS | **55.56** | 25.93 | 7.41 | 22.22 | 0.098 | -1.092 | 1.3285 | 0.0657 | 137 |
| ASTS | **51.85** | 7.41 | 25.93 | 18.52 | 0.347 | +0.096 | 1.1704 | 0.0579 | 137 |
| PR | **44.44** | 18.52 | 18.52 | 7.41 | 0.150 | -0.081 | 0.3723 | 0.0184 | 137 |
| RKLB | **44.44** | 3.70 | 29.63 | 11.11 | 0.458 | +0.434 | 0.8490 | 0.0420 | 137 |
| RS | **37.04** | 11.11 | 22.22 | 3.70 | 0.342 | +0.087 | 0.2267 | 0.0112 | 137 |

## Per-ticker FF5 Detail

### BATL

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.0089 (adjusted = -0.0041)
- Alpha (annualized): **+303.02%** (daily = +0.012025, t = +1.33, p = 0.1842)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.1220 | -0.13 | 0.8982  |
| SMB | +0.4616 | +0.28 | 0.7794  |
| HML | -1.7834 | -1.20 | 0.2319  |
| RMW | +2.6969 | +1.49 | 0.1369  |
| CMA | -0.5473 | -0.28 | 0.7764  |

_Interpretation: Growth tilt; Robust profitability; Aggressive investment; Low explanatory power — likely sentiment-driven_

### ASTS

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.3112 (adjusted = 0.3022)
- Alpha (annualized): **+96.11%** (daily = +0.003814, t = +1.42, p = 0.1560)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3159 | +4.66 | 0.0000 *** |
| SMB | +1.2521 | +2.56 | 0.0108 * |
| HML | -1.1322 | -2.56 | 0.0108 * |
| RMW | -2.8892 | -5.38 | 0.0000 *** |
| CMA | -0.3200 | -0.56 | 0.5757  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### SUNE

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.0527 (adjusted = 0.0402)
- Alpha (annualized): **-195.44%** (daily = -0.007756, t = -1.17, p = 0.2436)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5886 | +2.27 | 0.0238 * |
| SMB | +2.0159 | +1.67 | 0.0965  |
| HML | -1.6906 | -1.54 | 0.1232  |
| RMW | +0.6972 | +0.52 | 0.6003  |
| CMA | +3.5030 | +2.48 | 0.0137 * |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Conservative investment; Modest factor fit_

### LABT

Status: `insufficient_data` — only 0 overlapping days after factor join


### PR

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.3282 (adjusted = 0.3194)
- Alpha (annualized): **+21.04%** (daily = +0.000835, t = +0.78, p = 0.4359)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3850 | +12.28 | 0.0000 *** |
| SMB | +0.1331 | +0.68 | 0.4954  |
| HML | +0.8086 | +4.59 | 0.0000 *** |
| RMW | +0.3543 | +1.65 | 0.0989  |
| CMA | +0.3882 | +1.70 | 0.0894  |

_Interpretation: Value tilt_

### BAOS

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.0174 (adjusted = 0.0045)
- Alpha (annualized): **+168.67%** (daily = +0.006693, t = +0.74, p = 0.4576)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7670 | +1.86 | 0.0632  |
| SMB | -0.5001 | -0.30 | 0.7606  |
| HML | -0.0217 | -0.01 | 0.9883  |
| RMW | -0.6605 | -0.37 | 0.7142  |
| CMA | -1.5877 | -0.83 | 0.4081  |

_Interpretation: Large-cap tilt; Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven_

### SLS

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.0786 (adjusted = 0.0665)
- Alpha (annualized): **+92.44%** (daily = +0.003668, t = +1.30, p = 0.1952)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.1989 | +0.67 | 0.5047  |
| SMB | +0.6753 | +1.31 | 0.1905  |
| HML | +0.2397 | +0.51 | 0.6071  |
| RMW | -1.9111 | -3.38 | 0.0008 *** |
| CMA | -1.0366 | -1.72 | 0.0859  |

_Interpretation: Small-cap tilt; Weak profitability; Aggressive investment; Modest factor fit_

### TPET

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.0098 (adjusted = -0.0032)
- Alpha (annualized): **+66.92%** (daily = +0.002655, t = +0.38, p = 0.7070)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.8707 | -1.17 | 0.2424  |
| SMB | +0.6822 | +0.53 | 0.5961  |
| HML | -0.1998 | -0.17 | 0.8637  |
| RMW | +0.4761 | +0.34 | 0.7363  |
| CMA | -2.1067 | -1.40 | 0.1620  |

_Interpretation: Small-cap tilt; Aggressive investment; Low explanatory power — likely sentiment-driven_

### RS

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.4546 (adjusted = 0.4475)
- Alpha (annualized): **-3.41%** (daily = -0.000135, t = -0.21, p = 0.8360)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9166 | +13.30 | 0.0000 *** |
| SMB | +0.6741 | +5.66 | 0.0000 *** |
| HML | +0.5727 | +5.32 | 0.0000 *** |
| RMW | +0.3527 | +2.70 | 0.0074 ** |
| CMA | +0.2898 | +2.08 | 0.0381 * |

_Interpretation: Small-cap tilt; Value tilt_

### RKLB

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.3910 (adjusted = 0.3831)
- Alpha (annualized): **+153.33%** (daily = +0.006085, t = +2.63, p = 0.0090)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4201 | +5.82 | 0.0000 *** |
| SMB | +0.7370 | +1.75 | 0.0815  |
| HML | -0.9077 | -2.38 | 0.0179 * |
| RMW | -3.3563 | -7.24 | 0.0000 *** |
| CMA | +0.0135 | +0.03 | 0.9782  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._