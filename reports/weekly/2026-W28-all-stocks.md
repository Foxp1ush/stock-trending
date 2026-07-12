# Weekly Report — `all-stocks` — 2026-W28

Generated: 2026-07-12  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W28.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +50.54% | +1.959 | -0.403 | -0.165 | -1.052 | +0.410 | 0.406 | 431 | Weak profitability |
| MSFT | -15.14% | +0.885 | -0.265 | -0.406 | +0.137 | -0.504 | 0.520 | 431 | Aggressive investment |
| NVDA | +19.11% | +1.727 | -0.842 | -1.192 | -0.348 | +1.615 | 0.698 | 431 | Large-cap tilt; Growth tilt; Conservative investment |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| META | +6.79% | +1.368 | -0.075 | -0.613 | +0.517 | -0.590 | 0.510 | 431 | Growth tilt; Robust profitability; Aggressive investment |
| DTE | +6.38% | +0.296 | -0.201 | +0.561 | -0.190 | +0.049 | 0.143 | 431 | Value tilt; Modest factor fit |
| TSLA | +23.35% | +2.237 | +0.074 | -0.178 | -0.190 | -0.989 | 0.455 | 431 | Aggressive investment |
| WEN | -48.91% | +0.564 | +0.781 | +0.285 | +0.390 | +0.685 | 0.186 | 431 | Small-cap tilt; Conservative investment; Significant negative alpha; Modest factor fit |
| NBIS | +171.20% | +1.642 | +0.745 | -2.284 | -2.007 | -0.014 | 0.295 | 360 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| AMD | +0.02% | +1.577 | -0.631 | -0.531 | -1.710 | -0.065 | 0.488 | 431 | Large-cap tilt; Growth tilt; Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **93.33** | 30.00 | 33.33 | 30.00 | 0.290 | +1.885 | 0.9717 | 0.0559 | 181 |
| NBIS | **86.67** | 23.33 | 30.00 | 33.33 | 0.296 | +1.326 | 0.9923 | 0.0571 | 181 |
| MU | **73.33** | 20.00 | 26.67 | 26.67 | 0.310 | +0.659 | 0.5785 | 0.0333 | 181 |
| WEN | **50.00** | 26.67 | 3.33 | 20.00 | 0.295 | -0.900 | 0.3779 | 0.0218 | 181 |
| DTE | **50.00** | 33.33 | 13.33 | 3.33 | 0.066 | +0.083 | 0.1625 | 0.0094 | 181 |
| AMD | **50.00** | 6.67 | 20.00 | 23.33 | 0.444 | +0.459 | 0.5140 | 0.0296 | 181 |
| META | **46.67** | 16.67 | 16.67 | 13.33 | 0.350 | +0.230 | 0.3179 | 0.0183 | 181 |
| TSLA | **40.00** | 13.33 | 10.00 | 16.67 | 0.377 | -0.109 | 0.3701 | 0.0213 | 181 |
| NVDA | **36.67** | 3.33 | 23.33 | 10.00 | 0.642 | +0.481 | 0.2249 | 0.0129 | 181 |
| MSFT | **23.33** | 10.00 | 6.67 | 6.67 | 0.424 | -0.469 | 0.2003 | 0.0115 | 181 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.4065 (adjusted = 0.3995)
- Alpha (annualized): **+50.54%** (daily = +0.002006, t = +1.34, p = 0.1797)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9594 | +12.33 | 0.0000 *** |
| SMB | -0.4035 | -1.52 | 0.1296  |
| HML | -0.1648 | -0.68 | 0.4995  |
| RMW | -1.0520 | -3.44 | 0.0006 *** |
| CMA | +0.4100 | +1.32 | 0.1870  |

_Interpretation: Weak profitability_

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

### NVDA

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.6980 (adjusted = 0.6945)
- Alpha (annualized): **+19.11%** (daily = +0.000758, t = +0.92, p = 0.3572)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7272 | +19.71 | 0.0000 *** |
| SMB | -0.8421 | -5.75 | 0.0000 *** |
| HML | -1.1922 | -8.87 | 0.0000 *** |
| RMW | -0.3481 | -2.06 | 0.0398 * |
| CMA | +1.6149 | +9.44 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### SNDK

- Period: `2025-02-14` to `2026-03-31` (282 obs)
- R² = 0.2490 (adjusted = 0.2354)
- Alpha (annualized): **+277.05%** (daily = +0.010994, t = +3.31, p = 0.0011)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.3574 | +7.20 | 0.0000 *** |
| SMB | -0.0193 | -0.03 | 0.9748  |
| HML | +0.8466 | +1.41 | 0.1591  |
| RMW | -1.2601 | -1.98 | 0.0485 * |
| CMA | -1.2831 | -1.62 | 0.1062  |

_Interpretation: Value tilt; Weak profitability; Aggressive investment; Significant positive alpha_

### META

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.5097 (adjusted = 0.5039)
- Alpha (annualized): **+6.79%** (daily = +0.000269, t = +0.34, p = 0.7304)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3676 | +16.43 | 0.0000 *** |
| SMB | -0.0750 | -0.54 | 0.5903  |
| HML | -0.6135 | -4.81 | 0.0000 *** |
| RMW | +0.5173 | +3.23 | 0.0014 ** |
| CMA | -0.5901 | -3.63 | 0.0003 *** |

_Interpretation: Growth tilt; Robust profitability; Aggressive investment_

### DTE

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.1431 (adjusted = 0.1330)
- Alpha (annualized): **+6.38%** (daily = +0.000253, t = +0.52, p = 0.6026)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2962 | +5.73 | 0.0000 *** |
| SMB | -0.2009 | -2.32 | 0.0206 * |
| HML | +0.5607 | +7.07 | 0.0000 *** |
| RMW | -0.1904 | -1.91 | 0.0567  |
| CMA | +0.0491 | +0.49 | 0.6272  |

_Interpretation: Value tilt; Modest factor fit_

### TSLA

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.4551 (adjusted = 0.4486)
- Alpha (annualized): **+23.35%** (daily = +0.000927, t = +0.65, p = 0.5135)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2373 | +14.82 | 0.0000 *** |
| SMB | +0.0745 | +0.30 | 0.7680  |
| HML | -0.1784 | -0.77 | 0.4413  |
| RMW | -0.1898 | -0.65 | 0.5143  |
| CMA | -0.9891 | -3.36 | 0.0009 *** |

_Interpretation: Aggressive investment_

### WEN

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.1858 (adjusted = 0.1762)
- Alpha (annualized): **-48.91%** (daily = -0.001941, t = -1.98, p = 0.0486)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5637 | +5.39 | 0.0000 *** |
| SMB | +0.7813 | +4.47 | 0.0000 *** |
| HML | +0.2855 | +1.78 | 0.0756  |
| RMW | +0.3902 | +1.94 | 0.0532  |
| CMA | +0.6852 | +3.36 | 0.0009 *** |

_Interpretation: Small-cap tilt; Conservative investment; Significant negative alpha; Modest factor fit_

### NBIS

- Period: `2024-10-22` to `2026-03-31` (360 obs)
- R² = 0.2953 (adjusted = 0.2854)
- Alpha (annualized): **+171.20%** (daily = +0.006794, t = +2.15, p = 0.0320)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6416 | +5.06 | 0.0000 *** |
| SMB | +0.7454 | +1.29 | 0.1966  |
| HML | -2.2842 | -4.49 | 0.0000 *** |
| RMW | -2.0070 | -3.24 | 0.0013 ** |
| CMA | -0.0135 | -0.02 | 0.9839  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### AMD

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.4881 (adjusted = 0.4821)
- Alpha (annualized): **+0.02%** (daily = +0.000001, t = +0.00, p = 0.9996)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5769 | +11.68 | 0.0000 *** |
| SMB | -0.6312 | -2.80 | 0.0054 ** |
| HML | -0.5311 | -2.56 | 0.0107 * |
| RMW | -1.7095 | -6.57 | 0.0000 *** |
| CMA | -0.0654 | -0.25 | 0.8042  |

_Interpretation: Large-cap tilt; Growth tilt; Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._