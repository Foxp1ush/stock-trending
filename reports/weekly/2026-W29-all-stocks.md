# Weekly Report — `all-stocks` — 2026-W29

Generated: 2026-07-19  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W29.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +54.81% | +1.961 | -0.334 | -0.131 | -1.043 | +0.377 | 0.405 | 426 | Weak profitability |
| IBM | +10.95% | +0.808 | +0.065 | +0.173 | -0.020 | -0.054 | 0.202 | 426 | Neutral profile |
| MSFT | -15.19% | +0.885 | -0.261 | -0.418 | +0.136 | -0.499 | 0.520 | 426 | Neutral profile |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| ASTS | +152.22% | +1.394 | +1.779 | -1.510 | -2.750 | +0.024 | 0.291 | 426 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| NFLX | +13.83% | +0.734 | -0.757 | -0.191 | -0.605 | +0.145 | 0.267 | 426 | Large-cap tilt; Weak profitability |
| NVDA | +16.73% | +1.728 | -0.840 | -1.189 | -0.362 | +1.608 | 0.696 | 426 | Large-cap tilt; Growth tilt; Conservative investment |
| DTE | +5.41% | +0.297 | -0.211 | +0.549 | -0.189 | +0.050 | 0.140 | 426 | Value tilt; Modest factor fit |
| RKLB | +157.44% | +1.409 | +0.683 | -0.806 | -3.398 | -0.047 | 0.388 | 426 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| AMD | +5.01% | +1.575 | -0.597 | -0.484 | -1.702 | -0.091 | 0.483 | 426 | Large-cap tilt; Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **90.00** | 23.33 | 33.33 | 33.33 | 0.311 | +2.013 | 0.9755 | 0.0555 | 176 |
| MU | **70.00** | 16.67 | 30.00 | 23.33 | 0.330 | +0.714 | 0.5795 | 0.0330 | 176 |
| ASTS | **66.67** | 20.00 | 16.67 | 30.00 | 0.319 | +0.082 | 0.9610 | 0.0546 | 176 |
| RKLB | **60.00** | 13.33 | 20.00 | 26.67 | 0.415 | +0.472 | 0.7304 | 0.0415 | 176 |
| NFLX | **56.67** | 30.00 | 10.00 | 16.67 | 0.140 | -0.306 | 0.3505 | 0.0199 | 176 |
| DTE | **50.00** | 33.33 | 13.33 | 3.33 | 0.062 | +0.075 | 0.1651 | 0.0094 | 176 |
| AMD | **50.00** | 6.67 | 23.33 | 20.00 | 0.456 | +0.492 | 0.5172 | 0.0294 | 176 |
| IBM | **43.33** | 26.67 | 3.33 | 13.33 | 0.251 | -0.688 | 0.3385 | 0.0193 | 176 |
| NVDA | **40.00** | 3.33 | 26.67 | 10.00 | 0.652 | +0.495 | 0.2251 | 0.0128 | 176 |
| MSFT | **23.33** | 10.00 | 6.67 | 6.67 | 0.423 | -0.466 | 0.2052 | 0.0117 | 176 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.4046 (adjusted = 0.3976)
- Alpha (annualized): **+54.81%** (daily = +0.002175, t = +1.45, p = 0.1492)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9612 | +12.31 | 0.0000 *** |
| SMB | -0.3339 | -1.23 | 0.2191  |
| HML | -0.1307 | -0.53 | 0.5964  |
| RMW | -1.0428 | -3.39 | 0.0008 *** |
| CMA | +0.3771 | +1.21 | 0.2274  |

_Interpretation: Weak profitability_

### IBM

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.2018 (adjusted = 0.1923)
- Alpha (annualized): **+10.95%** (daily = +0.000435, t = +0.50, p = 0.6143)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8084 | +8.86 | 0.0000 *** |
| SMB | +0.0647 | +0.42 | 0.6771  |
| HML | +0.1729 | +1.22 | 0.2215  |
| RMW | -0.0202 | -0.11 | 0.9087  |
| CMA | -0.0538 | -0.30 | 0.7633  |

_Interpretation: Neutral profile_

### MSFT

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.5197 (adjusted = 0.5140)
- Alpha (annualized): **-15.19%** (daily = -0.000603, t = -1.13, p = 0.2590)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8854 | +15.68 | 0.0000 *** |
| SMB | -0.2606 | -2.71 | 0.0070 ** |
| HML | -0.4179 | -4.78 | 0.0000 *** |
| RMW | +0.1356 | +1.25 | 0.2138  |
| CMA | -0.4990 | -4.51 | 0.0000 *** |

_Interpretation: Neutral profile_

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

### ASTS

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.2906 (adjusted = 0.2822)
- Alpha (annualized): **+152.22%** (daily = +0.006040, t = +2.09, p = 0.0371)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3944 | +4.56 | 0.0000 *** |
| SMB | +1.7794 | +3.42 | 0.0007 *** |
| HML | -1.5103 | -3.19 | 0.0015 ** |
| RMW | -2.7498 | -4.66 | 0.0000 *** |
| CMA | +0.0244 | +0.04 | 0.9676  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### NFLX

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.2674 (adjusted = 0.2587)
- Alpha (annualized): **+13.83%** (daily = +0.000549, t = +0.62, p = 0.5361)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7345 | +7.83 | 0.0000 *** |
| SMB | -0.7567 | -4.74 | 0.0000 *** |
| HML | -0.1911 | -1.32 | 0.1888  |
| RMW | -0.6054 | -3.35 | 0.0009 *** |
| CMA | +0.1446 | +0.79 | 0.4315  |

_Interpretation: Large-cap tilt; Weak profitability_

### NVDA

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.6962 (adjusted = 0.6926)
- Alpha (annualized): **+16.73%** (daily = +0.000664, t = +0.80, p = 0.4238)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7275 | +19.68 | 0.0000 *** |
| SMB | -0.8400 | -5.62 | 0.0000 *** |
| HML | -1.1892 | -8.75 | 0.0000 *** |
| RMW | -0.3618 | -2.14 | 0.0332 * |
| CMA | +1.6075 | +9.35 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### DTE

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.1401 (adjusted = 0.1299)
- Alpha (annualized): **+5.41%** (daily = +0.000215, t = +0.44, p = 0.6598)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2974 | +5.76 | 0.0000 *** |
| SMB | -0.2105 | -2.40 | 0.0170 * |
| HML | +0.5489 | +6.87 | 0.0000 *** |
| RMW | -0.1890 | -1.90 | 0.0582  |
| CMA | +0.0497 | +0.49 | 0.6232  |

_Interpretation: Value tilt; Modest factor fit_

### RKLB

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.3885 (adjusted = 0.3812)
- Alpha (annualized): **+157.44%** (daily = +0.006248, t = +2.86, p = 0.0045)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4091 | +6.09 | 0.0000 *** |
| SMB | +0.6825 | +1.73 | 0.0841  |
| HML | -0.8064 | -2.25 | 0.0249 * |
| RMW | -3.3979 | -7.61 | 0.0000 *** |
| CMA | -0.0469 | -0.10 | 0.9177  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### AMD

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.4831 (adjusted = 0.4770)
- Alpha (annualized): **+5.01%** (daily = +0.000199, t = +0.16, p = 0.8763)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5753 | +11.66 | 0.0000 *** |
| SMB | -0.5974 | -2.60 | 0.0097 ** |
| HML | -0.4844 | -2.32 | 0.0210 * |
| RMW | -1.7022 | -6.53 | 0.0000 *** |
| CMA | -0.0909 | -0.34 | 0.7313  |

_Interpretation: Large-cap tilt; Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._