# Weekly Report — `Shortsqueeze` — 2026-W23

Generated: 2026-06-07  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W23.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| LFVN | -7.23% | +0.776 | +1.179 | -0.681 | +0.634 | +0.138 | 0.084 | 454 | Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit |
| SPCE | -86.70% | +0.887 | +2.184 | -0.839 | -2.057 | -0.242 | 0.290 | 454 | Small-cap tilt; Growth tilt; Weak profitability |
| IBKR | +21.42% | +1.577 | -0.552 | +0.580 | -0.993 | -0.269 | 0.514 | 454 | Large-cap tilt; Value tilt; Weak profitability |
| MC | -12.25% | +1.567 | +0.894 | +0.781 | -0.076 | +0.122 | 0.626 | 454 | Small-cap tilt; Value tilt |
| CC | -3.63% | +1.798 | +1.784 | +0.266 | +0.290 | +1.206 | 0.438 | 454 | Small-cap tilt; Conservative investment |
| DELL | +6.06% | +1.726 | -0.179 | -0.333 | -0.228 | +0.943 | 0.389 | 454 | Conservative investment |
| HPE | -2.64% | +1.602 | +0.095 | +0.371 | -0.453 | +0.307 | 0.441 | 454 | Neutral profile |
| AMZN | -1.64% | +1.336 | +0.017 | -0.328 | +0.208 | -0.556 | 0.552 | 454 | Aggressive investment |
| AAPL | +7.37% | +1.311 | -0.072 | -0.106 | +0.812 | +0.064 | 0.521 | 454 | Robust profitability |
| ALL | +1.96% | +0.678 | -0.291 | +0.819 | +0.309 | -0.142 | 0.211 | 454 | Value tilt |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| DELL | **70.00** | 26.67 | 20.00 | 23.33 | 0.188 | +0.020 | 0.4668 | 0.0289 | 204 |
| ALL | **66.67** | 33.33 | 26.67 | 6.67 | 0.137 | +0.056 | 0.2245 | 0.0139 | 204 |
| SPCE | **66.67** | 23.33 | 10.00 | 33.33 | 0.274 | -0.140 | 0.6212 | 0.0385 | 204 |
| LFVN | **63.33** | 30.00 | 3.33 | 30.00 | 0.165 | -0.711 | 0.5152 | 0.0319 | 204 |
| HPE | **63.33** | 13.33 | 30.00 | 20.00 | 0.393 | +0.143 | 0.3176 | 0.0197 | 204 |
| IBKR | **56.67** | 6.67 | 33.33 | 16.67 | 0.493 | +0.297 | 0.2728 | 0.0169 | 204 |
| CC | **53.33** | 10.00 | 16.67 | 26.67 | 0.422 | -0.038 | 0.4917 | 0.0305 | 204 |
| AAPL | **46.67** | 20.00 | 23.33 | 3.33 | 0.331 | +0.048 | 0.1861 | 0.0115 | 204 |
| AMZN | **33.33** | 16.67 | 6.67 | 10.00 | 0.393 | -0.408 | 0.2408 | 0.0149 | 204 |
| MC | **30.00** | 3.33 | 13.33 | 13.33 | 0.493 | -0.056 | 0.2512 | 0.0156 | 204 |

## Per-ticker FF5 Detail

### LFVN

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.0837 (adjusted = 0.0735)
- Alpha (annualized): **-7.23%** (daily = -0.000287, t = -0.15, p = 0.8827)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7761 | +3.71 | 0.0002 *** |
| SMB | +1.1790 | +3.50 | 0.0005 *** |
| HML | -0.6808 | -2.13 | 0.0336 * |
| RMW | +0.6342 | +1.59 | 0.1130  |
| CMA | +0.1378 | +0.34 | 0.7331  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit_

### SPCE

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.2899 (adjusted = 0.2820)
- Alpha (annualized): **-86.70%** (daily = -0.003441, t = -1.57, p = 0.1161)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8872 | +3.77 | 0.0002 *** |
| SMB | +2.1839 | +5.77 | 0.0000 *** |
| HML | -0.8393 | -2.34 | 0.0200 * |
| RMW | -2.0572 | -4.58 | 0.0000 *** |
| CMA | -0.2423 | -0.53 | 0.5941  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### IBKR

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.5139 (adjusted = 0.5085)
- Alpha (annualized): **+21.42%** (daily = +0.000850, t = +1.00, p = 0.3175)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5773 | +17.27 | 0.0000 *** |
| SMB | -0.5517 | -3.75 | 0.0002 *** |
| HML | +0.5804 | +4.16 | 0.0000 *** |
| RMW | -0.9929 | -5.69 | 0.0000 *** |
| CMA | -0.2686 | -1.52 | 0.1288  |

_Interpretation: Large-cap tilt; Value tilt; Weak profitability_

### MC

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.6258 (adjusted = 0.6217)
- Alpha (annualized): **-12.25%** (daily = -0.000486, t = -0.68, p = 0.4952)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5674 | +20.47 | 0.0000 *** |
| SMB | +0.8943 | +7.25 | 0.0000 *** |
| HML | +0.7814 | +6.67 | 0.0000 *** |
| RMW | -0.0763 | -0.52 | 0.6022  |
| CMA | +0.1221 | +0.83 | 0.4098  |

_Interpretation: Small-cap tilt; Value tilt_

### CC

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.4380 (adjusted = 0.4317)
- Alpha (annualized): **-3.63%** (daily = -0.000144, t = -0.10, p = 0.9169)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7985 | +12.11 | 0.0000 *** |
| SMB | +1.7838 | +7.46 | 0.0000 *** |
| HML | +0.2661 | +1.17 | 0.2418  |
| RMW | +0.2897 | +1.02 | 0.3079  |
| CMA | +1.2062 | +4.20 | 0.0000 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### DELL

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.3887 (adjusted = 0.3819)
- Alpha (annualized): **+6.06%** (daily = +0.000241, t = +0.20, p = 0.8450)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7262 | +13.05 | 0.0000 *** |
| SMB | -0.1791 | -0.84 | 0.4010  |
| HML | -0.3325 | -1.64 | 0.1009  |
| RMW | -0.2275 | -0.90 | 0.3686  |
| CMA | +0.9432 | +3.69 | 0.0003 *** |

_Interpretation: Conservative investment_

### HPE

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.4414 (adjusted = 0.4352)
- Alpha (annualized): **-2.64%** (daily = -0.000105, t = -0.11, p = 0.9148)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6023 | +15.23 | 0.0000 *** |
| SMB | +0.0951 | +0.56 | 0.5746  |
| HML | +0.3711 | +2.31 | 0.0215 * |
| RMW | -0.4531 | -2.25 | 0.0247 * |
| CMA | +0.3069 | +1.51 | 0.1318  |

_Interpretation: Neutral profile_

### AMZN

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.5523 (adjusted = 0.5473)
- Alpha (annualized): **-1.64%** (daily = -0.000065, t = -0.10, p = 0.9208)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3364 | +18.95 | 0.0000 *** |
| SMB | +0.0169 | +0.15 | 0.8817  |
| HML | -0.3276 | -3.04 | 0.0025 ** |
| RMW | +0.2083 | +1.55 | 0.1230  |
| CMA | -0.5558 | -4.08 | 0.0001 *** |

_Interpretation: Aggressive investment_

### AAPL

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.5214 (adjusted = 0.5160)
- Alpha (annualized): **+7.37%** (daily = +0.000292, t = +0.49, p = 0.6239)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3111 | +20.46 | 0.0000 *** |
| SMB | -0.0718 | -0.70 | 0.4869  |
| HML | -0.1059 | -1.08 | 0.2804  |
| RMW | +0.8121 | +6.63 | 0.0000 *** |
| CMA | +0.0636 | +0.51 | 0.6079  |

_Interpretation: Robust profitability_

### ALL

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.2106 (adjusted = 0.2018)
- Alpha (annualized): **+1.96%** (daily = +0.000078, t = +0.12, p = 0.9067)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6784 | +9.51 | 0.0000 *** |
| SMB | -0.2912 | -2.54 | 0.0116 * |
| HML | +0.8188 | +7.51 | 0.0000 *** |
| RMW | +0.3092 | +2.27 | 0.0238 * |
| CMA | -0.1415 | -1.03 | 0.3050  |

_Interpretation: Value tilt_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._