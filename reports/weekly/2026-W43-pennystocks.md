# Weekly Report — `pennystocks` — 2026-W43

Generated: 2026-10-25  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W43.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| TCRT | +59.36% | +0.175 | -0.436 | +0.475 | -1.858 | -0.727 | 0.027 | 357 | Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven |
| XXII | -463.33% | +0.892 | +0.390 | -0.305 | -0.837 | +1.668 | 0.039 | 357 | Weak profitability; Conservative investment; Significant negative alpha; Low explanatory power — likely sentiment-driven |
| WHLR | -683.60% | +1.108 | +0.240 | +1.085 | -1.537 | +0.011 | 0.024 | 357 | Value tilt; Weak profitability; Significant negative alpha; Low explanatory power — likely sentiment-driven |
| NUAI | +37.75% | +1.643 | -0.504 | +1.916 | -4.355 | +0.537 | 0.080 | 357 | Large-cap tilt; Value tilt; Weak profitability; Conservative investment; Modest factor fit |
| AIXI | -219.68% | +1.800 | +0.769 | -0.174 | -1.160 | +1.078 | 0.136 | 357 | Small-cap tilt; Weak profitability; Conservative investment; Significant negative alpha; Modest factor fit |
| BATL | +230.77% | -0.053 | +0.803 | -1.460 | +2.505 | -0.257 | 0.007 | 357 | Small-cap tilt; Growth tilt; Robust profitability; Low explanatory power — likely sentiment-driven |
| CC | +22.15% | +1.753 | +2.070 | +0.185 | +0.217 | +1.397 | 0.435 | 357 | Small-cap tilt; Conservative investment |
| AVGO | +53.78% | +1.599 | -0.097 | -1.293 | +0.085 | -0.249 | 0.460 | 357 | Growth tilt |
| IBKR | +21.90% | +1.649 | -0.511 | +0.517 | -1.084 | -0.023 | 0.551 | 357 | Large-cap tilt; Value tilt; Weak profitability |
| IP | -24.04% | +1.159 | +0.499 | +0.543 | +0.351 | +0.987 | 0.330 | 357 | Value tilt; Conservative investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| NUAI | **80.00** | 20.00 | 33.33 | 26.67 | 0.175 | +1.267 | 2.1376 | 0.0919 | 107 |
| AIXI | **76.67** | 23.33 | 30.00 | 23.33 | 0.134 | +0.590 | 1.7017 | 0.0732 | 107 |
| BATL | **76.67** | 33.33 | 10.00 | 33.33 | 0.029 | -1.311 | 6.6027 | 0.2839 | 107 |
| WHLR | **66.67** | 30.00 | 6.67 | 30.00 | 0.048 | -1.592 | 3.0795 | 0.1324 | 107 |
| TCRT | **56.67** | 26.67 | 13.33 | 16.67 | 0.097 | -0.665 | 1.1425 | 0.0491 | 107 |
| CC | **53.33** | 13.33 | 26.67 | 13.33 | 0.329 | +0.563 | 0.7712 | 0.0332 | 107 |
| XXII | **40.00** | 16.67 | 3.33 | 20.00 | 0.211 | -1.868 | 1.3560 | 0.0583 | 107 |
| AVGO | **36.67** | 6.67 | 23.33 | 6.67 | 0.573 | +0.505 | 0.4359 | 0.0187 | 107 |
| IP | **36.67** | 10.00 | 16.67 | 10.00 | 0.419 | -0.305 | 0.5089 | 0.0219 | 107 |
| IBKR | **26.67** | 3.33 | 20.00 | 3.33 | 0.682 | -0.001 | 0.3346 | 0.0144 | 107 |

## Per-ticker FF5 Detail

### TCRT

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.0268 (adjusted = 0.0130)
- Alpha (annualized): **+59.36%** (daily = +0.002355, t = +0.59, p = 0.5536)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.1751 | +0.43 | 0.6674  |
| SMB | -0.4359 | -0.60 | 0.5471  |
| HML | +0.4747 | +0.74 | 0.4591  |
| RMW | -1.8580 | -2.39 | 0.0174 * |
| CMA | -0.7270 | -0.86 | 0.3888  |

_Interpretation: Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven_

### XXII

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.0391 (adjusted = 0.0254)
- Alpha (annualized): **-463.33%** (daily = -0.018386, t = -4.20, p = 0.0000)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8919 | +1.99 | 0.0477 * |
| SMB | +0.3897 | +0.49 | 0.6254  |
| HML | -0.3054 | -0.43 | 0.6656  |
| RMW | -0.8371 | -0.98 | 0.3296  |
| CMA | +1.6676 | +1.80 | 0.0734  |

_Interpretation: Weak profitability; Conservative investment; Significant negative alpha; Low explanatory power — likely sentiment-driven_

### WHLR

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.0237 (adjusted = 0.0098)
- Alpha (annualized): **-683.60%** (daily = -0.027127, t = -4.30, p = 0.0000)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1082 | +1.71 | 0.0877  |
| SMB | +0.2405 | +0.21 | 0.8344  |
| HML | +1.0845 | +1.07 | 0.2874  |
| RMW | -1.5367 | -1.24 | 0.2147  |
| CMA | +0.0109 | +0.01 | 0.9935  |

_Interpretation: Value tilt; Weak profitability; Significant negative alpha; Low explanatory power — likely sentiment-driven_

### NUAI

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.0801 (adjusted = 0.0670)
- Alpha (annualized): **+37.75%** (daily = +0.001498, t = +0.23, p = 0.8144)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6434 | +2.52 | 0.0123 * |
| SMB | -0.5043 | -0.43 | 0.6642  |
| HML | +1.9158 | +1.86 | 0.0632  |
| RMW | -4.3553 | -3.49 | 0.0005 *** |
| CMA | +0.5374 | +0.40 | 0.6913  |

_Interpretation: Large-cap tilt; Value tilt; Weak profitability; Conservative investment; Modest factor fit_

### AIXI

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.1357 (adjusted = 0.1234)
- Alpha (annualized): **-219.68%** (daily = -0.008717, t = -2.38, p = 0.0179)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.8000 | +4.79 | 0.0000 *** |
| SMB | +0.7692 | +1.15 | 0.2499  |
| HML | -0.1740 | -0.29 | 0.7686  |
| RMW | -1.1598 | -1.62 | 0.1070  |
| CMA | +1.0782 | +1.39 | 0.1663  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Significant negative alpha; Modest factor fit_

### BATL

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.0069 (adjusted = -0.0073)
- Alpha (annualized): **+230.77%** (daily = +0.009157, t = +1.00, p = 0.3187)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.0527 | -0.06 | 0.9553  |
| SMB | +0.8029 | +0.48 | 0.6310  |
| HML | -1.4600 | -0.99 | 0.3242  |
| RMW | +2.5050 | +1.39 | 0.1640  |
| CMA | -0.2565 | -0.13 | 0.8952  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Low explanatory power — likely sentiment-driven_

### CC

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.4350 (adjusted = 0.4270)
- Alpha (annualized): **+22.15%** (daily = +0.000879, t = +0.53, p = 0.5945)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7526 | +10.36 | 0.0000 *** |
| SMB | +2.0697 | +6.89 | 0.0000 *** |
| HML | +0.1854 | +0.70 | 0.4863  |
| RMW | +0.2174 | +0.67 | 0.5014  |
| CMA | +1.3966 | +3.99 | 0.0001 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### AVGO

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.4600 (adjusted = 0.4523)
- Alpha (annualized): **+53.78%** (daily = +0.002134, t = +1.58, p = 0.1161)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5992 | +11.52 | 0.0000 *** |
| SMB | -0.0967 | -0.39 | 0.6952  |
| HML | -1.2932 | -5.92 | 0.0000 *** |
| RMW | +0.0846 | +0.32 | 0.7500  |
| CMA | -0.2493 | -0.87 | 0.3862  |

_Interpretation: Growth tilt_

### IBKR

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.5511 (adjusted = 0.5447)
- Alpha (annualized): **+21.90%** (daily = +0.000869, t = +0.87, p = 0.3848)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6489 | +16.11 | 0.0000 *** |
| SMB | -0.5108 | -2.81 | 0.0052 ** |
| HML | +0.5173 | +3.21 | 0.0014 ** |
| RMW | -1.0838 | -5.54 | 0.0000 *** |
| CMA | -0.0227 | -0.11 | 0.9148  |

_Interpretation: Large-cap tilt; Value tilt; Weak profitability_

### IP

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.3301 (adjusted = 0.3206)
- Alpha (annualized): **-24.04%** (daily = -0.000954, t = -0.87, p = 0.3875)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1594 | +10.26 | 0.0000 *** |
| SMB | +0.4995 | +2.49 | 0.0133 * |
| HML | +0.5429 | +3.05 | 0.0024 ** |
| RMW | +0.3510 | +1.63 | 0.1049  |
| CMA | +0.9866 | +4.22 | 0.0000 *** |

_Interpretation: Value tilt; Conservative investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._