# Weekly Report — `all-stocks` — 2026-W24

Generated: 2026-06-14  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W24.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +39.95% | +2.031 | -0.442 | -0.121 | -0.881 | +0.410 | 0.396 | 449 | Weak profitability |
| MSFT | -13.84% | +0.887 | -0.259 | -0.405 | +0.140 | -0.493 | 0.523 | 449 | Neutral profile |
| NVDA | +15.94% | +1.742 | -0.830 | -1.210 | -0.284 | +1.561 | 0.680 | 449 | Large-cap tilt; Growth tilt; Conservative investment |
| SPCE | -83.96% | +0.920 | +2.193 | -0.813 | -2.004 | -0.294 | 0.296 | 449 | Small-cap tilt; Growth tilt; Weak profitability |
| DTE | +6.14% | +0.272 | -0.111 | +0.556 | -0.207 | +0.045 | 0.144 | 449 | Value tilt; Modest factor fit |
| TSLA | +35.10% | +2.312 | -0.113 | -0.152 | -0.117 | -0.963 | 0.446 | 449 | Aggressive investment |
| MRVL | +14.38% | +1.996 | -0.416 | -0.745 | -1.186 | +0.854 | 0.461 | 449 | Growth tilt; Weak profitability; Conservative investment |
| ASTS | +154.28% | +1.522 | +1.535 | -1.458 | -2.534 | -0.061 | 0.278 | 449 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| RKLB | +154.48% | +1.441 | +0.578 | -0.766 | -3.344 | -0.090 | 0.381 | 449 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| ORCL | +6.42% | +1.250 | -0.143 | -0.742 | -0.288 | -0.643 | 0.288 | 449 | Growth tilt; Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| ASTS | **73.33** | 16.67 | 23.33 | 33.33 | 0.304 | +0.221 | 0.8828 | 0.0541 | 199 |
| RKLB | **73.33** | 10.00 | 33.33 | 30.00 | 0.405 | +0.688 | 0.6821 | 0.0418 | 199 |
| MU | **70.00** | 20.00 | 30.00 | 20.00 | 0.289 | +0.523 | 0.5324 | 0.0326 | 199 |
| ORCL | **66.67** | 30.00 | 13.33 | 23.33 | 0.213 | -0.056 | 0.5755 | 0.0352 | 199 |
| SPCE | **63.33** | 26.67 | 10.00 | 26.67 | 0.273 | -0.066 | 0.6250 | 0.0383 | 199 |
| MRVL | **60.00** | 23.33 | 20.00 | 16.67 | 0.286 | +0.148 | 0.5067 | 0.0310 | 199 |
| DTE | **53.33** | 33.33 | 16.67 | 3.33 | 0.056 | +0.103 | 0.1527 | 0.0093 | 199 |
| NVDA | **40.00** | 3.33 | 26.67 | 10.00 | 0.606 | +0.394 | 0.2181 | 0.0134 | 199 |
| TSLA | **33.33** | 13.33 | 6.67 | 13.33 | 0.347 | -0.095 | 0.3692 | 0.0226 | 199 |
| MSFT | **16.67** | 6.67 | 3.33 | 6.67 | 0.424 | -0.442 | 0.1827 | 0.0112 | 199 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.3957 (adjusted = 0.3889)
- Alpha (annualized): **+39.95%** (daily = +0.001585, t = +1.08, p = 0.2807)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.0313 | +12.93 | 0.0000 *** |
| SMB | -0.4420 | -1.74 | 0.0823  |
| HML | -0.1208 | -0.50 | 0.6165  |
| RMW | -0.8808 | -2.92 | 0.0037 ** |
| CMA | +0.4104 | +1.35 | 0.1775  |

_Interpretation: Weak profitability_

### MSFT

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.5233 (adjusted = 0.5179)
- Alpha (annualized): **-13.84%** (daily = -0.000549, t = -1.08, p = 0.2824)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8866 | +16.23 | 0.0000 *** |
| SMB | -0.2593 | -2.94 | 0.0035 ** |
| HML | -0.4047 | -4.83 | 0.0000 *** |
| RMW | +0.1399 | +1.33 | 0.1834  |
| CMA | -0.4926 | -4.66 | 0.0000 *** |

_Interpretation: Neutral profile_

### NVDA

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.6802 (adjusted = 0.6766)
- Alpha (annualized): **+15.94%** (daily = +0.000632, t = +0.76, p = 0.4485)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7421 | +19.52 | 0.0000 *** |
| SMB | -0.8297 | -5.76 | 0.0000 *** |
| HML | -1.2100 | -8.84 | 0.0000 *** |
| RMW | -0.2836 | -1.65 | 0.0987  |
| CMA | +1.5610 | +9.05 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### SPCE

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.2964 (adjusted = 0.2885)
- Alpha (annualized): **-83.96%** (daily = -0.003332, t = -1.54, p = 0.1249)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9196 | +3.96 | 0.0001 *** |
| SMB | +2.1926 | +5.85 | 0.0000 *** |
| HML | -0.8133 | -2.28 | 0.0228 * |
| RMW | -2.0036 | -4.50 | 0.0000 *** |
| CMA | -0.2940 | -0.66 | 0.5126  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### DTE

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.1440 (adjusted = 0.1344)
- Alpha (annualized): **+6.14%** (daily = +0.000243, t = +0.51, p = 0.6115)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2723 | +5.31 | 0.0000 *** |
| SMB | -0.1112 | -1.34 | 0.1801  |
| HML | +0.5559 | +7.07 | 0.0000 *** |
| RMW | -0.2066 | -2.10 | 0.0365 * |
| CMA | +0.0452 | +0.46 | 0.6487  |

_Interpretation: Value tilt; Modest factor fit_

### TSLA

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.4458 (adjusted = 0.4396)
- Alpha (annualized): **+35.10%** (daily = +0.001393, t = +0.99, p = 0.3223)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.3124 | +15.37 | 0.0000 *** |
| SMB | -0.1126 | -0.46 | 0.6435  |
| HML | -0.1521 | -0.66 | 0.5103  |
| RMW | -0.1167 | -0.40 | 0.6866  |
| CMA | -0.9626 | -3.31 | 0.0010 ** |

_Interpretation: Aggressive investment_

### MRVL

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.4608 (adjusted = 0.4547)
- Alpha (annualized): **+14.38%** (daily = +0.000571, t = +0.39, p = 0.6946)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9961 | +12.84 | 0.0000 *** |
| SMB | -0.4164 | -1.66 | 0.0981  |
| HML | -0.7450 | -3.12 | 0.0019 ** |
| RMW | -1.1862 | -3.97 | 0.0001 *** |
| CMA | +0.8538 | +2.84 | 0.0047 ** |

_Interpretation: Growth tilt; Weak profitability; Conservative investment_

### ASTS

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.2781 (adjusted = 0.2699)
- Alpha (annualized): **+154.28%** (daily = +0.006122, t = +2.18, p = 0.0300)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5215 | +5.06 | 0.0000 *** |
| SMB | +1.5347 | +3.16 | 0.0017 ** |
| HML | -1.4579 | -3.16 | 0.0017 ** |
| RMW | -2.5336 | -4.38 | 0.0000 *** |
| CMA | -0.0609 | -0.10 | 0.9167  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### RKLB

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.3813 (adjusted = 0.3744)
- Alpha (annualized): **+154.48%** (daily = +0.006130, t = +2.90, p = 0.0039)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4410 | +6.36 | 0.0000 *** |
| SMB | +0.5778 | +1.58 | 0.1149  |
| HML | -0.7661 | -2.21 | 0.0279 * |
| RMW | -3.3439 | -7.69 | 0.0000 *** |
| CMA | -0.0901 | -0.21 | 0.8370  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### ORCL

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.2877 (adjusted = 0.2796)
- Alpha (annualized): **+6.42%** (daily = +0.000255, t = +0.19, p = 0.8496)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2501 | +8.71 | 0.0000 *** |
| SMB | -0.1432 | -0.62 | 0.5373  |
| HML | -0.7417 | -3.37 | 0.0008 *** |
| RMW | -0.2881 | -1.04 | 0.2969  |
| CMA | -0.6434 | -2.32 | 0.0210 * |

_Interpretation: Growth tilt; Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._