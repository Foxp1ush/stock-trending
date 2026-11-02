# Weekly Report — `all-stocks` — 2026-W45

Generated: 2026-11-02  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W45.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| GOOG | +36.24% | +1.018 | +0.148 | -0.505 | +0.462 | -0.718 | 0.449 | 352 | Growth tilt; Aggressive investment |
| RDDT | +16.01% | +1.619 | -0.364 | -0.891 | -1.449 | -0.158 | 0.321 | 352 | Growth tilt; Weak profitability |
| GOOGL | +37.47% | +1.027 | +0.142 | -0.519 | +0.488 | -0.734 | 0.443 | 352 | Growth tilt; Aggressive investment |
| MSFT | -10.19% | +0.861 | -0.303 | -0.434 | +0.136 | -0.444 | 0.506 | 352 | Neutral profile |
| MU | +80.63% | +1.982 | -0.288 | -0.116 | -0.951 | +0.159 | 0.403 | 352 | Weak profitability |
| INTC | +27.92% | +1.545 | -0.418 | +1.284 | -1.769 | +0.417 | 0.281 | 352 | Value tilt; Weak profitability |
| NVDA | +19.49% | +1.644 | -0.826 | -1.110 | -0.298 | +1.090 | 0.661 | 352 | Large-cap tilt; Growth tilt; Conservative investment |
| AMZN | +3.29% | +1.327 | +0.067 | -0.368 | +0.313 | -0.459 | 0.554 | 352 | Neutral profile |
| TSLA | +18.77% | +2.211 | +0.051 | +0.121 | -0.344 | -1.192 | 0.494 | 352 | Aggressive investment |
| AMD | +13.11% | +1.603 | -0.601 | -0.375 | -1.647 | -0.303 | 0.481 | 352 | Large-cap tilt; Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| MU | **96.67** | 30.00 | 33.33 | 33.33 | 0.386 | +1.116 | 0.8787 | 0.0359 | 102 |
| INTC | **83.33** | 26.67 | 26.67 | 30.00 | 0.392 | +0.908 | 0.8341 | 0.0341 | 102 |
| RDDT | **63.33** | 33.33 | 3.33 | 26.67 | 0.313 | -1.134 | 0.8284 | 0.0339 | 102 |
| AMD | **60.00** | 6.67 | 30.00 | 23.33 | 0.564 | +1.000 | 0.6181 | 0.0253 | 102 |
| TSLA | **56.67** | 23.33 | 13.33 | 20.00 | 0.466 | +0.062 | 0.4485 | 0.0183 | 102 |
| GOOGL | **53.33** | 20.00 | 16.67 | 16.67 | 0.466 | +0.159 | 0.3184 | 0.0130 | 102 |
| GOOG | **40.00** | 16.67 | 20.00 | 3.33 | 0.473 | +0.164 | 0.3097 | 0.0127 | 102 |
| AMZN | **33.33** | 10.00 | 10.00 | 13.33 | 0.521 | -0.398 | 0.3148 | 0.0129 | 102 |
| NVDA | **33.33** | 3.33 | 23.33 | 6.67 | 0.701 | +0.667 | 0.3101 | 0.0127 | 102 |
| MSFT | **30.00** | 13.33 | 6.67 | 10.00 | 0.481 | -0.714 | 0.3131 | 0.0128 | 102 |

## Per-ticker FF5 Detail

### GOOG

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.4491 (adjusted = 0.4411)
- Alpha (annualized): **+36.24%** (daily = +0.001438, t = +1.84, p = 0.0669)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0180 | +12.75 | 0.0000 *** |
| SMB | +0.1479 | +1.04 | 0.2981  |
| HML | -0.5046 | -4.01 | 0.0001 *** |
| RMW | +0.4616 | +3.03 | 0.0026 ** |
| CMA | -0.7184 | -4.36 | 0.0000 *** |

_Interpretation: Growth tilt; Aggressive investment_

### RDDT

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.3211 (adjusted = 0.3113)
- Alpha (annualized): **+16.01%** (daily = +0.000635, t = +0.30, p = 0.7670)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6187 | +7.40 | 0.0000 *** |
| SMB | -0.3644 | -0.94 | 0.3494  |
| HML | -0.8909 | -2.58 | 0.0102 * |
| RMW | -1.4489 | -3.47 | 0.0006 *** |
| CMA | -0.1582 | -0.35 | 0.7264  |

_Interpretation: Growth tilt; Weak profitability_

### GOOGL

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.4433 (adjusted = 0.4352)
- Alpha (annualized): **+37.47%** (daily = +0.001487, t = +1.86, p = 0.0635)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0267 | +12.59 | 0.0000 *** |
| SMB | +0.1420 | +0.98 | 0.3277  |
| HML | -0.5185 | -4.03 | 0.0001 *** |
| RMW | +0.4878 | +3.14 | 0.0018 ** |
| CMA | -0.7339 | -4.36 | 0.0000 *** |

_Interpretation: Growth tilt; Aggressive investment_

### MSFT

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.5062 (adjusted = 0.4990)
- Alpha (annualized): **-10.19%** (daily = -0.000405, t = -0.66, p = 0.5086)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8612 | +13.80 | 0.0000 *** |
| SMB | -0.3027 | -2.73 | 0.0067 ** |
| HML | -0.4338 | -4.41 | 0.0000 *** |
| RMW | +0.1355 | +1.14 | 0.2552  |
| CMA | -0.4445 | -3.45 | 0.0006 *** |

_Interpretation: Neutral profile_

### MU

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.4034 (adjusted = 0.3947)
- Alpha (annualized): **+80.63%** (daily = +0.003200, t = +1.89, p = 0.0597)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9820 | +11.47 | 0.0000 *** |
| SMB | -0.2877 | -0.94 | 0.3498  |
| HML | -0.1159 | -0.43 | 0.6709  |
| RMW | -0.9509 | -2.89 | 0.0041 ** |
| CMA | +0.1590 | +0.45 | 0.6563  |

_Interpretation: Weak profitability_

### INTC

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.2815 (adjusted = 0.2711)
- Alpha (annualized): **+27.92%** (daily = +0.001108, t = +0.59, p = 0.5561)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5449 | +8.05 | 0.0000 *** |
| SMB | -0.4181 | -1.23 | 0.2211  |
| HML | +1.2839 | +4.24 | 0.0000 *** |
| RMW | -1.7687 | -4.84 | 0.0000 *** |
| CMA | +0.4172 | +1.05 | 0.2931  |

_Interpretation: Value tilt; Weak profitability_

### NVDA

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.6605 (adjusted = 0.6556)
- Alpha (annualized): **+19.49%** (daily = +0.000774, t = +0.85, p = 0.3984)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6441 | +17.61 | 0.0000 *** |
| SMB | -0.8256 | -4.97 | 0.0000 *** |
| HML | -1.1104 | -7.54 | 0.0000 *** |
| RMW | -0.2983 | -1.68 | 0.0947  |
| CMA | +1.0895 | +5.65 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### AMZN

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.5538 (adjusted = 0.5473)
- Alpha (annualized): **+3.29%** (daily = +0.000131, t = +0.17, p = 0.8651)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3269 | +16.94 | 0.0000 *** |
| SMB | +0.0672 | +0.48 | 0.6298  |
| HML | -0.3684 | -2.98 | 0.0031 ** |
| RMW | +0.3128 | +2.10 | 0.0369 * |
| CMA | -0.4586 | -2.84 | 0.0048 ** |

_Interpretation: Neutral profile_

### TSLA

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.4940 (adjusted = 0.4867)
- Alpha (annualized): **+18.77%** (daily = +0.000745, t = +0.50, p = 0.6152)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2109 | +14.63 | 0.0000 *** |
| SMB | +0.0514 | +0.19 | 0.8483  |
| HML | +0.1210 | +0.51 | 0.6120  |
| RMW | -0.3437 | -1.19 | 0.2337  |
| CMA | -1.1916 | -3.82 | 0.0002 *** |

_Interpretation: Aggressive investment_

### AMD

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.4812 (adjusted = 0.4737)
- Alpha (annualized): **+13.11%** (daily = +0.000520, t = +0.36, p = 0.7189)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6028 | +10.88 | 0.0000 *** |
| SMB | -0.6010 | -2.29 | 0.0224 * |
| HML | -0.3745 | -1.61 | 0.1079  |
| RMW | -1.6473 | -5.86 | 0.0000 *** |
| CMA | -0.3026 | -0.99 | 0.3207  |

_Interpretation: Large-cap tilt; Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._