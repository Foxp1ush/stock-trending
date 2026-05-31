# Weekly Report — `all-stocks` — 2026-W22

Generated: 2026-05-31  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W22.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +43.34% | +2.039 | -0.405 | -0.147 | -0.843 | +0.356 | 0.395 | 459 | Weak profitability |
| NVDA | +19.83% | +1.752 | -0.799 | -1.234 | -0.248 | +1.498 | 0.672 | 459 | Large-cap tilt; Growth tilt; Conservative investment |
| SPCE | -87.10% | +0.887 | +2.210 | -0.853 | -2.010 | -0.240 | 0.289 | 459 | Small-cap tilt; Growth tilt; Weak profitability |
| MSFT | -13.41% | +0.889 | -0.252 | -0.404 | +0.139 | -0.498 | 0.525 | 459 | Neutral profile |
| ASTS | +163.44% | +1.506 | +1.538 | -1.565 | -2.449 | -0.048 | 0.274 | 459 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| CRSR | -42.40% | +2.022 | +1.304 | +0.109 | -0.437 | +0.604 | 0.349 | 459 | Small-cap tilt; Conservative investment |
| AMD | -1.68% | +1.578 | -0.569 | -0.476 | -1.726 | -0.026 | 0.476 | 459 | Large-cap tilt; Weak profitability |
| RKLB | +154.98% | +1.453 | +0.574 | -0.751 | -3.314 | -0.059 | 0.381 | 459 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| LUNR | +99.31% | +1.527 | +1.281 | -0.670 | -3.999 | -0.439 | 0.317 | 459 | Small-cap tilt; Growth tilt; Weak profitability |
| DELL | -7.72% | +1.657 | -0.190 | -0.360 | -0.394 | +0.866 | 0.355 | 459 | Conservative investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| LUNR | **76.67** | 16.67 | 30.00 | 30.00 | 0.395 | +0.589 | 0.8082 | 0.0508 | 209 |
| ASTS | **70.00** | 20.00 | 16.67 | 33.33 | 0.292 | +0.056 | 0.8651 | 0.0544 | 209 |
| RKLB | **70.00** | 13.33 | 33.33 | 23.33 | 0.407 | +0.771 | 0.6581 | 0.0414 | 209 |
| MU | **66.67** | 23.33 | 26.67 | 16.67 | 0.284 | +0.458 | 0.5109 | 0.0321 | 209 |
| CRSR | **63.33** | 30.00 | 6.67 | 26.67 | 0.225 | -0.257 | 0.6659 | 0.0419 | 209 |
| DELL | **56.67** | 33.33 | 13.33 | 10.00 | 0.186 | +0.007 | 0.4578 | 0.0288 | 209 |
| SPCE | **56.67** | 26.67 | 10.00 | 20.00 | 0.273 | -0.174 | 0.6123 | 0.0385 | 209 |
| AMD | **40.00** | 6.67 | 20.00 | 13.33 | 0.425 | +0.271 | 0.4630 | 0.0291 | 209 |
| NVDA | **33.33** | 3.33 | 23.33 | 6.67 | 0.601 | +0.361 | 0.2109 | 0.0133 | 209 |
| MSFT | **16.67** | 10.00 | 3.33 | 3.33 | 0.414 | -0.410 | 0.1760 | 0.0111 | 209 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.3952 (adjusted = 0.3885)
- Alpha (annualized): **+43.34%** (daily = +0.001720, t = +1.19, p = 0.2338)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.0395 | +13.11 | 0.0000 *** |
| SMB | -0.4051 | -1.62 | 0.1060  |
| HML | -0.1466 | -0.62 | 0.5386  |
| RMW | -0.8426 | -2.84 | 0.0047 ** |
| CMA | +0.3556 | +1.18 | 0.2368  |

_Interpretation: Weak profitability_

### NVDA

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.6725 (adjusted = 0.6689)
- Alpha (annualized): **+19.83%** (daily = +0.000787, t = +0.95, p = 0.3446)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7516 | +19.53 | 0.0000 *** |
| SMB | -0.7990 | -5.54 | 0.0000 *** |
| HML | -1.2338 | -8.98 | 0.0000 *** |
| RMW | -0.2475 | -1.45 | 0.1487  |
| CMA | +1.4980 | +8.65 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### SPCE

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.2886 (adjusted = 0.2807)
- Alpha (annualized): **-87.10%** (daily = -0.003456, t = -1.59, p = 0.1117)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8870 | +3.79 | 0.0002 *** |
| SMB | +2.2100 | +5.88 | 0.0000 *** |
| HML | -0.8529 | -2.38 | 0.0176 * |
| RMW | -2.0101 | -4.51 | 0.0000 *** |
| CMA | -0.2403 | -0.53 | 0.5946  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### MSFT

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.5250 (adjusted = 0.5197)
- Alpha (annualized): **-13.41%** (daily = -0.000532, t = -1.06, p = 0.2882)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8890 | +16.48 | 0.0000 *** |
| SMB | -0.2523 | -2.91 | 0.0038 ** |
| HML | -0.4037 | -4.89 | 0.0000 *** |
| RMW | +0.1390 | +1.35 | 0.1774  |
| CMA | -0.4978 | -4.78 | 0.0000 *** |

_Interpretation: Neutral profile_

### ASTS

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.2737 (adjusted = 0.2657)
- Alpha (annualized): **+163.44%** (daily = +0.006486, t = +2.33, p = 0.0201)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5061 | +5.02 | 0.0000 *** |
| SMB | +1.5380 | +3.19 | 0.0015 ** |
| HML | -1.5649 | -3.41 | 0.0007 *** |
| RMW | -2.4491 | -4.28 | 0.0000 *** |
| CMA | -0.0478 | -0.08 | 0.9342  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### CRSR

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.3490 (adjusted = 0.3418)
- Alpha (annualized): **-42.40%** (daily = -0.001682, t = -0.96, p = 0.3352)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.0218 | +10.75 | 0.0000 *** |
| SMB | +1.3039 | +4.31 | 0.0000 *** |
| HML | +0.1092 | +0.38 | 0.7046  |
| RMW | -0.4368 | -1.22 | 0.2240  |
| CMA | +0.6041 | +1.66 | 0.0967  |

_Interpretation: Small-cap tilt; Conservative investment_

### AMD

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.4763 (adjusted = 0.4705)
- Alpha (annualized): **-1.68%** (daily = -0.000067, t = -0.05, p = 0.9564)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5777 | +11.99 | 0.0000 *** |
| SMB | -0.5693 | -2.69 | 0.0074 ** |
| HML | -0.4755 | -2.36 | 0.0187 * |
| RMW | -1.7265 | -6.88 | 0.0000 *** |
| CMA | -0.0259 | -0.10 | 0.9189  |

_Interpretation: Large-cap tilt; Weak profitability_

### RKLB

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.3806 (adjusted = 0.3738)
- Alpha (annualized): **+154.98%** (daily = +0.006150, t = +2.97, p = 0.0031)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4527 | +6.51 | 0.0000 *** |
| SMB | +0.5735 | +1.60 | 0.1110  |
| HML | -0.7506 | -2.20 | 0.0286 * |
| RMW | -3.3145 | -7.78 | 0.0000 *** |
| CMA | -0.0587 | -0.14 | 0.8918  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### LUNR

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.3174 (adjusted = 0.3099)
- Alpha (annualized): **+99.31%** (daily = +0.003941, t = +1.40, p = 0.1631)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5272 | +5.02 | 0.0000 *** |
| SMB | +1.2808 | +2.62 | 0.0091 ** |
| HML | -0.6696 | -1.44 | 0.1512  |
| RMW | -3.9991 | -6.89 | 0.0000 *** |
| CMA | -0.4391 | -0.75 | 0.4548  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### DELL

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.3545 (adjusted = 0.3474)
- Alpha (annualized): **-7.72%** (daily = -0.000306, t = -0.24, p = 0.8131)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6565 | +11.86 | 0.0000 *** |
| SMB | -0.1904 | -0.85 | 0.3971  |
| HML | -0.3601 | -1.68 | 0.0930  |
| RMW | -0.3942 | -1.48 | 0.1397  |
| CMA | +0.8661 | +3.21 | 0.0014 ** |

_Interpretation: Conservative investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._