# Weekly Report — `wallstreetbets` — 2026-W36

Generated: 2026-09-06  ·  Source: `apewisdom:wallstreetbets`  ·  Lookback: 7 days

[← Back to dashboard](2026-W36.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| AVGO | +50.03% | +1.651 | -0.135 | -1.323 | +0.105 | -0.170 | 0.468 | 392 | Growth tilt |
| MU | +74.42% | +1.950 | -0.274 | -0.121 | -0.989 | +0.312 | 0.385 | 392 | Weak profitability |
| NVDA | +24.24% | +1.657 | -0.847 | -1.136 | -0.316 | +1.240 | 0.670 | 392 | Large-cap tilt; Growth tilt; Conservative investment |
| LULU | -27.92% | +1.059 | +0.929 | -0.434 | +0.445 | +0.437 | 0.221 | 392 | Small-cap tilt |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| TSLA | +22.08% | +2.235 | +0.030 | -0.000 | -0.191 | -1.274 | 0.449 | 392 | Aggressive investment |
| DELL | +21.73% | +1.654 | +0.003 | -0.335 | -0.264 | +0.936 | 0.370 | 392 | Conservative investment |
| META | +2.66% | +1.392 | -0.015 | -0.537 | +0.461 | -0.569 | 0.509 | 392 | Growth tilt; Aggressive investment |
| DTE | +1.98% | +0.292 | -0.200 | +0.550 | -0.229 | +0.085 | 0.146 | 392 | Value tilt; Modest factor fit |
| HPE | +5.74% | +1.564 | +0.291 | +0.368 | -0.503 | +0.327 | 0.443 | 392 | Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **93.33** | 26.67 | 33.33 | 33.33 | 0.332 | +2.300 | 1.1552 | 0.0582 | 142 |
| MU | **83.33** | 23.33 | 30.00 | 30.00 | 0.344 | +0.819 | 0.6860 | 0.0346 | 142 |
| DELL | **63.33** | 30.00 | 6.67 | 26.67 | 0.189 | -0.152 | 0.6294 | 0.0317 | 142 |
| DTE | **50.00** | 33.33 | 13.33 | 3.33 | 0.059 | +0.050 | 0.1892 | 0.0095 | 142 |
| HPE | **50.00** | 13.33 | 16.67 | 20.00 | 0.422 | +0.075 | 0.4015 | 0.0202 | 142 |
| META | **50.00** | 20.00 | 20.00 | 10.00 | 0.351 | +0.076 | 0.3614 | 0.0182 | 142 |
| AVGO | **46.67** | 6.67 | 23.33 | 16.67 | 0.526 | +0.537 | 0.3977 | 0.0200 | 142 |
| TSLA | **43.33** | 10.00 | 10.00 | 23.33 | 0.422 | -0.132 | 0.4129 | 0.0208 | 142 |
| NVDA | **36.67** | 3.33 | 26.67 | 6.67 | 0.672 | +0.581 | 0.2593 | 0.0131 | 142 |
| LULU | **33.33** | 16.67 | 3.33 | 13.33 | 0.402 | -0.916 | 0.3808 | 0.0192 | 142 |

## Per-ticker FF5 Detail

### AVGO

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.4683 (adjusted = 0.4614)
- Alpha (annualized): **+50.03%** (daily = +0.001985, t = +1.56, p = 0.1186)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6510 | +12.32 | 0.0000 *** |
| SMB | -0.1354 | -0.59 | 0.5569  |
| HML | -1.3227 | -6.34 | 0.0000 *** |
| RMW | +0.1050 | +0.41 | 0.6786  |
| CMA | -0.1698 | -0.63 | 0.5304  |

_Interpretation: Growth tilt_

### MU

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.3851 (adjusted = 0.3771)
- Alpha (annualized): **+74.42%** (daily = +0.002953, t = +1.84, p = 0.0663)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9499 | +11.51 | 0.0000 *** |
| SMB | -0.2738 | -0.94 | 0.3472  |
| HML | -0.1215 | -0.46 | 0.6452  |
| RMW | -0.9886 | -3.09 | 0.0021 ** |
| CMA | +0.3115 | +0.91 | 0.3625  |

_Interpretation: Weak profitability_

### NVDA

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.6695 (adjusted = 0.6652)
- Alpha (annualized): **+24.24%** (daily = +0.000962, t = +1.13, p = 0.2575)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6567 | +18.49 | 0.0000 *** |
| SMB | -0.8474 | -5.50 | 0.0000 *** |
| HML | -1.1356 | -8.14 | 0.0000 *** |
| RMW | -0.3162 | -1.87 | 0.0625  |
| CMA | +1.2398 | +6.86 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### LULU

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.2208 (adjusted = 0.2107)
- Alpha (annualized): **-27.92%** (daily = -0.001108, t = -0.82, p = 0.4114)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0590 | +7.44 | 0.0000 *** |
| SMB | +0.9287 | +3.80 | 0.0002 *** |
| HML | -0.4341 | -1.96 | 0.0507  |
| RMW | +0.4449 | +1.65 | 0.0988  |
| CMA | +0.4369 | +1.52 | 0.1289  |

_Interpretation: Small-cap tilt_

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

### TSLA

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.4489 (adjusted = 0.4417)
- Alpha (annualized): **+22.08%** (daily = +0.000876, t = +0.59, p = 0.5580)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2348 | +14.16 | 0.0000 *** |
| SMB | +0.0297 | +0.11 | 0.9127  |
| HML | -0.0001 | -0.00 | 0.9996  |
| RMW | -0.1914 | -0.64 | 0.5211  |
| CMA | -1.2736 | -4.00 | 0.0001 *** |

_Interpretation: Aggressive investment_

### DELL

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.3700 (adjusted = 0.3618)
- Alpha (annualized): **+21.73%** (daily = +0.000862, t = +0.64, p = 0.5236)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6537 | +11.59 | 0.0000 *** |
| SMB | +0.0031 | +0.01 | 0.9899  |
| HML | -0.3345 | -1.51 | 0.1328  |
| RMW | -0.2639 | -0.98 | 0.3282  |
| CMA | +0.9360 | +3.25 | 0.0012 ** |

_Interpretation: Conservative investment_

### META

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.5092 (adjusted = 0.5028)
- Alpha (annualized): **+2.66%** (daily = +0.000105, t = +0.13, p = 0.8981)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3920 | +16.02 | 0.0000 *** |
| SMB | -0.0147 | -0.10 | 0.9215  |
| HML | -0.5366 | -3.97 | 0.0001 *** |
| RMW | +0.4613 | +2.81 | 0.0052 ** |
| CMA | -0.5686 | -3.24 | 0.0013 ** |

_Interpretation: Growth tilt; Aggressive investment_

### DTE

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.1459 (adjusted = 0.1349)
- Alpha (annualized): **+1.98%** (daily = +0.000079, t = +0.15, p = 0.8774)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2924 | +5.43 | 0.0000 *** |
| SMB | -0.1999 | -2.16 | 0.0311 * |
| HML | +0.5502 | +6.57 | 0.0000 *** |
| RMW | -0.2288 | -2.25 | 0.0249 * |
| CMA | +0.0850 | +0.78 | 0.4338  |

_Interpretation: Value tilt; Modest factor fit_

### HPE

- Period: `2024-09-06` to `2026-03-31` (392 obs)
- R² = 0.4429 (adjusted = 0.4357)
- Alpha (annualized): **+5.74%** (daily = +0.000228, t = +0.21, p = 0.8328)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5638 | +13.73 | 0.0000 *** |
| SMB | +0.2908 | +1.49 | 0.1381  |
| HML | +0.3683 | +2.08 | 0.0384 * |
| RMW | -0.5034 | -2.34 | 0.0198 * |
| CMA | +0.3275 | +1.43 | 0.1549  |

_Interpretation: Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._