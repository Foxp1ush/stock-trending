# Weekly Report — `pennystocks` — 2026-W46

Generated: 2026-11-09  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W46.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +66.18% | +1.071 | +2.183 | +0.893 | +0.258 | +0.071 | 0.099 | 347 | Small-cap tilt; Value tilt; Modest factor fit |
| VIVK | -155.50% | -0.107 | +0.553 | -0.382 | -1.727 | +0.772 | 0.011 | 347 | Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| AMD | +16.37% | +1.602 | -0.581 | -0.396 | -1.646 | -0.297 | 0.482 | 347 | Large-cap tilt; Weak profitability |
| AAPL | +5.75% | +1.403 | -0.092 | +0.075 | +0.795 | +0.076 | 0.568 | 347 | Robust profitability |
| CC | +21.48% | +1.882 | +2.091 | +0.439 | +0.197 | +1.150 | 0.462 | 347 | Small-cap tilt; Conservative investment |
| AVGO | +56.43% | +1.549 | -0.120 | -1.442 | +0.082 | -0.126 | 0.460 | 347 | Growth tilt |
| ET | +2.71% | +0.756 | -0.282 | +0.349 | -0.384 | +0.478 | 0.333 | 347 | Neutral profile |
| ALL | -4.68% | +0.704 | -0.248 | +0.866 | +0.306 | -0.126 | 0.220 | 347 | Value tilt |
| DTE | +6.65% | +0.335 | -0.180 | +0.571 | -0.203 | +0.058 | 0.165 | 347 | Value tilt; Modest factor fit |
| GO | -41.72% | +0.412 | +1.198 | +0.527 | +0.993 | -0.427 | 0.052 | 347 | Small-cap tilt; Value tilt; Robust profitability; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| GO | **83.33** | 23.33 | 30.00 | 30.00 | 0.218 | +0.832 | 0.9262 | 0.0364 | 97 |
| CC | **66.67** | 13.33 | 26.67 | 26.67 | 0.364 | +0.693 | 0.8288 | 0.0326 | 97 |
| VIVK | **66.67** | 30.00 | 3.33 | 33.33 | 0.091 | -2.202 | 4.2533 | 0.1671 | 97 |
| AMD | **60.00** | 6.67 | 33.33 | 20.00 | 0.557 | +0.950 | 0.6477 | 0.0254 | 97 |
| DTE | **56.67** | 33.33 | 16.67 | 6.67 | 0.061 | +0.046 | 0.2547 | 0.0100 | 97 |
| HTZ | **46.67** | 16.67 | 6.67 | 23.33 | 0.360 | -0.488 | 0.7726 | 0.0303 | 97 |
| ET | **43.33** | 26.67 | 13.33 | 3.33 | 0.121 | +0.015 | 0.2461 | 0.0097 | 97 |
| ALL | **43.33** | 20.00 | 10.00 | 13.33 | 0.240 | -0.255 | 0.3199 | 0.0126 | 97 |
| AVGO | **43.33** | 3.33 | 23.33 | 16.67 | 0.579 | +0.415 | 0.4816 | 0.0189 | 97 |
| AAPL | **40.00** | 10.00 | 20.00 | 10.00 | 0.392 | +0.147 | 0.2699 | 0.0106 | 97 |

## Per-ticker FF5 Detail

### HTZ

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.0989 (adjusted = 0.0856)
- Alpha (annualized): **+66.18%** (daily = +0.002626, t = +0.79, p = 0.4312)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0715 | +3.10 | 0.0021 ** |
| SMB | +2.1831 | +3.59 | 0.0004 *** |
| HML | +0.8928 | +1.56 | 0.1187  |
| RMW | +0.2576 | +0.40 | 0.6901  |
| CMA | +0.0706 | +0.10 | 0.9216  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### VIVK

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.0114 (adjusted = -0.0031)
- Alpha (annualized): **-155.50%** (daily = -0.006171, t = -0.93, p = 0.3525)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.1065 | -0.15 | 0.8771  |
| SMB | +0.5533 | +0.46 | 0.6478  |
| HML | -0.3816 | -0.34 | 0.7370  |
| RMW | -1.7266 | -1.34 | 0.1797  |
| CMA | +0.7723 | +0.54 | 0.5888  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### AMD

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.4820 (adjusted = 0.4744)
- Alpha (annualized): **+16.37%** (daily = +0.000650, t = +0.44, p = 0.6572)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6020 | +10.55 | 0.0000 *** |
| SMB | -0.5808 | -2.17 | 0.0304 * |
| HML | -0.3962 | -1.58 | 0.1148  |
| RMW | -1.6456 | -5.80 | 0.0000 *** |
| CMA | -0.2967 | -0.94 | 0.3470  |

_Interpretation: Large-cap tilt; Weak profitability_

### AAPL

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.5681 (adjusted = 0.5618)
- Alpha (annualized): **+5.75%** (daily = +0.000228, t = +0.34, p = 0.7352)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4029 | +20.04 | 0.0000 *** |
| SMB | -0.0915 | -0.74 | 0.4578  |
| HML | +0.0747 | +0.65 | 0.5181  |
| RMW | +0.7949 | +6.08 | 0.0000 *** |
| CMA | +0.0760 | +0.52 | 0.6009  |

_Interpretation: Robust profitability_

### CC

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.4621 (adjusted = 0.4542)
- Alpha (annualized): **+21.48%** (daily = +0.000853, t = +0.53, p = 0.5993)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.8819 | +11.18 | 0.0000 *** |
| SMB | +2.0910 | +7.06 | 0.0000 *** |
| HML | +0.4386 | +1.58 | 0.1151  |
| RMW | +0.1966 | +0.63 | 0.5317  |
| CMA | +1.1499 | +3.29 | 0.0011 ** |

_Interpretation: Small-cap tilt; Conservative investment_

### AVGO

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.4602 (adjusted = 0.4523)
- Alpha (annualized): **+56.43%** (daily = +0.002239, t = +1.62, p = 0.1072)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5493 | +10.76 | 0.0000 *** |
| SMB | -0.1204 | -0.48 | 0.6348  |
| HML | -1.4421 | -6.07 | 0.0000 *** |
| RMW | +0.0825 | +0.31 | 0.7591  |
| CMA | -0.1258 | -0.42 | 0.6738  |

_Interpretation: Growth tilt_

### ET

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.3334 (adjusted = 0.3237)
- Alpha (annualized): **+2.71%** (daily = +0.000107, t = +0.16, p = 0.8765)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7559 | +10.55 | 0.0000 *** |
| SMB | -0.2822 | -2.24 | 0.0258 * |
| HML | +0.3493 | +2.95 | 0.0034 ** |
| RMW | -0.3836 | -2.87 | 0.0044 ** |
| CMA | +0.4783 | +3.22 | 0.0014 ** |

_Interpretation: Neutral profile_

### ALL

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.2204 (adjusted = 0.2090)
- Alpha (annualized): **-4.68%** (daily = -0.000186, t = -0.24, p = 0.8108)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7041 | +8.75 | 0.0000 *** |
| SMB | -0.2479 | -1.75 | 0.0807  |
| HML | +0.8658 | +6.52 | 0.0000 *** |
| RMW | +0.3057 | +2.04 | 0.0425 * |
| CMA | -0.1263 | -0.76 | 0.4497  |

_Interpretation: Value tilt_

### DTE

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.1650 (adjusted = 0.1527)
- Alpha (annualized): **+6.65%** (daily = +0.000264, t = +0.50, p = 0.6200)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3354 | +6.08 | 0.0000 *** |
| SMB | -0.1796 | -1.85 | 0.0652  |
| HML | +0.5715 | +6.28 | 0.0000 *** |
| RMW | -0.2026 | -1.97 | 0.0501  |
| CMA | +0.0583 | +0.51 | 0.6110  |

_Interpretation: Value tilt; Modest factor fit_

### GO

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.0525 (adjusted = 0.0386)
- Alpha (annualized): **-41.72%** (daily = -0.001656, t = -0.72, p = 0.4700)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.4117 | +1.73 | 0.0841  |
| SMB | +1.1985 | +2.87 | 0.0044 ** |
| HML | +0.5272 | +1.34 | 0.1797  |
| RMW | +0.9934 | +2.24 | 0.0258 * |
| CMA | -0.4274 | -0.87 | 0.3865  |

_Interpretation: Small-cap tilt; Value tilt; Robust profitability; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._