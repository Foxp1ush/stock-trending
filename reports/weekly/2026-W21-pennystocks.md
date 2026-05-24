# Weekly Report — `pennystocks` — 2026-W21

Generated: 2026-05-24  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W21.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| GCTS | -54.85% | +1.006 | +0.501 | -0.662 | -0.465 | +0.716 | 0.080 | 463 | Small-cap tilt; Growth tilt; Conservative investment; Modest factor fit |
| CXAI | -61.86% | -0.586 | +3.663 | -3.187 | -1.225 | +0.247 | 0.145 | 463 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| VRAX | +31.62% | +0.721 | -0.249 | +0.570 | -3.014 | +1.305 | 0.032 | 463 | Value tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| FRGT | -247.44% | +0.908 | +1.239 | -0.911 | -0.875 | +0.027 | 0.048 | 463 | Small-cap tilt; Growth tilt; Weak profitability; Significant negative alpha; Low explanatory power — likely sentiment-driven |
| AM | +17.78% | +0.621 | -0.264 | +0.368 | -0.246 | +0.067 | 0.193 | 463 | Modest factor fit |
| CODX | +14.83% | +1.240 | +0.216 | -0.961 | -1.437 | -0.680 | 0.023 | 463 | Growth tilt; Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven |
| PR | +6.30% | +1.344 | +0.198 | +0.792 | +0.308 | +0.306 | 0.325 | 463 | Value tilt |
| HMR | -109.85% | +0.254 | +0.514 | +0.107 | +0.096 | +1.182 | 0.010 | 278 | Small-cap tilt; Conservative investment; Low explanatory power — likely sentiment-driven |
| NVDA | +25.20% | +1.751 | -0.771 | -1.277 | -0.202 | +1.397 | 0.662 | 463 | Large-cap tilt; Growth tilt; Conservative investment |
| DOW | -20.86% | +1.244 | +0.678 | +0.636 | +0.262 | +1.043 | 0.352 | 463 | Small-cap tilt; Value tilt; Conservative investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| GCTS | **80.00** | 26.67 | 33.33 | 20.00 | 0.077 | +1.034 | 0.7110 | 0.0453 | 213 |
| FRGT | **76.67** | 20.00 | 30.00 | 26.67 | 0.080 | +0.456 | 0.9534 | 0.0608 | 213 |
| HMR | **66.67** | 33.33 | 16.67 | 16.67 | 0.028 | -0.428 | 0.7008 | 0.0447 | 213 |
| CODX | **66.67** | 30.00 | 3.33 | 33.33 | 0.035 | -2.625 | 3.3737 | 0.2151 | 213 |
| VRAX | **56.67** | 16.67 | 10.00 | 30.00 | 0.117 | -0.951 | 1.1017 | 0.0703 | 213 |
| AM | **53.33** | 23.33 | 26.67 | 3.33 | 0.079 | +0.354 | 0.1972 | 0.0126 | 213 |
| PR | **43.33** | 13.33 | 20.00 | 10.00 | 0.185 | -0.290 | 0.2894 | 0.0185 | 213 |
| CXAI | **40.00** | 10.00 | 6.67 | 23.33 | 0.223 | -1.032 | 0.8441 | 0.0538 | 213 |
| DOW | **33.33** | 6.67 | 13.33 | 13.33 | 0.327 | -0.680 | 0.4015 | 0.0256 | 213 |
| NVDA | **33.33** | 3.33 | 23.33 | 6.67 | 0.584 | +0.353 | 0.2137 | 0.0136 | 213 |

## Per-ticker FF5 Detail

### GCTS

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.0804 (adjusted = 0.0703)
- Alpha (annualized): **-54.85%** (daily = -0.002177, t = -0.86, p = 0.3903)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0060 | +3.67 | 0.0003 *** |
| SMB | +0.5012 | +1.14 | 0.2540  |
| HML | -0.6616 | -1.58 | 0.1143  |
| RMW | -0.4654 | -0.89 | 0.3726  |
| CMA | +0.7160 | +1.37 | 0.1728  |

_Interpretation: Small-cap tilt; Growth tilt; Conservative investment; Modest factor fit_

### CXAI

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.1445 (adjusted = 0.1352)
- Alpha (annualized): **-61.86%** (daily = -0.002455, t = -0.69, p = 0.4930)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.5865 | -1.52 | 0.1302  |
| SMB | +3.6633 | +5.91 | 0.0000 *** |
| HML | -3.1871 | -5.39 | 0.0000 *** |
| RMW | -1.2247 | -1.66 | 0.0972  |
| CMA | +0.2466 | +0.33 | 0.7395  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### VRAX

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.0316 (adjusted = 0.0210)
- Alpha (annualized): **+31.62%** (daily = +0.001255, t = +0.23, p = 0.8215)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7211 | +1.20 | 0.2308  |
| SMB | -0.2492 | -0.26 | 0.7960  |
| HML | +0.5699 | +0.62 | 0.5351  |
| RMW | -3.0144 | -2.63 | 0.0087 ** |
| CMA | +1.3049 | +1.13 | 0.2575  |

_Interpretation: Value tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### FRGT

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.0483 (adjusted = 0.0379)
- Alpha (annualized): **-247.44%** (daily = -0.009819, t = -2.38, p = 0.0177)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9081 | +2.04 | 0.0424 * |
| SMB | +1.2393 | +1.73 | 0.0838  |
| HML | -0.9110 | -1.34 | 0.1821  |
| RMW | -0.8749 | -1.03 | 0.3038  |
| CMA | +0.0267 | +0.03 | 0.9751  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant negative alpha; Low explanatory power — likely sentiment-driven_

### AM

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.1935 (adjusted = 0.1847)
- Alpha (annualized): **+17.78%** (daily = +0.000705, t = +1.13, p = 0.2574)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6207 | +9.23 | 0.0000 *** |
| SMB | -0.2638 | -2.45 | 0.0148 * |
| HML | +0.3680 | +3.58 | 0.0004 *** |
| RMW | -0.2463 | -1.92 | 0.0552  |
| CMA | +0.0666 | +0.52 | 0.6057  |

_Interpretation: Modest factor fit_

### CODX

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.0231 (adjusted = 0.0125)
- Alpha (annualized): **+14.83%** (daily = +0.000588, t = +0.08, p = 0.9349)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2399 | +1.59 | 0.1119  |
| SMB | +0.2162 | +0.17 | 0.8625  |
| HML | -0.9607 | -0.81 | 0.4196  |
| RMW | -1.4373 | -0.97 | 0.3329  |
| CMA | -0.6796 | -0.46 | 0.6488  |

_Interpretation: Growth tilt; Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven_

### PR

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.3253 (adjusted = 0.3179)
- Alpha (annualized): **+6.30%** (daily = +0.000250, t = +0.26, p = 0.7921)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3435 | +13.11 | 0.0000 *** |
| SMB | +0.1985 | +1.21 | 0.2274  |
| HML | +0.7924 | +5.06 | 0.0000 *** |
| RMW | +0.3078 | +1.58 | 0.1154  |
| CMA | +0.3064 | +1.56 | 0.1191  |

_Interpretation: Value tilt_

### HMR

- Period: `2025-02-21` to `2026-03-31` (278 obs)
- R² = 0.0104 (adjusted = -0.0078)
- Alpha (annualized): **-109.85%** (daily = -0.004359, t = -0.87, p = 0.3843)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2541 | +0.52 | 0.6045  |
| SMB | +0.5144 | +0.56 | 0.5753  |
| HML | +0.1071 | +0.12 | 0.9053  |
| RMW | +0.0965 | +0.10 | 0.9197  |
| CMA | +1.1819 | +0.99 | 0.3233  |

_Interpretation: Small-cap tilt; Conservative investment; Low explanatory power — likely sentiment-driven_

### NVDA

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.6623 (adjusted = 0.6586)
- Alpha (annualized): **+25.20%** (daily = +0.001000, t = +1.19, p = 0.2363)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7509 | +19.20 | 0.0000 *** |
| SMB | -0.7709 | -5.27 | 0.0000 *** |
| HML | -1.2768 | -9.16 | 0.0000 *** |
| RMW | -0.2020 | -1.16 | 0.2454  |
| CMA | +1.3967 | +8.00 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### DOW

- Period: `2024-05-24` to `2026-03-31` (463 obs)
- R² = 0.3518 (adjusted = 0.3447)
- Alpha (annualized): **-20.86%** (daily = -0.000828, t = -0.82, p = 0.4144)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2442 | +11.36 | 0.0000 *** |
| SMB | +0.6777 | +3.86 | 0.0001 *** |
| HML | +0.6356 | +3.80 | 0.0002 *** |
| RMW | +0.2619 | +1.26 | 0.2100  |
| CMA | +1.0429 | +4.97 | 0.0000 *** |

_Interpretation: Small-cap tilt; Value tilt; Conservative investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._