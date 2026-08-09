# Weekly Report — `all-stocks` — 2026-W32

Generated: 2026-08-09  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W32.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +44.58% | +1.016 | +2.235 | +0.557 | +0.397 | +0.358 | 0.108 | 411 | Small-cap tilt; Value tilt; Modest factor fit |
| MU | +65.43% | +1.950 | -0.286 | -0.173 | -0.965 | +0.307 | 0.391 | 411 | Weak profitability |
| AMD | +6.53% | +1.610 | -0.554 | -0.477 | -1.661 | -0.172 | 0.487 | 411 | Large-cap tilt; Weak profitability |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| NVDA | +20.74% | +1.679 | -0.833 | -1.152 | -0.352 | +1.421 | 0.677 | 411 | Large-cap tilt; Growth tilt; Conservative investment |
| PLTR | +76.68% | +1.585 | -0.755 | -0.050 | -2.339 | -0.866 | 0.444 | 411 | Large-cap tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| MSFT | -11.85% | +0.884 | -0.272 | -0.433 | +0.144 | -0.460 | 0.512 | 411 | Neutral profile |
| DTE | +2.45% | +0.290 | -0.195 | +0.544 | -0.229 | +0.084 | 0.145 | 411 | Value tilt; Modest factor fit |
| GOOGL | +33.01% | +1.021 | +0.218 | -0.525 | +0.498 | -0.722 | 0.439 | 411 | Growth tilt; Aggressive investment |
| NBIS | +171.20% | +1.642 | +0.745 | -2.284 | -2.007 | -0.014 | 0.295 | 360 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| NBIS | **90.00** | 26.67 | 30.00 | 33.33 | 0.312 | +1.205 | 1.0585 | 0.0571 | 161 |
| SNDK | **86.67** | 23.33 | 33.33 | 30.00 | 0.319 | +2.192 | 1.0565 | 0.0570 | 161 |
| HTZ | **73.33** | 30.00 | 16.67 | 26.67 | 0.117 | +0.168 | 0.8338 | 0.0450 | 161 |
| MU | **70.00** | 20.00 | 26.67 | 23.33 | 0.336 | +0.800 | 0.6226 | 0.0336 | 161 |
| AMD | **53.33** | 10.00 | 23.33 | 20.00 | 0.482 | +0.597 | 0.5428 | 0.0293 | 161 |
| DTE | **43.33** | 33.33 | 6.67 | 3.33 | 0.068 | +0.042 | 0.1725 | 0.0093 | 161 |
| GOOGL | **40.00** | 16.67 | 10.00 | 13.33 | 0.381 | +0.142 | 0.2642 | 0.0142 | 161 |
| PLTR | **36.67** | 6.67 | 13.33 | 16.67 | 0.528 | +0.160 | 0.4054 | 0.0219 | 161 |
| NVDA | **33.33** | 3.33 | 20.00 | 10.00 | 0.665 | +0.554 | 0.2368 | 0.0128 | 161 |
| MSFT | **23.33** | 13.33 | 3.33 | 6.67 | 0.442 | -0.550 | 0.2142 | 0.0116 | 161 |

## Per-ticker FF5 Detail

### HTZ

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.1082 (adjusted = 0.0971)
- Alpha (annualized): **+44.58%** (daily = +0.001769, t = +0.60, p = 0.5456)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0161 | +3.25 | 0.0013 ** |
| SMB | +2.2346 | +4.25 | 0.0000 *** |
| HML | +0.5566 | +1.16 | 0.2463  |
| RMW | +0.3973 | +0.67 | 0.5031  |
| CMA | +0.3585 | +0.58 | 0.5615  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### MU

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.3913 (adjusted = 0.3837)
- Alpha (annualized): **+65.43%** (daily = +0.002596, t = +1.68, p = 0.0935)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9501 | +11.80 | 0.0000 *** |
| SMB | -0.2861 | -1.03 | 0.3038  |
| HML | -0.1733 | -0.68 | 0.4938  |
| RMW | -0.9650 | -3.08 | 0.0022 ** |
| CMA | +0.3067 | +0.94 | 0.3468  |

_Interpretation: Weak profitability_

### AMD

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.4873 (adjusted = 0.4810)
- Alpha (annualized): **+6.53%** (daily = +0.000259, t = +0.20, p = 0.8415)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6105 | +11.63 | 0.0000 *** |
| SMB | -0.5541 | -2.38 | 0.0178 * |
| HML | -0.4766 | -2.25 | 0.0252 * |
| RMW | -1.6609 | -6.33 | 0.0000 *** |
| CMA | -0.1720 | -0.63 | 0.5289  |

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

### NVDA

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.6771 (adjusted = 0.6731)
- Alpha (annualized): **+20.74%** (daily = +0.000823, t = +0.99, p = 0.3248)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6790 | +18.79 | 0.0000 *** |
| SMB | -0.8330 | -5.55 | 0.0000 *** |
| HML | -1.1523 | -8.42 | 0.0000 *** |
| RMW | -0.3521 | -2.08 | 0.0380 * |
| CMA | +1.4208 | +8.07 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### PLTR

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.4442 (adjusted = 0.4373)
- Alpha (annualized): **+76.68%** (daily = +0.003043, t = +2.01, p = 0.0451)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5846 | +9.78 | 0.0000 *** |
| SMB | -0.7552 | -2.77 | 0.0058 ** |
| HML | -0.0499 | -0.20 | 0.8408  |
| RMW | -2.3389 | -7.62 | 0.0000 *** |
| CMA | -0.8664 | -2.71 | 0.0069 ** |

_Interpretation: Large-cap tilt; Weak profitability; Aggressive investment; Significant positive alpha_

### MSFT

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.5124 (adjusted = 0.5063)
- Alpha (annualized): **-11.85%** (daily = -0.000470, t = -0.86, p = 0.3900)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8843 | +15.12 | 0.0000 *** |
| SMB | -0.2721 | -2.77 | 0.0059 ** |
| HML | -0.4329 | -4.83 | 0.0000 *** |
| RMW | +0.1444 | +1.30 | 0.1930  |
| CMA | -0.4601 | -3.99 | 0.0001 *** |

_Interpretation: Neutral profile_

### DTE

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.1455 (adjusted = 0.1349)
- Alpha (annualized): **+2.45%** (daily = +0.000097, t = +0.20, p = 0.8429)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2903 | +5.53 | 0.0000 *** |
| SMB | -0.1951 | -2.21 | 0.0277 * |
| HML | +0.5436 | +6.76 | 0.0000 *** |
| RMW | -0.2292 | -2.31 | 0.0216 * |
| CMA | +0.0837 | +0.81 | 0.4189  |

_Interpretation: Value tilt; Modest factor fit_

### GOOGL

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.4392 (adjusted = 0.4323)
- Alpha (annualized): **+33.01%** (daily = +0.001310, t = +1.84, p = 0.0667)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0212 | +13.39 | 0.0000 *** |
| SMB | +0.2180 | +1.70 | 0.0898  |
| HML | -0.5247 | -4.49 | 0.0000 *** |
| RMW | +0.4976 | +3.45 | 0.0006 *** |
| CMA | -0.7218 | -4.80 | 0.0000 *** |

_Interpretation: Growth tilt; Aggressive investment_

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

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._