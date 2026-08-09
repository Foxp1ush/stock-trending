# Weekly Report — `Shortsqueeze` — 2026-W32

Generated: 2026-08-09  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W32.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +44.58% | +1.016 | +2.235 | +0.557 | +0.397 | +0.358 | 0.108 | 411 | Small-cap tilt; Value tilt; Modest factor fit |
| RR | +157.76% | +1.093 | +1.947 | -1.357 | -4.087 | +1.101 | 0.174 | 411 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| BYND | -43.01% | +0.971 | +0.852 | +0.288 | -1.263 | +1.763 | 0.029 | 411 | Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| PLTR | +76.68% | +1.585 | -0.755 | -0.050 | -2.339 | -0.866 | 0.444 | 411 | Large-cap tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| AM | +20.20% | +0.603 | -0.282 | +0.360 | -0.240 | +0.080 | 0.183 | 411 | Modest factor fit |
| BE | +168.07% | +1.382 | -0.125 | -0.055 | -2.609 | -1.997 | 0.200 | 411 | Weak profitability; Aggressive investment; Significant positive alpha |
| OI | -8.18% | +1.098 | +1.323 | +0.315 | +0.490 | +0.959 | 0.364 | 411 | Small-cap tilt; Conservative investment |
| ET | +1.72% | +0.739 | -0.228 | +0.386 | -0.307 | +0.346 | 0.314 | 411 | Neutral profile |
| ES | -2.16% | +0.374 | -0.099 | +0.467 | -0.131 | +0.309 | 0.091 | 411 | Modest factor fit |
| EDIT | -4.22% | +1.149 | +2.045 | -0.391 | -2.986 | +1.070 | 0.210 | 411 | Small-cap tilt; Weak profitability; Conservative investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| RR | **76.67** | 16.67 | 30.00 | 30.00 | 0.267 | +0.747 | 1.3463 | 0.0726 | 161 |
| BYND | **70.00** | 33.33 | 3.33 | 33.33 | 0.043 | -2.290 | 3.2440 | 0.1750 | 161 |
| BE | **70.00** | 10.00 | 33.33 | 26.67 | 0.418 | +2.438 | 0.9815 | 0.0529 | 161 |
| HTZ | **63.33** | 20.00 | 23.33 | 20.00 | 0.117 | +0.168 | 0.8338 | 0.0450 | 161 |
| AM | **53.33** | 30.00 | 16.67 | 6.67 | 0.056 | +0.157 | 0.2136 | 0.0115 | 161 |
| OI | **46.67** | 6.67 | 26.67 | 13.33 | 0.430 | +0.214 | 0.3855 | 0.0208 | 161 |
| ES | **46.67** | 26.67 | 10.00 | 10.00 | 0.058 | -0.158 | 0.3053 | 0.0165 | 161 |
| EDIT | **43.33** | 13.33 | 6.67 | 23.33 | 0.405 | -0.377 | 0.8508 | 0.0459 | 161 |
| ET | **40.00** | 23.33 | 13.33 | 3.33 | 0.085 | +0.070 | 0.1754 | 0.0095 | 161 |
| PLTR | **40.00** | 3.33 | 20.00 | 16.67 | 0.528 | +0.160 | 0.4054 | 0.0219 | 161 |

## Per-ticker FF5 Detail

### HTZ

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.1082 (adjusted = 0.0971)
- Alpha (annualized): **+44.58%** (daily = +0.001769, t = +0.60, p = 0.5456)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0161 | +3.25 | 0.0013 ** |
| SMB | +2.2346 | +4.25 | 0.0000 *** |
| HML | +0.5566 | +1.16 | 0.2463  |
| RMW | +0.3973 | +0.67 | 0.5031  |
| CMA | +0.3585 | +0.58 | 0.5615  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### RR

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.1736 (adjusted = 0.1634)
- Alpha (annualized): **+157.76%** (daily = +0.006260, t = +1.36, p = 0.1734)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0932 | +2.22 | 0.0266 * |
| SMB | +1.9471 | +2.36 | 0.0189 * |
| HML | -1.3575 | -1.80 | 0.0719  |
| RMW | -4.0866 | -4.39 | 0.0000 *** |
| CMA | +1.1013 | +1.14 | 0.2560  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### BYND

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.0291 (adjusted = 0.0171)
- Alpha (annualized): **-43.01%** (daily = -0.001707, t = -0.30, p = 0.7657)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9707 | +1.58 | 0.1140  |
| SMB | +0.8517 | +0.83 | 0.4089  |
| HML | +0.2877 | +0.31 | 0.7593  |
| RMW | -1.2625 | -1.09 | 0.2771  |
| CMA | +1.7626 | +1.46 | 0.1451  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### PLTR

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.4442 (adjusted = 0.4373)
- Alpha (annualized): **+76.68%** (daily = +0.003043, t = +2.01, p = 0.0451)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5846 | +9.78 | 0.0000 *** |
| SMB | -0.7552 | -2.77 | 0.0058 ** |
| HML | -0.0499 | -0.20 | 0.8408  |
| RMW | -2.3389 | -7.62 | 0.0000 *** |
| CMA | -0.8664 | -2.71 | 0.0069 ** |

_Interpretation: Large-cap tilt; Weak profitability; Aggressive investment; Significant positive alpha_

### AM

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.1834 (adjusted = 0.1733)
- Alpha (annualized): **+20.20%** (daily = +0.000802, t = +1.19, p = 0.2363)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6035 | +8.34 | 0.0000 *** |
| SMB | -0.2822 | -2.32 | 0.0208 * |
| HML | +0.3597 | +3.25 | 0.0013 ** |
| RMW | -0.2403 | -1.75 | 0.0801  |
| CMA | +0.0801 | +0.56 | 0.5745  |

_Interpretation: Modest factor fit_

### BE

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.2005 (adjusted = 0.1906)
- Alpha (annualized): **+168.07%** (daily = +0.006669, t = +2.28, p = 0.0230)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3818 | +4.42 | 0.0000 *** |
| SMB | -0.1252 | -0.24 | 0.8119  |
| HML | -0.0555 | -0.12 | 0.9078  |
| RMW | -2.6086 | -4.41 | 0.0000 *** |
| CMA | -1.9974 | -3.24 | 0.0013 ** |

_Interpretation: Weak profitability; Aggressive investment; Significant positive alpha_

### OI

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.3636 (adjusted = 0.3558)
- Alpha (annualized): **-8.18%** (daily = -0.000324, t = -0.30, p = 0.7659)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0979 | +9.42 | 0.0000 *** |
| SMB | +1.3226 | +6.75 | 0.0000 *** |
| HML | +0.3152 | +1.77 | 0.0781  |
| RMW | +0.4900 | +2.22 | 0.0269 * |
| CMA | +0.9593 | +4.18 | 0.0000 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### ET

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.3137 (adjusted = 0.3052)
- Alpha (annualized): **+1.72%** (daily = +0.000068, t = +0.11, p = 0.9106)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7388 | +11.35 | 0.0000 *** |
| SMB | -0.2282 | -2.09 | 0.0376 * |
| HML | +0.3857 | +3.87 | 0.0001 *** |
| RMW | -0.3074 | -2.50 | 0.0130 * |
| CMA | +0.3464 | +2.70 | 0.0072 ** |

_Interpretation: Neutral profile_

### ES

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.0911 (adjusted = 0.0799)
- Alpha (annualized): **-2.16%** (daily = -0.000086, t = -0.11, p = 0.9085)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3738 | +4.68 | 0.0000 *** |
| SMB | -0.0993 | -0.74 | 0.4598  |
| HML | +0.4667 | +3.82 | 0.0002 *** |
| RMW | -0.1314 | -0.87 | 0.3853  |
| CMA | +0.3091 | +1.96 | 0.0502  |

_Interpretation: Modest factor fit_

### EDIT

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.2105 (adjusted = 0.2007)
- Alpha (annualized): **-4.22%** (daily = -0.000168, t = -0.05, p = 0.9599)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1491 | +3.22 | 0.0014 ** |
| SMB | +2.0447 | +3.41 | 0.0007 *** |
| HML | -0.3910 | -0.72 | 0.4745  |
| RMW | -2.9858 | -4.42 | 0.0000 *** |
| CMA | +1.0704 | +1.52 | 0.1286  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._