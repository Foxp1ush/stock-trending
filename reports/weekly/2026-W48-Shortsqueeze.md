# Weekly Report — `Shortsqueeze` — 2026-W48

Generated: 2026-11-23  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W48.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| SLS | +115.98% | +0.321 | +1.040 | +0.540 | -1.809 | -1.505 | 0.091 | 337 | Small-cap tilt; Value tilt; Weak profitability; Aggressive investment; Modest factor fit |
| HTZ | +52.08% | +1.029 | +2.407 | +0.732 | +0.263 | +0.035 | 0.104 | 337 | Small-cap tilt; Value tilt; Modest factor fit |
| AMD | +24.24% | +1.595 | -0.567 | -0.428 | -1.664 | -0.275 | 0.485 | 337 | Large-cap tilt; Weak profitability |
| AKAN | -200.01% | +0.062 | +0.125 | -0.803 | -2.093 | +1.637 | 0.056 | 337 | Growth tilt; Weak profitability; Conservative investment; Significant negative alpha; Modest factor fit |
| API | +4.15% | +0.246 | +0.612 | -0.884 | -1.396 | +0.718 | 0.101 | 337 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| ASTS | +127.15% | +1.336 | +1.254 | -1.271 | -2.790 | -0.420 | 0.333 | 337 | Small-cap tilt; Growth tilt; Weak profitability |
| CC | +18.79% | +1.869 | +2.154 | +0.374 | +0.190 | +1.107 | 0.464 | 337 | Small-cap tilt; Conservative investment |
| ALL | -9.08% | +0.702 | -0.293 | +0.882 | +0.302 | -0.101 | 0.225 | 337 | Value tilt |
| IP | -39.08% | +1.269 | +0.541 | +0.595 | +0.367 | +0.896 | 0.392 | 337 | Small-cap tilt; Value tilt; Conservative investment |
| IBKR | +10.39% | +1.588 | -0.635 | +0.234 | -1.074 | +0.248 | 0.559 | 337 | Large-cap tilt; Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SLS | **83.33** | 23.33 | 30.00 | 30.00 | 0.245 | +0.812 | 1.7059 | 0.0623 | 87 |
| AKAN | **66.67** | 30.00 | 3.33 | 33.33 | 0.161 | -1.371 | 2.4970 | 0.0912 | 87 |
| CC | **66.67** | 16.67 | 26.67 | 23.33 | 0.352 | +0.677 | 0.9149 | 0.0334 | 87 |
| ASTS | **63.33** | 13.33 | 23.33 | 26.67 | 0.394 | +0.338 | 1.6083 | 0.0587 | 87 |
| API | **60.00** | 33.33 | 10.00 | 16.67 | 0.135 | -0.272 | 0.6887 | 0.0251 | 87 |
| AMD | **53.33** | 6.67 | 33.33 | 13.33 | 0.591 | +1.053 | 0.6484 | 0.0237 | 87 |
| HTZ | **46.67** | 20.00 | 6.67 | 20.00 | 0.301 | -0.479 | 0.8540 | 0.0312 | 87 |
| ALL | **43.33** | 26.67 | 13.33 | 3.33 | 0.239 | -0.228 | 0.3497 | 0.0128 | 87 |
| IP | **36.67** | 10.00 | 16.67 | 10.00 | 0.438 | -0.213 | 0.5363 | 0.0196 | 87 |
| IBKR | **30.00** | 3.33 | 20.00 | 6.67 | 0.689 | -0.079 | 0.3784 | 0.0138 | 87 |

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

### HTZ

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.1045 (adjusted = 0.0910)
- Alpha (annualized): **+52.08%** (daily = +0.002067, t = +0.61, p = 0.5411)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0288 | +2.97 | 0.0032 ** |
| SMB | +2.4066 | +3.88 | 0.0001 *** |
| HML | +0.7319 | +1.25 | 0.2127  |
| RMW | +0.2632 | +0.41 | 0.6850  |
| CMA | +0.0345 | +0.05 | 0.9626  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

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

### API

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.1008 (adjusted = 0.0872)
- Alpha (annualized): **+4.15%** (daily = +0.000165, t = +0.07, p = 0.9476)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2458 | +0.96 | 0.3394  |
| SMB | +0.6117 | +1.33 | 0.1842  |
| HML | -0.8843 | -2.04 | 0.0424 * |
| RMW | -1.3959 | -2.91 | 0.0039 ** |
| CMA | +0.7179 | +1.32 | 0.1877  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### ASTS

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.3330 (adjusted = 0.3229)
- Alpha (annualized): **+127.15%** (daily = +0.005046, t = +1.77, p = 0.0773)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3362 | +4.57 | 0.0000 *** |
| SMB | +1.2536 | +2.40 | 0.0171 * |
| HML | -1.2708 | -2.57 | 0.0106 * |
| RMW | -2.7904 | -5.11 | 0.0000 *** |
| CMA | -0.4203 | -0.68 | 0.4976  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### CC

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.4644 (adjusted = 0.4563)
- Alpha (annualized): **+18.79%** (daily = +0.000746, t = +0.45, p = 0.6518)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.8690 | +11.02 | 0.0000 *** |
| SMB | +2.1541 | +7.10 | 0.0000 *** |
| HML | +0.3742 | +1.31 | 0.1924  |
| RMW | +0.1905 | +0.60 | 0.5482  |
| CMA | +1.1065 | +3.08 | 0.0022 ** |

_Interpretation: Small-cap tilt; Conservative investment_

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

### IP

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.3923 (adjusted = 0.3831)
- Alpha (annualized): **-39.08%** (daily = -0.001551, t = -1.47, p = 0.1432)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2691 | +11.69 | 0.0000 *** |
| SMB | +0.5414 | +2.79 | 0.0056 ** |
| HML | +0.5947 | +3.24 | 0.0013 ** |
| RMW | +0.3665 | +1.81 | 0.0717  |
| CMA | +0.8960 | +3.90 | 0.0001 *** |

_Interpretation: Small-cap tilt; Value tilt; Conservative investment_

### IBKR

- Period: `2024-11-22` to `2026-03-31` (337 obs)
- R² = 0.5589 (adjusted = 0.5522)
- Alpha (annualized): **+10.39%** (daily = +0.000412, t = +0.41, p = 0.6849)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5877 | +15.22 | 0.0000 *** |
| SMB | -0.6349 | -3.40 | 0.0008 *** |
| HML | +0.2336 | +1.33 | 0.1860  |
| RMW | -1.0741 | -5.51 | 0.0000 *** |
| CMA | +0.2478 | +1.12 | 0.2625  |

_Interpretation: Large-cap tilt; Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._