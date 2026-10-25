# Weekly Report — `Shortsqueeze` — 2026-W43

Generated: 2026-10-25  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W43.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| HTZ | +58.56% | +1.014 | +2.072 | +0.654 | +0.265 | +0.288 | 0.097 | 357 | Small-cap tilt; Value tilt; Modest factor fit |
| IBKR | +21.90% | +1.649 | -0.511 | +0.517 | -1.084 | -0.023 | 0.551 | 357 | Large-cap tilt; Value tilt; Weak profitability |
| AM | +21.91% | +0.608 | -0.356 | +0.390 | -0.299 | +0.137 | 0.195 | 357 | Modest factor fit |
| AMD | +11.56% | +1.591 | -0.595 | -0.422 | -1.674 | -0.276 | 0.477 | 357 | Large-cap tilt; Weak profitability |
| ALL | -4.53% | +0.683 | -0.276 | +0.784 | +0.302 | -0.054 | 0.219 | 357 | Value tilt |
| ES | -1.68% | +0.395 | -0.082 | +0.451 | -0.127 | +0.380 | 0.100 | 357 | Modest factor fit |
| BB | +19.72% | +1.010 | +0.197 | -0.470 | -1.241 | +0.820 | 0.278 | 357 | Weak profitability; Conservative investment |
| DTE | -0.70% | +0.300 | -0.230 | +0.557 | -0.243 | +0.127 | 0.154 | 357 | Value tilt; Modest factor fit |
| CC | +22.15% | +1.753 | +2.070 | +0.185 | +0.217 | +1.397 | 0.435 | 357 | Small-cap tilt; Conservative investment |
| EU | -22.35% | +0.850 | +1.504 | -1.202 | -0.991 | -0.132 | 0.171 | 357 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| EU | **76.67** | 13.33 | 33.33 | 30.00 | 0.296 | +1.231 | 0.9621 | 0.0414 | 107 |
| AM | **63.33** | 33.33 | 23.33 | 6.67 | 0.042 | +0.142 | 0.2797 | 0.0120 | 107 |
| CC | **63.33** | 10.00 | 26.67 | 26.67 | 0.329 | +0.563 | 0.7712 | 0.0332 | 107 |
| HTZ | **63.33** | 23.33 | 6.67 | 33.33 | 0.131 | -0.352 | 1.1262 | 0.0484 | 107 |
| ES | **60.00** | 30.00 | 13.33 | 16.67 | 0.063 | -0.163 | 0.4048 | 0.0174 | 107 |
| AMD | **60.00** | 6.67 | 30.00 | 23.33 | 0.563 | +1.026 | 0.5791 | 0.0249 | 107 |
| DTE | **50.00** | 26.67 | 20.00 | 3.33 | 0.064 | +0.052 | 0.2340 | 0.0101 | 107 |
| ALL | **40.00** | 20.00 | 10.00 | 10.00 | 0.239 | -0.281 | 0.2880 | 0.0124 | 107 |
| BB | **40.00** | 16.67 | 3.33 | 20.00 | 0.240 | -0.555 | 0.4640 | 0.0199 | 107 |
| IBKR | **33.33** | 3.33 | 16.67 | 13.33 | 0.682 | -0.001 | 0.3346 | 0.0144 | 107 |

## Per-ticker FF5 Detail

### HTZ

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.0966 (adjusted = 0.0837)
- Alpha (annualized): **+58.56%** (daily = +0.002324, t = +0.71, p = 0.4758)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0138 | +3.04 | 0.0026 ** |
| SMB | +2.0718 | +3.49 | 0.0005 *** |
| HML | +0.6541 | +1.25 | 0.2135  |
| RMW | +0.2651 | +0.42 | 0.6777  |
| CMA | +0.2878 | +0.42 | 0.6771  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### IBKR

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.5511 (adjusted = 0.5447)
- Alpha (annualized): **+21.90%** (daily = +0.000869, t = +0.87, p = 0.3848)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6489 | +16.11 | 0.0000 *** |
| SMB | -0.5108 | -2.81 | 0.0052 ** |
| HML | +0.5173 | +3.21 | 0.0014 ** |
| RMW | -1.0838 | -5.54 | 0.0000 *** |
| CMA | -0.0227 | -0.11 | 0.9148  |

_Interpretation: Large-cap tilt; Value tilt; Weak profitability_

### AM

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.1948 (adjusted = 0.1833)
- Alpha (annualized): **+21.91%** (daily = +0.000869, t = +1.17, p = 0.2421)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6076 | +7.99 | 0.0000 *** |
| SMB | -0.3563 | -2.64 | 0.0087 ** |
| HML | +0.3897 | +3.26 | 0.0012 ** |
| RMW | -0.2989 | -2.06 | 0.0404 * |
| CMA | +0.1371 | +0.87 | 0.3841  |

_Interpretation: Modest factor fit_

### AMD

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.4774 (adjusted = 0.4700)
- Alpha (annualized): **+11.56%** (daily = +0.000459, t = +0.32, p = 0.7518)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5909 | +10.71 | 0.0000 *** |
| SMB | -0.5948 | -2.25 | 0.0249 * |
| HML | -0.4224 | -1.81 | 0.0716  |
| RMW | -1.6740 | -5.90 | 0.0000 *** |
| CMA | -0.2760 | -0.90 | 0.3701  |

_Interpretation: Large-cap tilt; Weak profitability_

### ALL

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.2194 (adjusted = 0.2083)
- Alpha (annualized): **-4.53%** (daily = -0.000180, t = -0.24, p = 0.8134)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6833 | +8.76 | 0.0000 *** |
| SMB | -0.2758 | -1.99 | 0.0472 * |
| HML | +0.7838 | +6.39 | 0.0000 *** |
| RMW | +0.3016 | +2.02 | 0.0437 * |
| CMA | -0.0535 | -0.33 | 0.7402  |

_Interpretation: Value tilt_

### ES

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.0996 (adjusted = 0.0868)
- Alpha (annualized): **-1.68%** (daily = -0.000067, t = -0.08, p = 0.9363)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3954 | +4.62 | 0.0000 *** |
| SMB | -0.0822 | -0.54 | 0.5890  |
| HML | +0.4507 | +3.35 | 0.0009 *** |
| RMW | -0.1272 | -0.78 | 0.4369  |
| CMA | +0.3803 | +2.15 | 0.0324 * |

_Interpretation: Modest factor fit_

### BB

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.2777 (adjusted = 0.2674)
- Alpha (annualized): **+19.72%** (daily = +0.000782, t = +0.49, p = 0.6248)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0097 | +6.16 | 0.0000 *** |
| SMB | +0.1971 | +0.68 | 0.4988  |
| HML | -0.4697 | -1.82 | 0.0692  |
| RMW | -1.2409 | -3.96 | 0.0001 *** |
| CMA | +0.8202 | +2.42 | 0.0161 * |

_Interpretation: Weak profitability; Conservative investment_

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

### CC

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.4350 (adjusted = 0.4270)
- Alpha (annualized): **+22.15%** (daily = +0.000879, t = +0.53, p = 0.5945)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7526 | +10.36 | 0.0000 *** |
| SMB | +2.0697 | +6.89 | 0.0000 *** |
| HML | +0.1854 | +0.70 | 0.4863  |
| RMW | +0.2174 | +0.67 | 0.5014  |
| CMA | +1.3966 | +3.99 | 0.0001 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### EU

- Period: `2024-10-25` to `2026-03-31` (357 obs)
- R² = 0.1712 (adjusted = 0.1594)
- Alpha (annualized): **-22.35%** (daily = -0.000887, t = -0.33, p = 0.7392)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8497 | +3.11 | 0.0020 ** |
| SMB | +1.5044 | +3.10 | 0.0021 ** |
| HML | -1.2021 | -2.80 | 0.0054 ** |
| RMW | -0.9907 | -1.90 | 0.0581  |
| CMA | -0.1323 | -0.23 | 0.8148  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._