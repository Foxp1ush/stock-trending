# Weekly Report — `wallstreetbets` — 2026-W40

Generated: 2026-09-28  ·  Source: `apewisdom:wallstreetbets`  ·  Lookback: 7 days

[← Back to dashboard](2026-W40.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| META | +1.49% | +1.379 | -0.013 | -0.553 | +0.445 | -0.542 | 0.505 | 377 | Growth tilt; Aggressive investment |
| MU | +69.57% | +1.971 | -0.288 | -0.130 | -0.935 | +0.222 | 0.398 | 377 | Weak profitability |
| AMD | +2.99% | +1.591 | -0.599 | -0.403 | -1.670 | -0.267 | 0.472 | 377 | Large-cap tilt; Weak profitability |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| DTE | +0.28% | +0.294 | -0.194 | +0.556 | -0.233 | +0.096 | 0.151 | 377 | Value tilt; Modest factor fit |
| GOOG | +39.22% | +1.009 | +0.177 | -0.508 | +0.474 | -0.743 | 0.445 | 377 | Growth tilt; Aggressive investment; Significant positive alpha |
| GOOGL | +40.25% | +1.018 | +0.170 | -0.523 | +0.500 | -0.758 | 0.440 | 377 | Growth tilt; Robust profitability; Aggressive investment; Significant positive alpha |
| NVDA | +23.36% | +1.649 | -0.860 | -1.098 | -0.329 | +1.188 | 0.661 | 377 | Large-cap tilt; Growth tilt; Conservative investment |
| MSFT | -12.71% | +0.879 | -0.299 | -0.421 | +0.133 | -0.463 | 0.504 | 377 | Neutral profile |
| BB | +13.64% | +1.027 | +0.248 | -0.442 | -1.246 | +0.818 | 0.281 | 377 | Weak profitability; Conservative investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **93.33** | 26.67 | 33.33 | 33.33 | 0.333 | +2.363 | 1.2718 | 0.0602 | 127 |
| MU | **83.33** | 23.33 | 30.00 | 30.00 | 0.362 | +0.910 | 0.7407 | 0.0351 | 127 |
| AMD | **60.00** | 6.67 | 26.67 | 26.67 | 0.516 | +0.649 | 0.6504 | 0.0308 | 127 |
| BB | **60.00** | 30.00 | 6.67 | 23.33 | 0.266 | -0.517 | 0.4429 | 0.0210 | 127 |
| GOOGL | **53.33** | 16.67 | 20.00 | 16.67 | 0.427 | +0.155 | 0.2820 | 0.0133 | 127 |
| META | **53.33** | 20.00 | 13.33 | 20.00 | 0.383 | +0.122 | 0.3914 | 0.0185 | 127 |
| DTE | **46.67** | 33.33 | 10.00 | 3.33 | 0.066 | +0.055 | 0.2036 | 0.0096 | 127 |
| GOOG | **43.33** | 13.33 | 16.67 | 13.33 | 0.431 | +0.153 | 0.2751 | 0.0130 | 127 |
| NVDA | **36.67** | 3.33 | 23.33 | 10.00 | 0.697 | +0.613 | 0.2685 | 0.0127 | 127 |
| MSFT | **20.00** | 10.00 | 3.33 | 6.67 | 0.456 | -0.623 | 0.2604 | 0.0123 | 127 |

## Per-ticker FF5 Detail

### META

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.5045 (adjusted = 0.4979)
- Alpha (annualized): **+1.49%** (daily = +0.000059, t = +0.07, p = 0.9446)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3792 | +15.49 | 0.0000 *** |
| SMB | -0.0128 | -0.08 | 0.9350  |
| HML | -0.5535 | -3.97 | 0.0001 *** |
| RMW | +0.4453 | +2.63 | 0.0089 ** |
| CMA | -0.5418 | -2.99 | 0.0030 ** |

_Interpretation: Growth tilt; Aggressive investment_

### MU

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.3979 (adjusted = 0.3898)
- Alpha (annualized): **+69.57%** (daily = +0.002761, t = +1.71, p = 0.0873)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9710 | +11.72 | 0.0000 *** |
| SMB | -0.2881 | -0.98 | 0.3297  |
| HML | -0.1295 | -0.49 | 0.6237  |
| RMW | -0.9352 | -2.92 | 0.0037 ** |
| CMA | +0.2216 | +0.65 | 0.5184  |

_Interpretation: Weak profitability_

### AMD

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.4723 (adjusted = 0.4652)
- Alpha (annualized): **+2.99%** (daily = +0.000119, t = +0.09, p = 0.9322)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5910 | +10.92 | 0.0000 *** |
| SMB | -0.5994 | -2.34 | 0.0196 * |
| HML | -0.4032 | -1.77 | 0.0783  |
| RMW | -1.6700 | -6.02 | 0.0000 *** |
| CMA | -0.2667 | -0.90 | 0.3697  |

_Interpretation: Large-cap tilt; Weak profitability_

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

### DTE

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.1506 (adjusted = 0.1391)
- Alpha (annualized): **+0.28%** (daily = +0.000011, t = +0.02, p = 0.9828)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2941 | +5.39 | 0.0000 *** |
| SMB | -0.1940 | -2.03 | 0.0436 * |
| HML | +0.5562 | +6.50 | 0.0000 *** |
| RMW | -0.2332 | -2.24 | 0.0254 * |
| CMA | +0.0963 | +0.87 | 0.3872  |

_Interpretation: Value tilt; Modest factor fit_

### GOOG

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.4449 (adjusted = 0.4374)
- Alpha (annualized): **+39.22%** (daily = +0.001556, t = +2.09, p = 0.0369)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0093 | +13.00 | 0.0000 *** |
| SMB | +0.1772 | +1.30 | 0.1943  |
| HML | -0.5084 | -4.18 | 0.0000 *** |
| RMW | +0.4744 | +3.21 | 0.0014 ** |
| CMA | -0.7431 | -4.70 | 0.0000 *** |

_Interpretation: Growth tilt; Aggressive investment; Significant positive alpha_

### GOOGL

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.4397 (adjusted = 0.4321)
- Alpha (annualized): **+40.25%** (daily = +0.001597, t = +2.11, p = 0.0357)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0176 | +12.85 | 0.0000 *** |
| SMB | +0.1703 | +1.23 | 0.2211  |
| HML | -0.5231 | -4.21 | 0.0000 *** |
| RMW | +0.5002 | +3.32 | 0.0010 *** |
| CMA | -0.7578 | -4.70 | 0.0000 *** |

_Interpretation: Growth tilt; Robust profitability; Aggressive investment; Significant positive alpha_

### NVDA

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.6613 (adjusted = 0.6568)
- Alpha (annualized): **+23.36%** (daily = +0.000927, t = +1.06, p = 0.2896)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6493 | +18.06 | 0.0000 *** |
| SMB | -0.8598 | -5.37 | 0.0000 *** |
| HML | -1.0982 | -7.67 | 0.0000 *** |
| RMW | -0.3285 | -1.89 | 0.0595  |
| CMA | +1.1881 | +6.38 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### MSFT

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.5037 (adjusted = 0.4970)
- Alpha (annualized): **-12.71%** (daily = -0.000505, t = -0.86, p = 0.3927)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8786 | +14.26 | 0.0000 *** |
| SMB | -0.2992 | -2.77 | 0.0059 ** |
| HML | -0.4213 | -4.36 | 0.0000 *** |
| RMW | +0.1326 | +1.13 | 0.2588  |
| CMA | -0.4635 | -3.69 | 0.0003 *** |

_Interpretation: Neutral profile_

### BB

- Period: `2024-09-27` to `2026-03-31` (377 obs)
- R² = 0.2806 (adjusted = 0.2709)
- Alpha (annualized): **+13.64%** (daily = +0.000541, t = +0.35, p = 0.7254)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0273 | +6.39 | 0.0000 *** |
| SMB | +0.2483 | +0.88 | 0.3795  |
| HML | -0.4420 | -1.75 | 0.0804  |
| RMW | -1.2460 | -4.07 | 0.0001 *** |
| CMA | +0.8177 | +2.49 | 0.0130 * |

_Interpretation: Weak profitability; Conservative investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._