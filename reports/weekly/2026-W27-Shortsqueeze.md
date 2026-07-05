# Weekly Report — `Shortsqueeze` — 2026-W27

Generated: 2026-07-05  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W27.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| WEN | -48.11% | +0.553 | +0.830 | +0.284 | +0.388 | +0.648 | 0.192 | 436 | Small-cap tilt; Conservative investment; Modest factor fit |
| JACK | -82.91% | +0.987 | +2.024 | -0.038 | +0.851 | +0.968 | 0.239 | 436 | Small-cap tilt; Robust profitability; Conservative investment; Significant negative alpha |
| LFVN | +4.27% | +0.790 | +1.197 | -0.687 | +0.661 | +0.179 | 0.087 | 436 | Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit |
| AAPL | +2.45% | +1.305 | -0.108 | -0.054 | +0.743 | +0.092 | 0.537 | 436 | Robust profitability |
| BB | +9.13% | +1.015 | +0.315 | -0.379 | -1.269 | +0.691 | 0.303 | 436 | Weak profitability; Conservative investment |
| AMZN | -2.15% | +1.353 | +0.024 | -0.332 | +0.265 | -0.554 | 0.564 | 436 | Aggressive investment |
| BE | +156.95% | +1.431 | -0.030 | -0.045 | -2.641 | -1.760 | 0.208 | 436 | Weak profitability; Aggressive investment; Significant positive alpha |
| ET | +3.35% | +0.751 | -0.217 | +0.374 | -0.285 | +0.324 | 0.321 | 436 | Neutral profile |
| DTE | +8.14% | +0.281 | -0.123 | +0.551 | -0.186 | +0.018 | 0.141 | 436 | Value tilt; Modest factor fit |
| ALL | +5.17% | +0.691 | -0.286 | +0.803 | +0.356 | -0.172 | 0.214 | 436 | Value tilt |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| BE | **73.33** | 6.67 | 33.33 | 33.33 | 0.367 | +1.950 | 0.9419 | 0.0548 | 186 |
| DTE | **66.67** | 33.33 | 30.00 | 3.33 | 0.066 | +0.078 | 0.1606 | 0.0093 | 186 |
| ET | **63.33** | 30.00 | 26.67 | 6.67 | 0.068 | +0.058 | 0.1622 | 0.0094 | 186 |
| ALL | **60.00** | 26.67 | 20.00 | 13.33 | 0.164 | -0.060 | 0.2314 | 0.0135 | 186 |
| LFVN | **60.00** | 23.33 | 10.00 | 26.67 | 0.170 | -0.705 | 0.5630 | 0.0328 | 186 |
| BB | **56.67** | 20.00 | 16.67 | 20.00 | 0.247 | -0.381 | 0.3639 | 0.0212 | 186 |
| JACK | **50.00** | 16.67 | 3.33 | 30.00 | 0.286 | -1.082 | 0.6429 | 0.0374 | 186 |
| WEN | **43.33** | 13.33 | 6.67 | 23.33 | 0.295 | -0.865 | 0.3709 | 0.0216 | 186 |
| AAPL | **43.33** | 10.00 | 23.33 | 10.00 | 0.339 | +0.047 | 0.1994 | 0.0116 | 186 |
| AMZN | **33.33** | 3.33 | 13.33 | 16.67 | 0.394 | -0.397 | 0.2615 | 0.0152 | 186 |

## Per-ticker FF5 Detail

### WEN

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.1917 (adjusted = 0.1823)
- Alpha (annualized): **-48.11%** (daily = -0.001909, t = -1.96, p = 0.0511)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5531 | +5.33 | 0.0000 *** |
| SMB | +0.8296 | +4.94 | 0.0000 *** |
| HML | +0.2843 | +1.78 | 0.0753  |
| RMW | +0.3876 | +1.93 | 0.0538  |
| CMA | +0.6475 | +3.20 | 0.0015 ** |

_Interpretation: Small-cap tilt; Conservative investment; Modest factor fit_

### JACK

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.2388 (adjusted = 0.2300)
- Alpha (annualized): **-82.91%** (daily = -0.003290, t = -2.00, p = 0.0461)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9875 | +5.64 | 0.0000 *** |
| SMB | +2.0237 | +7.15 | 0.0000 *** |
| HML | -0.0379 | -0.14 | 0.8879  |
| RMW | +0.8514 | +2.52 | 0.0121 * |
| CMA | +0.9681 | +2.84 | 0.0047 ** |

_Interpretation: Small-cap tilt; Robust profitability; Conservative investment; Significant negative alpha_

### LFVN

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.0868 (adjusted = 0.0762)
- Alpha (annualized): **+4.27%** (daily = +0.000169, t = +0.08, p = 0.9326)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7904 | +3.71 | 0.0002 *** |
| SMB | +1.1969 | +3.47 | 0.0006 *** |
| HML | -0.6874 | -2.10 | 0.0361 * |
| RMW | +0.6612 | +1.61 | 0.1085  |
| CMA | +0.1790 | +0.43 | 0.6661  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Modest factor fit_

### AAPL

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.5373 (adjusted = 0.5319)
- Alpha (annualized): **+2.45%** (daily = +0.000097, t = +0.16, p = 0.8691)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3048 | +20.76 | 0.0000 *** |
| SMB | -0.1076 | -1.06 | 0.2907  |
| HML | -0.0542 | -0.56 | 0.5744  |
| RMW | +0.7434 | +6.13 | 0.0000 *** |
| CMA | +0.0919 | +0.75 | 0.4532  |

_Interpretation: Robust profitability_

### BB

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.3028 (adjusted = 0.2947)
- Alpha (annualized): **+9.13%** (daily = +0.000362, t = +0.27, p = 0.7890)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0152 | +7.05 | 0.0000 *** |
| SMB | +0.3151 | +1.35 | 0.1769  |
| HML | -0.3794 | -1.72 | 0.0868  |
| RMW | -1.2691 | -4.57 | 0.0000 *** |
| CMA | +0.6909 | +2.46 | 0.0141 * |

_Interpretation: Weak profitability; Conservative investment_

### AMZN

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.5641 (adjusted = 0.5590)
- Alpha (annualized): **-2.15%** (daily = -0.000085, t = -0.13, p = 0.8979)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3534 | +19.10 | 0.0000 *** |
| SMB | +0.0243 | +0.21 | 0.8325  |
| HML | -0.3319 | -3.05 | 0.0024 ** |
| RMW | +0.2646 | +1.93 | 0.0537  |
| CMA | -0.5540 | -4.01 | 0.0001 *** |

_Interpretation: Aggressive investment_

### BE

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.2082 (adjusted = 0.1990)
- Alpha (annualized): **+156.95%** (daily = +0.006228, t = +2.24, p = 0.0253)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4312 | +4.85 | 0.0000 *** |
| SMB | -0.0296 | -0.06 | 0.9507  |
| HML | -0.0447 | -0.10 | 0.9215  |
| RMW | -2.6412 | -4.63 | 0.0000 *** |
| CMA | -1.7603 | -3.06 | 0.0023 ** |

_Interpretation: Weak profitability; Aggressive investment; Significant positive alpha_

### ET

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.3207 (adjusted = 0.3128)
- Alpha (annualized): **+3.35%** (daily = +0.000133, t = +0.23, p = 0.8214)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7509 | +11.99 | 0.0000 *** |
| SMB | -0.2174 | -2.15 | 0.0325 * |
| HML | +0.3745 | +3.89 | 0.0001 *** |
| RMW | -0.2848 | -2.35 | 0.0190 * |
| CMA | +0.3243 | +2.66 | 0.0082 ** |

_Interpretation: Neutral profile_

### DTE

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.1410 (adjusted = 0.1310)
- Alpha (annualized): **+8.14%** (daily = +0.000323, t = +0.66, p = 0.5083)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2807 | +5.41 | 0.0000 *** |
| SMB | -0.1234 | -1.47 | 0.1423  |
| HML | +0.5508 | +6.91 | 0.0000 *** |
| RMW | -0.1861 | -1.86 | 0.0640  |
| CMA | +0.0184 | +0.18 | 0.8558  |

_Interpretation: Value tilt; Modest factor fit_

### ALL

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.2135 (adjusted = 0.2044)
- Alpha (annualized): **+5.17%** (daily = +0.000205, t = +0.30, p = 0.7639)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6912 | +9.52 | 0.0000 *** |
| SMB | -0.2864 | -2.44 | 0.0152 * |
| HML | +0.8034 | +7.20 | 0.0000 *** |
| RMW | +0.3561 | +2.54 | 0.0115 * |
| CMA | -0.1718 | -1.21 | 0.2252  |

_Interpretation: Value tilt_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._