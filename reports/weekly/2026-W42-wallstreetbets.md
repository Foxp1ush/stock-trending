# Weekly Report — `wallstreetbets` — 2026-W42

Generated: 2026-10-18  ·  Source: `apewisdom:wallstreetbets`  ·  Lookback: 7 days

[← Back to dashboard](2026-W42.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +73.45% | +1.988 | -0.273 | -0.130 | -0.925 | +0.142 | 0.405 | 362 | Weak profitability |
| NBIS | +171.20% | +1.642 | +0.745 | -2.284 | -2.007 | -0.014 | 0.295 | 360 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| TSLA | +32.46% | +2.215 | +0.073 | +0.063 | -0.270 | -1.267 | 0.458 | 362 | Aggressive investment |
| CRWV | +106.86% | +2.051 | +0.880 | -1.356 | -0.298 | -2.178 | 0.214 | 252 | Small-cap tilt; Growth tilt; Aggressive investment |
| NVDA | +18.89% | +1.650 | -0.836 | -1.103 | -0.297 | +1.089 | 0.664 | 362 | Large-cap tilt; Growth tilt; Conservative investment |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| ASTS | +100.05% | +1.290 | +0.984 | -1.186 | -2.924 | -0.341 | 0.315 | 362 | Small-cap tilt; Growth tilt; Weak profitability |
| DTE | -0.10% | +0.299 | -0.230 | +0.564 | -0.245 | +0.123 | 0.156 | 362 | Value tilt; Modest factor fit |
| AMD | +9.48% | +1.588 | -0.584 | -0.418 | -1.665 | -0.279 | 0.476 | 362 | Large-cap tilt; Weak profitability |
| RKLB | +135.30% | +1.459 | +0.634 | -0.873 | -3.354 | -0.029 | 0.404 | 362 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **96.67** | 30.00 | 33.33 | 33.33 | 0.340 | +2.643 | 1.3451 | 0.0593 | 112 |
| CRWV | **76.67** | 20.00 | 30.00 | 26.67 | 0.403 | +1.706 | 1.0920 | 0.0482 | 112 |
| ASTS | **70.00** | 26.67 | 13.33 | 30.00 | 0.369 | +0.366 | 1.2883 | 0.0568 | 112 |
| NBIS | **63.33** | 13.33 | 26.67 | 23.33 | 0.464 | +1.435 | 1.0418 | 0.0459 | 112 |
| MU | **63.33** | 23.33 | 23.33 | 16.67 | 0.391 | +1.199 | 0.7850 | 0.0346 | 112 |
| DTE | **43.33** | 33.33 | 6.67 | 3.33 | 0.060 | +0.046 | 0.2255 | 0.0099 | 112 |
| AMD | **40.00** | 6.67 | 20.00 | 13.33 | 0.572 | +1.015 | 0.5615 | 0.0248 | 112 |
| RKLB | **40.00** | 10.00 | 10.00 | 20.00 | 0.522 | +0.261 | 0.9234 | 0.0407 | 112 |
| TSLA | **30.00** | 16.67 | 3.33 | 10.00 | 0.461 | +0.016 | 0.4228 | 0.0186 | 112 |
| NVDA | **26.67** | 3.33 | 16.67 | 6.67 | 0.713 | +0.677 | 0.2817 | 0.0124 | 112 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.4046 (adjusted = 0.3962)
- Alpha (annualized): **+73.45%** (daily = +0.002915, t = +1.76, p = 0.0788)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9877 | +11.66 | 0.0000 *** |
| SMB | -0.2735 | -0.91 | 0.3645  |
| HML | -0.1296 | -0.49 | 0.6273  |
| RMW | -0.9246 | -2.84 | 0.0047 ** |
| CMA | +0.1421 | +0.41 | 0.6857  |

_Interpretation: Weak profitability_

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

### TSLA

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.4581 (adjusted = 0.4505)
- Alpha (annualized): **+32.46%** (daily = +0.001288, t = +0.83, p = 0.4096)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2146 | +13.77 | 0.0000 *** |
| SMB | +0.0727 | +0.26 | 0.7981  |
| HML | +0.0627 | +0.25 | 0.8034  |
| RMW | -0.2697 | -0.88 | 0.3800  |
| CMA | -1.2670 | -3.83 | 0.0002 *** |

_Interpretation: Aggressive investment_

### CRWV

- Period: `2025-03-31` to `2026-03-31` (252 obs)
- R² = 0.2140 (adjusted = 0.1981)
- Alpha (annualized): **+106.86%** (daily = +0.004241, t = +0.99, p = 0.3214)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.0513 | +4.87 | 0.0000 *** |
| SMB | +0.8804 | +1.10 | 0.2704  |
| HML | -1.3559 | -1.62 | 0.1060  |
| RMW | -0.2978 | -0.35 | 0.7255  |
| CMA | -2.1775 | -1.99 | 0.0472 * |

_Interpretation: Small-cap tilt; Growth tilt; Aggressive investment_

### NVDA

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.6638 (adjusted = 0.6590)
- Alpha (annualized): **+18.89%** (daily = +0.000750, t = +0.84, p = 0.4016)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6497 | +17.92 | 0.0000 *** |
| SMB | -0.8360 | -5.14 | 0.0000 *** |
| HML | -1.1029 | -7.66 | 0.0000 *** |
| RMW | -0.2973 | -1.69 | 0.0912  |
| CMA | +1.0890 | +5.75 | 0.0000 *** |

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

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.3145 (adjusted = 0.3049)
- Alpha (annualized): **+100.05%** (daily = +0.003970, t = +1.43, p = 0.1530)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2895 | +4.51 | 0.0000 *** |
| SMB | +0.9843 | +1.95 | 0.0521  |
| HML | -1.1855 | -2.65 | 0.0084 ** |
| RMW | -2.9244 | -5.37 | 0.0000 *** |
| CMA | -0.3406 | -0.58 | 0.5630  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### DTE

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.1556 (adjusted = 0.1438)
- Alpha (annualized): **-0.10%** (daily = -0.000004, t = -0.01, p = 0.9939)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2995 | +5.42 | 0.0000 *** |
| SMB | -0.2297 | -2.35 | 0.0191 * |
| HML | +0.5636 | +6.52 | 0.0000 *** |
| RMW | -0.2453 | -2.33 | 0.0205 * |
| CMA | +0.1227 | +1.08 | 0.2813  |

_Interpretation: Value tilt; Modest factor fit_

### AMD

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.4759 (adjusted = 0.4685)
- Alpha (annualized): **+9.48%** (daily = +0.000376, t = +0.26, p = 0.7931)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5881 | +10.75 | 0.0000 *** |
| SMB | -0.5839 | -2.24 | 0.0259 * |
| HML | -0.4177 | -1.81 | 0.0717  |
| RMW | -1.6648 | -5.91 | 0.0000 *** |
| CMA | -0.2787 | -0.92 | 0.3602  |

_Interpretation: Large-cap tilt; Weak profitability_

### RKLB

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.4037 (adjusted = 0.3954)
- Alpha (annualized): **+135.30%** (daily = +0.005369, t = +2.25, p = 0.0248)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4593 | +5.94 | 0.0000 *** |
| SMB | +0.6340 | +1.46 | 0.1449  |
| HML | -0.8729 | -2.27 | 0.0237 * |
| RMW | -3.3544 | -7.16 | 0.0000 *** |
| CMA | -0.0290 | -0.06 | 0.9542  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._