# Weekly Report — `pennystocks` — 2026-W22

Generated: 2026-05-31  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W22.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HUBC | -298.22% | +2.108 | -1.061 | +0.826 | -0.360 | -0.159 | 0.044 | 459 | Large-cap tilt; Value tilt; Significant negative alpha; Low explanatory power — likely sentiment-driven |
| OTLK | -94.80% | +0.316 | +1.735 | -1.612 | -0.328 | +0.102 | 0.053 | 459 | Small-cap tilt; Growth tilt; Modest factor fit |
| SPCE | -87.10% | +0.887 | +2.210 | -0.853 | -2.010 | -0.240 | 0.289 | 459 | Small-cap tilt; Growth tilt; Weak profitability |
| HOTH | +80.39% | -0.019 | +1.500 | -1.574 | -1.294 | -0.426 | 0.030 | 459 | Small-cap tilt; Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven |
| ASTC | -4.96% | +0.182 | +0.600 | -0.130 | -0.134 | -0.355 | 0.010 | 459 | Small-cap tilt; Low explanatory power — likely sentiment-driven |
| CXAI | -41.31% | -0.594 | +3.737 | -3.307 | -1.068 | +0.084 | 0.148 | 459 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| LFVN | -8.17% | +0.773 | +1.189 | -0.697 | +0.651 | +0.139 | 0.084 | 459 | Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit |
| ELAB | -355.32% | +1.563 | +0.429 | -0.054 | -0.256 | +0.238 | 0.024 | 459 | Significant negative alpha; Low explanatory power — likely sentiment-driven |
| GNS | -58.82% | +0.946 | +0.406 | -0.102 | -2.926 | +0.528 | 0.078 | 459 | Weak profitability; Conservative investment; Modest factor fit |
| CTM | +148.65% | +0.732 | +1.297 | -0.843 | -1.116 | +0.420 | 0.035 | 459 | Small-cap tilt; Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| HUBC | **90.00** | 26.67 | 33.33 | 30.00 | 0.053 | +1.047 | 1.6366 | 0.1029 | 209 |
| GNS | **66.67** | 20.00 | 20.00 | 26.67 | 0.123 | -0.246 | 1.3521 | 0.0850 | 209 |
| OTLK | **63.33** | 30.00 | 10.00 | 23.33 | 0.052 | -1.253 | 1.3282 | 0.0835 | 209 |
| ASTC | **60.00** | 33.33 | 6.67 | 20.00 | 0.040 | -1.559 | 1.2278 | 0.0772 | 209 |
| ELAB | **60.00** | 23.33 | 3.33 | 33.33 | 0.091 | -3.127 | 2.0483 | 0.1288 | 209 |
| HOTH | **56.67** | 16.67 | 23.33 | 16.67 | 0.131 | -0.198 | 0.9759 | 0.0614 | 209 |
| CTM | **50.00** | 10.00 | 30.00 | 10.00 | 0.185 | +0.033 | 0.6753 | 0.0425 | 209 |
| SPCE | **36.67** | 3.33 | 26.67 | 6.67 | 0.273 | -0.174 | 0.6123 | 0.0385 | 209 |
| CXAI | **33.33** | 6.67 | 13.33 | 13.33 | 0.220 | -1.024 | 0.8633 | 0.0543 | 209 |
| LFVN | **33.33** | 13.33 | 16.67 | 3.33 | 0.166 | -0.720 | 0.5049 | 0.0318 | 209 |

## Per-ticker FF5 Detail

### HUBC

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.0436 (adjusted = 0.0331)
- Alpha (annualized): **-298.22%** (daily = -0.011834, t = -2.52, p = 0.0120)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.1077 | +4.16 | 0.0000 *** |
| SMB | -1.0613 | -1.30 | 0.1929  |
| HML | +0.8260 | +1.07 | 0.2870  |
| RMW | -0.3605 | -0.37 | 0.7090  |
| CMA | -0.1593 | -0.16 | 0.8705  |

_Interpretation: Large-cap tilt; Value tilt; Significant negative alpha; Low explanatory power — likely sentiment-driven_

### OTLK

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.0534 (adjusted = 0.0430)
- Alpha (annualized): **-94.80%** (daily = -0.003762, t = -1.08, p = 0.2793)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3162 | +0.84 | 0.3989  |
| SMB | +1.7350 | +2.88 | 0.0041 ** |
| HML | -1.6121 | -2.81 | 0.0051 ** |
| RMW | -0.3283 | -0.46 | 0.6460  |
| CMA | +0.1022 | +0.14 | 0.8876  |

_Interpretation: Small-cap tilt; Growth tilt; Modest factor fit_

### SPCE

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.2886 (adjusted = 0.2807)
- Alpha (annualized): **-87.10%** (daily = -0.003456, t = -1.59, p = 0.1117)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8870 | +3.79 | 0.0002 *** |
| SMB | +2.2100 | +5.88 | 0.0000 *** |
| HML | -0.8529 | -2.38 | 0.0176 * |
| RMW | -2.0101 | -4.51 | 0.0000 *** |
| CMA | -0.2403 | -0.53 | 0.5946  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### HOTH

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.0302 (adjusted = 0.0195)
- Alpha (annualized): **+80.39%** (daily = +0.003190, t = +0.63, p = 0.5307)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.0194 | -0.04 | 0.9718  |
| SMB | +1.5002 | +1.70 | 0.0895  |
| HML | -1.5738 | -1.87 | 0.0614  |
| RMW | -1.2937 | -1.24 | 0.2167  |
| CMA | -0.4259 | -0.40 | 0.6874  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

### ASTC

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.0096 (adjusted = -0.0014)
- Alpha (annualized): **-4.96%** (daily = -0.000197, t = -0.07, p = 0.9426)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.1815 | +0.62 | 0.5384  |
| SMB | +0.5999 | +1.27 | 0.2065  |
| HML | -0.1297 | -0.29 | 0.7740  |
| RMW | -0.1343 | -0.24 | 0.8113  |
| CMA | -0.3548 | -0.62 | 0.5333  |

_Interpretation: Small-cap tilt; Low explanatory power — likely sentiment-driven_

### CXAI

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.1479 (adjusted = 0.1385)
- Alpha (annualized): **-41.31%** (daily = -0.001639, t = -0.46, p = 0.6472)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.5943 | -1.54 | 0.1243  |
| SMB | +3.7369 | +6.02 | 0.0000 *** |
| HML | -3.3075 | -5.60 | 0.0000 *** |
| RMW | -1.0684 | -1.45 | 0.1474  |
| CMA | +0.0843 | +0.11 | 0.9099  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### LFVN

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.0839 (adjusted = 0.0738)
- Alpha (annualized): **-8.17%** (daily = -0.000324, t = -0.17, p = 0.8665)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7729 | +3.72 | 0.0002 *** |
| SMB | +1.1887 | +3.56 | 0.0004 *** |
| HML | -0.6973 | -2.19 | 0.0290 * |
| RMW | +0.6512 | +1.64 | 0.1013  |
| CMA | +0.1392 | +0.35 | 0.7288  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit_

### ELAB

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.0237 (adjusted = 0.0129)
- Alpha (annualized): **-355.32%** (daily = -0.014100, t = -2.48, p = 0.0137)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5632 | +2.55 | 0.0112 * |
| SMB | +0.4293 | +0.43 | 0.6639  |
| HML | -0.0536 | -0.06 | 0.9546  |
| RMW | -0.2561 | -0.22 | 0.8270  |
| CMA | +0.2383 | +0.20 | 0.8407  |

_Interpretation: Significant negative alpha; Low explanatory power — likely sentiment-driven_

### GNS

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.0776 (adjusted = 0.0674)
- Alpha (annualized): **-58.82%** (daily = -0.002334, t = -0.56, p = 0.5725)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9458 | +2.12 | 0.0343 * |
| SMB | +0.4057 | +0.57 | 0.5716  |
| HML | -0.1018 | -0.15 | 0.8815  |
| RMW | -2.9259 | -3.44 | 0.0006 *** |
| CMA | +0.5284 | +0.61 | 0.5392  |

_Interpretation: Weak profitability; Conservative investment; Modest factor fit_

### CTM

- Period: `2024-05-31` to `2026-03-31` (459 obs)
- R² = 0.0349 (adjusted = 0.0242)
- Alpha (annualized): **+148.65%** (daily = +0.005899, t = +1.22, p = 0.2228)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7317 | +1.40 | 0.1609  |
| SMB | +1.2972 | +1.55 | 0.1223  |
| HML | -0.8427 | -1.06 | 0.2914  |
| RMW | -1.1161 | -1.12 | 0.2620  |
| CMA | +0.4201 | +0.42 | 0.6763  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._