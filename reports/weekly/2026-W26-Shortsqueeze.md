# Weekly Report — `Shortsqueeze` — 2026-W26

Generated: 2026-06-28  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W26.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| GRPN | -3.32% | +0.668 | +1.130 | -0.326 | -1.854 | +0.630 | 0.163 | 440 | Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit |
| LFVN | -0.69% | +0.787 | +1.202 | -0.677 | +0.655 | +0.146 | 0.086 | 440 | Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit |
| WEN | -50.24% | +0.549 | +0.836 | +0.280 | +0.382 | +0.649 | 0.193 | 440 | Small-cap tilt; Conservative investment; Significant negative alpha; Modest factor fit |
| ALL | +4.08% | +0.687 | -0.285 | +0.797 | +0.352 | -0.168 | 0.212 | 440 | Value tilt |
| AMD | +6.07% | +1.579 | -0.573 | -0.517 | -1.700 | -0.093 | 0.483 | 440 | Large-cap tilt; Growth tilt; Weak profitability |
| CC | -5.11% | +1.790 | +1.781 | +0.303 | +0.212 | +1.226 | 0.443 | 440 | Small-cap tilt; Conservative investment |
| GE | +21.85% | +1.175 | -0.282 | +0.101 | -0.125 | -0.098 | 0.406 | 440 | Neutral profile |
| GL | +13.56% | +0.893 | -0.142 | +0.806 | -0.005 | -0.099 | 0.375 | 440 | Value tilt |
| ET | +3.74% | +0.751 | -0.218 | +0.379 | -0.285 | +0.323 | 0.320 | 440 | Neutral profile |
| DTE | +6.70% | +0.278 | -0.119 | +0.548 | -0.190 | +0.019 | 0.140 | 440 | Value tilt; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| LFVN | **60.00** | 20.00 | 10.00 | 30.00 | 0.168 | -0.696 | 0.5539 | 0.0326 | 190 |
| AMD | **60.00** | 6.67 | 30.00 | 23.33 | 0.424 | +0.347 | 0.5032 | 0.0297 | 190 |
| ET | **60.00** | 33.33 | 20.00 | 6.67 | 0.060 | +0.070 | 0.1608 | 0.0095 | 190 |
| GL | **60.00** | 23.33 | 26.67 | 10.00 | 0.137 | +0.145 | 0.2134 | 0.0126 | 190 |
| GRPN | **56.67** | 16.67 | 6.67 | 33.33 | 0.258 | -0.757 | 0.5702 | 0.0336 | 190 |
| ALL | **56.67** | 26.67 | 13.33 | 16.67 | 0.130 | -0.020 | 0.2359 | 0.0139 | 190 |
| GE | **56.67** | 10.00 | 33.33 | 13.33 | 0.411 | +0.699 | 0.2336 | 0.0138 | 190 |
| DTE | **56.67** | 30.00 | 23.33 | 3.33 | 0.066 | +0.090 | 0.1583 | 0.0093 | 190 |
| CC | **46.67** | 3.33 | 16.67 | 26.67 | 0.426 | +0.058 | 0.5259 | 0.0310 | 190 |
| WEN | **36.67** | 13.33 | 3.33 | 20.00 | 0.298 | -0.852 | 0.3648 | 0.0215 | 190 |

## Per-ticker FF5 Detail

### GRPN

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.1631 (adjusted = 0.1534)
- Alpha (annualized): **-3.32%** (daily = -0.000132, t = -0.06, p = 0.9540)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6681 | +2.75 | 0.0063 ** |
| SMB | +1.1305 | +2.87 | 0.0043 ** |
| HML | -0.3263 | -0.87 | 0.3829  |
| RMW | -1.8540 | -3.94 | 0.0001 *** |
| CMA | +0.6298 | +1.33 | 0.1830  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit_

### LFVN

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.0861 (adjusted = 0.0756)
- Alpha (annualized): **-0.69%** (daily = -0.000027, t = -0.01, p = 0.9890)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7869 | +3.72 | 0.0002 *** |
| SMB | +1.2023 | +3.51 | 0.0005 *** |
| HML | -0.6766 | -2.08 | 0.0379 * |
| RMW | +0.6548 | +1.60 | 0.1103  |
| CMA | +0.1456 | +0.35 | 0.7232  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit_

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

### ALL

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.2119 (adjusted = 0.2028)
- Alpha (annualized): **+4.08%** (daily = +0.000162, t = +0.24, p = 0.8111)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6874 | +9.52 | 0.0000 *** |
| SMB | -0.2845 | -2.43 | 0.0153 * |
| HML | +0.7971 | +7.19 | 0.0000 *** |
| RMW | +0.3525 | +2.53 | 0.0119 * |
| CMA | -0.1675 | -1.20 | 0.2323  |

_Interpretation: Value tilt_

### AMD

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.4833 (adjusted = 0.4774)
- Alpha (annualized): **+6.07%** (daily = +0.000241, t = +0.19, p = 0.8481)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5792 | +11.79 | 0.0000 *** |
| SMB | -0.5730 | -2.64 | 0.0086 ** |
| HML | -0.5173 | -2.52 | 0.0123 * |
| RMW | -1.7000 | -6.57 | 0.0000 *** |
| CMA | -0.0928 | -0.36 | 0.7212  |

_Interpretation: Large-cap tilt; Growth tilt; Weak profitability_

### CC

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.4426 (adjusted = 0.4361)
- Alpha (annualized): **-5.11%** (daily = -0.000203, t = -0.14, p = 0.8858)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7904 | +11.90 | 0.0000 *** |
| SMB | +1.7809 | +7.31 | 0.0000 *** |
| HML | +0.3025 | +1.31 | 0.1906  |
| RMW | +0.2120 | +0.73 | 0.4661  |
| CMA | +1.2257 | +4.20 | 0.0000 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### GE

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.4065 (adjusted = 0.3996)
- Alpha (annualized): **+21.85%** (daily = +0.000867, t = +1.17, p = 0.2446)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1751 | +14.81 | 0.0000 *** |
| SMB | -0.2821 | -2.20 | 0.0286 * |
| HML | +0.1012 | +0.83 | 0.4061  |
| RMW | -0.1250 | -0.82 | 0.4151  |
| CMA | -0.0983 | -0.64 | 0.5232  |

_Interpretation: Neutral profile_

### GL

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.3753 (adjusted = 0.3681)
- Alpha (annualized): **+13.56%** (daily = +0.000538, t = +0.93, p = 0.3516)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8928 | +14.52 | 0.0000 *** |
| SMB | -0.1420 | -1.43 | 0.1547  |
| HML | +0.8060 | +8.54 | 0.0000 *** |
| RMW | -0.0055 | -0.05 | 0.9633  |
| CMA | -0.0990 | -0.83 | 0.4071  |

_Interpretation: Value tilt_

### ET

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.3199 (adjusted = 0.3121)
- Alpha (annualized): **+3.74%** (daily = +0.000149, t = +0.25, p = 0.7995)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7508 | +12.05 | 0.0000 *** |
| SMB | -0.2178 | -2.16 | 0.0314 * |
| HML | +0.3795 | +3.97 | 0.0001 *** |
| RMW | -0.2855 | -2.37 | 0.0181 * |
| CMA | +0.3228 | +2.67 | 0.0078 ** |

_Interpretation: Neutral profile_

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

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._