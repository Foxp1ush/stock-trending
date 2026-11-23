# Weekly Report — `pennystocks` — 2026-W48

Generated: 2026-11-23  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W48.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| SLS | +115.98% | +0.321 | +1.040 | +0.540 | -1.809 | -1.505 | 0.091 | 337 | Small-cap tilt; Value tilt; Weak profitability; Aggressive investment; Modest factor fit |
| AKAN | -200.01% | +0.062 | +0.125 | -0.803 | -2.093 | +1.637 | 0.056 | 337 | Growth tilt; Weak profitability; Conservative investment; Significant negative alpha; Modest factor fit |
| SEAT | -147.57% | +1.427 | +1.126 | +0.351 | +0.603 | -0.501 | 0.084 | 337 | Small-cap tilt; Robust profitability; Aggressive investment; Modest factor fit |
| VIVS | +102.89% | +0.547 | +2.027 | +0.272 | +2.552 | -1.442 | 0.012 | 337 | Small-cap tilt; Robust profitability; Aggressive investment; Low explanatory power — likely sentiment-driven |
| NVDA | +18.85% | +1.559 | -0.917 | -1.364 | -0.319 | +1.287 | 0.679 | 337 | Large-cap tilt; Growth tilt; Conservative investment |
| AAPL | +5.11% | +1.402 | -0.068 | +0.072 | +0.789 | +0.071 | 0.570 | 337 | Robust profitability |
| ALL | -9.08% | +0.702 | -0.293 | +0.882 | +0.302 | -0.101 | 0.225 | 337 | Value tilt |
| AMD | +24.24% | +1.595 | -0.567 | -0.428 | -1.664 | -0.275 | 0.485 | 337 | Large-cap tilt; Weak profitability |
| AMZN | +2.86% | +1.324 | +0.096 | -0.320 | +0.300 | -0.523 | 0.565 | 337 | Aggressive investment |
| INTC | +23.10% | +1.554 | -0.394 | +1.529 | -1.868 | +0.257 | 0.290 | 337 | Value tilt; Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| VIVS | **96.67** | 33.33 | 30.00 | 33.33 | 0.013 | +1.015 | 2.5984 | 0.0949 | 87 |
| SLS | **70.00** | 20.00 | 23.33 | 26.67 | 0.245 | +0.812 | 1.7059 | 0.0623 | 87 |
| AKAN | **66.67** | 30.00 | 6.67 | 30.00 | 0.161 | -1.371 | 2.4970 | 0.0912 | 87 |
| INTC | **63.33** | 16.67 | 26.67 | 20.00 | 0.380 | +0.893 | 0.9817 | 0.0359 | 87 |
| AMD | **56.67** | 6.67 | 33.33 | 16.67 | 0.591 | +1.053 | 0.6484 | 0.0237 | 87 |
| SEAT | **53.33** | 26.67 | 3.33 | 23.33 | 0.223 | -2.466 | 1.2625 | 0.0461 | 87 |
| ALL | **46.67** | 23.33 | 13.33 | 10.00 | 0.239 | -0.228 | 0.3497 | 0.0128 | 87 |
| NVDA | **36.67** | 3.33 | 20.00 | 13.33 | 0.661 | +0.685 | 0.3516 | 0.0128 | 87 |
| AAPL | **33.33** | 13.33 | 16.67 | 3.33 | 0.392 | +0.185 | 0.2948 | 0.0108 | 87 |
| AMZN | **26.67** | 10.00 | 10.00 | 6.67 | 0.521 | -0.401 | 0.3411 | 0.0125 | 87 |

## Per-ticker FF5 Detail

### SLS

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.0915 (adjusted = 0.0778)
- Alpha (annualized): **+115.98%** (daily = +0.004602, t = +1.46, p = 0.1460)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3205 | +0.99 | 0.3239  |
| SMB | +1.0403 | +1.79 | 0.0740  |
| HML | +0.5405 | +0.99 | 0.3248  |
| RMW | -1.8089 | -2.98 | 0.0031 ** |
| CMA | -1.5055 | -2.19 | 0.0290 * |

_Interpretation: Small-cap tilt; Value tilt; Weak profitability; Aggressive investment; Modest factor fit_

### AKAN

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.0560 (adjusted = 0.0418)
- Alpha (annualized): **-200.01%** (daily = -0.007937, t = -2.06, p = 0.0398)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.0618 | +0.16 | 0.8757  |
| SMB | +0.1249 | +0.18 | 0.8598  |
| HML | -0.8025 | -1.20 | 0.2299  |
| RMW | -2.0932 | -2.84 | 0.0048 ** |
| CMA | +1.6374 | +1.96 | 0.0509  |

_Interpretation: Growth tilt; Weak profitability; Conservative investment; Significant negative alpha; Modest factor fit_

### SEAT

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.0836 (adjusted = 0.0698)
- Alpha (annualized): **-147.57%** (daily = -0.005856, t = -1.88, p = 0.0614)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4271 | +4.45 | 0.0000 *** |
| SMB | +1.1256 | +1.96 | 0.0504  |
| HML | +0.3515 | +0.65 | 0.5166  |
| RMW | +0.6026 | +1.01 | 0.3150  |
| CMA | -0.5008 | -0.74 | 0.4607  |

_Interpretation: Small-cap tilt; Robust profitability; Aggressive investment; Modest factor fit_

### VIVS

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.0115 (adjusted = -0.0034)
- Alpha (annualized): **+102.89%** (daily = +0.004083, t = +0.48, p = 0.6335)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5473 | +0.62 | 0.5338  |
| SMB | +2.0270 | +1.29 | 0.1981  |
| HML | +0.2719 | +0.18 | 0.8548  |
| RMW | +2.5518 | +1.55 | 0.1211  |
| CMA | -1.4417 | -0.78 | 0.4387  |

_Interpretation: Small-cap tilt; Robust profitability; Aggressive investment; Low explanatory power — likely sentiment-driven_

### NVDA

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.6792 (adjusted = 0.6744)
- Alpha (annualized): **+18.85%** (daily = +0.000748, t = +0.82, p = 0.4153)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5587 | +16.55 | 0.0000 *** |
| SMB | -0.9166 | -5.44 | 0.0000 *** |
| HML | -1.3635 | -8.57 | 0.0000 *** |
| RMW | -0.3185 | -1.81 | 0.0713  |
| CMA | +1.2868 | +6.45 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### AAPL

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.5698 (adjusted = 0.5633)
- Alpha (annualized): **+5.11%** (daily = +0.000203, t = +0.29, p = 0.7690)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4024 | +19.78 | 0.0000 *** |
| SMB | -0.0676 | -0.53 | 0.5944  |
| HML | +0.0717 | +0.60 | 0.5498  |
| RMW | +0.7888 | +5.95 | 0.0000 *** |
| CMA | +0.0705 | +0.47 | 0.6388  |

_Interpretation: Robust profitability_

### ALL

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.2250 (adjusted = 0.2133)
- Alpha (annualized): **-9.08%** (daily = -0.000360, t = -0.46, p = 0.6456)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7016 | +8.72 | 0.0000 *** |
| SMB | -0.2928 | -2.04 | 0.0426 * |
| HML | +0.8816 | +6.49 | 0.0000 *** |
| RMW | +0.3017 | +2.01 | 0.0455 * |
| CMA | -0.1010 | -0.59 | 0.5531  |

_Interpretation: Value tilt_

### AMD

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.4853 (adjusted = 0.4776)
- Alpha (annualized): **+24.24%** (daily = +0.000962, t = +0.64, p = 0.5203)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5954 | +10.39 | 0.0000 *** |
| SMB | -0.5671 | -2.07 | 0.0397 * |
| HML | -0.4280 | -1.65 | 0.0998  |
| RMW | -1.6636 | -5.80 | 0.0000 *** |
| CMA | -0.2755 | -0.85 | 0.3970  |

_Interpretation: Large-cap tilt; Weak profitability_

### AMZN

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.5647 (adjusted = 0.5581)
- Alpha (annualized): **+2.86%** (daily = +0.000114, t = +0.15, p = 0.8825)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3239 | +16.77 | 0.0000 *** |
| SMB | +0.0961 | +0.68 | 0.4967  |
| HML | -0.3196 | -2.40 | 0.0171 * |
| RMW | +0.3001 | +2.03 | 0.0427 * |
| CMA | -0.5225 | -3.13 | 0.0019 ** |

_Interpretation: Aggressive investment_

### INTC

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.2896 (adjusted = 0.2789)
- Alpha (annualized): **+23.10%** (daily = +0.000917, t = +0.48, p = 0.6330)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5537 | +7.89 | 0.0000 *** |
| SMB | -0.3939 | -1.12 | 0.2646  |
| HML | +1.5293 | +4.60 | 0.0000 *** |
| RMW | -1.8676 | -5.07 | 0.0000 *** |
| CMA | +0.2573 | +0.62 | 0.5376  |

_Interpretation: Value tilt; Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._