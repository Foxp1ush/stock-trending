# Weekly Report — `pennystocks` — 2026-W23

Generated: 2026-06-07  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W23.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| CXAI | -49.59% | -0.607 | +3.718 | -3.268 | -1.154 | +0.111 | 0.148 | 454 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| HUBC | -293.85% | +2.121 | -1.116 | +0.845 | -0.352 | -0.090 | 0.044 | 454 | Large-cap tilt; Value tilt; Significant negative alpha; Low explanatory power — likely sentiment-driven |
| LASE | +93.76% | +1.230 | +0.788 | +0.035 | -0.307 | -1.164 | 0.023 | 454 | Small-cap tilt; Aggressive investment; Low explanatory power — likely sentiment-driven |
| SPCE | -86.70% | +0.887 | +2.184 | -0.839 | -2.057 | -0.242 | 0.290 | 454 | Small-cap tilt; Growth tilt; Weak profitability |
| STI | +58.43% | +2.129 | +0.586 | +0.493 | -1.931 | -0.120 | 0.029 | 454 | Small-cap tilt; Weak profitability; Low explanatory power — likely sentiment-driven |
| LFVN | -7.23% | +0.776 | +1.179 | -0.681 | +0.634 | +0.138 | 0.084 | 454 | Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit |
| PR | +7.17% | +1.351 | +0.179 | +0.799 | +0.313 | +0.326 | 0.328 | 454 | Value tilt |
| OTLK | -94.81% | +0.322 | +1.762 | -1.614 | -0.305 | +0.088 | 0.054 | 454 | Small-cap tilt; Growth tilt; Modest factor fit |
| ELAB | -357.14% | +1.563 | +0.429 | -0.047 | -0.284 | +0.233 | 0.024 | 454 | Significant negative alpha; Low explanatory power — likely sentiment-driven |
| VERU | -54.14% | +0.948 | +0.585 | -0.653 | -1.106 | +0.488 | 0.113 | 454 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| STI | **100.00** | 33.33 | 33.33 | 33.33 | 0.050 | +1.082 | 3.7048 | 0.2297 | 204 |
| HUBC | **80.00** | 26.67 | 30.00 | 23.33 | 0.056 | +1.037 | 1.6763 | 0.1039 | 204 |
| OTLK | **60.00** | 30.00 | 10.00 | 20.00 | 0.050 | -1.222 | 1.3628 | 0.0845 | 204 |
| LASE | **56.67** | 23.33 | 6.67 | 26.67 | 0.070 | -2.224 | 1.7146 | 0.1063 | 204 |
| ELAB | **53.33** | 20.00 | 3.33 | 30.00 | 0.093 | -3.203 | 2.0999 | 0.1302 | 204 |
| VERU | **46.67** | 13.33 | 20.00 | 13.33 | 0.172 | -0.464 | 0.6539 | 0.0405 | 204 |
| SPCE | **40.00** | 3.33 | 26.67 | 10.00 | 0.274 | -0.140 | 0.6212 | 0.0385 | 204 |
| LFVN | **40.00** | 16.67 | 16.67 | 6.67 | 0.165 | -0.711 | 0.5152 | 0.0319 | 204 |
| CXAI | **36.67** | 6.67 | 13.33 | 16.67 | 0.218 | -1.014 | 0.8853 | 0.0549 | 204 |
| PR | **36.67** | 10.00 | 23.33 | 3.33 | 0.189 | -0.244 | 0.2974 | 0.0184 | 204 |

## Per-ticker FF5 Detail

### CXAI

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.1484 (adjusted = 0.1389)
- Alpha (annualized): **-49.59%** (daily = -0.001968, t = -0.55, p = 0.5854)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.6071 | -1.57 | 0.1181  |
| SMB | +3.7184 | +5.95 | 0.0000 *** |
| HML | -3.2683 | -5.51 | 0.0000 *** |
| RMW | -1.1545 | -1.56 | 0.1200  |
| CMA | +0.1111 | +0.15 | 0.8822  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### HUBC

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.0439 (adjusted = 0.0333)
- Alpha (annualized): **-293.85%** (daily = -0.011661, t = -2.46, p = 0.0143)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.1215 | +4.16 | 0.0000 *** |
| SMB | -1.1160 | -1.36 | 0.1748  |
| HML | +0.8447 | +1.08 | 0.2792  |
| RMW | -0.3516 | -0.36 | 0.7184  |
| CMA | -0.0901 | -0.09 | 0.9272  |

_Interpretation: Large-cap tilt; Value tilt; Significant negative alpha; Low explanatory power — likely sentiment-driven_

### LASE

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.0231 (adjusted = 0.0122)
- Alpha (annualized): **+93.76%** (daily = +0.003721, t = +0.70, p = 0.4867)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2295 | +2.14 | 0.0330 * |
| SMB | +0.7881 | +0.85 | 0.3951  |
| HML | +0.0345 | +0.04 | 0.9687  |
| RMW | -0.3072 | -0.28 | 0.7799  |
| CMA | -1.1643 | -1.05 | 0.2952  |

_Interpretation: Small-cap tilt; Aggressive investment; Low explanatory power — likely sentiment-driven_

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

### STI

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.0290 (adjusted = 0.0182)
- Alpha (annualized): **+58.43%** (daily = +0.002318, t = +0.27, p = 0.7837)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.1286 | +2.34 | 0.0195 * |
| SMB | +0.5860 | +0.40 | 0.6888  |
| HML | +0.4930 | +0.36 | 0.7227  |
| RMW | -1.9311 | -1.11 | 0.2665  |
| CMA | -0.1201 | -0.07 | 0.9455  |

_Interpretation: Small-cap tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

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

### PR

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.3282 (adjusted = 0.3207)
- Alpha (annualized): **+7.17%** (daily = +0.000284, t = +0.30, p = 0.7663)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3507 | +13.13 | 0.0000 *** |
| SMB | +0.1791 | +1.08 | 0.2805  |
| HML | +0.7991 | +5.08 | 0.0000 *** |
| RMW | +0.3129 | +1.59 | 0.1123  |
| CMA | +0.3261 | +1.64 | 0.1018  |

_Interpretation: Value tilt_

### OTLK

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.0536 (adjusted = 0.0430)
- Alpha (annualized): **-94.81%** (daily = -0.003762, t = -1.07, p = 0.2843)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3223 | +0.85 | 0.3937  |
| SMB | +1.7625 | +2.90 | 0.0039 ** |
| HML | -1.6141 | -2.80 | 0.0054 ** |
| RMW | -0.3049 | -0.42 | 0.6728  |
| CMA | +0.0884 | +0.12 | 0.9036  |

_Interpretation: Small-cap tilt; Growth tilt; Modest factor fit_

### ELAB

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.0238 (adjusted = 0.0129)
- Alpha (annualized): **-357.14%** (daily = -0.014172, t = -2.46, p = 0.0142)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5626 | +2.52 | 0.0120 * |
| SMB | +0.4294 | +0.43 | 0.6670  |
| HML | -0.0467 | -0.05 | 0.9607  |
| RMW | -0.2839 | -0.24 | 0.8105  |
| CMA | +0.2327 | +0.19 | 0.8459  |

_Interpretation: Significant negative alpha; Low explanatory power — likely sentiment-driven_

### VERU

- Period: `2024-06-07` to `2026-03-31` (454 obs)
- R² = 0.1130 (adjusted = 0.1031)
- Alpha (annualized): **-54.14%** (daily = -0.002148, t = -0.88, p = 0.3775)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9475 | +3.62 | 0.0003 *** |
| SMB | +0.5850 | +1.39 | 0.1656  |
| HML | -0.6526 | -1.63 | 0.1035  |
| RMW | -1.1057 | -2.21 | 0.0275 * |
| CMA | +0.4883 | +0.97 | 0.3346  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._