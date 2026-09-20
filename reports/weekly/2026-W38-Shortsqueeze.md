# Weekly Report — `Shortsqueeze` — 2026-W38

Generated: 2026-09-20  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W38.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +54.63% | +1.029 | +2.130 | +0.632 | +0.378 | +0.289 | 0.101 | 382 | Small-cap tilt; Value tilt; Modest factor fit |
| ALL | -4.65% | +0.695 | -0.243 | +0.780 | +0.313 | -0.109 | 0.219 | 382 | Value tilt |
| AMD | +5.35% | +1.591 | -0.615 | -0.399 | -1.688 | -0.243 | 0.472 | 382 | Large-cap tilt; Weak profitability |
| ASTS | +95.27% | +1.333 | +1.192 | -1.101 | -2.882 | -0.355 | 0.310 | 382 | Small-cap tilt; Growth tilt; Weak profitability |
| API | +86.61% | +0.084 | +0.692 | -1.396 | -1.605 | +0.834 | 0.064 | 382 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| ES | -2.21% | +0.386 | -0.046 | +0.444 | -0.103 | +0.323 | 0.094 | 382 | Modest factor fit |
| EU | -11.20% | +0.872 | +1.439 | -1.224 | -0.962 | -0.134 | 0.169 | 382 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| FOR | -14.05% | +0.876 | +1.722 | +0.103 | +1.194 | +0.417 | 0.445 | 382 | Small-cap tilt; Robust profitability |
| DTE | +1.51% | +0.295 | -0.204 | +0.553 | -0.223 | +0.079 | 0.147 | 382 | Value tilt; Modest factor fit |
| IP | -25.72% | +1.149 | +0.487 | +0.571 | +0.341 | +0.934 | 0.323 | 382 | Value tilt; Conservative investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| HTZ | **83.33** | 26.67 | 26.67 | 30.00 | 0.104 | +0.068 | 0.9712 | 0.0469 | 132 |
| EU | **76.67** | 16.67 | 33.33 | 26.67 | 0.301 | +1.351 | 0.8696 | 0.0420 | 132 |
| ASTS | **66.67** | 13.33 | 20.00 | 33.33 | 0.365 | -0.053 | 1.1969 | 0.0578 | 132 |
| DTE | **60.00** | 33.33 | 23.33 | 3.33 | 0.066 | +0.030 | 0.1987 | 0.0096 | 132 |
| AMD | **56.67** | 3.33 | 30.00 | 23.33 | 0.513 | +0.670 | 0.6274 | 0.0303 | 132 |
| ES | **53.33** | 30.00 | 13.33 | 10.00 | 0.069 | -0.205 | 0.3408 | 0.0164 | 132 |
| API | **46.67** | 23.33 | 3.33 | 20.00 | 0.128 | -0.363 | 0.5606 | 0.0271 | 132 |
| ALL | **36.67** | 20.00 | 10.00 | 6.67 | 0.241 | -0.240 | 0.2563 | 0.0124 | 132 |
| FOR | **36.67** | 6.67 | 16.67 | 13.33 | 0.455 | -0.201 | 0.3463 | 0.0167 | 132 |
| IP | **33.33** | 10.00 | 6.67 | 16.67 | 0.388 | -0.268 | 0.4290 | 0.0207 | 132 |

## Per-ticker FF5 Detail

### HTZ

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.1011 (adjusted = 0.0891)
- Alpha (annualized): **+54.63%** (daily = +0.002168, t = +0.70, p = 0.4815)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0287 | +3.18 | 0.0016 ** |
| SMB | +2.1303 | +3.77 | 0.0002 *** |
| HML | +0.6323 | +1.25 | 0.2120  |
| RMW | +0.3775 | +0.61 | 0.5391  |
| CMA | +0.2886 | +0.44 | 0.6593  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### ALL

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.2188 (adjusted = 0.2084)
- Alpha (annualized): **-4.65%** (daily = -0.000185, t = -0.25, p = 0.8000)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6953 | +9.09 | 0.0000 *** |
| SMB | -0.2434 | -1.82 | 0.0696  |
| HML | +0.7800 | +6.52 | 0.0000 *** |
| RMW | +0.3135 | +2.16 | 0.0315 * |
| CMA | -0.1091 | -0.70 | 0.4813  |

_Interpretation: Value tilt_

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

### ASTS

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.3101 (adjusted = 0.3009)
- Alpha (annualized): **+95.27%** (daily = +0.003781, t = +1.40, p = 0.1634)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3333 | +4.69 | 0.0000 *** |
| SMB | +1.1925 | +2.40 | 0.0170 * |
| HML | -1.1008 | -2.47 | 0.0138 * |
| RMW | -2.8817 | -5.33 | 0.0000 *** |
| CMA | -0.3551 | -0.62 | 0.5375  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### API

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.0644 (adjusted = 0.0520)
- Alpha (annualized): **+86.61%** (daily = +0.003437, t = +0.99, p = 0.3239)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.0843 | +0.23 | 0.8178  |
| SMB | +0.6921 | +1.08 | 0.2799  |
| HML | -1.3962 | -2.44 | 0.0151 * |
| RMW | -1.6051 | -2.31 | 0.0213 * |
| CMA | +0.8345 | +1.13 | 0.2599  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### ES

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.0936 (adjusted = 0.0816)
- Alpha (annualized): **-2.21%** (daily = -0.000088, t = -0.11, p = 0.9121)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3859 | +4.62 | 0.0000 *** |
| SMB | -0.0462 | -0.32 | 0.7516  |
| HML | +0.4440 | +3.40 | 0.0007 *** |
| RMW | -0.1034 | -0.65 | 0.5144  |
| CMA | +0.3228 | +1.91 | 0.0567  |

_Interpretation: Modest factor fit_

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

### FOR

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.4452 (adjusted = 0.4378)
- Alpha (annualized): **-14.05%** (daily = -0.000558, t = -0.64, p = 0.5216)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8759 | +9.59 | 0.0000 *** |
| SMB | +1.7225 | +10.78 | 0.0000 *** |
| HML | +0.1032 | +0.72 | 0.4705  |
| RMW | +1.1937 | +6.88 | 0.0000 *** |
| CMA | +0.4166 | +2.25 | 0.0247 * |

_Interpretation: Small-cap tilt; Robust profitability_

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

### IP

- Period: `2024-09-20` to `2026-03-31` (382 obs)
- R² = 0.3228 (adjusted = 0.3138)
- Alpha (annualized): **-25.72%** (daily = -0.001021, t = -0.97, p = 0.3310)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1491 | +10.43 | 0.0000 *** |
| SMB | +0.4866 | +2.52 | 0.0120 * |
| HML | +0.5714 | +3.32 | 0.0010 ** |
| RMW | +0.3410 | +1.63 | 0.1040  |
| CMA | +0.9345 | +4.19 | 0.0000 *** |

_Interpretation: Value tilt; Conservative investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._