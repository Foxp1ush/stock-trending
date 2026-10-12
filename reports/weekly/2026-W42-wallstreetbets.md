# Weekly Report — `wallstreetbets` — 2026-W42

Generated: 2026-10-12  ·  Source: `apewisdom:wallstreetbets`  ·  Lookback: 7 days

[← Back to dashboard](2026-W42.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +74.75% | +1.996 | -0.279 | -0.132 | -0.914 | +0.178 | 0.404 | 367 | Weak profitability |
| NVDA | +20.50% | +1.657 | -0.834 | -1.101 | -0.299 | +1.121 | 0.664 | 367 | Large-cap tilt; Growth tilt; Conservative investment |
| ASTS | +109.46% | +1.310 | +1.024 | -1.181 | -2.937 | -0.204 | 0.313 | 367 | Small-cap tilt; Growth tilt; Weak profitability |
| AMD | +4.87% | +1.595 | -0.612 | -0.412 | -1.663 | -0.277 | 0.475 | 367 | Large-cap tilt; Weak profitability |
| APLD | +141.44% | +1.346 | +1.163 | -2.127 | -2.799 | -0.839 | 0.269 | 367 | Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment |
| DTE | +1.72% | +0.296 | -0.214 | +0.565 | -0.249 | +0.118 | 0.156 | 367 | Value tilt; Modest factor fit |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| MSFT | -9.95% | +0.877 | -0.303 | -0.421 | +0.137 | -0.473 | 0.503 | 367 | Neutral profile |
| HTZ | +55.53% | +1.035 | +2.082 | +0.641 | +0.339 | +0.288 | 0.098 | 367 | Small-cap tilt; Value tilt; Modest factor fit |
| BULL | +66.63% | +1.011 | +0.027 | +1.512 | -3.188 | +0.274 | 0.016 | 367 | Value tilt; Weak profitability; Low explanatory power — likely sentiment-driven |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **93.33** | 26.67 | 33.33 | 33.33 | 0.348 | +2.660 | 1.3083 | 0.0595 | 117 |
| MU | **70.00** | 23.33 | 26.67 | 20.00 | 0.377 | +1.191 | 0.7654 | 0.0348 | 117 |
| HTZ | **66.67** | 30.00 | 10.00 | 26.67 | 0.108 | -0.201 | 1.0600 | 0.0482 | 117 |
| ASTS | **66.67** | 20.00 | 16.67 | 30.00 | 0.385 | +0.417 | 1.2294 | 0.0559 | 117 |
| APLD | **60.00** | 6.67 | 30.00 | 23.33 | 0.562 | +2.034 | 1.0232 | 0.0466 | 117 |
| DTE | **50.00** | 33.33 | 13.33 | 3.33 | 0.069 | +0.041 | 0.2148 | 0.0098 | 117 |
| AMD | **50.00** | 10.00 | 23.33 | 16.67 | 0.559 | +0.981 | 0.5563 | 0.0253 | 117 |
| BULL | **33.33** | 13.33 | 6.67 | 13.33 | 0.555 | -0.359 | 0.5090 | 0.0232 | 117 |
| NVDA | **30.00** | 3.33 | 20.00 | 6.67 | 0.709 | +0.676 | 0.2753 | 0.0125 | 117 |
| MSFT | **30.00** | 16.67 | 3.33 | 10.00 | 0.454 | -0.665 | 0.2778 | 0.0126 | 117 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.4045 (adjusted = 0.3962)
- Alpha (annualized): **+74.75%** (daily = +0.002966, t = +1.81, p = 0.0708)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9959 | +11.77 | 0.0000 *** |
| SMB | -0.2794 | -0.94 | 0.3496  |
| HML | -0.1319 | -0.50 | 0.6194  |
| RMW | -0.9141 | -2.83 | 0.0050 ** |
| CMA | +0.1782 | +0.51 | 0.6088  |

_Interpretation: Weak profitability_

### NVDA

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.6639 (adjusted = 0.6593)
- Alpha (annualized): **+20.50%** (daily = +0.000813, t = +0.92, p = 0.3592)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6566 | +18.05 | 0.0000 *** |
| SMB | -0.8343 | -5.17 | 0.0000 *** |
| HML | -1.1007 | -7.66 | 0.0000 *** |
| RMW | -0.2993 | -1.71 | 0.0880  |
| CMA | +1.1209 | +5.95 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### ASTS

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.3131 (adjusted = 0.3036)
- Alpha (annualized): **+109.46%** (daily = +0.004344, t = +1.57, p = 0.1172)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3102 | +4.57 | 0.0000 *** |
| SMB | +1.0236 | +2.03 | 0.0430 * |
| HML | -1.1808 | -2.63 | 0.0088 ** |
| RMW | -2.9371 | -5.38 | 0.0000 *** |
| CMA | -0.2043 | -0.35 | 0.7283  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### AMD

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.4746 (adjusted = 0.4674)
- Alpha (annualized): **+4.87%** (daily = +0.000193, t = +0.14, p = 0.8918)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5954 | +10.84 | 0.0000 *** |
| SMB | -0.6121 | -2.36 | 0.0186 * |
| HML | -0.4118 | -1.79 | 0.0747  |
| RMW | -1.6632 | -5.93 | 0.0000 *** |
| CMA | -0.2771 | -0.92 | 0.3593  |

_Interpretation: Large-cap tilt; Weak profitability_

### APLD

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.2687 (adjusted = 0.2586)
- Alpha (annualized): **+141.44%** (daily = +0.005613, t = +1.60, p = 0.1107)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3464 | +3.70 | 0.0002 *** |
| SMB | +1.1629 | +1.82 | 0.0698  |
| HML | -2.1265 | -3.74 | 0.0002 *** |
| RMW | -2.7986 | -4.04 | 0.0001 *** |
| CMA | -0.8388 | -1.12 | 0.2614  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment_

### DTE

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.1560 (adjusted = 0.1443)
- Alpha (annualized): **+1.72%** (daily = +0.000068, t = +0.13, p = 0.8979)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2958 | +5.38 | 0.0000 *** |
| SMB | -0.2142 | -2.21 | 0.0274 * |
| HML | +0.5650 | +6.57 | 0.0000 *** |
| RMW | -0.2488 | -2.37 | 0.0181 * |
| CMA | +0.1176 | +1.04 | 0.2975  |

_Interpretation: Value tilt; Modest factor fit_

### SNDK

- Period: `2025-02-14` to `2026-03-31` (282 obs)
- R² = 0.2490 (adjusted = 0.2354)
- Alpha (annualized): **+277.05%** (daily = +0.010994, t = +3.31, p = 0.0011)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.3574 | +7.20 | 0.0000 *** |
| SMB | -0.0193 | -0.03 | 0.9748  |
| HML | +0.8466 | +1.41 | 0.1591  |
| RMW | -1.2601 | -1.98 | 0.0485 * |
| CMA | -1.2831 | -1.62 | 0.1062  |

_Interpretation: Value tilt; Weak profitability; Aggressive investment; Significant positive alpha_

### MSFT

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.5033 (adjusted = 0.4964)
- Alpha (annualized): **-9.95%** (daily = -0.000395, t = -0.66, p = 0.5123)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8768 | +14.05 | 0.0000 *** |
| SMB | -0.3030 | -2.76 | 0.0061 ** |
| HML | -0.4210 | -4.31 | 0.0000 *** |
| RMW | +0.1370 | +1.15 | 0.2499  |
| CMA | -0.4730 | -3.70 | 0.0003 *** |

_Interpretation: Neutral profile_

### HTZ

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.0985 (adjusted = 0.0860)
- Alpha (annualized): **+55.53%** (daily = +0.002204, t = +0.69, p = 0.4897)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0353 | +3.14 | 0.0019 ** |
| SMB | +2.0815 | +3.58 | 0.0004 *** |
| HML | +0.6405 | +1.24 | 0.2159  |
| RMW | +0.3386 | +0.54 | 0.5909  |
| CMA | +0.2878 | +0.43 | 0.6710  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### BULL

- Period: `2024-10-11` to `2026-03-31` (367 obs)
- R² = 0.0156 (adjusted = 0.0020)
- Alpha (annualized): **+66.63%** (daily = +0.002644, t = +0.25, p = 0.8027)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0112 | +0.92 | 0.3565  |
| SMB | +0.0266 | +0.01 | 0.9890  |
| HML | +1.5120 | +0.88 | 0.3784  |
| RMW | -3.1884 | -1.53 | 0.1276  |
| CMA | +0.2740 | +0.12 | 0.9030  |

_Interpretation: Value tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._