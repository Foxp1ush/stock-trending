# Weekly Report — `pennystocks` — 2026-W32

Generated: 2026-08-09  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W32.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +44.58% | +1.016 | +2.235 | +0.557 | +0.397 | +0.358 | 0.108 | 411 | Small-cap tilt; Value tilt; Modest factor fit |
| WU | -12.28% | +0.712 | +0.578 | +0.223 | +0.518 | +0.320 | 0.227 | 411 | Small-cap tilt; Robust profitability |
| NVDA | +20.74% | +1.679 | -0.833 | -1.152 | -0.352 | +1.421 | 0.677 | 411 | Large-cap tilt; Growth tilt; Conservative investment |
| DFNS | +503.81% | -2.229 | -0.700 | -3.235 | -1.531 | +2.742 | 0.005 | 411 | Large-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| RS | -5.42% | +0.908 | +0.704 | +0.510 | +0.370 | +0.288 | 0.450 | 411 | Small-cap tilt; Value tilt |
| GCTS | -40.11% | +0.951 | +0.446 | -0.784 | -0.450 | +0.431 | 0.086 | 411 | Growth tilt; Modest factor fit |
| AMD | +6.53% | +1.610 | -0.554 | -0.477 | -1.661 | -0.172 | 0.487 | 411 | Large-cap tilt; Weak profitability |
| CXAI | -34.56% | -0.806 | +4.507 | -3.399 | -1.202 | +0.034 | 0.164 | 411 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| IVVD | +138.05% | +0.386 | +0.747 | -0.096 | -3.179 | -0.268 | 0.032 | 411 | Small-cap tilt; Weak profitability; Low explanatory power — likely sentiment-driven |
| MVIS | +0.63% | +1.073 | +1.468 | -0.996 | -1.729 | +0.560 | 0.211 | 411 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| IVVD | **86.67** | 33.33 | 20.00 | 33.33 | 0.091 | +0.203 | 1.7831 | 0.0962 | 161 |
| GCTS | **83.33** | 30.00 | 33.33 | 20.00 | 0.116 | +1.613 | 0.8118 | 0.0438 | 161 |
| HTZ | **66.67** | 26.67 | 16.67 | 23.33 | 0.117 | +0.168 | 0.8338 | 0.0450 | 161 |
| MVIS | **60.00** | 13.33 | 30.00 | 16.67 | 0.319 | +0.662 | 0.7654 | 0.0413 | 161 |
| DFNS | **60.00** | 23.33 | 6.67 | 30.00 | 0.146 | -0.977 | 1.5691 | 0.0846 | 161 |
| AMD | **46.67** | 6.67 | 26.67 | 13.33 | 0.482 | +0.597 | 0.5428 | 0.0293 | 161 |
| CXAI | **46.67** | 16.67 | 3.33 | 26.67 | 0.219 | -1.050 | 1.0924 | 0.0589 | 161 |
| WU | **40.00** | 20.00 | 10.00 | 10.00 | 0.167 | -0.528 | 0.3232 | 0.0174 | 161 |
| NVDA | **33.33** | 3.33 | 23.33 | 6.67 | 0.665 | +0.554 | 0.2368 | 0.0128 | 161 |
| RS | **26.67** | 10.00 | 13.33 | 3.33 | 0.393 | +0.061 | 0.1979 | 0.0107 | 161 |

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

### WU

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.2272 (adjusted = 0.2176)
- Alpha (annualized): **-12.28%** (daily = -0.000487, t = -0.60, p = 0.5457)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7125 | +8.26 | 0.0000 *** |
| SMB | +0.5776 | +3.98 | 0.0001 *** |
| HML | +0.2226 | +1.69 | 0.0926  |
| RMW | +0.5176 | +3.17 | 0.0016 ** |
| CMA | +0.3202 | +1.88 | 0.0602  |

_Interpretation: Small-cap tilt; Robust profitability_

### NVDA

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.6771 (adjusted = 0.6731)
- Alpha (annualized): **+20.74%** (daily = +0.000823, t = +0.99, p = 0.3248)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6790 | +18.79 | 0.0000 *** |
| SMB | -0.8330 | -5.55 | 0.0000 *** |
| HML | -1.1523 | -8.42 | 0.0000 *** |
| RMW | -0.3521 | -2.08 | 0.0380 * |
| CMA | +1.4208 | +8.07 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### DFNS

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.0054 (adjusted = -0.0069)
- Alpha (annualized): **+503.81%** (daily = +0.019992, t = +0.96, p = 0.3355)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -2.2294 | -1.00 | 0.3157  |
| SMB | -0.6999 | -0.19 | 0.8513  |
| HML | -3.2353 | -0.95 | 0.3416  |
| RMW | -1.5306 | -0.36 | 0.7158  |
| CMA | +2.7425 | +0.63 | 0.5308  |

_Interpretation: Large-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### RS

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.4498 (adjusted = 0.4430)
- Alpha (annualized): **-5.42%** (daily = -0.000215, t = -0.34, p = 0.7338)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9075 | +13.42 | 0.0000 *** |
| SMB | +0.7038 | +6.19 | 0.0000 *** |
| HML | +0.5099 | +4.93 | 0.0000 *** |
| RMW | +0.3705 | +2.89 | 0.0040 ** |
| CMA | +0.2877 | +2.16 | 0.0314 * |

_Interpretation: Small-cap tilt; Value tilt_

### GCTS

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.0863 (adjusted = 0.0750)
- Alpha (annualized): **-40.11%** (daily = -0.001592, t = -0.62, p = 0.5349)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9512 | +3.47 | 0.0006 *** |
| SMB | +0.4455 | +0.97 | 0.3345  |
| HML | -0.7843 | -1.87 | 0.0625  |
| RMW | -0.4497 | -0.87 | 0.3870  |
| CMA | +0.4310 | +0.80 | 0.4256  |

_Interpretation: Growth tilt; Modest factor fit_

### AMD

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.4873 (adjusted = 0.4810)
- Alpha (annualized): **+6.53%** (daily = +0.000259, t = +0.20, p = 0.8415)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6105 | +11.63 | 0.0000 *** |
| SMB | -0.5541 | -2.38 | 0.0178 * |
| HML | -0.4766 | -2.25 | 0.0252 * |
| RMW | -1.6609 | -6.33 | 0.0000 *** |
| CMA | -0.1720 | -0.63 | 0.5289  |

_Interpretation: Large-cap tilt; Weak profitability_

### CXAI

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.1639 (adjusted = 0.1536)
- Alpha (annualized): **-34.56%** (daily = -0.001371, t = -0.35, p = 0.7263)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.8059 | -1.92 | 0.0552  |
| SMB | +4.5073 | +6.40 | 0.0000 *** |
| HML | -3.3993 | -5.30 | 0.0000 *** |
| RMW | -1.2018 | -1.51 | 0.1306  |
| CMA | +0.0342 | +0.04 | 0.9670  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### IVVD

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.0317 (adjusted = 0.0197)
- Alpha (annualized): **+138.05%** (daily = +0.005478, t = +0.82, p = 0.4148)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3861 | +0.54 | 0.5913  |
| SMB | +0.7469 | +0.62 | 0.5366  |
| HML | -0.0956 | -0.09 | 0.9308  |
| RMW | -3.1793 | -2.34 | 0.0199 * |
| CMA | -0.2685 | -0.19 | 0.8496  |

_Interpretation: Small-cap tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

### MVIS

- Period: `2024-08-09` to `2026-03-31` (411 obs)
- R² = 0.2114 (adjusted = 0.2017)
- Alpha (annualized): **+0.63%** (daily = +0.000025, t = +0.01, p = 0.9922)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0726 | +3.90 | 0.0001 *** |
| SMB | +1.4681 | +3.18 | 0.0016 ** |
| HML | -0.9956 | -2.37 | 0.0184 * |
| RMW | -1.7291 | -3.32 | 0.0010 *** |
| CMA | +0.5604 | +1.04 | 0.3013  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._