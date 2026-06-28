# Weekly Report — `all-stocks` — 2026-W26

Generated: 2026-06-28  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W26.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +46.16% | +1.978 | -0.450 | -0.138 | -1.038 | +0.465 | 0.405 | 440 | Weak profitability |
| WEN | -50.24% | +0.549 | +0.836 | +0.280 | +0.382 | +0.649 | 0.193 | 440 | Small-cap tilt; Conservative investment; Significant negative alpha; Modest factor fit |
| MSFT | -14.54% | +0.889 | -0.263 | -0.409 | +0.149 | -0.511 | 0.525 | 440 | Aggressive investment |
| NVDA | +19.65% | +1.721 | -0.821 | -1.174 | -0.368 | +1.684 | 0.698 | 440 | Large-cap tilt; Growth tilt; Conservative investment |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| ASTS | +148.81% | +1.412 | +1.601 | -1.517 | -2.769 | +0.011 | 0.291 | 440 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| DTE | +6.70% | +0.278 | -0.119 | +0.548 | -0.190 | +0.019 | 0.140 | 440 | Value tilt; Modest factor fit |
| MSTR | -9.77% | +1.703 | +0.705 | -0.211 | -2.644 | -0.518 | 0.351 | 440 | Small-cap tilt; Weak profitability; Aggressive investment |
| RKLB | +154.85% | +1.409 | +0.581 | -0.797 | -3.407 | -0.065 | 0.389 | 440 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| GOOG | +24.03% | +1.042 | +0.132 | -0.498 | +0.476 | -0.731 | 0.463 | 440 | Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **96.67** | 30.00 | 33.33 | 33.33 | 0.280 | +1.785 | 0.9366 | 0.0552 | 190 |
| ASTS | **76.67** | 26.67 | 20.00 | 30.00 | 0.296 | +0.112 | 0.9229 | 0.0544 | 190 |
| MU | **73.33** | 23.33 | 30.00 | 20.00 | 0.296 | +0.567 | 0.5601 | 0.0330 | 190 |
| RKLB | **63.33** | 10.00 | 26.67 | 26.67 | 0.409 | +0.557 | 0.7024 | 0.0414 | 190 |
| DTE | **53.33** | 33.33 | 16.67 | 3.33 | 0.066 | +0.090 | 0.1583 | 0.0093 | 190 |
| MSTR | **46.67** | 13.33 | 10.00 | 23.33 | 0.387 | -0.289 | 0.6038 | 0.0356 | 190 |
| GOOG | **43.33** | 16.67 | 13.33 | 13.33 | 0.365 | +0.061 | 0.2304 | 0.0136 | 190 |
| WEN | **40.00** | 20.00 | 3.33 | 16.67 | 0.298 | -0.852 | 0.3648 | 0.0215 | 190 |
| NVDA | **36.67** | 3.33 | 23.33 | 10.00 | 0.633 | +0.420 | 0.2199 | 0.0130 | 190 |
| MSFT | **20.00** | 6.67 | 6.67 | 6.67 | 0.428 | -0.465 | 0.1918 | 0.0113 | 190 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.4054 (adjusted = 0.3986)
- Alpha (annualized): **+46.16%** (daily = +0.001832, t = +1.25, p = 0.2136)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9784 | +12.62 | 0.0000 *** |
| SMB | -0.4500 | -1.77 | 0.0768  |
| HML | -0.1380 | -0.57 | 0.5664  |
| RMW | -1.0383 | -3.43 | 0.0007 *** |
| CMA | +0.4653 | +1.53 | 0.1267  |

_Interpretation: Weak profitability_

### WEN

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.1926 (adjusted = 0.1833)
- Alpha (annualized): **-50.24%** (daily = -0.001994, t = -2.06, p = 0.0402)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5493 | +5.32 | 0.0000 *** |
| SMB | +0.8360 | +5.00 | 0.0000 *** |
| HML | +0.2804 | +1.77 | 0.0774  |
| RMW | +0.3817 | +1.91 | 0.0564  |
| CMA | +0.6491 | +3.24 | 0.0013 ** |

_Interpretation: Small-cap tilt; Conservative investment; Significant negative alpha; Modest factor fit_

### MSFT

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.5252 (adjusted = 0.5197)
- Alpha (annualized): **-14.54%** (daily = -0.000577, t = -1.11, p = 0.2668)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8891 | +16.08 | 0.0000 *** |
| SMB | -0.2633 | -2.94 | 0.0035 ** |
| HML | -0.4086 | -4.81 | 0.0000 *** |
| RMW | +0.1493 | +1.40 | 0.1630  |
| CMA | -0.5109 | -4.76 | 0.0000 *** |

_Interpretation: Aggressive investment_

### NVDA

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.6980 (adjusted = 0.6945)
- Alpha (annualized): **+19.65%** (daily = +0.000780, t = +0.96, p = 0.3384)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7206 | +19.84 | 0.0000 *** |
| SMB | -0.8210 | -5.85 | 0.0000 *** |
| HML | -1.1737 | -8.82 | 0.0000 *** |
| RMW | -0.3678 | -2.19 | 0.0287 * |
| CMA | +1.6836 | +10.01 | 0.0000 *** |

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

### ASTS

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.2910 (adjusted = 0.2828)
- Alpha (annualized): **+148.81%** (daily = +0.005905, t = +2.10, p = 0.0367)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4123 | +4.70 | 0.0000 *** |
| SMB | +1.6014 | +3.29 | 0.0011 ** |
| HML | -1.5168 | -3.29 | 0.0011 ** |
| RMW | -2.7686 | -4.77 | 0.0000 *** |
| CMA | +0.0109 | +0.02 | 0.9851  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### DTE

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.1404 (adjusted = 0.1305)
- Alpha (annualized): **+6.70%** (daily = +0.000266, t = +0.55, p = 0.5836)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2784 | +5.38 | 0.0000 *** |
| SMB | -0.1188 | -1.42 | 0.1565  |
| HML | +0.5485 | +6.91 | 0.0000 *** |
| RMW | -0.1900 | -1.90 | 0.0578  |
| CMA | +0.0194 | +0.19 | 0.8463  |

_Interpretation: Value tilt; Modest factor fit_

### MSTR

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.3508 (adjusted = 0.3433)
- Alpha (annualized): **-9.77%** (daily = -0.000388, t = -0.18, p = 0.8558)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7028 | +7.49 | 0.0000 *** |
| SMB | +0.7053 | +1.92 | 0.0561  |
| HML | -0.2109 | -0.60 | 0.5460  |
| RMW | -2.6445 | -6.02 | 0.0000 *** |
| CMA | -0.5180 | -1.17 | 0.2411  |

_Interpretation: Small-cap tilt; Weak profitability; Aggressive investment_

### RKLB

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.3886 (adjusted = 0.3815)
- Alpha (annualized): **+154.85%** (daily = +0.006145, t = +2.89, p = 0.0041)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4092 | +6.21 | 0.0000 *** |
| SMB | +0.5809 | +1.58 | 0.1145  |
| HML | -0.7970 | -2.29 | 0.0226 * |
| RMW | -3.4069 | -7.77 | 0.0000 *** |
| CMA | -0.0648 | -0.15 | 0.8830  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### GOOG

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.4626 (adjusted = 0.4564)
- Alpha (annualized): **+24.03%** (daily = +0.000953, t = +1.43, p = 0.1521)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0424 | +14.71 | 0.0000 *** |
| SMB | +0.1315 | +1.15 | 0.2522  |
| HML | -0.4983 | -4.58 | 0.0000 *** |
| RMW | +0.4764 | +3.48 | 0.0006 *** |
| CMA | -0.7306 | -5.32 | 0.0000 *** |

_Interpretation: Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._