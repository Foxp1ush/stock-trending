# Weekly Report — `Shortsqueeze` — 2026-W24

Generated: 2026-06-14  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W24.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| LFVN | -6.62% | +0.783 | +1.213 | -0.685 | +0.648 | +0.101 | 0.086 | 449 | Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit |
| SPCE | -83.96% | +0.920 | +2.193 | -0.813 | -2.004 | -0.294 | 0.296 | 449 | Small-cap tilt; Growth tilt; Weak profitability |
| AMD | +3.35% | +1.571 | -0.584 | -0.494 | -1.740 | -0.055 | 0.481 | 449 | Large-cap tilt; Weak profitability |
| AMZN | +0.68% | +1.342 | +0.024 | -0.341 | +0.239 | -0.562 | 0.556 | 449 | Aggressive investment |
| AAPL | +2.98% | +1.310 | -0.096 | -0.066 | +0.772 | +0.070 | 0.537 | 449 | Robust profitability |
| ALL | +3.18% | +0.680 | -0.279 | +0.810 | +0.320 | -0.153 | 0.211 | 449 | Value tilt |
| GL | +14.59% | +0.893 | -0.144 | +0.818 | -0.016 | -0.088 | 0.374 | 449 | Value tilt |
| IBM | +13.37% | +0.806 | +0.068 | +0.208 | -0.037 | -0.036 | 0.200 | 449 | Neutral profile |
| JPM | +1.12% | +1.190 | -0.283 | +1.094 | -0.351 | -0.383 | 0.629 | 449 | Value tilt |
| HPE | -8.78% | +1.593 | +0.116 | +0.385 | -0.492 | +0.314 | 0.447 | 449 | Neutral profile |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| GL | **70.00** | 30.00 | 30.00 | 10.00 | 0.145 | +0.153 | 0.2019 | 0.0124 | 199 |
| SPCE | **66.67** | 20.00 | 13.33 | 33.33 | 0.273 | -0.066 | 0.6250 | 0.0383 | 199 |
| AMD | **66.67** | 6.67 | 33.33 | 26.67 | 0.426 | +0.338 | 0.4823 | 0.0295 | 199 |
| HPE | **63.33** | 13.33 | 26.67 | 23.33 | 0.390 | +0.142 | 0.3251 | 0.0199 | 199 |
| ALL | **63.33** | 33.33 | 16.67 | 13.33 | 0.141 | -0.008 | 0.2248 | 0.0138 | 199 |
| LFVN | **60.00** | 26.67 | 3.33 | 30.00 | 0.167 | -0.730 | 0.5258 | 0.0322 | 199 |
| IBM | **50.00** | 23.33 | 6.67 | 20.00 | 0.224 | -0.547 | 0.3061 | 0.0187 | 199 |
| AAPL | **43.33** | 16.67 | 20.00 | 6.67 | 0.326 | +0.039 | 0.1894 | 0.0116 | 199 |
| AMZN | **36.67** | 10.00 | 10.00 | 16.67 | 0.394 | -0.411 | 0.2454 | 0.0150 | 199 |
| JPM | **30.00** | 3.33 | 23.33 | 3.33 | 0.437 | +0.055 | 0.1691 | 0.0104 | 199 |

## Per-ticker FF5 Detail

### LFVN

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.0860 (adjusted = 0.0757)
- Alpha (annualized): **-6.62%** (daily = -0.000263, t = -0.13, p = 0.8933)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7835 | +3.74 | 0.0002 *** |
| SMB | +1.2130 | +3.58 | 0.0004 *** |
| HML | -0.6848 | -2.13 | 0.0338 * |
| RMW | +0.6479 | +1.61 | 0.1083  |
| CMA | +0.1010 | +0.25 | 0.8034  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit_

### SPCE

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.2964 (adjusted = 0.2885)
- Alpha (annualized): **-83.96%** (daily = -0.003332, t = -1.54, p = 0.1249)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9196 | +3.96 | 0.0001 *** |
| SMB | +2.1926 | +5.85 | 0.0000 *** |
| HML | -0.8133 | -2.28 | 0.0228 * |
| RMW | -2.0036 | -4.50 | 0.0000 *** |
| CMA | -0.2940 | -0.66 | 0.5126  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### AMD

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.4811 (adjusted = 0.4753)
- Alpha (annualized): **+3.35%** (daily = +0.000133, t = +0.11, p = 0.9145)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5713 | +11.86 | 0.0000 *** |
| SMB | -0.5837 | -2.73 | 0.0067 ** |
| HML | -0.4944 | -2.43 | 0.0154 * |
| RMW | -1.7397 | -6.83 | 0.0000 *** |
| CMA | -0.0552 | -0.22 | 0.8295  |

_Interpretation: Large-cap tilt; Weak profitability_

### AMZN

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.5556 (adjusted = 0.5506)
- Alpha (annualized): **+0.68%** (daily = +0.000027, t = +0.04, p = 0.9672)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3425 | +19.00 | 0.0000 *** |
| SMB | +0.0243 | +0.21 | 0.8314  |
| HML | -0.3409 | -3.14 | 0.0018 ** |
| RMW | +0.2388 | +1.76 | 0.0793  |
| CMA | -0.5621 | -4.11 | 0.0000 *** |

_Interpretation: Aggressive investment_

### AAPL

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.5367 (adjusted = 0.5315)
- Alpha (annualized): **+2.98%** (daily = +0.000118, t = +0.20, p = 0.8383)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3104 | +21.11 | 0.0000 *** |
| SMB | -0.0955 | -0.95 | 0.3413  |
| HML | -0.0664 | -0.70 | 0.4861  |
| RMW | +0.7717 | +6.47 | 0.0000 *** |
| CMA | +0.0699 | +0.58 | 0.5607  |

_Interpretation: Robust profitability_

### ALL

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.2107 (adjusted = 0.2018)
- Alpha (annualized): **+3.18%** (daily = +0.000126, t = +0.19, p = 0.8505)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6805 | +9.49 | 0.0000 *** |
| SMB | -0.2788 | -2.41 | 0.0164 * |
| HML | +0.8105 | +7.37 | 0.0000 *** |
| RMW | +0.3198 | +2.32 | 0.0206 * |
| CMA | -0.1529 | -1.10 | 0.2707  |

_Interpretation: Value tilt_

### GL

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.3736 (adjusted = 0.3665)
- Alpha (annualized): **+14.59%** (daily = +0.000579, t = +1.01, p = 0.3122)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8935 | +14.59 | 0.0000 *** |
| SMB | -0.1439 | -1.45 | 0.1466  |
| HML | +0.8176 | +8.70 | 0.0000 *** |
| RMW | -0.0161 | -0.14 | 0.8912  |
| CMA | -0.0882 | -0.74 | 0.4568  |

_Interpretation: Value tilt_

### IBM

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.2004 (adjusted = 0.1914)
- Alpha (annualized): **+13.37%** (daily = +0.000531, t = +0.64, p = 0.5207)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8059 | +9.12 | 0.0000 *** |
| SMB | +0.0678 | +0.48 | 0.6347  |
| HML | +0.2078 | +1.53 | 0.1260  |
| RMW | -0.0372 | -0.22 | 0.8264  |
| CMA | -0.0359 | -0.21 | 0.8338  |

_Interpretation: Neutral profile_

### JPM

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.6285 (adjusted = 0.6243)
- Alpha (annualized): **+1.12%** (daily = +0.000045, t = +0.10, p = 0.9242)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1899 | +23.73 | 0.0000 *** |
| SMB | -0.2832 | -3.50 | 0.0005 *** |
| HML | +1.0936 | +14.22 | 0.0000 *** |
| RMW | -0.3512 | -3.65 | 0.0003 *** |
| CMA | -0.3833 | -3.95 | 0.0001 *** |

_Interpretation: Value tilt_

### HPE

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.4474 (adjusted = 0.4411)
- Alpha (annualized): **-8.78%** (daily = -0.000349, t = -0.36, p = 0.7222)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5928 | +15.19 | 0.0000 *** |
| SMB | +0.1158 | +0.68 | 0.4947  |
| HML | +0.3849 | +2.39 | 0.0172 * |
| RMW | -0.4923 | -2.44 | 0.0149 * |
| CMA | +0.3137 | +1.55 | 0.1227  |

_Interpretation: Neutral profile_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._