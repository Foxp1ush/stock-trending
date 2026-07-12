# Weekly Report — `pennystocks` — 2026-W28

Generated: 2026-07-12  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W28.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| BATL | +256.24% | +0.031 | +0.753 | -1.800 | +2.653 | -0.394 | 0.008 | 431 | Small-cap tilt; Growth tilt; Robust profitability; Low explanatory power — likely sentiment-driven |
| LUCY | -32.99% | +0.456 | +0.464 | -0.611 | -1.900 | -0.488 | 0.036 | 431 | Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven |
| ELAB | -361.44% | +1.549 | +0.489 | -0.036 | -0.302 | +0.232 | 0.024 | 431 | Significant negative alpha; Low explanatory power — likely sentiment-driven |
| RS | -6.60% | +0.886 | +0.706 | +0.493 | +0.357 | +0.311 | 0.452 | 431 | Small-cap tilt |
| SUNE | -298.39% | +1.393 | +2.227 | -1.282 | +1.180 | +2.460 | 0.041 | 431 | Small-cap tilt; Growth tilt; Robust profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| CXAI | -48.33% | -0.784 | +4.298 | -3.371 | -1.253 | +0.092 | 0.165 | 431 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| PR | +6.20% | +1.377 | +0.135 | +0.792 | +0.372 | +0.284 | 0.332 | 431 | Value tilt |
| LGO | -21.42% | +1.394 | +0.419 | +0.642 | -1.451 | -0.031 | 0.157 | 431 | Value tilt; Weak profitability; Modest factor fit |
| AMD | +0.02% | +1.577 | -0.631 | -0.531 | -1.710 | -0.065 | 0.488 | 431 | Large-cap tilt; Growth tilt; Weak profitability |
| AVGO | +45.07% | +1.698 | -0.184 | -1.367 | +0.063 | +0.134 | 0.492 | 431 | Growth tilt |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| BATL | **76.67** | 33.33 | 10.00 | 33.33 | 0.018 | -1.029 | 3.8425 | 0.2212 | 181 |
| LGO | **73.33** | 16.67 | 33.33 | 23.33 | 0.183 | +1.005 | 1.0058 | 0.0579 | 181 |
| SUNE | **70.00** | 30.00 | 13.33 | 26.67 | 0.094 | -0.698 | 1.4145 | 0.0814 | 181 |
| LUCY | **63.33** | 23.33 | 23.33 | 16.67 | 0.154 | +0.345 | 0.9202 | 0.0530 | 181 |
| ELAB | **60.00** | 26.67 | 3.33 | 30.00 | 0.102 | -3.569 | 2.3565 | 0.1356 | 181 |
| AMD | **50.00** | 6.67 | 30.00 | 13.33 | 0.444 | +0.459 | 0.5140 | 0.0296 | 181 |
| PR | **43.33** | 20.00 | 16.67 | 6.67 | 0.176 | -0.110 | 0.3246 | 0.0187 | 181 |
| AVGO | **40.00** | 3.33 | 26.67 | 10.00 | 0.474 | +0.365 | 0.3524 | 0.0203 | 181 |
| CXAI | **40.00** | 13.33 | 6.67 | 20.00 | 0.216 | -1.047 | 0.9836 | 0.0566 | 181 |
| RS | **33.33** | 10.00 | 20.00 | 3.33 | 0.350 | +0.109 | 0.2294 | 0.0132 | 181 |

## Per-ticker FF5 Detail

### BATL

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.0083 (adjusted = -0.0033)
- Alpha (annualized): **+256.24%** (daily = +0.010168, t = +1.25, p = 0.2119)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.0315 | +0.04 | 0.9710  |
| SMB | +0.7535 | +0.52 | 0.6030  |
| HML | -1.7997 | -1.35 | 0.1762  |
| RMW | +2.6531 | +1.59 | 0.1126  |
| CMA | -0.3941 | -0.23 | 0.8158  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Low explanatory power — likely sentiment-driven_

### LUCY

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.0361 (adjusted = 0.0247)
- Alpha (annualized): **-32.99%** (daily = -0.001309, t = -0.28, p = 0.7775)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.4564 | +0.93 | 0.3551  |
| SMB | +0.4636 | +0.56 | 0.5740  |
| HML | -0.6112 | -0.81 | 0.4194  |
| RMW | -1.9002 | -2.00 | 0.0461 * |
| CMA | -0.4882 | -0.51 | 0.6122  |

_Interpretation: Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

### ELAB

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.0238 (adjusted = 0.0123)
- Alpha (annualized): **-361.44%** (daily = -0.014343, t = -2.37, p = 0.0184)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5491 | +2.40 | 0.0169 * |
| SMB | +0.4894 | +0.45 | 0.6504  |
| HML | -0.0359 | -0.04 | 0.9711  |
| RMW | -0.3016 | -0.24 | 0.8086  |
| CMA | +0.2317 | +0.18 | 0.8542  |

_Interpretation: Significant negative alpha; Low explanatory power — likely sentiment-driven_

### RS

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.4519 (adjusted = 0.4454)
- Alpha (annualized): **-6.60%** (daily = -0.000262, t = -0.42, p = 0.6712)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8863 | +13.50 | 0.0000 *** |
| SMB | +0.7056 | +6.43 | 0.0000 *** |
| HML | +0.4929 | +4.89 | 0.0000 *** |
| RMW | +0.3575 | +2.83 | 0.0049 ** |
| CMA | +0.3106 | +2.42 | 0.0158 * |

_Interpretation: Small-cap tilt_

### SUNE

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.0408 (adjusted = 0.0295)
- Alpha (annualized): **-298.39%** (daily = -0.011841, t = -1.89, p = 0.0595)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3935 | +2.09 | 0.0374 * |
| SMB | +2.2275 | +2.00 | 0.0464 * |
| HML | -1.2824 | -1.25 | 0.2109  |
| RMW | +1.1803 | +0.92 | 0.3591  |
| CMA | +2.4598 | +1.89 | 0.0596  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### CXAI

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.1652 (adjusted = 0.1553)
- Alpha (annualized): **-48.33%** (daily = -0.001918, t = -0.51, p = 0.6084)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.7845 | -1.97 | 0.0495 * |
| SMB | +4.2976 | +6.46 | 0.0000 *** |
| HML | -3.3715 | -5.52 | 0.0000 *** |
| RMW | -1.2533 | -1.63 | 0.1032  |
| CMA | +0.0916 | +0.12 | 0.9062  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### PR

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.3320 (adjusted = 0.3242)
- Alpha (annualized): **+6.20%** (daily = +0.000246, t = +0.25, p = 0.8041)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3774 | +13.05 | 0.0000 *** |
| SMB | +0.1346 | +0.76 | 0.4460  |
| HML | +0.7916 | +4.89 | 0.0000 *** |
| RMW | +0.3722 | +1.83 | 0.0679  |
| CMA | +0.2842 | +1.38 | 0.1684  |

_Interpretation: Value tilt_

### LGO

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.1571 (adjusted = 0.1472)
- Alpha (annualized): **-21.42%** (daily = -0.000850, t = -0.36, p = 0.7208)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3939 | +5.51 | 0.0000 *** |
| SMB | +0.4190 | +0.99 | 0.3225  |
| HML | +0.6417 | +1.65 | 0.0991  |
| RMW | -1.4512 | -2.98 | 0.0031 ** |
| CMA | -0.0306 | -0.06 | 0.9506  |

_Interpretation: Value tilt; Weak profitability; Modest factor fit_

### AMD

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.4881 (adjusted = 0.4821)
- Alpha (annualized): **+0.02%** (daily = +0.000001, t = +0.00, p = 0.9996)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5769 | +11.68 | 0.0000 *** |
| SMB | -0.6312 | -2.80 | 0.0054 ** |
| HML | -0.5311 | -2.56 | 0.0107 * |
| RMW | -1.7095 | -6.57 | 0.0000 *** |
| CMA | -0.0654 | -0.25 | 0.8042  |

_Interpretation: Large-cap tilt; Growth tilt; Weak profitability_

### AVGO

- Period: `2024-07-12` to `2026-03-31` (431 obs)
- R² = 0.4918 (adjusted = 0.4859)
- Alpha (annualized): **+45.07%** (daily = +0.001788, t = +1.49, p = 0.1373)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6979 | +13.27 | 0.0000 *** |
| SMB | -0.1835 | -0.86 | 0.3911  |
| HML | -1.3671 | -6.97 | 0.0000 *** |
| RMW | +0.0633 | +0.26 | 0.7975  |
| CMA | +0.1340 | +0.54 | 0.5916  |

_Interpretation: Growth tilt_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._