# Weekly Report — `all-stocks` — 2026-W21

Generated: 2026-05-22  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W21.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +46.18% | +2.041 | -0.400 | -0.174 | -0.804 | +0.290 | 0.395 | 464 | Weak profitability |
| NVDA | +31.75% | +1.744 | -0.744 | -1.333 | -0.095 | +1.336 | 0.645 | 464 | Large-cap tilt; Growth tilt; Conservative investment |
| MSFT | -15.43% | +0.893 | -0.269 | -0.394 | +0.121 | -0.498 | 0.527 | 464 | Neutral profile |
| NOW | -26.81% | +0.972 | -0.144 | -0.432 | -0.597 | -0.170 | 0.299 | 464 | Weak profitability |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| DTE | +5.98% | +0.278 | -0.106 | +0.565 | -0.200 | +0.084 | 0.149 | 464 | Value tilt; Modest factor fit |
| RKLB | +158.45% | +1.446 | +0.618 | -0.765 | -3.285 | -0.059 | 0.380 | 464 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| AMD | +2.32% | +1.582 | -0.532 | -0.478 | -1.702 | -0.039 | 0.474 | 464 | Large-cap tilt; Weak profitability |
| TSLA | +30.89% | +2.307 | -0.113 | -0.113 | -0.135 | -0.868 | 0.440 | 464 | Aggressive investment |
| ASTS | +211.78% | +1.409 | +1.672 | -1.912 | -2.151 | -0.187 | 0.217 | 464 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **93.33** | 30.00 | 33.33 | 30.00 | 0.256 | +1.573 | 0.8357 | 0.0533 | 214 |
| MU | **76.67** | 26.67 | 26.67 | 23.33 | 0.284 | +0.437 | 0.4993 | 0.0319 | 214 |
| RKLB | **70.00** | 13.33 | 30.00 | 26.67 | 0.402 | +0.718 | 0.6540 | 0.0417 | 214 |
| ASTS | **70.00** | 23.33 | 13.33 | 33.33 | 0.292 | +0.021 | 0.8446 | 0.0539 | 214 |
| DTE | **53.33** | 33.33 | 16.67 | 3.33 | 0.062 | +0.097 | 0.1449 | 0.0092 | 214 |
| AMD | **46.67** | 6.67 | 20.00 | 20.00 | 0.425 | +0.247 | 0.4526 | 0.0289 | 214 |
| TSLA | **46.67** | 20.00 | 10.00 | 16.67 | 0.325 | -0.258 | 0.3848 | 0.0246 | 214 |
| NVDA | **36.67** | 3.33 | 23.33 | 10.00 | 0.585 | +0.351 | 0.2130 | 0.0136 | 214 |
| NOW | **33.33** | 16.67 | 3.33 | 13.33 | 0.359 | -1.374 | 0.2912 | 0.0186 | 214 |
| MSFT | **23.33** | 10.00 | 6.67 | 6.67 | 0.421 | -0.410 | 0.1719 | 0.0110 | 214 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.3947 (adjusted = 0.3881)
- Alpha (annualized): **+46.18%** (daily = +0.001832, t = +1.28, p = 0.2003)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.0408 | +13.19 | 0.0000 *** |
| SMB | -0.3996 | -1.61 | 0.1076  |
| HML | -0.1745 | -0.74 | 0.4597  |
| RMW | -0.8038 | -2.74 | 0.0063 ** |
| CMA | +0.2895 | +0.98 | 0.3283  |

_Interpretation: Weak profitability_

### NVDA

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.6449 (adjusted = 0.6410)
- Alpha (annualized): **+31.75%** (daily = +0.001260, t = +1.45, p = 0.1485)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7438 | +18.50 | 0.0000 *** |
| SMB | -0.7442 | -4.93 | 0.0000 *** |
| HML | -1.3325 | -9.27 | 0.0000 *** |
| RMW | -0.0950 | -0.53 | 0.5951  |
| CMA | +1.3364 | +7.41 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### MSFT

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.5267 (adjusted = 0.5215)
- Alpha (annualized): **-15.43%** (daily = -0.000612, t = -1.23, p = 0.2181)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8926 | +16.60 | 0.0000 *** |
| SMB | -0.2693 | -3.13 | 0.0019 ** |
| HML | -0.3937 | -4.81 | 0.0000 *** |
| RMW | +0.1211 | +1.19 | 0.2348  |
| CMA | -0.4975 | -4.84 | 0.0000 *** |

_Interpretation: Neutral profile_

### NOW

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.2995 (adjusted = 0.2918)
- Alpha (annualized): **-26.81%** (daily = -0.001064, t = -1.06, p = 0.2917)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9724 | +8.91 | 0.0000 *** |
| SMB | -0.1444 | -0.83 | 0.4094  |
| HML | -0.4325 | -2.60 | 0.0096 ** |
| RMW | -0.5972 | -2.89 | 0.0040 ** |
| CMA | -0.1699 | -0.81 | 0.4161  |

_Interpretation: Weak profitability_

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

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.1487 (adjusted = 0.1394)
- Alpha (annualized): **+5.98%** (daily = +0.000237, t = +0.50, p = 0.6179)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2783 | +5.41 | 0.0000 *** |
| SMB | -0.1065 | -1.29 | 0.1971  |
| HML | +0.5646 | +7.20 | 0.0000 *** |
| RMW | -0.1996 | -2.05 | 0.0411 * |
| CMA | +0.0844 | +0.86 | 0.3915  |

_Interpretation: Value tilt; Modest factor fit_

### RKLB

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.3803 (adjusted = 0.3735)
- Alpha (annualized): **+158.45%** (daily = +0.006288, t = +3.06, p = 0.0023)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4455 | +6.51 | 0.0000 *** |
| SMB | +0.6179 | +1.74 | 0.0832  |
| HML | -0.7653 | -2.26 | 0.0243 * |
| RMW | -3.2846 | -7.81 | 0.0000 *** |
| CMA | -0.0590 | -0.14 | 0.8896  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### AMD

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.4743 (adjusted = 0.4686)
- Alpha (annualized): **+2.32%** (daily = +0.000092, t = +0.08, p = 0.9396)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5817 | +12.04 | 0.0000 *** |
| SMB | -0.5319 | -2.53 | 0.0118 * |
| HML | -0.4782 | -2.39 | 0.0173 * |
| RMW | -1.7020 | -6.84 | 0.0000 *** |
| CMA | -0.0393 | -0.16 | 0.8758  |

_Interpretation: Large-cap tilt; Weak profitability_

### TSLA

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.4398 (adjusted = 0.4337)
- Alpha (annualized): **+30.89%** (daily = +0.001226, t = +0.89, p = 0.3718)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.3072 | +15.54 | 0.0000 *** |
| SMB | -0.1133 | -0.48 | 0.6341  |
| HML | -0.1132 | -0.50 | 0.6170  |
| RMW | -0.1350 | -0.48 | 0.6314  |
| CMA | -0.8677 | -3.06 | 0.0024 ** |

_Interpretation: Aggressive investment_

### ASTS

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.2170 (adjusted = 0.2085)
- Alpha (annualized): **+211.78%** (daily = +0.008404, t = +2.65, p = 0.0084)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4092 | +4.10 | 0.0000 *** |
| SMB | +1.6719 | +3.04 | 0.0025 ** |
| HML | -1.9119 | -3.65 | 0.0003 *** |
| RMW | -2.1505 | -3.31 | 0.0010 ** |
| CMA | -0.1871 | -0.28 | 0.7759  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._