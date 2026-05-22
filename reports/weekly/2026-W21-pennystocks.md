# Weekly Report — `pennystocks` — 2026-W21

Generated: 2026-05-22  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W21.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| CXAI | -59.93% | -0.589 | +3.671 | -3.204 | -1.193 | +0.229 | 0.144 | 464 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| GCTS | -53.26% | +1.004 | +0.508 | -0.675 | -0.439 | +0.701 | 0.080 | 464 | Small-cap tilt; Growth tilt; Conservative investment; Modest factor fit |
| VRAX | +33.21% | +0.719 | -0.243 | +0.556 | -2.988 | +1.290 | 0.032 | 464 | Value tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| CODX | +15.39% | +1.239 | +0.219 | -0.966 | -1.428 | -0.685 | 0.023 | 464 | Growth tilt; Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven |
| IBRX | +47.56% | +0.719 | +1.494 | -1.047 | -1.936 | +0.787 | 0.143 | 464 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| AM | +17.18% | +0.621 | -0.266 | +0.373 | -0.256 | +0.072 | 0.196 | 464 | Modest factor fit |
| SLS | +80.37% | +0.182 | +0.453 | +0.104 | -2.108 | -0.716 | 0.081 | 464 | Weak profitability; Aggressive investment; Modest factor fit |
| PR | +7.11% | +1.343 | +0.202 | +0.785 | +0.321 | +0.299 | 0.325 | 464 | Value tilt |
| KOPN | +78.34% | +1.959 | +1.499 | -0.485 | -1.923 | +0.288 | 0.297 | 464 | Small-cap tilt; Weak profitability |
| SATL | +121.51% | +1.126 | +1.439 | -0.456 | -3.198 | +0.148 | 0.183 | 464 | Small-cap tilt; Weak profitability; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| GCTS | **76.67** | 30.00 | 33.33 | 13.33 | 0.075 | +1.007 | 0.7100 | 0.0453 | 214 |
| SLS | **73.33** | 23.33 | 30.00 | 20.00 | 0.116 | +0.777 | 0.8469 | 0.0541 | 214 |
| CODX | **70.00** | 33.33 | 3.33 | 33.33 | 0.035 | -2.629 | 3.3622 | 0.2146 | 214 |
| IBRX | **63.33** | 16.67 | 23.33 | 23.33 | 0.144 | +0.574 | 1.0016 | 0.0639 | 214 |
| SATL | **60.00** | 6.67 | 26.67 | 26.67 | 0.261 | +0.740 | 1.0029 | 0.0640 | 214 |
| VRAX | **60.00** | 20.00 | 10.00 | 30.00 | 0.116 | -0.925 | 1.0988 | 0.0701 | 214 |
| AM | **50.00** | 26.67 | 20.00 | 3.33 | 0.080 | +0.356 | 0.1966 | 0.0125 | 214 |
| PR | **33.33** | 13.33 | 13.33 | 6.67 | 0.185 | -0.298 | 0.2887 | 0.0184 | 214 |
| CXAI | **33.33** | 10.00 | 6.67 | 16.67 | 0.224 | -1.041 | 0.8414 | 0.0537 | 214 |
| KOPN | **30.00** | 3.33 | 16.67 | 10.00 | 0.447 | +0.026 | 0.6791 | 0.0434 | 214 |

## Per-ticker FF5 Detail

### CXAI

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.1443 (adjusted = 0.1350)
- Alpha (annualized): **-59.93%** (daily = -0.002378, t = -0.67, p = 0.5056)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.5886 | -1.52 | 0.1285  |
| SMB | +3.6711 | +5.93 | 0.0000 *** |
| HML | -3.2035 | -5.44 | 0.0000 *** |
| RMW | -1.1930 | -1.63 | 0.1038  |
| CMA | +0.2287 | +0.31 | 0.7571  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### GCTS

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.0800 (adjusted = 0.0700)
- Alpha (annualized): **-53.26%** (daily = -0.002113, t = -0.84, p = 0.4031)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0043 | +3.67 | 0.0003 *** |
| SMB | +0.5076 | +1.16 | 0.2472  |
| HML | -0.6752 | -1.62 | 0.1060  |
| RMW | -0.4394 | -0.85 | 0.3967  |
| CMA | +0.7013 | +1.34 | 0.1806  |

_Interpretation: Small-cap tilt; Growth tilt; Conservative investment; Modest factor fit_

### VRAX

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.0316 (adjusted = 0.0210)
- Alpha (annualized): **+33.21%** (daily = +0.001318, t = +0.24, p = 0.8122)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7194 | +1.20 | 0.2314  |
| SMB | -0.2427 | -0.25 | 0.8009  |
| HML | +0.5563 | +0.61 | 0.5434  |
| RMW | -2.9884 | -2.63 | 0.0089 ** |
| CMA | +1.2902 | +1.12 | 0.2615  |

_Interpretation: Value tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### CODX

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.0231 (adjusted = 0.0125)
- Alpha (annualized): **+15.39%** (daily = +0.000611, t = +0.09, p = 0.9323)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2393 | +1.59 | 0.1117  |
| SMB | +0.2185 | +0.18 | 0.8608  |
| HML | -0.9655 | -0.81 | 0.4157  |
| RMW | -1.4281 | -0.97 | 0.3327  |
| CMA | -0.6848 | -0.46 | 0.6453  |

_Interpretation: Growth tilt; Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven_

### IBRX

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.1431 (adjusted = 0.1337)
- Alpha (annualized): **+47.56%** (daily = +0.001887, t = +0.66, p = 0.5091)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7189 | +2.32 | 0.0206 * |
| SMB | +1.4940 | +3.02 | 0.0027 ** |
| HML | -1.0470 | -2.22 | 0.0268 * |
| RMW | -1.9359 | -3.31 | 0.0010 ** |
| CMA | +0.7874 | +1.33 | 0.1837  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### AM

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.1955 (adjusted = 0.1867)
- Alpha (annualized): **+17.18%** (daily = +0.000682, t = +1.10, p = 0.2727)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6213 | +9.24 | 0.0000 *** |
| SMB | -0.2662 | -2.47 | 0.0138 * |
| HML | +0.3730 | +3.64 | 0.0003 *** |
| RMW | -0.2560 | -2.01 | 0.0449 * |
| CMA | +0.0720 | +0.56 | 0.5754  |

_Interpretation: Modest factor fit_

### SLS

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.0813 (adjusted = 0.0713)
- Alpha (annualized): **+80.37%** (daily = +0.003189, t = +1.29, p = 0.1972)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.1816 | +0.68 | 0.4974  |
| SMB | +0.4531 | +1.06 | 0.2908  |
| HML | +0.1041 | +0.26 | 0.7986  |
| RMW | -2.1082 | -4.16 | 0.0000 *** |
| CMA | -0.7164 | -1.40 | 0.1619  |

_Interpretation: Weak profitability; Aggressive investment; Modest factor fit_

### PR

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.3247 (adjusted = 0.3173)
- Alpha (annualized): **+7.11%** (daily = +0.000282, t = +0.30, p = 0.7655)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3427 | +13.12 | 0.0000 *** |
| SMB | +0.2018 | +1.23 | 0.2192  |
| HML | +0.7855 | +5.03 | 0.0000 *** |
| RMW | +0.3210 | +1.66 | 0.0984  |
| CMA | +0.2989 | +1.53 | 0.1274  |

_Interpretation: Value tilt_

### KOPN

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.2965 (adjusted = 0.2889)
- Alpha (annualized): **+78.34%** (daily = +0.003109, t = +1.26, p = 0.2070)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9593 | +7.36 | 0.0000 *** |
| SMB | +1.4987 | +3.51 | 0.0005 *** |
| HML | -0.4848 | -1.19 | 0.2330  |
| RMW | -1.9225 | -3.81 | 0.0002 *** |
| CMA | +0.2876 | +0.56 | 0.5725  |

_Interpretation: Small-cap tilt; Weak profitability_

### SATL

- Period: `2024-05-23` to `2026-03-31` (464 obs)
- R² = 0.1834 (adjusted = 0.1745)
- Alpha (annualized): **+121.51%** (daily = +0.004822, t = +1.48, p = 0.1387)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1262 | +3.20 | 0.0015 ** |
| SMB | +1.4385 | +2.55 | 0.0111 * |
| HML | -0.4557 | -0.85 | 0.3962  |
| RMW | -3.1984 | -4.80 | 0.0000 *** |
| CMA | +0.1483 | +0.22 | 0.8258  |

_Interpretation: Small-cap tilt; Weak profitability; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._