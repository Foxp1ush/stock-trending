# Weekly Report — `all-stocks` — 2026-W31

Generated: 2026-08-02  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W31.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +61.73% | +1.942 | -0.275 | -0.138 | -1.006 | +0.251 | 0.397 | 416 | Weak profitability |
| MSFT | -13.26% | +0.888 | -0.270 | -0.425 | +0.147 | -0.468 | 0.518 | 416 | Neutral profile |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| NVDA | +18.97% | +1.700 | -0.829 | -1.152 | -0.352 | +1.435 | 0.686 | 416 | Large-cap tilt; Growth tilt; Conservative investment |
| AAPL | +1.61% | +1.315 | -0.129 | -0.059 | +0.771 | +0.149 | 0.537 | 416 | Robust profitability |
| META | +4.75% | +1.372 | -0.020 | -0.553 | +0.461 | -0.574 | 0.515 | 416 | Growth tilt; Aggressive investment |
| RDDT | +55.49% | +1.545 | -0.130 | -0.748 | -1.306 | -0.446 | 0.248 | 416 | Growth tilt; Weak profitability |
| AMZN | +0.19% | +1.357 | +0.058 | -0.334 | +0.281 | -0.576 | 0.561 | 416 | Aggressive investment |
| DTE | +1.43% | +0.308 | -0.199 | +0.548 | -0.207 | +0.083 | 0.151 | 416 | Value tilt; Modest factor fit |
| TSLA | +25.91% | +2.185 | +0.110 | -0.099 | -0.242 | -1.153 | 0.452 | 416 | Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **93.33** | 26.67 | 33.33 | 33.33 | 0.312 | +2.129 | 1.0218 | 0.0568 | 166 |
| MU | **76.67** | 20.00 | 30.00 | 26.67 | 0.330 | +0.775 | 0.6025 | 0.0335 | 166 |
| RDDT | **63.33** | 30.00 | 3.33 | 30.00 | 0.263 | -0.699 | 0.6240 | 0.0347 | 166 |
| META | **56.67** | 16.67 | 20.00 | 20.00 | 0.371 | +0.063 | 0.3093 | 0.0172 | 166 |
| AAPL | **56.67** | 23.33 | 23.33 | 10.00 | 0.329 | +0.086 | 0.2174 | 0.0121 | 166 |
| DTE | **53.33** | 33.33 | 16.67 | 3.33 | 0.069 | +0.053 | 0.1671 | 0.0093 | 166 |
| TSLA | **46.67** | 10.00 | 13.33 | 23.33 | 0.415 | -0.088 | 0.3674 | 0.0204 | 166 |
| NVDA | **43.33** | 3.33 | 26.67 | 13.33 | 0.654 | +0.546 | 0.2322 | 0.0129 | 166 |
| AMZN | **40.00** | 13.33 | 10.00 | 16.67 | 0.401 | -0.491 | 0.2698 | 0.0150 | 166 |
| MSFT | **20.00** | 6.67 | 6.67 | 6.67 | 0.444 | -0.550 | 0.2067 | 0.0115 | 166 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.3965 (adjusted = 0.3892)
- Alpha (annualized): **+61.73%** (daily = +0.002449, t = +1.60, p = 0.1110)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9425 | +12.00 | 0.0000 *** |
| SMB | -0.2746 | -0.99 | 0.3233  |
| HML | -0.1375 | -0.55 | 0.5846  |
| RMW | -1.0056 | -3.22 | 0.0014 ** |
| CMA | +0.2510 | +0.78 | 0.4365  |

_Interpretation: Weak profitability_

### MSFT

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.5183 (adjusted = 0.5125)
- Alpha (annualized): **-13.26%** (daily = -0.000526, t = -0.97, p = 0.3310)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8877 | +15.55 | 0.0000 *** |
| SMB | -0.2703 | -2.76 | 0.0060 ** |
| HML | -0.4248 | -4.79 | 0.0000 *** |
| RMW | +0.1466 | +1.33 | 0.1832  |
| CMA | -0.4683 | -4.12 | 0.0000 *** |

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

### NVDA

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.6858 (adjusted = 0.6819)
- Alpha (annualized): **+18.97%** (daily = +0.000753, t = +0.91, p = 0.3634)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7002 | +19.47 | 0.0000 *** |
| SMB | -0.8287 | -5.53 | 0.0000 *** |
| HML | -1.1520 | -8.50 | 0.0000 *** |
| RMW | -0.3521 | -2.09 | 0.0369 * |
| CMA | +1.4352 | +8.26 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### AAPL

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.5370 (adjusted = 0.5314)
- Alpha (annualized): **+1.61%** (daily = +0.000064, t = +0.10, p = 0.9166)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3149 | +20.40 | 0.0000 *** |
| SMB | -0.1286 | -1.16 | 0.2453  |
| HML | -0.0586 | -0.59 | 0.5585  |
| RMW | +0.7713 | +6.22 | 0.0000 *** |
| CMA | +0.1492 | +1.16 | 0.2453  |

_Interpretation: Robust profitability_

### META

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.5152 (adjusted = 0.5093)
- Alpha (annualized): **+4.75%** (daily = +0.000188, t = +0.24, p = 0.8101)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3724 | +16.60 | 0.0000 *** |
| SMB | -0.0199 | -0.14 | 0.8883  |
| HML | -0.5530 | -4.31 | 0.0000 *** |
| RMW | +0.4614 | +2.90 | 0.0040 ** |
| CMA | -0.5741 | -3.49 | 0.0005 *** |

_Interpretation: Growth tilt; Aggressive investment_

### RDDT

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.2476 (adjusted = 0.2384)
- Alpha (annualized): **+55.49%** (daily = +0.002202, t = +1.02, p = 0.3087)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5449 | +6.77 | 0.0000 *** |
| SMB | -0.1299 | -0.33 | 0.7401  |
| HML | -0.7478 | -2.11 | 0.0353 * |
| RMW | -1.3064 | -2.97 | 0.0031 ** |
| CMA | -0.4458 | -0.98 | 0.3267  |

_Interpretation: Growth tilt; Weak profitability_

### AMZN

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.5613 (adjusted = 0.5559)
- Alpha (annualized): **+0.19%** (daily = +0.000008, t = +0.01, p = 0.9912)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3573 | +18.58 | 0.0000 *** |
| SMB | +0.0582 | +0.46 | 0.6424  |
| HML | -0.3336 | -2.94 | 0.0035 ** |
| RMW | +0.2814 | +2.00 | 0.0462 * |
| CMA | -0.5764 | -3.96 | 0.0001 *** |

_Interpretation: Aggressive investment_

### DTE

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.1509 (adjusted = 0.1405)
- Alpha (annualized): **+1.43%** (daily = +0.000057, t = +0.12, p = 0.9081)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3075 | +5.94 | 0.0000 *** |
| SMB | -0.1991 | -2.24 | 0.0254 * |
| HML | +0.5484 | +6.82 | 0.0000 *** |
| RMW | -0.2068 | -2.07 | 0.0386 * |
| CMA | +0.0828 | +0.80 | 0.4220  |

_Interpretation: Value tilt; Modest factor fit_

### TSLA

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.4518 (adjusted = 0.4451)
- Alpha (annualized): **+25.91%** (daily = +0.001028, t = +0.72, p = 0.4746)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.1852 | +14.40 | 0.0000 *** |
| SMB | +0.1095 | +0.42 | 0.6740  |
| HML | -0.0986 | -0.42 | 0.6757  |
| RMW | -0.2420 | -0.83 | 0.4079  |
| CMA | -1.1531 | -3.82 | 0.0002 *** |

_Interpretation: Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._