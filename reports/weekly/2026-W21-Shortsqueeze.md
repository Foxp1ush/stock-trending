# Weekly Report — `Shortsqueeze` — 2026-W21

Generated: 2026-05-22  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W21.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| GRPN | -0.44% | +0.691 | +1.234 | -0.379 | -1.673 | +0.645 | 0.161 | 464 | Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit |
| AAPL | +6.37% | +1.306 | -0.068 | -0.102 | +0.791 | +0.079 | 0.519 | 464 | Robust profitability |
| AMD | +2.32% | +1.582 | -0.532 | -0.478 | -1.702 | -0.039 | 0.474 | 464 | Large-cap tilt; Weak profitability |
| ALL | +1.08% | +0.679 | -0.288 | +0.828 | +0.301 | -0.120 | 0.214 | 464 | Value tilt |
| BE | +130.80% | +1.424 | +0.104 | +0.020 | -2.694 | -1.531 | 0.204 | 464 | Weak profitability; Aggressive investment |
| BB | +1.56% | +0.997 | +0.421 | -0.344 | -1.381 | +0.675 | 0.304 | 464 | Weak profitability; Conservative investment |
| BYND | -36.68% | +1.144 | +0.794 | +0.282 | -1.166 | +1.481 | 0.034 | 464 | Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| AMZN | -2.65% | +1.324 | +0.004 | -0.329 | +0.179 | -0.551 | 0.549 | 464 | Aggressive investment |
| GO | -51.13% | +0.477 | +0.902 | +0.508 | +0.889 | -0.361 | 0.054 | 464 | Small-cap tilt; Value tilt; Robust profitability; Modest factor fit |
| CAR | +14.60% | +1.477 | +1.310 | +0.332 | +0.293 | +0.770 | 0.264 | 464 | Small-cap tilt; Conservative investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| GO | **86.67** | 30.00 | 30.00 | 26.67 | 0.066 | +0.629 | 0.6678 | 0.0426 | 214 |
| BE | **73.33** | 10.00 | 33.33 | 30.00 | 0.365 | +1.833 | 0.8266 | 0.0528 | 214 |
| BYND | **70.00** | 33.33 | 3.33 | 33.33 | 0.042 | -2.019 | 2.4033 | 0.1534 | 214 |
| CAR | **70.00** | 23.33 | 26.67 | 20.00 | 0.176 | +0.257 | 0.5145 | 0.0328 | 214 |
| ALL | **53.33** | 26.67 | 20.00 | 6.67 | 0.142 | +0.066 | 0.2158 | 0.0138 | 214 |
| GRPN | **46.67** | 16.67 | 6.67 | 23.33 | 0.220 | -0.692 | 0.5378 | 0.0343 | 214 |
| BB | **46.67** | 20.00 | 13.33 | 13.33 | 0.218 | -0.319 | 0.3695 | 0.0236 | 214 |
| AMD | **43.33** | 3.33 | 23.33 | 16.67 | 0.425 | +0.247 | 0.4526 | 0.0289 | 214 |
| AAPL | **33.33** | 13.33 | 16.67 | 3.33 | 0.346 | +0.035 | 0.1787 | 0.0114 | 214 |
| AMZN | **26.67** | 6.67 | 10.00 | 10.00 | 0.397 | -0.394 | 0.2301 | 0.0147 | 214 |

## Per-ticker FF5 Detail

### GRPN

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.1610 (adjusted = 0.1518)
- Alpha (annualized): **-0.44%** (daily = -0.000017, t = -0.01, p = 0.9936)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6913 | +2.91 | 0.0038 ** |
| SMB | +1.2339 | +3.24 | 0.0013 ** |
| HML | -0.3794 | -1.05 | 0.2951  |
| RMW | -1.6730 | -3.72 | 0.0002 *** |
| CMA | +0.6452 | +1.42 | 0.1560  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit_

### AAPL

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.5187 (adjusted = 0.5134)
- Alpha (annualized): **+6.37%** (daily = +0.000253, t = +0.43, p = 0.6664)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3060 | +20.59 | 0.0000 *** |
| SMB | -0.0680 | -0.67 | 0.5036  |
| HML | -0.1015 | -1.05 | 0.2941  |
| RMW | +0.7913 | +6.59 | 0.0000 *** |
| CMA | +0.0788 | +0.65 | 0.5160  |

_Interpretation: Robust profitability_

### AMD

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.4743 (adjusted = 0.4686)
- Alpha (annualized): **+2.32%** (daily = +0.000092, t = +0.08, p = 0.9396)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5817 | +12.04 | 0.0000 *** |
| SMB | -0.5319 | -2.53 | 0.0118 * |
| HML | -0.4782 | -2.39 | 0.0173 * |
| RMW | -1.7020 | -6.84 | 0.0000 *** |
| CMA | -0.0393 | -0.16 | 0.8758  |

_Interpretation: Large-cap tilt; Weak profitability_

### ALL

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.2138 (adjusted = 0.2052)
- Alpha (annualized): **+1.08%** (daily = +0.000043, t = +0.07, p = 0.9476)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6787 | +9.64 | 0.0000 *** |
| SMB | -0.2878 | -2.55 | 0.0111 * |
| HML | +0.8284 | +7.72 | 0.0000 *** |
| RMW | +0.3010 | +2.26 | 0.0244 * |
| CMA | -0.1201 | -0.89 | 0.3727  |

_Interpretation: Value tilt_

### BE

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.2040 (adjusted = 0.1953)
- Alpha (annualized): **+130.80%** (daily = +0.005190, t = +1.95, p = 0.0516)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4243 | +4.95 | 0.0000 *** |
| SMB | +0.1042 | +0.23 | 0.8214  |
| HML | +0.0195 | +0.04 | 0.9645  |
| RMW | -2.6938 | -4.94 | 0.0000 *** |
| CMA | -1.5314 | -2.78 | 0.0056 ** |

_Interpretation: Weak profitability; Aggressive investment_

### BB

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.3040 (adjusted = 0.2964)
- Alpha (annualized): **+1.56%** (daily = +0.000062, t = +0.05, p = 0.9624)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9971 | +7.01 | 0.0000 *** |
| SMB | +0.4210 | +1.85 | 0.0654  |
| HML | -0.3440 | -1.59 | 0.1134  |
| RMW | -1.3813 | -5.13 | 0.0000 *** |
| CMA | +0.6748 | +2.48 | 0.0135 * |

_Interpretation: Weak profitability; Conservative investment_

### BYND

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.0336 (adjusted = 0.0230)
- Alpha (annualized): **-36.68%** (daily = -0.001456, t = -0.29, p = 0.7754)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1444 | +2.07 | 0.0388 * |
| SMB | +0.7943 | +0.90 | 0.3698  |
| HML | +0.2819 | +0.33 | 0.7378  |
| RMW | -1.1659 | -1.11 | 0.2655  |
| CMA | +1.4810 | +1.40 | 0.1614  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### AMZN

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.5490 (adjusted = 0.5441)
- Alpha (annualized): **-2.65%** (daily = -0.000105, t = -0.16, p = 0.8705)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3243 | +18.95 | 0.0000 *** |
| SMB | +0.0039 | +0.03 | 0.9724  |
| HML | -0.3286 | -3.09 | 0.0022 ** |
| RMW | +0.1793 | +1.35 | 0.1761  |
| CMA | -0.5514 | -4.13 | 0.0000 *** |

_Interpretation: Aggressive investment_

### GO

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.0536 (adjusted = 0.0432)
- Alpha (annualized): **-51.13%** (daily = -0.002029, t = -1.10, p = 0.2717)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.4775 | +2.39 | 0.0172 * |
| SMB | +0.9018 | +2.82 | 0.0050 ** |
| HML | +0.5076 | +1.67 | 0.0960  |
| RMW | +0.8889 | +2.35 | 0.0192 * |
| CMA | -0.3615 | -0.95 | 0.3443  |

_Interpretation: Small-cap tilt; Value tilt; Robust profitability; Modest factor fit_

### CAR

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.2636 (adjusted = 0.2556)
- Alpha (annualized): **+14.60%** (daily = +0.000579, t = +0.37, p = 0.7101)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4768 | +8.75 | 0.0000 *** |
| SMB | +1.3099 | +4.85 | 0.0000 *** |
| HML | +0.3323 | +1.29 | 0.1969  |
| RMW | +0.2933 | +0.92 | 0.3591  |
| CMA | +0.7699 | +2.39 | 0.0174 * |

_Interpretation: Small-cap tilt; Conservative investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._