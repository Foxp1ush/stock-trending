# Weekly Report — `Shortsqueeze` — 2026-W46

Generated: 2026-11-09  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W46.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +66.18% | +1.071 | +2.183 | +0.893 | +0.258 | +0.071 | 0.099 | 347 | Small-cap tilt; Value tilt; Modest factor fit |
| ASTS | +132.66% | +1.391 | +1.127 | -1.131 | -2.808 | -0.510 | 0.323 | 347 | Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment |
| IQ | -42.22% | +1.098 | +0.339 | +0.189 | -0.495 | +0.055 | 0.162 | 347 | Modest factor fit |
| GME | +17.05% | +0.531 | +0.844 | -0.759 | -0.146 | +0.138 | 0.114 | 347 | Small-cap tilt; Growth tilt; Modest factor fit |
| API | +28.39% | +0.229 | +0.930 | -0.958 | -1.281 | +0.288 | 0.087 | 347 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| EU | -7.82% | +0.817 | +1.590 | -1.375 | -0.963 | -0.054 | 0.176 | 347 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| RDDT | +14.41% | +1.612 | -0.315 | -0.833 | -1.447 | -0.188 | 0.322 | 347 | Growth tilt; Weak profitability |
| YOU | +46.17% | +0.941 | +0.483 | +0.365 | +0.388 | -0.330 | 0.090 | 347 | Modest factor fit |
| PR | +19.03% | +1.434 | +0.131 | +0.956 | +0.239 | +0.343 | 0.350 | 347 | Value tilt |
| NBIS | +178.07% | +1.650 | +0.621 | -2.394 | -1.985 | +0.083 | 0.306 | 347 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| ASTS | **66.67** | 6.67 | 26.67 | 33.33 | 0.390 | +0.314 | 1.4655 | 0.0576 | 97 |
| EU | **66.67** | 13.33 | 30.00 | 23.33 | 0.331 | +1.155 | 1.0281 | 0.0404 | 97 |
| NBIS | **63.33** | 3.33 | 33.33 | 26.67 | 0.463 | +1.292 | 1.1791 | 0.0463 | 97 |
| YOU | **63.33** | 30.00 | 3.33 | 30.00 | 0.142 | -1.383 | 1.1795 | 0.0463 | 97 |
| API | **60.00** | 33.33 | 13.33 | 13.33 | 0.104 | -0.325 | 0.6701 | 0.0263 | 97 |
| IQ | **53.33** | 20.00 | 23.33 | 10.00 | 0.178 | +0.044 | 0.6601 | 0.0259 | 97 |
| GME | **50.00** | 26.67 | 16.67 | 6.67 | 0.156 | -0.233 | 0.5268 | 0.0207 | 97 |
| PR | **46.67** | 23.33 | 20.00 | 3.33 | 0.172 | -0.024 | 0.4274 | 0.0168 | 97 |
| RDDT | **43.33** | 16.67 | 6.67 | 20.00 | 0.301 | -1.139 | 0.8467 | 0.0333 | 97 |
| HTZ | **36.67** | 10.00 | 10.00 | 16.67 | 0.360 | -0.488 | 0.7726 | 0.0303 | 97 |

## Per-ticker FF5 Detail

### HTZ

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.0989 (adjusted = 0.0856)
- Alpha (annualized): **+66.18%** (daily = +0.002626, t = +0.79, p = 0.4312)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0715 | +3.10 | 0.0021 ** |
| SMB | +2.1831 | +3.59 | 0.0004 *** |
| HML | +0.8928 | +1.56 | 0.1187  |
| RMW | +0.2576 | +0.40 | 0.6901  |
| CMA | +0.0706 | +0.10 | 0.9216  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### ASTS

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.3235 (adjusted = 0.3136)
- Alpha (annualized): **+132.66%** (daily = +0.005264, t = +1.85, p = 0.0658)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3914 | +4.70 | 0.0000 *** |
| SMB | +1.1268 | +2.16 | 0.0312 * |
| HML | -1.1309 | -2.31 | 0.0212 * |
| RMW | -2.8085 | -5.08 | 0.0000 *** |
| CMA | -0.5104 | -0.83 | 0.4066  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment_

### IQ

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.1623 (adjusted = 0.1500)
- Alpha (annualized): **-42.22%** (daily = -0.001675, t = -0.94, p = 0.3492)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0977 | +5.92 | 0.0000 *** |
| SMB | +0.3390 | +1.04 | 0.2996  |
| HML | +0.1891 | +0.62 | 0.5371  |
| RMW | -0.4948 | -1.43 | 0.1540  |
| CMA | +0.0554 | +0.14 | 0.8857  |

_Interpretation: Modest factor fit_

### GME

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.1140 (adjusted = 0.1010)
- Alpha (annualized): **+17.05%** (daily = +0.000677, t = +0.38, p = 0.7007)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5309 | +2.91 | 0.0039 ** |
| SMB | +0.8436 | +2.63 | 0.0090 ** |
| HML | -0.7590 | -2.52 | 0.0122 * |
| RMW | -0.1462 | -0.43 | 0.6683  |
| CMA | +0.1384 | +0.37 | 0.7150  |

_Interpretation: Small-cap tilt; Growth tilt; Modest factor fit_

### API

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.0870 (adjusted = 0.0736)
- Alpha (annualized): **+28.39%** (daily = +0.001126, t = +0.40, p = 0.6868)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2292 | +0.79 | 0.4296  |
| SMB | +0.9304 | +1.83 | 0.0688  |
| HML | -0.9578 | -2.00 | 0.0459 * |
| RMW | -1.2808 | -2.37 | 0.0184 * |
| CMA | +0.2884 | +0.48 | 0.6316  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### EU

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.1761 (adjusted = 0.1641)
- Alpha (annualized): **-7.82%** (daily = -0.000310, t = -0.11, p = 0.9095)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8173 | +2.89 | 0.0042 ** |
| SMB | +1.5898 | +3.19 | 0.0015 ** |
| HML | -1.3749 | -2.94 | 0.0035 ** |
| RMW | -0.9630 | -1.82 | 0.0694  |
| CMA | -0.0539 | -0.09 | 0.9270  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### RDDT

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.3220 (adjusted = 0.3121)
- Alpha (annualized): **+14.41%** (daily = +0.000572, t = +0.27, p = 0.7894)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6118 | +7.25 | 0.0000 *** |
| SMB | -0.3153 | -0.81 | 0.4204  |
| HML | -0.8331 | -2.27 | 0.0237 * |
| RMW | -1.4472 | -3.49 | 0.0005 *** |
| CMA | -0.1882 | -0.41 | 0.6833  |

_Interpretation: Growth tilt; Weak profitability_

### YOU

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.0905 (adjusted = 0.0772)
- Alpha (annualized): **+46.17%** (daily = +0.001832, t = +1.03, p = 0.3035)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9411 | +5.10 | 0.0000 *** |
| SMB | +0.4828 | +1.49 | 0.1379  |
| HML | +0.3652 | +1.20 | 0.2313  |
| RMW | +0.3876 | +1.13 | 0.2613  |
| CMA | -0.3296 | -0.86 | 0.3900  |

_Interpretation: Modest factor fit_

### PR

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.3499 (adjusted = 0.3404)
- Alpha (annualized): **+19.03%** (daily = +0.000755, t = +0.67, p = 0.5050)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4345 | +12.21 | 0.0000 *** |
| SMB | +0.1305 | +0.63 | 0.5281  |
| HML | +0.9564 | +4.93 | 0.0000 *** |
| RMW | +0.2393 | +1.09 | 0.2760  |
| CMA | +0.3426 | +1.41 | 0.1607  |

_Interpretation: Value tilt_

### NBIS

- Period: `2024-11-08` to `2026-03-31` (347 obs)
- R² = 0.3064 (adjusted = 0.2963)
- Alpha (annualized): **+178.07%** (daily = +0.007066, t = +2.23, p = 0.0264)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6497 | +5.01 | 0.0000 *** |
| SMB | +0.6206 | +1.07 | 0.2842  |
| HML | -2.3945 | -4.41 | 0.0000 *** |
| RMW | -1.9853 | -3.23 | 0.0013 ** |
| CMA | +0.0827 | +0.12 | 0.9036  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._