# Weekly Report — `all-stocks` — 2026-W27

Generated: 2026-07-05  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W27.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +45.46% | +1.979 | -0.451 | -0.134 | -1.038 | +0.454 | 0.405 | 436 | Weak profitability |
| MSFT | -15.23% | +0.888 | -0.259 | -0.408 | +0.146 | -0.509 | 0.524 | 436 | Aggressive investment |
| WEN | -48.11% | +0.553 | +0.830 | +0.284 | +0.388 | +0.648 | 0.192 | 436 | Small-cap tilt; Conservative investment; Modest factor fit |
| META | +7.61% | +1.376 | -0.124 | -0.620 | +0.513 | -0.618 | 0.513 | 436 | Growth tilt; Robust profitability; Aggressive investment |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| NVDA | +18.99% | +1.726 | -0.828 | -1.169 | -0.359 | +1.657 | 0.698 | 436 | Large-cap tilt; Growth tilt; Conservative investment |
| NBIS | +171.20% | +1.642 | +0.745 | -2.284 | -2.007 | -0.014 | 0.295 | 360 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| AMD | +5.10% | +1.575 | -0.583 | -0.551 | -1.694 | -0.084 | 0.488 | 436 | Large-cap tilt; Growth tilt; Weak profitability |
| ASTS | +148.78% | +1.420 | +1.581 | -1.511 | -2.751 | -0.036 | 0.290 | 436 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| TSLA | +20.22% | +2.265 | -0.108 | -0.156 | -0.223 | -0.924 | 0.452 | 436 | Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **96.67** | 33.33 | 33.33 | 30.00 | 0.288 | +1.817 | 0.9513 | 0.0554 | 186 |
| NBIS | **93.33** | 30.00 | 30.00 | 33.33 | 0.292 | +1.299 | 0.9751 | 0.0567 | 186 |
| MU | **70.00** | 20.00 | 26.67 | 23.33 | 0.300 | +0.577 | 0.5706 | 0.0332 | 186 |
| ASTS | **63.33** | 23.33 | 13.33 | 26.67 | 0.299 | +0.122 | 0.9394 | 0.0547 | 186 |
| AMD | **46.67** | 6.67 | 20.00 | 20.00 | 0.428 | +0.370 | 0.5107 | 0.0297 | 186 |
| WEN | **43.33** | 26.67 | 3.33 | 13.33 | 0.295 | -0.865 | 0.3709 | 0.0216 | 186 |
| META | **43.33** | 16.67 | 16.67 | 10.00 | 0.348 | +0.232 | 0.3113 | 0.0181 | 186 |
| TSLA | **40.00** | 13.33 | 10.00 | 16.67 | 0.369 | -0.183 | 0.3732 | 0.0217 | 186 |
| NVDA | **33.33** | 3.33 | 23.33 | 6.67 | 0.631 | +0.433 | 0.2233 | 0.0130 | 186 |
| MSFT | **20.00** | 10.00 | 6.67 | 3.33 | 0.426 | -0.462 | 0.1957 | 0.0114 | 186 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.4050 (adjusted = 0.3981)
- Alpha (annualized): **+45.46%** (daily = +0.001804, t = +1.22, p = 0.2246)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9787 | +12.54 | 0.0000 *** |
| SMB | -0.4513 | -1.77 | 0.0779  |
| HML | -0.1337 | -0.55 | 0.5813  |
| RMW | -1.0379 | -3.41 | 0.0007 *** |
| CMA | +0.4543 | +1.48 | 0.1402  |

_Interpretation: Weak profitability_

### MSFT

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.5238 (adjusted = 0.5183)
- Alpha (annualized): **-15.23%** (daily = -0.000604, t = -1.16, p = 0.2482)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8880 | +15.97 | 0.0000 *** |
| SMB | -0.2595 | -2.88 | 0.0041 ** |
| HML | -0.4081 | -4.78 | 0.0000 *** |
| RMW | +0.1464 | +1.36 | 0.1734  |
| CMA | -0.5092 | -4.70 | 0.0000 *** |

_Interpretation: Aggressive investment_

### WEN

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.1917 (adjusted = 0.1823)
- Alpha (annualized): **-48.11%** (daily = -0.001909, t = -1.96, p = 0.0511)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5531 | +5.33 | 0.0000 *** |
| SMB | +0.8296 | +4.94 | 0.0000 *** |
| HML | +0.2843 | +1.78 | 0.0753  |
| RMW | +0.3876 | +1.93 | 0.0538  |
| CMA | +0.6475 | +3.20 | 0.0015 ** |

_Interpretation: Small-cap tilt; Conservative investment; Modest factor fit_

### META

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.5129 (adjusted = 0.5072)
- Alpha (annualized): **+7.61%** (daily = +0.000302, t = +0.39, p = 0.6987)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3758 | +16.58 | 0.0000 *** |
| SMB | -0.1235 | -0.92 | 0.3579  |
| HML | -0.6203 | -4.87 | 0.0000 *** |
| RMW | +0.5127 | +3.20 | 0.0015 ** |
| CMA | -0.6179 | -3.82 | 0.0002 *** |

_Interpretation: Growth tilt; Robust profitability; Aggressive investment_

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

### NVDA

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.6977 (adjusted = 0.6942)
- Alpha (annualized): **+18.99%** (daily = +0.000754, t = +0.92, p = 0.3581)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7257 | +19.80 | 0.0000 *** |
| SMB | -0.8284 | -5.87 | 0.0000 *** |
| HML | -1.1690 | -8.74 | 0.0000 *** |
| RMW | -0.3594 | -2.14 | 0.0333 * |
| CMA | +1.6572 | +9.76 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

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

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.4877 (adjusted = 0.4817)
- Alpha (annualized): **+5.10%** (daily = +0.000202, t = +0.16, p = 0.8725)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5749 | +11.75 | 0.0000 *** |
| SMB | -0.5833 | -2.69 | 0.0074 ** |
| HML | -0.5513 | -2.68 | 0.0077 ** |
| RMW | -1.6940 | -6.54 | 0.0000 *** |
| CMA | -0.0844 | -0.32 | 0.7468  |

_Interpretation: Large-cap tilt; Growth tilt; Weak profitability_

### ASTS

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.2903 (adjusted = 0.2821)
- Alpha (annualized): **+148.78%** (daily = +0.005904, t = +2.08, p = 0.0382)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4200 | +4.70 | 0.0000 *** |
| SMB | +1.5810 | +3.23 | 0.0013 ** |
| HML | -1.5107 | -3.26 | 0.0012 ** |
| RMW | -2.7512 | -4.72 | 0.0000 *** |
| CMA | -0.0358 | -0.06 | 0.9515  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### TSLA

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.4517 (adjusted = 0.4453)
- Alpha (annualized): **+20.22%** (daily = +0.000803, t = +0.57, p = 0.5709)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2645 | +15.04 | 0.0000 *** |
| SMB | -0.1078 | -0.44 | 0.6582  |
| HML | -0.1556 | -0.67 | 0.5011  |
| RMW | -0.2227 | -0.77 | 0.4441  |
| CMA | -0.9243 | -3.15 | 0.0017 ** |

_Interpretation: Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._