# Weekly Report — `pennystocks` — 2026-W36

Generated: 2026-08-31  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W36.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| VNRX | -51.92% | +0.202 | -0.289 | +0.171 | -1.032 | +0.074 | 0.013 | 396 | Weak profitability; Low explanatory power — likely sentiment-driven |
| EPOW | +19.76% | -0.030 | -0.213 | -0.259 | -0.682 | +0.713 | 0.007 | 396 | Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| APRE | -66.26% | +0.261 | +1.035 | -0.693 | -1.094 | +0.767 | 0.070 | 396 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| CXAI | -65.32% | -0.997 | +4.264 | -2.994 | -1.151 | -0.883 | 0.187 | 396 | Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Modest factor fit |
| AMZN | +6.09% | +1.334 | +0.021 | -0.365 | +0.290 | -0.502 | 0.555 | 396 | Aggressive investment |
| AMD | +7.92% | +1.611 | -0.567 | -0.459 | -1.646 | -0.207 | 0.482 | 396 | Large-cap tilt; Weak profitability |
| AVGO | +49.64% | +1.663 | -0.143 | -1.319 | +0.104 | -0.162 | 0.473 | 396 | Growth tilt |
| AEMD | -76.11% | -0.376 | +0.646 | -0.840 | -2.505 | +0.617 | 0.033 | 396 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| DTE | +1.56% | +0.293 | -0.201 | +0.557 | -0.228 | +0.079 | 0.147 | 396 | Value tilt; Modest factor fit |
| IT | -70.16% | +0.844 | +0.352 | -0.180 | +0.184 | +0.045 | 0.145 | 396 | Significant negative alpha; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| EPOW | **100.00** | 33.33 | 33.33 | 33.33 | 0.021 | +1.256 | 1.6183 | 0.0825 | 146 |
| VNRX | **73.33** | 30.00 | 20.00 | 23.33 | 0.031 | -0.146 | 1.1515 | 0.0587 | 146 |
| AEMD | **70.00** | 23.33 | 16.67 | 30.00 | 0.080 | -0.411 | 1.4109 | 0.0720 | 146 |
| CXAI | **53.33** | 16.67 | 10.00 | 26.67 | 0.218 | -1.237 | 1.2012 | 0.0613 | 146 |
| DTE | **53.33** | 26.67 | 23.33 | 3.33 | 0.059 | +0.051 | 0.1852 | 0.0094 | 146 |
| AMD | **50.00** | 3.33 | 30.00 | 16.67 | 0.490 | +0.702 | 0.5864 | 0.0299 | 146 |
| APRE | **46.67** | 20.00 | 6.67 | 20.00 | 0.104 | -1.542 | 1.0587 | 0.0540 | 146 |
| AVGO | **43.33** | 6.67 | 26.67 | 10.00 | 0.469 | +0.462 | 0.4254 | 0.0217 | 146 |
| IT | **30.00** | 13.33 | 3.33 | 13.33 | 0.333 | -1.770 | 0.4868 | 0.0248 | 146 |
| AMZN | **30.00** | 10.00 | 13.33 | 6.67 | 0.417 | -0.469 | 0.2966 | 0.0151 | 146 |

## Per-ticker FF5 Detail

### VNRX

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.0130 (adjusted = 0.0003)
- Alpha (annualized): **-51.92%** (daily = -0.002060, t = -0.69, p = 0.4910)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2019 | +0.64 | 0.5231  |
| SMB | -0.2885 | -0.53 | 0.5953  |
| HML | +0.1705 | +0.35 | 0.7278  |
| RMW | -1.0324 | -1.72 | 0.0856  |
| CMA | +0.0744 | +0.12 | 0.9070  |

_Interpretation: Weak profitability; Low explanatory power — likely sentiment-driven_

### EPOW

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.0070 (adjusted = -0.0057)
- Alpha (annualized): **+19.76%** (daily = +0.000784, t = +0.24, p = 0.8100)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.0302 | -0.09 | 0.9302  |
| SMB | -0.2127 | -0.36 | 0.7193  |
| HML | -0.2593 | -0.49 | 0.6273  |
| RMW | -0.6822 | -1.04 | 0.2968  |
| CMA | +0.7133 | +1.03 | 0.3049  |

_Interpretation: Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### APRE

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.0699 (adjusted = 0.0580)
- Alpha (annualized): **-66.26%** (daily = -0.002629, t = -1.00, p = 0.3174)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2610 | +0.94 | 0.3474  |
| SMB | +1.0347 | +2.17 | 0.0306 * |
| HML | -0.6931 | -1.61 | 0.1080  |
| RMW | -1.0939 | -2.08 | 0.0384 * |
| CMA | +0.7668 | +1.37 | 0.1715  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### CXAI

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.1866 (adjusted = 0.1762)
- Alpha (annualized): **-65.32%** (daily = -0.002592, t = -0.77, p = 0.4439)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.9973 | -2.79 | 0.0055 ** |
| SMB | +4.2642 | +6.94 | 0.0000 *** |
| HML | -2.9939 | -5.40 | 0.0000 *** |
| RMW | -1.1515 | -1.70 | 0.0902  |
| CMA | -0.8832 | -1.23 | 0.2211  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Modest factor fit_

### AMZN

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.5549 (adjusted = 0.5492)
- Alpha (annualized): **+6.09%** (daily = +0.000242, t = +0.34, p = 0.7321)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3344 | +17.91 | 0.0000 *** |
| SMB | +0.0209 | +0.16 | 0.8705  |
| HML | -0.3653 | -3.16 | 0.0017 ** |
| RMW | +0.2902 | +2.05 | 0.0407 * |
| CMA | -0.5017 | -3.34 | 0.0009 *** |

_Interpretation: Aggressive investment_

### AMD

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.4820 (adjusted = 0.4753)
- Alpha (annualized): **+7.92%** (daily = +0.000314, t = +0.24, p = 0.8142)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6111 | +11.40 | 0.0000 *** |
| SMB | -0.5673 | -2.34 | 0.0200 * |
| HML | -0.4593 | -2.10 | 0.0366 * |
| RMW | -1.6463 | -6.14 | 0.0000 *** |
| CMA | -0.2069 | -0.73 | 0.4683  |

_Interpretation: Large-cap tilt; Weak profitability_

### AVGO

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.4731 (adjusted = 0.4663)
- Alpha (annualized): **+49.64%** (daily = +0.001970, t = +1.57, p = 0.1183)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6627 | +12.51 | 0.0000 *** |
| SMB | -0.1428 | -0.62 | 0.5325  |
| HML | -1.3187 | -6.40 | 0.0000 *** |
| RMW | +0.1044 | +0.41 | 0.6792  |
| CMA | -0.1623 | -0.61 | 0.5454  |

_Interpretation: Growth tilt_

### AEMD

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.0327 (adjusted = 0.0203)
- Alpha (annualized): **-76.11%** (daily = -0.003020, t = -0.61, p = 0.5400)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.3756 | -0.72 | 0.4708  |
| SMB | +0.6463 | +0.72 | 0.4702  |
| HML | -0.8401 | -1.04 | 0.2983  |
| RMW | -2.5050 | -2.54 | 0.0115 * |
| CMA | +0.6167 | +0.59 | 0.5571  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### DTE

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.1469 (adjusted = 0.1359)
- Alpha (annualized): **+1.56%** (daily = +0.000062, t = +0.12, p = 0.9027)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2928 | +5.47 | 0.0000 *** |
| SMB | -0.2013 | -2.19 | 0.0293 * |
| HML | +0.5565 | +6.70 | 0.0000 *** |
| RMW | -0.2281 | -2.25 | 0.0253 * |
| CMA | +0.0790 | +0.73 | 0.4646  |

_Interpretation: Value tilt; Modest factor fit_

### IT

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.1445 (adjusted = 0.1336)
- Alpha (annualized): **-70.16%** (daily = -0.002784, t = -2.25, p = 0.0250)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8444 | +6.46 | 0.0000 *** |
| SMB | +0.3523 | +1.57 | 0.1176  |
| HML | -0.1797 | -0.89 | 0.3756  |
| RMW | +0.1843 | +0.74 | 0.4578  |
| CMA | +0.0447 | +0.17 | 0.8654  |

_Interpretation: Significant negative alpha; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._