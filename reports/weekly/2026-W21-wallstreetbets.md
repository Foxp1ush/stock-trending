# Weekly Report — `wallstreetbets` — 2026-W21

Generated: 2026-05-24  ·  Source: `apewisdom:wallstreetbets`  ·  Lookback: 7 days

[← Back to dashboard](2026-W21.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +44.72% | +2.042 | -0.406 | -0.162 | -0.828 | +0.303 | 0.395 | 463 | Weak profitability |
| NVDA | +25.20% | +1.751 | -0.771 | -1.277 | -0.202 | +1.397 | 0.662 | 463 | Large-cap tilt; Growth tilt; Conservative investment |
| MSFT | -14.84% | +0.892 | -0.267 | -0.399 | +0.131 | -0.503 | 0.527 | 463 | Aggressive investment |
| NOW | -26.49% | +0.972 | -0.143 | -0.435 | -0.592 | -0.173 | 0.299 | 463 | Weak profitability |
| ASTS | +217.12% | +1.404 | +1.694 | -1.957 | -2.063 | -0.236 | 0.216 | 463 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| AMD | +2.58% | +1.581 | -0.531 | -0.480 | -1.698 | -0.042 | 0.473 | 463 | Large-cap tilt; Weak profitability |
| RKLB | +157.37% | +1.447 | +0.613 | -0.756 | -3.302 | -0.049 | 0.380 | 463 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| DTE | +7.15% | +0.277 | -0.102 | +0.555 | -0.180 | +0.074 | 0.144 | 463 | Value tilt; Modest factor fit |
| RDDT | +59.23% | +1.590 | +0.025 | -0.889 | -1.089 | -0.678 | 0.254 | 463 | Growth tilt; Weak profitability; Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **90.00** | 26.67 | 33.33 | 30.00 | 0.257 | +1.591 | 0.8380 | 0.0534 | 213 |
| RKLB | **70.00** | 13.33 | 30.00 | 26.67 | 0.403 | +0.734 | 0.6556 | 0.0418 | 213 |
| MU | **70.00** | 23.33 | 26.67 | 20.00 | 0.284 | +0.446 | 0.5008 | 0.0319 | 213 |
| ASTS | **66.67** | 20.00 | 13.33 | 33.33 | 0.292 | +0.036 | 0.8471 | 0.0540 | 213 |
| RDDT | **60.00** | 30.00 | 6.67 | 23.33 | 0.176 | -0.429 | 0.5810 | 0.0371 | 213 |
| DTE | **53.33** | 33.33 | 16.67 | 3.33 | 0.062 | +0.090 | 0.1449 | 0.0092 | 213 |
| AMD | **43.33** | 6.67 | 20.00 | 16.67 | 0.425 | +0.251 | 0.4541 | 0.0290 | 213 |
| NVDA | **36.67** | 3.33 | 23.33 | 10.00 | 0.584 | +0.353 | 0.2137 | 0.0136 | 213 |
| NOW | **33.33** | 16.67 | 3.33 | 13.33 | 0.360 | -1.380 | 0.2920 | 0.0186 | 213 |
| MSFT | **26.67** | 10.00 | 10.00 | 6.67 | 0.419 | -0.410 | 0.1725 | 0.0110 | 213 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.3954 (adjusted = 0.3888)
- Alpha (annualized): **+44.72%** (daily = +0.001775, t = +1.24, p = 0.2157)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.0424 | +13.19 | 0.0000 *** |
| SMB | -0.4056 | -1.63 | 0.1028  |
| HML | -0.1621 | -0.69 | 0.4934  |
| RMW | -0.8275 | -2.81 | 0.0052 ** |
| CMA | +0.3029 | +1.02 | 0.3076  |

_Interpretation: Weak profitability_

### NVDA

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.6623 (adjusted = 0.6586)
- Alpha (annualized): **+25.20%** (daily = +0.001000, t = +1.19, p = 0.2363)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7509 | +19.20 | 0.0000 *** |
| SMB | -0.7709 | -5.27 | 0.0000 *** |
| HML | -1.2768 | -9.16 | 0.0000 *** |
| RMW | -0.2020 | -1.16 | 0.2454  |
| CMA | +1.3967 | +8.00 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### MSFT

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.5272 (adjusted = 0.5220)
- Alpha (annualized): **-14.84%** (daily = -0.000589, t = -1.18, p = 0.2370)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8919 | +16.59 | 0.0000 *** |
| SMB | -0.2669 | -3.10 | 0.0021 ** |
| HML | -0.3988 | -4.85 | 0.0000 *** |
| RMW | +0.1307 | +1.28 | 0.2024  |
| CMA | -0.5030 | -4.88 | 0.0000 *** |

_Interpretation: Aggressive investment_

### NOW

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.2990 (adjusted = 0.2913)
- Alpha (annualized): **-26.49%** (daily = -0.001051, t = -1.04, p = 0.2987)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9720 | +8.89 | 0.0000 *** |
| SMB | -0.1431 | -0.82 | 0.4144  |
| HML | -0.4352 | -2.61 | 0.0094 ** |
| RMW | -0.5919 | -2.84 | 0.0047 ** |
| CMA | -0.1728 | -0.83 | 0.4094  |

_Interpretation: Weak profitability_

### ASTS

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.2155 (adjusted = 0.2069)
- Alpha (annualized): **+217.12%** (daily = +0.008616, t = +2.71, p = 0.0069)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4035 | +4.09 | 0.0001 *** |
| SMB | +1.6937 | +3.08 | 0.0022 ** |
| HML | -1.9573 | -3.73 | 0.0002 *** |
| RMW | -2.0633 | -3.15 | 0.0017 ** |
| CMA | -0.2362 | -0.36 | 0.7196  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### AMD

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.4735 (adjusted = 0.4677)
- Alpha (annualized): **+2.58%** (daily = +0.000103, t = +0.08, p = 0.9328)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5814 | +12.02 | 0.0000 *** |
| SMB | -0.5308 | -2.52 | 0.0121 * |
| HML | -0.4805 | -2.39 | 0.0172 * |
| RMW | -1.6977 | -6.78 | 0.0000 *** |
| CMA | -0.0417 | -0.17 | 0.8685  |

_Interpretation: Large-cap tilt; Weak profitability_

### RKLB

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.3800 (adjusted = 0.3732)
- Alpha (annualized): **+157.37%** (daily = +0.006245, t = +3.04, p = 0.0025)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4467 | +6.51 | 0.0000 *** |
| SMB | +0.6135 | +1.72 | 0.0859  |
| HML | -0.7562 | -2.23 | 0.0265 * |
| RMW | -3.3022 | -7.80 | 0.0000 *** |
| CMA | -0.0491 | -0.12 | 0.9083  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

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

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.1438 (adjusted = 0.1345)
- Alpha (annualized): **+7.15%** (daily = +0.000284, t = +0.60, p = 0.5500)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2770 | +5.40 | 0.0000 *** |
| SMB | -0.1017 | -1.24 | 0.2170  |
| HML | +0.5546 | +7.07 | 0.0000 *** |
| RMW | -0.1804 | -1.85 | 0.0657  |
| CMA | +0.0735 | +0.75 | 0.4549  |

_Interpretation: Value tilt; Modest factor fit_

### RDDT

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.2537 (adjusted = 0.2455)
- Alpha (annualized): **+59.23%** (daily = +0.002351, t = +1.17, p = 0.2410)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5903 | +7.34 | 0.0000 *** |
| SMB | +0.0249 | +0.07 | 0.9428  |
| HML | -0.8886 | -2.69 | 0.0075 ** |
| RMW | -1.0894 | -2.64 | 0.0085 ** |
| CMA | -0.6785 | -1.64 | 0.1025  |

_Interpretation: Growth tilt; Weak profitability; Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._