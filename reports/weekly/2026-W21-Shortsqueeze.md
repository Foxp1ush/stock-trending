# Weekly Report — `Shortsqueeze` — 2026-W21

Generated: 2026-05-24  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W21.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| GRPN | -2.13% | +0.693 | +1.227 | -0.365 | -1.701 | +0.661 | 0.161 | 463 | Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit |
| AAPL | +7.70% | +1.305 | -0.063 | -0.113 | +0.813 | +0.067 | 0.520 | 463 | Robust profitability |
| AMD | +2.58% | +1.581 | -0.531 | -0.480 | -1.698 | -0.042 | 0.473 | 463 | Large-cap tilt; Weak profitability |
| AMZN | -2.14% | +1.324 | +0.006 | -0.333 | +0.188 | -0.556 | 0.549 | 463 | Aggressive investment |
| BYND | -38.29% | +1.146 | +0.788 | +0.296 | -1.192 | +1.496 | 0.034 | 463 | Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| BE | +133.63% | +1.421 | +0.116 | -0.005 | -2.647 | -1.557 | 0.202 | 463 | Weak profitability; Aggressive investment; Significant positive alpha |
| CAR | +15.20% | +1.476 | +1.312 | +0.327 | +0.303 | +0.764 | 0.262 | 463 | Small-cap tilt; Conservative investment |
| DTE | +7.15% | +0.277 | -0.102 | +0.555 | -0.180 | +0.074 | 0.144 | 463 | Value tilt; Modest factor fit |
| CC | -10.09% | +1.784 | +1.785 | +0.258 | +0.237 | +1.139 | 0.435 | 463 | Small-cap tilt; Conservative investment |
| ALL | +1.63% | +0.678 | -0.286 | +0.824 | +0.310 | -0.125 | 0.213 | 463 | Value tilt |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| BE | **76.67** | 13.33 | 33.33 | 30.00 | 0.365 | +1.804 | 0.8280 | 0.0528 | 213 |
| CAR | **73.33** | 23.33 | 26.67 | 23.33 | 0.177 | +0.245 | 0.5159 | 0.0329 | 213 |
| BYND | **70.00** | 33.33 | 3.33 | 33.33 | 0.042 | -2.022 | 2.4115 | 0.1538 | 213 |
| DTE | **56.67** | 30.00 | 23.33 | 3.33 | 0.062 | +0.090 | 0.1449 | 0.0092 | 213 |
| ALL | **56.67** | 26.67 | 20.00 | 10.00 | 0.142 | +0.062 | 0.2164 | 0.0138 | 213 |
| GRPN | **53.33** | 20.00 | 6.67 | 26.67 | 0.222 | -0.708 | 0.5390 | 0.0344 | 213 |
| AMD | **50.00** | 3.33 | 30.00 | 16.67 | 0.425 | +0.251 | 0.4541 | 0.0290 | 213 |
| AAPL | **40.00** | 16.67 | 16.67 | 6.67 | 0.341 | +0.048 | 0.1779 | 0.0113 | 213 |
| CC | **40.00** | 6.67 | 13.33 | 20.00 | 0.412 | -0.038 | 0.4846 | 0.0309 | 213 |
| AMZN | **33.33** | 10.00 | 10.00 | 13.33 | 0.396 | -0.397 | 0.2308 | 0.0147 | 213 |

## Per-ticker FF5 Detail

### GRPN

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.1615 (adjusted = 0.1523)
- Alpha (annualized): **-2.13%** (daily = -0.000084, t = -0.04, p = 0.9694)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6931 | +2.92 | 0.0037 ** |
| SMB | +1.2271 | +3.22 | 0.0014 ** |
| HML | -0.3651 | -1.01 | 0.3152  |
| RMW | -1.7005 | -3.76 | 0.0002 *** |
| CMA | +0.6608 | +1.45 | 0.1474  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit_

### AAPL

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.5201 (adjusted = 0.5148)
- Alpha (annualized): **+7.70%** (daily = +0.000305, t = +0.52, p = 0.6021)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3046 | +20.61 | 0.0000 *** |
| SMB | -0.0626 | -0.62 | 0.5376  |
| HML | -0.1128 | -1.17 | 0.2439  |
| RMW | +0.8131 | +6.74 | 0.0000 *** |
| CMA | +0.0666 | +0.55 | 0.5833  |

_Interpretation: Robust profitability_

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

### AMZN

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.5490 (adjusted = 0.5441)
- Alpha (annualized): **-2.14%** (daily = -0.000085, t = -0.13, p = 0.8956)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3237 | +18.92 | 0.0000 *** |
| SMB | +0.0060 | +0.05 | 0.9577  |
| HML | -0.3330 | -3.12 | 0.0019 ** |
| RMW | +0.1877 | +1.41 | 0.1596  |
| CMA | -0.5561 | -4.15 | 0.0000 *** |

_Interpretation: Aggressive investment_

### BYND

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.0336 (adjusted = 0.0231)
- Alpha (annualized): **-38.29%** (daily = -0.001519, t = -0.30, p = 0.7665)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1461 | +2.07 | 0.0387 * |
| SMB | +0.7877 | +0.89 | 0.3745  |
| HML | +0.2956 | +0.35 | 0.7265  |
| RMW | -1.1921 | -1.13 | 0.2582  |
| CMA | +1.4958 | +1.41 | 0.1585  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### BE

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.2023 (adjusted = 0.1935)
- Alpha (annualized): **+133.63%** (daily = +0.005303, t = +1.99, p = 0.0471)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4212 | +4.93 | 0.0000 *** |
| SMB | +0.1157 | +0.25 | 0.8022  |
| HML | -0.0046 | -0.01 | 0.9917  |
| RMW | -2.6474 | -4.82 | 0.0000 *** |
| CMA | -1.5575 | -2.82 | 0.0050 ** |

_Interpretation: Weak profitability; Aggressive investment; Significant positive alpha_

### CAR

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.2625 (adjusted = 0.2544)
- Alpha (annualized): **+15.20%** (daily = +0.000603, t = +0.39, p = 0.6995)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4762 | +8.74 | 0.0000 *** |
| SMB | +1.3123 | +4.85 | 0.0000 *** |
| HML | +0.3272 | +1.27 | 0.2054  |
| RMW | +0.3031 | +0.94 | 0.3467  |
| CMA | +0.7644 | +2.36 | 0.0186 * |

_Interpretation: Small-cap tilt; Conservative investment_

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

### CC

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.4349 (adjusted = 0.4287)
- Alpha (annualized): **-10.09%** (daily = -0.000400, t = -0.29, p = 0.7693)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7840 | +12.09 | 0.0000 *** |
| SMB | +1.7852 | +7.55 | 0.0000 *** |
| HML | +0.2577 | +1.14 | 0.2534  |
| RMW | +0.2374 | +0.85 | 0.3985  |
| CMA | +1.1387 | +4.03 | 0.0001 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### ALL

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.2131 (adjusted = 0.2045)
- Alpha (annualized): **+1.63%** (daily = +0.000065, t = +0.10, p = 0.9207)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6781 | +9.62 | 0.0000 *** |
| SMB | -0.2855 | -2.53 | 0.0118 * |
| HML | +0.8237 | +7.65 | 0.0000 *** |
| RMW | +0.3101 | +2.31 | 0.0213 * |
| CMA | -0.1253 | -0.93 | 0.3539  |

_Interpretation: Value tilt_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._