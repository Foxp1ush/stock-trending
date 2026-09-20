# Weekly Report — `all-stocks` — 2026-W38

Generated: 2026-09-20  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W38.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +80.60% | +1.981 | -0.345 | -0.091 | -1.001 | +0.293 | 0.389 | 382 | Weak profitability |
| NVDA | +22.78% | +1.647 | -0.855 | -1.103 | -0.337 | +1.213 | 0.661 | 382 | Large-cap tilt; Growth tilt; Conservative investment |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| DTE | +1.51% | +0.295 | -0.204 | +0.553 | -0.223 | +0.079 | 0.147 | 382 | Value tilt; Modest factor fit |
| AMD | +5.35% | +1.591 | -0.615 | -0.399 | -1.688 | -0.243 | 0.472 | 382 | Large-cap tilt; Weak profitability |
| NBIS | +171.20% | +1.642 | +0.745 | -2.284 | -2.007 | -0.014 | 0.295 | 360 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| META | +1.91% | +1.378 | -0.017 | -0.555 | +0.443 | -0.541 | 0.504 | 382 | Growth tilt; Aggressive investment |
| AVGO | +50.10% | +1.613 | -0.141 | -1.275 | +0.083 | -0.212 | 0.459 | 382 | Growth tilt |
| IQ | -31.15% | +1.031 | +0.333 | +0.183 | -0.674 | +0.255 | 0.141 | 382 | Weak profitability; Modest factor fit |
| EU | -11.20% | +0.872 | +1.439 | -1.224 | -0.962 | -0.134 | 0.169 | 382 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **90.00** | 23.33 | 33.33 | 33.33 | 0.332 | +2.343 | 1.2347 | 0.0596 | 132 |
| EU | **83.33** | 26.67 | 30.00 | 26.67 | 0.301 | +1.351 | 0.8696 | 0.0420 | 132 |
| NBIS | **70.00** | 13.33 | 26.67 | 30.00 | 0.424 | +1.307 | 0.9535 | 0.0460 | 132 |
| MU | **66.67** | 20.00 | 23.33 | 23.33 | 0.360 | +0.918 | 0.7173 | 0.0346 | 132 |
| IQ | **56.67** | 30.00 | 10.00 | 16.67 | 0.196 | +0.124 | 0.5140 | 0.0248 | 132 |
| AMD | **50.00** | 10.00 | 20.00 | 20.00 | 0.513 | +0.670 | 0.6274 | 0.0303 | 132 |
| DTE | **40.00** | 33.33 | 3.33 | 3.33 | 0.066 | +0.030 | 0.1987 | 0.0096 | 132 |
| AVGO | **33.33** | 6.67 | 13.33 | 13.33 | 0.556 | +0.493 | 0.3920 | 0.0189 | 132 |
| META | **33.33** | 16.67 | 6.67 | 10.00 | 0.368 | +0.123 | 0.3824 | 0.0185 | 132 |
| NVDA | **26.67** | 3.33 | 16.67 | 6.67 | 0.696 | +0.615 | 0.2633 | 0.0127 | 132 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.3891 (adjusted = 0.3810)
- Alpha (annualized): **+80.60%** (daily = +0.003198, t = +1.96, p = 0.0504)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9811 | +11.57 | 0.0000 *** |
| SMB | -0.3445 | -1.15 | 0.2507  |
| HML | -0.0909 | -0.34 | 0.7345  |
| RMW | -1.0011 | -3.08 | 0.0022 ** |
| CMA | +0.2931 | +0.85 | 0.3979  |

_Interpretation: Weak profitability_

### NVDA

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.6609 (adjusted = 0.6564)
- Alpha (annualized): **+22.78%** (daily = +0.000904, t = +1.04, p = 0.2973)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6467 | +18.10 | 0.0000 *** |
| SMB | -0.8553 | -5.37 | 0.0000 *** |
| HML | -1.1035 | -7.75 | 0.0000 *** |
| RMW | -0.3374 | -1.95 | 0.0517  |
| CMA | +1.2133 | +6.59 | 0.0000 *** |

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

### DTE

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.1466 (adjusted = 0.1352)
- Alpha (annualized): **+1.51%** (daily = +0.000060, t = +0.12, p = 0.9080)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2953 | +5.42 | 0.0000 *** |
| SMB | -0.2038 | -2.14 | 0.0332 * |
| HML | +0.5532 | +6.49 | 0.0000 *** |
| RMW | -0.2231 | -2.15 | 0.0319 * |
| CMA | +0.0789 | +0.72 | 0.4750  |

_Interpretation: Value tilt; Modest factor fit_

### AMD

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.4723 (adjusted = 0.4653)
- Alpha (annualized): **+5.35%** (daily = +0.000212, t = +0.15, p = 0.8777)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5911 | +10.99 | 0.0000 *** |
| SMB | -0.6149 | -2.43 | 0.0157 * |
| HML | -0.3991 | -1.76 | 0.0790  |
| RMW | -1.6875 | -6.13 | 0.0000 *** |
| CMA | -0.2435 | -0.83 | 0.4066  |

_Interpretation: Large-cap tilt; Weak profitability_

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

### META

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.5043 (adjusted = 0.4977)
- Alpha (annualized): **+1.91%** (daily = +0.000076, t = +0.09, p = 0.9284)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3781 | +15.59 | 0.0000 *** |
| SMB | -0.0174 | -0.11 | 0.9107  |
| HML | -0.5550 | -4.01 | 0.0001 *** |
| RMW | +0.4432 | +2.64 | 0.0087 ** |
| CMA | -0.5409 | -3.02 | 0.0027 ** |

_Interpretation: Growth tilt; Aggressive investment_

### AVGO

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.4592 (adjusted = 0.4520)
- Alpha (annualized): **+50.10%** (daily = +0.001988, t = +1.55, p = 0.1219)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6128 | +11.97 | 0.0000 *** |
| SMB | -0.1409 | -0.60 | 0.5502  |
| HML | -1.2753 | -6.05 | 0.0000 *** |
| RMW | +0.0829 | +0.32 | 0.7460  |
| CMA | -0.2119 | -0.78 | 0.4375  |

_Interpretation: Growth tilt_

### IQ

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.1406 (adjusted = 0.1292)
- Alpha (annualized): **-31.15%** (daily = -0.001236, t = -0.68, p = 0.4988)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0311 | +5.38 | 0.0000 *** |
| SMB | +0.3332 | +0.99 | 0.3214  |
| HML | +0.1830 | +0.61 | 0.5425  |
| RMW | -0.6739 | -1.85 | 0.0652  |
| CMA | +0.2548 | +0.66 | 0.5120  |

_Interpretation: Weak profitability; Modest factor fit_

### EU

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.1686 (adjusted = 0.1575)
- Alpha (annualized): **-11.20%** (daily = -0.000444, t = -0.18, p = 0.8608)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8716 | +3.27 | 0.0012 ** |
| SMB | +1.4388 | +3.09 | 0.0022 ** |
| HML | -1.2235 | -2.94 | 0.0035 ** |
| RMW | -0.9617 | -1.90 | 0.0579  |
| CMA | -0.1341 | -0.25 | 0.8034  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._