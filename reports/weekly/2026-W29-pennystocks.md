# Weekly Report — `pennystocks` — 2026-W29

Generated: 2026-07-19  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W29.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| BATL | +256.82% | +0.032 | +0.719 | -1.794 | +2.670 | -0.386 | 0.008 | 426 | Small-cap tilt; Growth tilt; Robust profitability; Low explanatory power — likely sentiment-driven |
| SLND | -42.65% | +1.065 | +1.087 | +1.022 | +0.060 | +0.895 | 0.089 | 426 | Small-cap tilt; Value tilt; Conservative investment; Modest factor fit |
| TRX | +89.97% | +0.487 | +0.092 | -0.301 | -1.225 | -0.708 | 0.078 | 426 | Weak profitability; Aggressive investment; Modest factor fit |
| JTAI | -263.44% | +1.398 | +0.225 | +0.740 | -1.266 | +1.026 | 0.023 | 426 | Value tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| NOW | -25.90% | +0.967 | -0.087 | -0.436 | -0.554 | -0.046 | 0.308 | 426 | Weak profitability |
| MSFT | -15.19% | +0.885 | -0.261 | -0.418 | +0.136 | -0.499 | 0.520 | 426 | Neutral profile |
| ALL | -0.23% | +0.704 | -0.339 | +0.811 | +0.336 | -0.169 | 0.218 | 426 | Value tilt |
| AAPL | +0.76% | +1.302 | -0.115 | -0.039 | +0.755 | +0.105 | 0.536 | 426 | Robust profitability |
| MS | +7.62% | +1.465 | -0.108 | +0.955 | -0.487 | -0.186 | 0.690 | 426 | Value tilt |
| AMD | +5.01% | +1.575 | -0.597 | -0.484 | -1.702 | -0.091 | 0.483 | 426 | Large-cap tilt; Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| BATL | **80.00** | 33.33 | 13.33 | 33.33 | 0.017 | -1.016 | 3.9428 | 0.2242 | 176 |
| TRX | **76.67** | 20.00 | 33.33 | 23.33 | 0.192 | +1.523 | 1.0227 | 0.0582 | 176 |
| JTAI | **70.00** | 30.00 | 10.00 | 30.00 | 0.099 | -1.350 | 1.3967 | 0.0794 | 176 |
| SLND | **56.67** | 26.67 | 3.33 | 26.67 | 0.115 | -2.032 | 1.2493 | 0.0710 | 176 |
| AMD | **56.67** | 6.67 | 30.00 | 20.00 | 0.456 | +0.492 | 0.5172 | 0.0294 | 176 |
| ALL | **56.67** | 23.33 | 20.00 | 13.33 | 0.176 | -0.101 | 0.2372 | 0.0135 | 176 |
| AAPL | **50.00** | 16.67 | 23.33 | 10.00 | 0.337 | +0.062 | 0.2084 | 0.0119 | 176 |
| MSFT | **36.67** | 13.33 | 16.67 | 6.67 | 0.423 | -0.466 | 0.2052 | 0.0117 | 176 |
| MS | **33.33** | 3.33 | 26.67 | 3.33 | 0.511 | +0.086 | 0.2042 | 0.0116 | 176 |
| NOW | **33.33** | 10.00 | 6.67 | 16.67 | 0.431 | -1.683 | 0.3268 | 0.0186 | 176 |

## Per-ticker FF5 Detail

### BATL

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.0084 (adjusted = -0.0034)
- Alpha (annualized): **+256.82%** (daily = +0.010191, t = +1.24, p = 0.2162)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.0318 | +0.04 | 0.9709  |
| SMB | +0.7194 | +0.49 | 0.6278  |
| HML | -1.7945 | -1.33 | 0.1839  |
| RMW | +2.6704 | +1.59 | 0.1127  |
| CMA | -0.3857 | -0.23 | 0.8212  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Low explanatory power — likely sentiment-driven_

### SLND

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.0890 (adjusted = 0.0782)
- Alpha (annualized): **-42.65%** (daily = -0.001692, t = -0.63, p = 0.5311)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0654 | +3.73 | 0.0002 *** |
| SMB | +1.0867 | +2.23 | 0.0261 * |
| HML | +1.0216 | +2.31 | 0.0214 * |
| RMW | +0.0604 | +0.11 | 0.9128  |
| CMA | +0.8948 | +1.60 | 0.1106  |

_Interpretation: Small-cap tilt; Value tilt; Conservative investment; Modest factor fit_

### TRX

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.0784 (adjusted = 0.0674)
- Alpha (annualized): **+89.97%** (daily = +0.003570, t = +1.62, p = 0.1069)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.4866 | +2.08 | 0.0381 * |
| SMB | +0.0921 | +0.23 | 0.8172  |
| HML | -0.3015 | -0.83 | 0.4055  |
| RMW | -1.2246 | -2.71 | 0.0069 ** |
| CMA | -0.7079 | -1.55 | 0.1229  |

_Interpretation: Weak profitability; Aggressive investment; Modest factor fit_

### JTAI

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.0233 (adjusted = 0.0117)
- Alpha (annualized): **-263.44%** (daily = -0.010454, t = -1.63, p = 0.1037)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3976 | +2.06 | 0.0401 * |
| SMB | +0.2249 | +0.19 | 0.8457  |
| HML | +0.7397 | +0.70 | 0.4817  |
| RMW | -1.2655 | -0.97 | 0.3342  |
| CMA | +1.0259 | +0.77 | 0.4404  |

_Interpretation: Value tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### NOW

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.3081 (adjusted = 0.2998)
- Alpha (annualized): **-25.90%** (daily = -0.001028, t = -0.99, p = 0.3247)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9666 | +8.76 | 0.0000 *** |
| SMB | -0.0867 | -0.46 | 0.6446  |
| HML | -0.4358 | -2.55 | 0.0111 * |
| RMW | -0.5541 | -2.60 | 0.0095 ** |
| CMA | -0.0462 | -0.21 | 0.8309  |

_Interpretation: Weak profitability_

### MSFT

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.5197 (adjusted = 0.5140)
- Alpha (annualized): **-15.19%** (daily = -0.000603, t = -1.13, p = 0.2590)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8854 | +15.68 | 0.0000 *** |
| SMB | -0.2606 | -2.71 | 0.0070 ** |
| HML | -0.4179 | -4.78 | 0.0000 *** |
| RMW | +0.1356 | +1.25 | 0.2138  |
| CMA | -0.4990 | -4.51 | 0.0000 *** |

_Interpretation: Neutral profile_

### ALL

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.2181 (adjusted = 0.2088)
- Alpha (annualized): **-0.23%** (daily = -0.000009, t = -0.01, p = 0.9895)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7038 | +9.64 | 0.0000 *** |
| SMB | -0.3394 | -2.73 | 0.0066 ** |
| HML | +0.8110 | +7.18 | 0.0000 *** |
| RMW | +0.3358 | +2.39 | 0.0175 * |
| CMA | -0.1689 | -1.18 | 0.2379  |

_Interpretation: Value tilt_

### AAPL

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.5356 (adjusted = 0.5301)
- Alpha (annualized): **+0.76%** (daily = +0.000030, t = +0.05, p = 0.9599)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3018 | +20.52 | 0.0000 *** |
| SMB | -0.1148 | -1.06 | 0.2883  |
| HML | -0.0389 | -0.40 | 0.6921  |
| RMW | +0.7549 | +6.17 | 0.0000 *** |
| CMA | +0.1052 | +0.85 | 0.3973  |

_Interpretation: Robust profitability_

### MS

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.6904 (adjusted = 0.6867)
- Alpha (annualized): **+7.62%** (daily = +0.000303, t = +0.56, p = 0.5733)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4653 | +25.78 | 0.0000 *** |
| SMB | -0.1082 | -1.12 | 0.2640  |
| HML | +0.9554 | +10.86 | 0.0000 *** |
| RMW | -0.4873 | -4.45 | 0.0000 *** |
| CMA | -0.1864 | -1.68 | 0.0947  |

_Interpretation: Value tilt_

### AMD

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.4831 (adjusted = 0.4770)
- Alpha (annualized): **+5.01%** (daily = +0.000199, t = +0.16, p = 0.8763)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5753 | +11.66 | 0.0000 *** |
| SMB | -0.5974 | -2.60 | 0.0097 ** |
| HML | -0.4844 | -2.32 | 0.0210 * |
| RMW | -1.7022 | -6.53 | 0.0000 *** |
| CMA | -0.0909 | -0.34 | 0.7313  |

_Interpretation: Large-cap tilt; Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._