# Weekly Report — `Shortsqueeze` — 2026-W47

Generated: 2026-11-16  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W47.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +45.94% | +1.050 | +2.392 | +0.795 | +0.264 | -0.001 | 0.105 | 342 | Small-cap tilt; Value tilt; Modest factor fit |
| GME | +4.24% | +0.525 | +0.775 | -0.836 | -0.122 | +0.299 | 0.116 | 342 | Small-cap tilt; Growth tilt; Modest factor fit |
| ALL | -5.98% | +0.706 | -0.280 | +0.884 | +0.300 | -0.091 | 0.227 | 342 | Value tilt |
| API | +8.13% | +0.238 | +0.603 | -0.785 | -1.415 | +0.694 | 0.096 | 342 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| ASTS | +115.38% | +1.366 | +1.239 | -1.248 | -2.758 | -0.474 | 0.331 | 342 | Small-cap tilt; Growth tilt; Weak profitability |
| AMD | +21.33% | +1.606 | -0.587 | -0.389 | -1.654 | -0.325 | 0.485 | 342 | Large-cap tilt; Weak profitability |
| AMC | -102.02% | +0.828 | +0.572 | -0.457 | -0.085 | +0.541 | 0.130 | 342 | Small-cap tilt; Conservative investment; Significant negative alpha; Modest factor fit |
| EU | -6.91% | +0.818 | +1.657 | -1.375 | -0.986 | -0.135 | 0.180 | 342 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| GL | +4.29% | +0.878 | -0.247 | +0.740 | +0.004 | +0.038 | 0.357 | 342 | Value tilt |
| GOOG | +40.24% | +0.997 | +0.154 | -0.573 | +0.470 | -0.688 | 0.451 | 342 | Growth tilt; Aggressive investment; Significant positive alpha |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| EU | **80.00** | 16.67 | 33.33 | 30.00 | 0.317 | +1.158 | 1.0800 | 0.0410 | 92 |
| ASTS | **70.00** | 10.00 | 26.67 | 33.33 | 0.410 | +0.325 | 1.5224 | 0.0578 | 92 |
| API | **63.33** | 33.33 | 10.00 | 20.00 | 0.106 | -0.328 | 0.7085 | 0.0269 | 92 |
| GME | **56.67** | 30.00 | 13.33 | 13.33 | 0.152 | -0.248 | 0.5569 | 0.0211 | 92 |
| AMC | **56.67** | 26.67 | 3.33 | 26.67 | 0.233 | -0.791 | 0.8054 | 0.0306 | 92 |
| AMD | **50.00** | 3.33 | 30.00 | 16.67 | 0.588 | +0.989 | 0.6324 | 0.0240 | 92 |
| ALL | **50.00** | 23.33 | 16.67 | 10.00 | 0.254 | -0.243 | 0.3305 | 0.0126 | 92 |
| HTZ | **43.33** | 13.33 | 6.67 | 23.33 | 0.348 | -0.493 | 0.8026 | 0.0305 | 92 |
| GL | **43.33** | 20.00 | 20.00 | 3.33 | 0.254 | -0.052 | 0.2540 | 0.0096 | 92 |
| GOOG | **36.67** | 6.67 | 23.33 | 6.67 | 0.473 | +0.121 | 0.3267 | 0.0124 | 92 |

## Per-ticker FF5 Detail

### HTZ

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.1054 (adjusted = 0.0921)
- Alpha (annualized): **+45.94%** (daily = +0.001823, t = +0.55, p = 0.5859)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0498 | +3.04 | 0.0025 ** |
| SMB | +2.3918 | +3.88 | 0.0001 *** |
| HML | +0.7948 | +1.39 | 0.1658  |
| RMW | +0.2638 | +0.41 | 0.6826  |
| CMA | -0.0011 | -0.00 | 0.9988  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### GME

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.1160 (adjusted = 0.1028)
- Alpha (annualized): **+4.24%** (daily = +0.000168, t = +0.10, p = 0.9235)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5251 | +2.91 | 0.0039 ** |
| SMB | +0.7754 | +2.40 | 0.0167 * |
| HML | -0.8363 | -2.79 | 0.0055 ** |
| RMW | -0.1225 | -0.36 | 0.7168  |
| CMA | +0.2993 | +0.79 | 0.4298  |

_Interpretation: Small-cap tilt; Growth tilt; Modest factor fit_

### ALL

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.2273 (adjusted = 0.2158)
- Alpha (annualized): **-5.98%** (daily = -0.000237, t = -0.31, p = 0.7603)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7058 | +8.80 | 0.0000 *** |
| SMB | -0.2805 | -1.96 | 0.0510  |
| HML | +0.8843 | +6.65 | 0.0000 *** |
| RMW | +0.2995 | +2.00 | 0.0464 * |
| CMA | -0.0914 | -0.54 | 0.5870  |

_Interpretation: Value tilt_

### API

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.0964 (adjusted = 0.0830)
- Alpha (annualized): **+8.13%** (daily = +0.000323, t = +0.13, p = 0.8972)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2382 | +0.93 | 0.3553  |
| SMB | +0.6026 | +1.31 | 0.1906  |
| HML | -0.7853 | -1.84 | 0.0667  |
| RMW | -1.4148 | -2.94 | 0.0035 ** |
| CMA | +0.6939 | +1.29 | 0.1994  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### ASTS

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.3315 (adjusted = 0.3215)
- Alpha (annualized): **+115.38%** (daily = +0.004578, t = +1.61, p = 0.1073)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3659 | +4.67 | 0.0000 *** |
| SMB | +1.2385 | +2.37 | 0.0183 * |
| HML | -1.2484 | -2.57 | 0.0105 * |
| RMW | -2.7581 | -5.04 | 0.0000 *** |
| CMA | -0.4740 | -0.77 | 0.4404  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

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

### AMC

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.1297 (adjusted = 0.1168)
- Alpha (annualized): **-102.02%** (daily = -0.004048, t = -2.27, p = 0.0236)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8276 | +4.50 | 0.0000 *** |
| SMB | +0.5721 | +1.74 | 0.0821  |
| HML | -0.4570 | -1.50 | 0.1347  |
| RMW | -0.0851 | -0.25 | 0.8044  |
| CMA | +0.5414 | +1.41 | 0.1609  |

_Interpretation: Small-cap tilt; Conservative investment; Significant negative alpha; Modest factor fit_

### EU

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.1798 (adjusted = 0.1676)
- Alpha (annualized): **-6.91%** (daily = -0.000274, t = -0.10, p = 0.9207)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8185 | +2.88 | 0.0042 ** |
| SMB | +1.6567 | +3.27 | 0.0012 ** |
| HML | -1.3747 | -2.92 | 0.0038 ** |
| RMW | -0.9863 | -1.86 | 0.0640  |
| CMA | -0.1354 | -0.23 | 0.8204  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### GL

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.3572 (adjusted = 0.3477)
- Alpha (annualized): **+4.29%** (daily = +0.000170, t = +0.26, p = 0.7976)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8784 | +12.84 | 0.0000 *** |
| SMB | -0.2468 | -2.02 | 0.0442 * |
| HML | +0.7395 | +6.52 | 0.0000 *** |
| RMW | +0.0041 | +0.03 | 0.9747  |
| CMA | +0.0376 | +0.26 | 0.7934  |

_Interpretation: Value tilt_

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

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._