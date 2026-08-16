# Weekly Report — `Shortsqueeze` — 2026-W33

Generated: 2026-08-16  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W33.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +47.67% | +1.023 | +2.142 | +0.598 | +0.383 | +0.351 | 0.104 | 406 | Small-cap tilt; Value tilt; Modest factor fit |
| ONDS | +216.37% | +1.576 | +1.469 | -0.590 | -2.351 | -1.076 | 0.165 | 406 | Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Significant positive alpha; Modest factor fit |
| WEN | -50.97% | +0.591 | +0.782 | +0.208 | +0.374 | +0.858 | 0.194 | 406 | Small-cap tilt; Conservative investment; Significant negative alpha; Modest factor fit |
| AMZN | +4.02% | +1.332 | +0.028 | -0.375 | +0.292 | -0.509 | 0.556 | 406 | Aggressive investment |
| BC | -4.10% | +1.490 | +1.796 | +0.307 | +0.761 | +0.666 | 0.638 | 406 | Small-cap tilt; Robust profitability; Conservative investment |
| AMC | -99.10% | +0.827 | +0.624 | -0.231 | -0.148 | +0.293 | 0.126 | 406 | Small-cap tilt; Significant negative alpha; Modest factor fit |
| CAPR | +317.06% | +0.269 | +2.964 | -0.867 | -3.060 | +1.554 | 0.029 | 406 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| ES | -1.05% | +0.377 | -0.073 | +0.451 | -0.120 | +0.310 | 0.092 | 406 | Modest factor fit |
| AMD | +7.08% | +1.616 | -0.576 | -0.464 | -1.662 | -0.178 | 0.486 | 406 | Large-cap tilt; Weak profitability |
| IBKR | +26.52% | +1.610 | -0.480 | +0.526 | -0.997 | -0.142 | 0.525 | 406 | Value tilt; Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| ONDS | **80.00** | 16.67 | 33.33 | 30.00 | 0.299 | +1.051 | 1.3029 | 0.0684 | 156 |
| HTZ | **76.67** | 26.67 | 23.33 | 26.67 | 0.119 | +0.090 | 0.8662 | 0.0455 | 156 |
| CAPR | **70.00** | 33.33 | 3.33 | 33.33 | 0.052 | -3.937 | 5.6024 | 0.2942 | 156 |
| AMD | **63.33** | 10.00 | 30.00 | 23.33 | 0.494 | +0.669 | 0.5556 | 0.0292 | 156 |
| ES | **60.00** | 30.00 | 16.67 | 13.33 | 0.060 | -0.185 | 0.3174 | 0.0167 | 156 |
| AMC | **53.33** | 23.33 | 10.00 | 20.00 | 0.169 | -0.609 | 0.5526 | 0.0290 | 156 |
| WEN | **43.33** | 20.00 | 6.67 | 16.67 | 0.294 | -0.970 | 0.4186 | 0.0220 | 156 |
| BC | **36.67** | 6.67 | 20.00 | 10.00 | 0.559 | -0.089 | 0.3096 | 0.0163 | 156 |
| IBKR | **36.67** | 3.33 | 26.67 | 6.67 | 0.568 | +0.196 | 0.3035 | 0.0159 | 156 |
| AMZN | **30.00** | 13.33 | 13.33 | 3.33 | 0.432 | -0.473 | 0.2797 | 0.0147 | 156 |

## Per-ticker FF5 Detail

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

### WEN

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.1937 (adjusted = 0.1837)
- Alpha (annualized): **-50.97%** (daily = -0.002022, t = -1.99, p = 0.0473)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5910 | +5.44 | 0.0000 *** |
| SMB | +0.7824 | +4.26 | 0.0000 *** |
| HML | +0.2075 | +1.25 | 0.2132  |
| RMW | +0.3744 | +1.83 | 0.0686  |
| CMA | +0.8578 | +3.98 | 0.0001 *** |

_Interpretation: Small-cap tilt; Conservative investment; Significant negative alpha; Modest factor fit_

### AMZN

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.5561 (adjusted = 0.5505)
- Alpha (annualized): **+4.02%** (daily = +0.000159, t = +0.23, p = 0.8172)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3320 | +18.09 | 0.0000 *** |
| SMB | +0.0278 | +0.22 | 0.8236  |
| HML | -0.3750 | -3.32 | 0.0010 *** |
| RMW | +0.2918 | +2.10 | 0.0365 * |
| CMA | -0.5087 | -3.48 | 0.0006 *** |

_Interpretation: Aggressive investment_

### BC

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.6375 (adjusted = 0.6330)
- Alpha (annualized): **-4.10%** (daily = -0.000163, t = -0.20, p = 0.8384)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4899 | +17.52 | 0.0000 *** |
| SMB | +1.7964 | +12.47 | 0.0000 *** |
| HML | +0.3073 | +2.36 | 0.0189 * |
| RMW | +0.7612 | +4.74 | 0.0000 *** |
| CMA | +0.6660 | +3.95 | 0.0001 *** |

_Interpretation: Small-cap tilt; Robust profitability; Conservative investment_

### AMC

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.1257 (adjusted = 0.1147)
- Alpha (annualized): **-99.10%** (daily = -0.003933, t = -2.51, p = 0.0125)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8272 | +4.95 | 0.0000 *** |
| SMB | +0.6242 | +2.20 | 0.0282 * |
| HML | -0.2308 | -0.90 | 0.3688  |
| RMW | -0.1476 | -0.47 | 0.6407  |
| CMA | +0.2932 | +0.88 | 0.3775  |

_Interpretation: Small-cap tilt; Significant negative alpha; Modest factor fit_

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

### ES

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.0921 (adjusted = 0.0807)
- Alpha (annualized): **-1.05%** (daily = -0.000042, t = -0.06, p = 0.9556)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3768 | +4.70 | 0.0000 *** |
| SMB | -0.0733 | -0.54 | 0.5903  |
| HML | +0.4509 | +3.66 | 0.0003 *** |
| RMW | -0.1202 | -0.79 | 0.4284  |
| CMA | +0.3096 | +1.94 | 0.0525  |

_Interpretation: Modest factor fit_

### AMD

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.4860 (adjusted = 0.4795)
- Alpha (annualized): **+7.08%** (daily = +0.000281, t = +0.21, p = 0.8299)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6158 | +11.58 | 0.0000 *** |
| SMB | -0.5765 | -2.44 | 0.0152 * |
| HML | -0.4638 | -2.17 | 0.0308 * |
| RMW | -1.6623 | -6.31 | 0.0000 *** |
| CMA | -0.1783 | -0.64 | 0.5200  |

_Interpretation: Large-cap tilt; Weak profitability_

### IBKR

- Period: `2024-08-16` to `2026-03-31` (406 obs)
- R² = 0.5252 (adjusted = 0.5193)
- Alpha (annualized): **+26.52%** (daily = +0.001052, t = +1.14, p = 0.2530)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6095 | +16.40 | 0.0000 *** |
| SMB | -0.4801 | -2.89 | 0.0041 ** |
| HML | +0.5259 | +3.49 | 0.0005 *** |
| RMW | -0.9974 | -5.38 | 0.0000 *** |
| CMA | -0.1424 | -0.73 | 0.4652  |

_Interpretation: Value tilt; Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._