# Weekly Report — `pennystocks` — 2026-W34

Generated: 2026-08-23  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W34.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **9 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| CAST | — | — | — | — | — | — | — | — | _insufficient_data_ |
| CXAI | -73.43% | -0.997 | +4.255 | -3.005 | -1.170 | -0.859 | 0.189 | 401 | Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Modest factor fit |
| MMA | -36.16% | +0.458 | +0.519 | -0.634 | -0.557 | -0.112 | 0.014 | 401 | Small-cap tilt; Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven |
| MSS | -26.58% | +0.217 | +0.337 | -0.963 | -1.296 | +1.487 | 0.028 | 401 | Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| YJ | +16.78% | -0.410 | +0.596 | -1.145 | +0.328 | -0.237 | 0.018 | 401 | Small-cap tilt; Growth tilt; Low explanatory power — likely sentiment-driven |
| RS | -3.18% | +0.914 | +0.681 | +0.530 | +0.353 | +0.307 | 0.450 | 401 | Small-cap tilt; Value tilt |
| FEMY | -13.03% | +0.511 | +0.834 | -0.692 | -1.464 | +0.614 | 0.064 | 401 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| AMZN | +4.56% | +1.332 | +0.026 | -0.370 | +0.289 | -0.509 | 0.555 | 401 | Aggressive investment |
| AAPL | +1.73% | +1.331 | -0.111 | -0.063 | +0.751 | +0.168 | 0.539 | 401 | Robust profitability |
| ALL | -2.22% | +0.687 | -0.245 | +0.776 | +0.313 | -0.116 | 0.217 | 401 | Value tilt |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| MSS | **92.59** | 33.33 | 33.33 | 25.93 | 0.049 | +0.250 | 1.3931 | 0.0714 | 151 |
| FEMY | **70.37** | 29.63 | 7.41 | 33.33 | 0.065 | -0.823 | 1.7859 | 0.0916 | 151 |
| MMA | **66.67** | 22.22 | 14.81 | 29.63 | 0.071 | -0.728 | 1.6486 | 0.0845 | 151 |
| YJ | **55.56** | 25.93 | 11.11 | 18.52 | 0.070 | -0.757 | 0.9640 | 0.0494 | 151 |
| ALL | **48.15** | 14.81 | 22.22 | 11.11 | 0.220 | -0.238 | 0.2463 | 0.0126 | 151 |
| AAPL | **48.15** | 11.11 | 29.63 | 7.41 | 0.318 | +0.087 | 0.2263 | 0.0116 | 151 |
| CXAI | **44.44** | 18.52 | 3.70 | 22.22 | 0.217 | -1.167 | 1.1791 | 0.0604 | 151 |
| RS | **37.04** | 7.41 | 25.93 | 3.70 | 0.360 | +0.077 | 0.2125 | 0.0109 | 151 |
| AMZN | **37.04** | 3.70 | 18.52 | 14.81 | 0.419 | -0.463 | 0.2903 | 0.0149 | 151 |

## Per-ticker FF5 Detail

### CAST

Status: `insufficient_data` — only 15 overlapping days after factor join


### CXAI

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.1891 (adjusted = 0.1788)
- Alpha (annualized): **-73.43%** (daily = -0.002914, t = -0.87, p = 0.3842)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.9966 | -2.81 | 0.0053 ** |
| SMB | +4.2553 | +7.04 | 0.0000 *** |
| HML | -3.0054 | -5.47 | 0.0000 *** |
| RMW | -1.1703 | -1.74 | 0.0833  |
| CMA | -0.8591 | -1.21 | 0.2262  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Modest factor fit_

### MMA

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.0137 (adjusted = 0.0012)
- Alpha (annualized): **-36.16%** (daily = -0.001435, t = -0.30, p = 0.7633)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.4584 | +0.91 | 0.3651  |
| SMB | +0.5186 | +0.60 | 0.5471  |
| HML | -0.6337 | -0.81 | 0.4185  |
| RMW | -0.5569 | -0.58 | 0.5620  |
| CMA | -0.1125 | -0.11 | 0.9113  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

### MSS

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.0277 (adjusted = 0.0154)
- Alpha (annualized): **-26.58%** (daily = -0.001055, t = -0.24, p = 0.8104)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2171 | +0.47 | 0.6419  |
| SMB | +0.3368 | +0.42 | 0.6715  |
| HML | -0.9633 | -1.33 | 0.1827  |
| RMW | -1.2962 | -1.46 | 0.1439  |
| CMA | +1.4869 | +1.60 | 0.1109  |

_Interpretation: Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### YJ

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.0182 (adjusted = 0.0057)
- Alpha (annualized): **+16.78%** (daily = +0.000666, t = +0.24, p = 0.8108)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.4102 | -1.39 | 0.1655  |
| SMB | +0.5955 | +1.19 | 0.2367  |
| HML | -1.1446 | -2.51 | 0.0126 * |
| RMW | +0.3280 | +0.59 | 0.5586  |
| CMA | -0.2372 | -0.40 | 0.6874  |

_Interpretation: Small-cap tilt; Growth tilt; Low explanatory power — likely sentiment-driven_

### RS

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.4501 (adjusted = 0.4432)
- Alpha (annualized): **-3.18%** (daily = -0.000126, t = -0.20, p = 0.8449)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9139 | +13.37 | 0.0000 *** |
| SMB | +0.6814 | +5.86 | 0.0000 *** |
| HML | +0.5304 | +5.01 | 0.0000 *** |
| RMW | +0.3530 | +2.72 | 0.0068 ** |
| CMA | +0.3074 | +2.25 | 0.0247 * |

_Interpretation: Small-cap tilt; Value tilt_

### FEMY

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.0641 (adjusted = 0.0523)
- Alpha (annualized): **-13.03%** (daily = -0.000517, t = -0.16, p = 0.8763)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5107 | +1.45 | 0.1481  |
| SMB | +0.8337 | +1.39 | 0.1654  |
| HML | -0.6920 | -1.27 | 0.2052  |
| RMW | -1.4642 | -2.19 | 0.0292 * |
| CMA | +0.6141 | +0.87 | 0.3830  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### AMZN

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.5548 (adjusted = 0.5492)
- Alpha (annualized): **+4.56%** (daily = +0.000181, t = +0.26, p = 0.7956)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3320 | +17.98 | 0.0000 *** |
| SMB | +0.0256 | +0.20 | 0.8392  |
| HML | -0.3696 | -3.23 | 0.0014 ** |
| RMW | +0.2894 | +2.06 | 0.0402 * |
| CMA | -0.5093 | -3.45 | 0.0006 *** |

_Interpretation: Aggressive investment_

### AAPL

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.5387 (adjusted = 0.5328)
- Alpha (annualized): **+1.73%** (daily = +0.000069, t = +0.11, p = 0.9122)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3307 | +20.10 | 0.0000 *** |
| SMB | -0.1108 | -0.98 | 0.3258  |
| HML | -0.0634 | -0.62 | 0.5364  |
| RMW | +0.7512 | +5.98 | 0.0000 *** |
| CMA | +0.1684 | +1.28 | 0.2030  |

_Interpretation: Robust profitability_

### ALL

- Period: `2024-08-23` to `2026-03-31` (401 obs)
- R² = 0.2175 (adjusted = 0.2075)
- Alpha (annualized): **-2.22%** (daily = -0.000088, t = -0.13, p = 0.8999)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6869 | +9.25 | 0.0000 *** |
| SMB | -0.2453 | -1.94 | 0.0529  |
| HML | +0.7764 | +6.76 | 0.0000 *** |
| RMW | +0.3135 | +2.23 | 0.0266 * |
| CMA | -0.1155 | -0.78 | 0.4359  |

_Interpretation: Value tilt_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._