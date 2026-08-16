# Weekly Report — `pennystocks` — 2026-W33

Generated: 2026-08-16  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W33.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| NXXT | -89.72% | +0.707 | -0.224 | +1.067 | -1.480 | +0.526 | 0.033 | 406 | Value tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| HTZ | +47.67% | +1.023 | +2.142 | +0.598 | +0.383 | +0.351 | 0.104 | 406 | Small-cap tilt; Value tilt; Modest factor fit |
| CXAI | -69.23% | -1.005 | +4.327 | -3.101 | -1.182 | -0.807 | 0.196 | 406 | Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Modest factor fit |
| CAPR | +317.06% | +0.269 | +2.964 | -0.867 | -3.060 | +1.554 | 0.029 | 406 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| RS | -3.87% | +0.911 | +0.697 | +0.508 | +0.371 | +0.297 | 0.448 | 406 | Small-cap tilt; Value tilt |
| SBS | +25.47% | +0.539 | +0.048 | +0.393 | -0.190 | -0.246 | 0.097 | 406 | Modest factor fit |
| ONDS | +216.37% | +1.576 | +1.469 | -0.590 | -2.351 | -1.076 | 0.165 | 406 | Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Significant positive alpha; Modest factor fit |
| BYND | -36.02% | +0.980 | +0.813 | +0.246 | -1.277 | +1.885 | 0.029 | 406 | Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| OTLK | -113.42% | +0.364 | +1.484 | -1.476 | -0.172 | -0.112 | 0.039 | 406 | Small-cap tilt; Growth tilt; Low explanatory power — likely sentiment-driven |
| SURG | -17.08% | +0.578 | +1.074 | -0.201 | -0.638 | -0.471 | 0.041 | 406 | Small-cap tilt; Weak profitability; Low explanatory power — likely sentiment-driven |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| BYND | **70.00** | 33.33 | 6.67 | 30.00 | 0.047 | -2.550 | 3.3766 | 0.1773 | 156 |
| OTLK | **66.67** | 26.67 | 13.33 | 26.67 | 0.059 | -1.399 | 1.7685 | 0.0929 | 156 |
| CAPR | **66.67** | 30.00 | 3.33 | 33.33 | 0.052 | -3.937 | 5.6024 | 0.2942 | 156 |
| SURG | **63.33** | 23.33 | 26.67 | 13.33 | 0.099 | +0.465 | 0.9873 | 0.0518 | 156 |
| ONDS | **60.00** | 6.67 | 33.33 | 20.00 | 0.299 | +1.051 | 1.3029 | 0.0684 | 156 |
| HTZ | **53.33** | 20.00 | 23.33 | 10.00 | 0.119 | +0.090 | 0.8662 | 0.0455 | 156 |
| SBS | **50.00** | 13.33 | 30.00 | 6.67 | 0.208 | +0.530 | 0.3597 | 0.0189 | 156 |
| NXXT | **50.00** | 16.67 | 10.00 | 23.33 | 0.159 | -1.575 | 1.4957 | 0.0785 | 156 |
| CXAI | **43.33** | 10.00 | 16.67 | 16.67 | 0.226 | -1.196 | 1.1330 | 0.0595 | 156 |
| RS | **26.67** | 3.33 | 20.00 | 3.33 | 0.379 | +0.067 | 0.2051 | 0.0108 | 156 |

## Per-ticker FF5 Detail

### NXXT

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.0327 (adjusted = 0.0207)
- Alpha (annualized): **-89.72%** (daily = -0.003560, t = -1.00, p = 0.3167)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7074 | +1.87 | 0.0628  |
| SMB | -0.2244 | -0.35 | 0.7269  |
| HML | +1.0668 | +1.83 | 0.0673  |
| RMW | -1.4796 | -2.07 | 0.0395 * |
| CMA | +0.5259 | +0.70 | 0.4849  |

_Interpretation: Value tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### HTZ

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.1036 (adjusted = 0.0924)
- Alpha (annualized): **+47.67%** (daily = +0.001892, t = +0.64, p = 0.5224)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0232 | +3.24 | 0.0013 ** |
| SMB | +2.1423 | +4.01 | 0.0001 *** |
| HML | +0.5982 | +1.24 | 0.2170  |
| RMW | +0.3825 | +0.64 | 0.5212  |
| CMA | +0.3506 | +0.56 | 0.5757  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### CXAI

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.1963 (adjusted = 0.1862)
- Alpha (annualized): **-69.23%** (daily = -0.002747, t = -0.83, p = 0.4079)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -1.0049 | -2.84 | 0.0048 ** |
| SMB | +4.3268 | +7.21 | 0.0000 *** |
| HML | -3.1010 | -5.71 | 0.0000 *** |
| RMW | -1.1818 | -1.77 | 0.0780  |
| CMA | -0.8067 | -1.15 | 0.2515  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Modest factor fit_

### CAPR

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.0290 (adjusted = 0.0169)
- Alpha (annualized): **+317.06%** (daily = +0.012582, t = +1.27, p = 0.2044)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2689 | +0.25 | 0.7993  |
| SMB | +2.9636 | +1.66 | 0.0986  |
| HML | -0.8666 | -0.53 | 0.5931  |
| RMW | -3.0605 | -1.53 | 0.1260  |
| CMA | +1.5544 | +0.74 | 0.4589  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### RS

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.4480 (adjusted = 0.4411)
- Alpha (annualized): **-3.87%** (daily = -0.000154, t = -0.24, p = 0.8100)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9114 | +13.37 | 0.0000 *** |
| SMB | +0.6967 | +6.03 | 0.0000 *** |
| HML | +0.5075 | +4.85 | 0.0000 *** |
| RMW | +0.3713 | +2.88 | 0.0041 ** |
| CMA | +0.2971 | +2.20 | 0.0286 * |

_Interpretation: Small-cap tilt; Value tilt_

### SBS

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.0968 (adjusted = 0.0855)
- Alpha (annualized): **+25.47%** (daily = +0.001011, t = +1.04, p = 0.2971)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5391 | +5.22 | 0.0000 *** |
| SMB | +0.0483 | +0.28 | 0.7827  |
| HML | +0.3934 | +2.48 | 0.0135 * |
| RMW | -0.1903 | -0.97 | 0.3303  |
| CMA | -0.2459 | -1.20 | 0.2311  |

_Interpretation: Modest factor fit_

### ONDS

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.1651 (adjusted = 0.1547)
- Alpha (annualized): **+216.37%** (daily = +0.008586, t = +2.25, p = 0.0252)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5759 | +3.86 | 0.0001 *** |
| SMB | +1.4686 | +2.12 | 0.0342 * |
| HML | -0.5905 | -0.94 | 0.3459  |
| RMW | -2.3509 | -3.05 | 0.0024 ** |
| CMA | -1.0758 | -1.33 | 0.1846  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Significant positive alpha; Modest factor fit_

### BYND

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.0293 (adjusted = 0.0172)
- Alpha (annualized): **-36.02%** (daily = -0.001429, t = -0.25, p = 0.8050)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9798 | +1.59 | 0.1136  |
| SMB | +0.8129 | +0.78 | 0.4378  |
| HML | +0.2459 | +0.26 | 0.7954  |
| RMW | -1.2772 | -1.09 | 0.2744  |
| CMA | +1.8854 | +1.54 | 0.1248  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### OTLK

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.0392 (adjusted = 0.0272)
- Alpha (annualized): **-113.42%** (daily = -0.004501, t = -1.16, p = 0.2480)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3636 | +0.88 | 0.3819  |
| SMB | +1.4839 | +2.11 | 0.0356 * |
| HML | -1.4759 | -2.32 | 0.0210 * |
| RMW | -0.1716 | -0.22 | 0.8270  |
| CMA | -0.1117 | -0.14 | 0.8923  |

_Interpretation: Small-cap tilt; Growth tilt; Low explanatory power — likely sentiment-driven_

### SURG

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.0406 (adjusted = 0.0286)
- Alpha (annualized): **-17.08%** (daily = -0.000678, t = -0.21, p = 0.8361)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5777 | +1.65 | 0.0992  |
| SMB | +1.0742 | +1.81 | 0.0704  |
| HML | -0.2007 | -0.37 | 0.7084  |
| RMW | -0.6375 | -0.97 | 0.3349  |
| CMA | -0.4711 | -0.68 | 0.4974  |

_Interpretation: Small-cap tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._