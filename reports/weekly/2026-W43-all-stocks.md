# Weekly Report — `all-stocks` — 2026-W43

Generated: 2026-10-25  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W43.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MU | +77.43% | +1.983 | -0.312 | -0.138 | -0.953 | +0.174 | 0.405 | 357 | Weak profitability |
| TSLA | +18.03% | +2.207 | +0.024 | +0.107 | -0.327 | -1.187 | 0.491 | 357 | Aggressive investment |
| META | +1.24% | +1.379 | -0.018 | -0.560 | +0.432 | -0.508 | 0.506 | 357 | Growth tilt; Aggressive investment |
| CRWV | +106.86% | +2.051 | +0.880 | -1.356 | -0.298 | -2.178 | 0.214 | 252 | Small-cap tilt; Growth tilt; Aggressive investment |
| NFLX | +9.53% | +0.717 | -0.827 | -0.165 | -0.600 | +0.185 | 0.256 | 357 | Large-cap tilt; Weak profitability |
| NBIS | +176.79% | +1.641 | +0.721 | -2.233 | -2.018 | -0.046 | 0.293 | 357 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| NVDA | +18.13% | +1.651 | -0.825 | -1.103 | -0.297 | +1.085 | 0.663 | 357 | Large-cap tilt; Growth tilt; Conservative investment |
| GOOG | +40.11% | +1.017 | +0.159 | -0.504 | +0.472 | -0.733 | 0.447 | 357 | Growth tilt; Aggressive investment; Significant positive alpha |
| DTE | -0.70% | +0.300 | -0.230 | +0.557 | -0.243 | +0.127 | 0.154 | 357 | Value tilt; Modest factor fit |
| GOOGL | +41.48% | +1.026 | +0.154 | -0.519 | +0.498 | -0.748 | 0.442 | 357 | Growth tilt; Aggressive investment; Significant positive alpha |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| CRWV | **86.67** | 20.00 | 33.33 | 33.33 | 0.423 | +1.598 | 1.1110 | 0.0478 | 107 |
| MU | **80.00** | 26.67 | 26.67 | 26.67 | 0.379 | +1.176 | 0.8212 | 0.0353 | 107 |
| NBIS | **70.00** | 10.00 | 30.00 | 30.00 | 0.472 | +1.293 | 1.0562 | 0.0454 | 107 |
| META | **56.67** | 23.33 | 13.33 | 20.00 | 0.387 | +0.113 | 0.4525 | 0.0195 | 107 |
| NFLX | **56.67** | 30.00 | 3.33 | 23.33 | 0.221 | -0.550 | 0.4734 | 0.0204 | 107 |
| GOOGL | **46.67** | 16.67 | 16.67 | 13.33 | 0.428 | +0.156 | 0.3175 | 0.0137 | 107 |
| DTE | **46.67** | 33.33 | 10.00 | 3.33 | 0.064 | +0.052 | 0.2340 | 0.0101 | 107 |
| GOOG | **43.33** | 13.33 | 20.00 | 10.00 | 0.436 | +0.158 | 0.3090 | 0.0133 | 107 |
| NVDA | **33.33** | 3.33 | 23.33 | 6.67 | 0.711 | +0.672 | 0.2946 | 0.0127 | 107 |
| TSLA | **30.00** | 6.67 | 6.67 | 16.67 | 0.484 | -0.006 | 0.4274 | 0.0184 | 107 |

## Per-ticker FF5 Detail

### MU

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.4051 (adjusted = 0.3967)
- Alpha (annualized): **+77.43%** (daily = +0.003073, t = +1.84, p = 0.0671)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9828 | +11.56 | 0.0000 *** |
| SMB | -0.3121 | -1.02 | 0.3063  |
| HML | -0.1378 | -0.51 | 0.6096  |
| RMW | -0.9525 | -2.91 | 0.0039 ** |
| CMA | +0.1745 | +0.49 | 0.6232  |

_Interpretation: Weak profitability_

### TSLA

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.4913 (adjusted = 0.4840)
- Alpha (annualized): **+18.03%** (daily = +0.000716, t = +0.49, p = 0.6260)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2067 | +14.67 | 0.0000 *** |
| SMB | +0.0242 | +0.09 | 0.9280  |
| HML | +0.1067 | +0.45 | 0.6523  |
| RMW | -0.3275 | -1.14 | 0.2551  |
| CMA | -1.1873 | -3.82 | 0.0002 *** |

_Interpretation: Aggressive investment_

### META

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.5060 (adjusted = 0.4989)
- Alpha (annualized): **+1.24%** (daily = +0.000049, t = +0.06, p = 0.9559)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3795 | +15.11 | 0.0000 *** |
| SMB | -0.0183 | -0.11 | 0.9102  |
| HML | -0.5598 | -3.90 | 0.0001 *** |
| RMW | +0.4322 | +2.48 | 0.0137 * |
| CMA | -0.5080 | -2.69 | 0.0075 ** |

_Interpretation: Growth tilt; Aggressive investment_

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

### NFLX

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.2561 (adjusted = 0.2456)
- Alpha (annualized): **+9.53%** (daily = +0.000378, t = +0.38, p = 0.7029)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7172 | +7.06 | 0.0000 *** |
| SMB | -0.8267 | -4.58 | 0.0000 *** |
| HML | -0.1655 | -1.04 | 0.3009  |
| RMW | -0.6003 | -3.09 | 0.0021 ** |
| CMA | +0.1851 | +0.88 | 0.3791  |

_Interpretation: Large-cap tilt; Weak profitability_

### NBIS

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.2926 (adjusted = 0.2825)
- Alpha (annualized): **+176.79%** (daily = +0.007015, t = +2.21, p = 0.0277)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6409 | +5.04 | 0.0000 *** |
| SMB | +0.7208 | +1.25 | 0.2133  |
| HML | -2.2330 | -4.36 | 0.0000 *** |
| RMW | -2.0182 | -3.25 | 0.0013 ** |
| CMA | -0.0460 | -0.07 | 0.9455  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### NVDA

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.6626 (adjusted = 0.6578)
- Alpha (annualized): **+18.13%** (daily = +0.000719, t = +0.80, p = 0.4261)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6506 | +17.84 | 0.0000 *** |
| SMB | -0.8252 | -5.02 | 0.0000 *** |
| HML | -1.1026 | -7.57 | 0.0000 *** |
| RMW | -0.2974 | -1.68 | 0.0934  |
| CMA | +1.0851 | +5.67 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### GOOG

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.4472 (adjusted = 0.4394)
- Alpha (annualized): **+40.11%** (daily = +0.001592, t = +2.05, p = 0.0412)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0173 | +12.77 | 0.0000 *** |
| SMB | +0.1589 | +1.12 | 0.2622  |
| HML | -0.5037 | -4.02 | 0.0001 *** |
| RMW | +0.4724 | +3.10 | 0.0021 ** |
| CMA | -0.7325 | -4.44 | 0.0000 *** |

_Interpretation: Growth tilt; Aggressive investment; Significant positive alpha_

### DTE

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.1543 (adjusted = 0.1422)
- Alpha (annualized): **-0.70%** (daily = -0.000028, t = -0.05, p = 0.9594)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3004 | +5.40 | 0.0000 *** |
| SMB | -0.2304 | -2.33 | 0.0202 * |
| HML | +0.5566 | +6.37 | 0.0000 *** |
| RMW | -0.2435 | -2.29 | 0.0224 * |
| CMA | +0.1272 | +1.11 | 0.2696  |

_Interpretation: Value tilt; Modest factor fit_

### GOOGL

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.4417 (adjusted = 0.4338)
- Alpha (annualized): **+41.48%** (daily = +0.001646, t = +2.08, p = 0.0386)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0256 | +12.62 | 0.0000 *** |
| SMB | +0.1538 | +1.07 | 0.2875  |
| HML | -0.5186 | -4.06 | 0.0001 *** |
| RMW | +0.4982 | +3.21 | 0.0015 ** |
| CMA | -0.7479 | -4.45 | 0.0000 *** |

_Interpretation: Growth tilt; Aggressive investment; Significant positive alpha_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._