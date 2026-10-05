# Weekly Report — `pennystocks` — 2026-W41

Generated: 2026-10-05  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W41.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **9 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| GLND | — | — | — | — | — | — | — | — | _insufficient_data_ |
| SLND | -45.69% | +1.003 | +1.176 | +1.025 | +0.138 | +0.846 | 0.079 | 372 | Small-cap tilt; Value tilt; Conservative investment; Modest factor fit |
| KALA | -90.21% | +1.203 | +0.737 | +0.269 | -0.452 | -0.278 | 0.035 | 372 | Small-cap tilt; Low explanatory power — likely sentiment-driven |
| ABAT | +120.44% | +0.945 | +0.754 | -0.086 | -3.509 | +0.219 | 0.120 | 372 | Small-cap tilt; Weak profitability; Modest factor fit |
| FFAI | -76.33% | +0.982 | +1.586 | -1.119 | -1.403 | +1.503 | 0.078 | 372 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| RS | -3.21% | +0.912 | +0.689 | +0.583 | +0.353 | +0.278 | 0.457 | 372 | Small-cap tilt; Value tilt |
| FLNA | -112.71% | +0.401 | +1.244 | +0.470 | -2.700 | +1.759 | 0.106 | 372 | Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit |
| WBUY | +86.73% | -0.198 | +0.582 | -0.687 | -3.299 | -0.094 | 0.020 | 372 | Small-cap tilt; Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven |
| AVGO | +50.39% | +1.612 | -0.113 | -1.279 | +0.116 | -0.250 | 0.459 | 372 | Growth tilt |
| AAPL | +3.91% | +1.350 | -0.152 | -0.053 | +0.767 | +0.172 | 0.551 | 372 | Robust profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| KALA | **85.19** | 29.63 | 25.93 | 29.63 | 0.057 | +0.470 | 1.8395 | 0.0859 | 122 |
| WBUY | **74.07** | 33.33 | 7.41 | 33.33 | 0.044 | -0.521 | 2.7044 | 0.1262 | 122 |
| ABAT | **74.07** | 18.52 | 33.33 | 22.22 | 0.299 | +1.142 | 1.6914 | 0.0789 | 122 |
| SLND | **55.56** | 25.93 | 3.70 | 25.93 | 0.163 | -3.032 | 1.7252 | 0.0805 | 122 |
| FFAI | **51.85** | 22.22 | 11.11 | 18.52 | 0.220 | -0.396 | 1.2186 | 0.0569 | 122 |
| FLNA | **48.15** | 11.11 | 22.22 | 14.81 | 0.375 | +0.166 | 0.9516 | 0.0444 | 122 |
| AVGO | **44.44** | 3.70 | 29.63 | 11.11 | 0.586 | +0.542 | 0.4056 | 0.0189 | 122 |
| RS | **40.74** | 14.81 | 18.52 | 7.41 | 0.355 | +0.097 | 0.2448 | 0.0114 | 122 |
| AAPL | **25.93** | 7.41 | 14.81 | 3.70 | 0.396 | +0.070 | 0.2270 | 0.0106 | 122 |

## Per-ticker FF5 Detail

### GLND

Status: `insufficient_data` — only 6 overlapping days after factor join


### SLND

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.0791 (adjusted = 0.0665)
- Alpha (annualized): **-45.69%** (daily = -0.001813, t = -0.59, p = 0.5528)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0034 | +3.17 | 0.0017 ** |
| SMB | +1.1762 | +2.11 | 0.0357 * |
| HML | +1.0254 | +2.06 | 0.0397 * |
| RMW | +0.1384 | +0.23 | 0.8194  |
| CMA | +0.8458 | +1.30 | 0.1931  |

_Interpretation: Small-cap tilt; Value tilt; Conservative investment; Modest factor fit_

### KALA

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.0348 (adjusted = 0.0217)
- Alpha (annualized): **-90.21%** (daily = -0.003580, t = -0.78, p = 0.4360)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2032 | +2.52 | 0.0121 * |
| SMB | +0.7373 | +0.88 | 0.3801  |
| HML | +0.2688 | +0.36 | 0.7192  |
| RMW | -0.4518 | -0.50 | 0.6203  |
| CMA | -0.2785 | -0.29 | 0.7755  |

_Interpretation: Small-cap tilt; Low explanatory power — likely sentiment-driven_

### ABAT

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.1199 (adjusted = 0.1079)
- Alpha (annualized): **+120.44%** (daily = +0.004779, t = +1.10, p = 0.2737)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9454 | +2.09 | 0.0375 * |
| SMB | +0.7542 | +0.95 | 0.3445  |
| HML | -0.0864 | -0.12 | 0.9031  |
| RMW | -3.5087 | -4.05 | 0.0001 *** |
| CMA | +0.2192 | +0.24 | 0.8132  |

_Interpretation: Small-cap tilt; Weak profitability; Modest factor fit_

### FFAI

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.0782 (adjusted = 0.0656)
- Alpha (annualized): **-76.33%** (daily = -0.003029, t = -0.66, p = 0.5110)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9819 | +2.05 | 0.0408 * |
| SMB | +1.5860 | +1.88 | 0.0603  |
| HML | -1.1190 | -1.49 | 0.1362  |
| RMW | -1.4029 | -1.53 | 0.1257  |
| CMA | +1.5029 | +1.54 | 0.1255  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### RS

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.4571 (adjusted = 0.4497)
- Alpha (annualized): **-3.21%** (daily = -0.000127, t = -0.19, p = 0.8493)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9117 | +13.10 | 0.0000 *** |
| SMB | +0.6893 | +5.63 | 0.0000 *** |
| HML | +0.5834 | +5.35 | 0.0000 *** |
| RMW | +0.3525 | +2.65 | 0.0084 ** |
| CMA | +0.2784 | +1.95 | 0.0514  |

_Interpretation: Small-cap tilt; Value tilt_

### FLNA

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.1059 (adjusted = 0.0937)
- Alpha (annualized): **-112.71%** (daily = -0.004473, t = -1.22, p = 0.2221)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.4014 | +1.06 | 0.2913  |
| SMB | +1.2437 | +1.86 | 0.0635  |
| HML | +0.4698 | +0.79 | 0.4303  |
| RMW | -2.6999 | -3.72 | 0.0002 *** |
| CMA | +1.7593 | +2.26 | 0.0242 * |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit_

### WBUY

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.0195 (adjusted = 0.0061)
- Alpha (annualized): **+86.73%** (daily = +0.003442, t = +0.39, p = 0.6934)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.1976 | -0.22 | 0.8275  |
| SMB | +0.5819 | +0.37 | 0.7153  |
| HML | -0.6873 | -0.48 | 0.6285  |
| RMW | -3.2992 | -1.91 | 0.0575  |
| CMA | -0.0935 | -0.05 | 0.9598  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

### AVGO

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.4593 (adjusted = 0.4519)
- Alpha (annualized): **+50.39%** (daily = +0.002000, t = +1.52, p = 0.1284)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6119 | +11.83 | 0.0000 *** |
| SMB | -0.1125 | -0.47 | 0.6391  |
| HML | -1.2790 | -5.99 | 0.0000 *** |
| RMW | +0.1163 | +0.45 | 0.6556  |
| CMA | -0.2501 | -0.90 | 0.3704  |

_Interpretation: Growth tilt_

### AAPL

- Period: `2024-10-04` to `2026-03-31` (372 obs)
- R² = 0.5512 (adjusted = 0.5451)
- Alpha (annualized): **+3.91%** (daily = +0.000155, t = +0.24, p = 0.8117)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3495 | +19.99 | 0.0000 *** |
| SMB | -0.1519 | -1.28 | 0.2017  |
| HML | -0.0526 | -0.50 | 0.6189  |
| RMW | +0.7671 | +5.95 | 0.0000 *** |
| CMA | +0.1720 | +1.24 | 0.2139  |

_Interpretation: Robust profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._