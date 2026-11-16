# Weekly Report — `all-stocks` — 2026-W47

Generated: 2026-11-16  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W47.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| NVDA | +18.25% | +1.551 | -0.919 | -1.365 | -0.330 | +1.304 | 0.681 | 342 | Large-cap tilt; Growth tilt; Conservative investment |
| AMD | +21.33% | +1.606 | -0.587 | -0.389 | -1.654 | -0.325 | 0.485 | 342 | Large-cap tilt; Weak profitability |
| NBIS | +186.14% | +1.656 | +0.559 | -2.431 | -1.960 | +0.106 | 0.307 | 342 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| MSFT | -10.65% | +0.839 | -0.286 | -0.495 | +0.127 | -0.430 | 0.510 | 342 | Neutral profile |
| CRWV | +106.86% | +2.051 | +0.880 | -1.356 | -0.298 | -2.178 | 0.214 | 252 | Small-cap tilt; Growth tilt; Aggressive investment |
| MU | +89.05% | +1.976 | -0.354 | -0.122 | -0.987 | +0.164 | 0.404 | 342 | Weak profitability; Significant positive alpha |
| DTE | +5.89% | +0.336 | -0.199 | +0.567 | -0.200 | +0.082 | 0.165 | 342 | Value tilt; Modest factor fit |
| GOOG | +40.24% | +0.997 | +0.154 | -0.573 | +0.470 | -0.688 | 0.451 | 342 | Growth tilt; Aggressive investment; Significant positive alpha |
| GOOGL | +41.54% | +1.007 | +0.149 | -0.582 | +0.496 | -0.707 | 0.445 | 342 | Growth tilt; Aggressive investment; Significant positive alpha |
| TSLA | +11.78% | +2.126 | -0.171 | -0.067 | -0.362 | -0.826 | 0.486 | 342 | Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| CRWV | **93.33** | 26.67 | 33.33 | 33.33 | 0.433 | +1.463 | 1.2528 | 0.0476 | 92 |
| MU | **83.33** | 30.00 | 26.67 | 26.67 | 0.378 | +1.015 | 0.9441 | 0.0359 | 92 |
| NBIS | **70.00** | 10.00 | 30.00 | 30.00 | 0.506 | +1.238 | 1.1706 | 0.0445 | 92 |
| AMD | **53.33** | 6.67 | 23.33 | 23.33 | 0.588 | +0.989 | 0.6324 | 0.0240 | 92 |
| TSLA | **50.00** | 23.33 | 6.67 | 20.00 | 0.434 | -0.040 | 0.4638 | 0.0176 | 92 |
| GOOGL | **46.67** | 20.00 | 13.33 | 13.33 | 0.463 | +0.114 | 0.3363 | 0.0128 | 92 |
| DTE | **46.67** | 33.33 | 10.00 | 3.33 | 0.067 | +0.036 | 0.2604 | 0.0099 | 92 |
| MSFT | **36.67** | 16.67 | 3.33 | 16.67 | 0.469 | -0.712 | 0.3507 | 0.0133 | 92 |
| GOOG | **36.67** | 13.33 | 16.67 | 6.67 | 0.473 | +0.121 | 0.3267 | 0.0124 | 92 |
| NVDA | **33.33** | 3.33 | 20.00 | 10.00 | 0.672 | +0.666 | 0.3344 | 0.0127 | 92 |

## Per-ticker FF5 Detail

### NVDA

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.6812 (adjusted = 0.6764)
- Alpha (annualized): **+18.25%** (daily = +0.000724, t = +0.80, p = 0.4252)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5513 | +16.58 | 0.0000 *** |
| SMB | -0.9188 | -5.50 | 0.0000 *** |
| HML | -1.3655 | -8.80 | 0.0000 *** |
| RMW | -0.3303 | -1.89 | 0.0598  |
| CMA | +1.3037 | +6.64 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### AMD

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.4849 (adjusted = 0.4773)
- Alpha (annualized): **+21.33%** (daily = +0.000847, t = +0.57, p = 0.5667)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6064 | +10.55 | 0.0000 *** |
| SMB | -0.5865 | -2.16 | 0.0318 * |
| HML | -0.3886 | -1.54 | 0.1250  |
| RMW | -1.6535 | -5.81 | 0.0000 *** |
| CMA | -0.3247 | -1.02 | 0.3101  |

_Interpretation: Large-cap tilt; Weak profitability_

### NBIS

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.3068 (adjusted = 0.2965)
- Alpha (annualized): **+186.14%** (daily = +0.007386, t = +2.31, p = 0.0215)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6559 | +5.02 | 0.0000 *** |
| SMB | +0.5593 | +0.95 | 0.3434  |
| HML | -2.4306 | -4.44 | 0.0000 *** |
| RMW | -1.9599 | -3.18 | 0.0016 ** |
| CMA | +0.1058 | +0.15 | 0.8786  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### MSFT

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.5104 (adjusted = 0.5031)
- Alpha (annualized): **-10.65%** (daily = -0.000423, t = -0.68, p = 0.4981)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8386 | +13.04 | 0.0000 *** |
| SMB | -0.2859 | -2.49 | 0.0133 * |
| HML | -0.4947 | -4.64 | 0.0000 *** |
| RMW | +0.1265 | +1.05 | 0.2931  |
| CMA | -0.4304 | -3.19 | 0.0015 ** |

_Interpretation: Neutral profile_

### CRWV

- Period: `2025-03-31` to `2026-03-31` (252 obs)
- R² = 0.2140 (adjusted = 0.1981)
- Alpha (annualized): **+106.86%** (daily = +0.004241, t = +0.99, p = 0.3214)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.0513 | +4.87 | 0.0000 *** |
| SMB | +0.8804 | +1.10 | 0.2704  |
| HML | -1.3559 | -1.62 | 0.1060  |
| RMW | -0.2978 | -0.35 | 0.7255  |
| CMA | -2.1775 | -1.99 | 0.0472 * |

_Interpretation: Small-cap tilt; Growth tilt; Aggressive investment_

### MU

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.4045 (adjusted = 0.3956)
- Alpha (annualized): **+89.05%** (daily = +0.003534, t = +2.05, p = 0.0416)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9759 | +11.08 | 0.0000 *** |
| SMB | -0.3539 | -1.11 | 0.2670  |
| HML | -0.1219 | -0.41 | 0.6803  |
| RMW | -0.9870 | -2.96 | 0.0033 ** |
| CMA | +0.1644 | +0.44 | 0.6604  |

_Interpretation: Weak profitability; Significant positive alpha_

### DTE

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.1653 (adjusted = 0.1529)
- Alpha (annualized): **+5.89%** (daily = +0.000234, t = +0.44, p = 0.6629)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3363 | +6.08 | 0.0000 *** |
| SMB | -0.1992 | -2.02 | 0.0443 * |
| HML | +0.5666 | +6.18 | 0.0000 *** |
| RMW | -0.2003 | -1.94 | 0.0533  |
| CMA | +0.0821 | +0.71 | 0.4792  |

_Interpretation: Value tilt; Modest factor fit_

### GOOG

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.4507 (adjusted = 0.4426)
- Alpha (annualized): **+40.24%** (daily = +0.001597, t = +2.01, p = 0.0455)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9970 | +12.15 | 0.0000 *** |
| SMB | +0.1540 | +1.05 | 0.2941  |
| HML | -0.5731 | -4.21 | 0.0000 *** |
| RMW | +0.4703 | +3.07 | 0.0023 ** |
| CMA | -0.6881 | -4.00 | 0.0001 *** |

_Interpretation: Growth tilt; Aggressive investment; Significant positive alpha_

### GOOGL

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.4447 (adjusted = 0.4364)
- Alpha (annualized): **+41.54%** (daily = +0.001648, t = +2.03, p = 0.0432)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0068 | +12.01 | 0.0000 *** |
| SMB | +0.1485 | +0.99 | 0.3217  |
| HML | -0.5821 | -4.19 | 0.0000 *** |
| RMW | +0.4964 | +3.17 | 0.0017 ** |
| CMA | -0.7068 | -4.02 | 0.0001 *** |

_Interpretation: Growth tilt; Aggressive investment; Significant positive alpha_

### TSLA

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.4856 (adjusted = 0.4780)
- Alpha (annualized): **+11.78%** (daily = +0.000468, t = +0.32, p = 0.7505)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.1256 | +14.02 | 0.0000 *** |
| SMB | -0.1710 | -0.63 | 0.5280  |
| HML | -0.0671 | -0.27 | 0.7898  |
| RMW | -0.3623 | -1.28 | 0.2018  |
| CMA | -0.8257 | -2.60 | 0.0098 ** |

_Interpretation: Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._