# Weekly Report — `wallstreetbets` — 2026-W23

Generated: 2026-06-07  ·  Source: `apewisdom:wallstreetbets`  ·  Lookback: 7 days

[← Back to dashboard](2026-W23.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| SPCE | -86.70% | +0.887 | +2.184 | -0.839 | -2.057 | -0.242 | 0.290 | 454 | Small-cap tilt; Growth tilt; Weak profitability |
| MU | +43.99% | +2.040 | -0.438 | -0.127 | -0.856 | +0.392 | 0.396 | 454 | Weak profitability |
| AVGO | +50.59% | +1.735 | -0.157 | -1.370 | +0.220 | +0.190 | 0.475 | 454 | Growth tilt |
| MRVL | +16.96% | +2.002 | -0.402 | -0.749 | -1.174 | +0.835 | 0.461 | 454 | Growth tilt; Weak profitability; Conservative investment |
| NVDA | +17.44% | +1.752 | -0.822 | -1.207 | -0.263 | +1.547 | 0.678 | 454 | Large-cap tilt; Growth tilt; Conservative investment |
| MSFT | -13.10% | +0.888 | -0.252 | -0.406 | +0.143 | -0.500 | 0.524 | 454 | Neutral profile |
| HPE | -2.64% | +1.602 | +0.095 | +0.371 | -0.453 | +0.307 | 0.441 | 454 | Neutral profile |
| NOW | -22.22% | +0.951 | -0.061 | -0.441 | -0.563 | -0.114 | 0.304 | 454 | Weak profitability |
| ASTS | +159.78% | +1.512 | +1.585 | -1.574 | -2.432 | -0.064 | 0.275 | 454 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| OPEN | +101.24% | +1.358 | +2.230 | -0.668 | -1.379 | +1.402 | 0.130 | 454 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| MU | **83.33** | 26.67 | 33.33 | 23.33 | 0.288 | +0.473 | 0.5209 | 0.0323 | 204 |
| OPEN | **76.67** | 33.33 | 10.00 | 33.33 | 0.090 | -0.158 | 1.7036 | 0.1056 | 204 |
| SPCE | **70.00** | 30.00 | 13.33 | 26.67 | 0.274 | -0.140 | 0.6212 | 0.0385 | 204 |
| ASTS | **66.67** | 20.00 | 16.67 | 30.00 | 0.300 | +0.052 | 0.8707 | 0.0540 | 204 |
| MRVL | **66.67** | 23.33 | 23.33 | 20.00 | 0.289 | +0.161 | 0.4952 | 0.0307 | 204 |
| HPE | **50.00** | 13.33 | 20.00 | 16.67 | 0.393 | +0.143 | 0.3176 | 0.0197 | 204 |
| AVGO | **46.67** | 6.67 | 26.67 | 13.33 | 0.477 | +0.382 | 0.3159 | 0.0196 | 204 |
| NVDA | **40.00** | 3.33 | 30.00 | 6.67 | 0.605 | +0.385 | 0.2140 | 0.0133 | 204 |
| NOW | **30.00** | 16.67 | 3.33 | 10.00 | 0.363 | -1.401 | 0.3048 | 0.0189 | 204 |
| MSFT | **20.00** | 10.00 | 6.67 | 3.33 | 0.418 | -0.414 | 0.1798 | 0.0111 | 204 |

## Per-ticker FF5 Detail

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

### MU

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.3956 (adjusted = 0.3889)
- Alpha (annualized): **+43.99%** (daily = +0.001745, t = +1.20, p = 0.2304)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.0405 | +13.05 | 0.0000 *** |
| SMB | -0.4381 | -1.74 | 0.0825  |
| HML | -0.1266 | -0.53 | 0.5967  |
| RMW | -0.8562 | -2.87 | 0.0044 ** |
| CMA | +0.3919 | +1.30 | 0.1951  |

_Interpretation: Weak profitability_

### AVGO

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.4747 (adjusted = 0.4689)
- Alpha (annualized): **+50.59%** (daily = +0.002008, t = +1.69, p = 0.0925)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7350 | +13.55 | 0.0000 *** |
| SMB | -0.1569 | -0.76 | 0.4472  |
| HML | -1.3697 | -6.99 | 0.0000 *** |
| RMW | +0.2195 | +0.90 | 0.3703  |
| CMA | +0.1896 | +0.77 | 0.4441  |

_Interpretation: Growth tilt_

### MRVL

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.4608 (adjusted = 0.4548)
- Alpha (annualized): **+16.96%** (daily = +0.000673, t = +0.47, p = 0.6398)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.0020 | +12.95 | 0.0000 *** |
| SMB | -0.4018 | -1.61 | 0.1074  |
| HML | -0.7489 | -3.17 | 0.0016 ** |
| RMW | -1.1739 | -3.97 | 0.0001 *** |
| CMA | +0.8349 | +2.79 | 0.0054 ** |

_Interpretation: Growth tilt; Weak profitability; Conservative investment_

### NVDA

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.6775 (adjusted = 0.6739)
- Alpha (annualized): **+17.44%** (daily = +0.000692, t = +0.83, p = 0.4046)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7519 | +19.63 | 0.0000 *** |
| SMB | -0.8216 | -5.72 | 0.0000 *** |
| HML | -1.2070 | -8.85 | 0.0000 *** |
| RMW | -0.2628 | -1.54 | 0.1241  |
| CMA | +1.5467 | +8.97 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### MSFT

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.5242 (adjusted = 0.5189)
- Alpha (annualized): **-13.10%** (daily = -0.000520, t = -1.03, p = 0.3043)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8882 | +16.34 | 0.0000 *** |
| SMB | -0.2517 | -2.88 | 0.0042 ** |
| HML | -0.4063 | -4.89 | 0.0000 *** |
| RMW | +0.1427 | +1.37 | 0.1703  |
| CMA | -0.4999 | -4.76 | 0.0000 *** |

_Interpretation: Neutral profile_

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

### NOW

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.3036 (adjusted = 0.2959)
- Alpha (annualized): **-22.22%** (daily = -0.000882, t = -0.88, p = 0.3768)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9512 | +8.87 | 0.0000 *** |
| SMB | -0.0609 | -0.35 | 0.7244  |
| HML | -0.4414 | -2.69 | 0.0074 ** |
| RMW | -0.5629 | -2.75 | 0.0063 ** |
| CMA | -0.1140 | -0.55 | 0.5824  |

_Interpretation: Weak profitability_

### ASTS

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.2753 (adjusted = 0.2672)
- Alpha (annualized): **+159.78%** (daily = +0.006341, t = +2.26, p = 0.0243)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5115 | +5.01 | 0.0000 *** |
| SMB | +1.5850 | +3.26 | 0.0012 ** |
| HML | -1.5741 | -3.41 | 0.0007 *** |
| RMW | -2.4316 | -4.22 | 0.0000 *** |
| CMA | -0.0639 | -0.11 | 0.9128  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### OPEN

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.1303 (adjusted = 0.1206)
- Alpha (annualized): **+101.24%** (daily = +0.004017, t = +1.07, p = 0.2848)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3583 | +3.37 | 0.0008 *** |
| SMB | +2.2295 | +3.43 | 0.0007 *** |
| HML | -0.6684 | -1.08 | 0.2793  |
| RMW | -1.3789 | -1.79 | 0.0744  |
| CMA | +1.4022 | +1.80 | 0.0728  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._