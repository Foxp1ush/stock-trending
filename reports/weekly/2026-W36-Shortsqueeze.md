# Weekly Report — `Shortsqueeze` — 2026-W36

Generated: 2026-08-31  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W36.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **9 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| IQ | -34.86% | +1.039 | +0.304 | +0.241 | -0.702 | +0.225 | 0.142 | 396 | Weak profitability; Modest factor fit |
| IP | -22.96% | +1.139 | +0.466 | +0.589 | +0.329 | +0.916 | 0.322 | 396 | Value tilt; Conservative investment |
| IT | -70.16% | +0.844 | +0.352 | -0.180 | +0.184 | +0.045 | 0.145 | 396 | Significant negative alpha; Modest factor fit |
| MRNA | -26.54% | +0.676 | +0.886 | -0.174 | -2.045 | +1.638 | 0.244 | 396 | Small-cap tilt; Weak profitability; Conservative investment |
| PS | — | — | — | — | — | — | — | — | _insufficient_data_ |
| ONDS | +209.45% | +1.601 | +1.598 | -0.584 | -2.352 | -1.015 | 0.169 | 396 | Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Significant positive alpha; Modest factor fit |
| ON | -18.81% | +1.812 | +0.633 | -0.020 | -0.210 | +1.061 | 0.435 | 396 | Small-cap tilt; Conservative investment |
| SO | +1.97% | +0.102 | -0.234 | +0.476 | -0.043 | +0.120 | 0.084 | 396 | Modest factor fit |
| WEN | -49.11% | +0.597 | +0.796 | +0.234 | +0.344 | +0.899 | 0.199 | 396 | Small-cap tilt; Conservative investment; Modest factor fit |
| SMCI | -7.12% | +1.198 | +0.244 | -2.054 | -2.046 | +1.982 | 0.250 | 396 | Growth tilt; Weak profitability; Conservative investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| ONDS | **92.59** | 25.93 | 33.33 | 33.33 | 0.284 | +1.077 | 1.3573 | 0.0692 | 146 |
| IQ | **74.07** | 29.63 | 22.22 | 22.22 | 0.164 | +0.036 | 0.4884 | 0.0249 | 146 |
| SO | **62.96** | 33.33 | 25.93 | 3.70 | 0.074 | +0.089 | 0.1956 | 0.0100 | 146 |
| SMCI | **62.96** | 14.81 | 18.52 | 29.63 | 0.323 | -0.105 | 0.7903 | 0.0403 | 146 |
| MRNA | **62.96** | 22.22 | 14.81 | 25.93 | 0.288 | -0.205 | 0.7382 | 0.0376 | 146 |
| ON | **48.15** | 3.70 | 29.63 | 14.81 | 0.380 | +0.268 | 0.4645 | 0.0237 | 146 |
| WEN | **37.04** | 18.52 | 7.41 | 11.11 | 0.291 | -0.980 | 0.4398 | 0.0224 | 146 |
| IT | **33.33** | 11.11 | 3.70 | 18.52 | 0.333 | -1.770 | 0.4868 | 0.0248 | 146 |
| IP | **25.93** | 7.41 | 11.11 | 7.41 | 0.372 | -0.311 | 0.3957 | 0.0202 | 146 |

## Per-ticker FF5 Detail

### IQ

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.1423 (adjusted = 0.1313)
- Alpha (annualized): **-34.86%** (daily = -0.001383, t = -0.78, p = 0.4363)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0387 | +5.54 | 0.0000 *** |
| SMB | +0.3035 | +0.94 | 0.3470  |
| HML | +0.2406 | +0.83 | 0.4085  |
| RMW | -0.7025 | -1.97 | 0.0490 * |
| CMA | +0.2250 | +0.59 | 0.5523  |

_Interpretation: Weak profitability; Modest factor fit_

### IP

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.3223 (adjusted = 0.3136)
- Alpha (annualized): **-22.96%** (daily = -0.000911, t = -0.90, p = 0.3698)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1386 | +10.62 | 0.0000 *** |
| SMB | +0.4661 | +2.53 | 0.0118 * |
| HML | +0.5886 | +3.54 | 0.0004 *** |
| RMW | +0.3291 | +1.62 | 0.1064  |
| CMA | +0.9163 | +4.24 | 0.0000 *** |

_Interpretation: Value tilt; Conservative investment_

### IT

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.1445 (adjusted = 0.1336)
- Alpha (annualized): **-70.16%** (daily = -0.002784, t = -2.25, p = 0.0250)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8444 | +6.46 | 0.0000 *** |
| SMB | +0.3523 | +1.57 | 0.1176  |
| HML | -0.1797 | -0.89 | 0.3756  |
| RMW | +0.1843 | +0.74 | 0.4578  |
| CMA | +0.0447 | +0.17 | 0.8654  |

_Interpretation: Significant negative alpha; Modest factor fit_

### MRNA

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.2437 (adjusted = 0.2340)
- Alpha (annualized): **-26.54%** (daily = -0.001053, t = -0.55, p = 0.5799)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6762 | +3.37 | 0.0008 *** |
| SMB | +0.8857 | +2.57 | 0.0107 * |
| HML | -0.1737 | -0.56 | 0.5773  |
| RMW | -2.0450 | -5.37 | 0.0000 *** |
| CMA | +1.6383 | +4.04 | 0.0001 *** |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment_

### PS

Status: `insufficient_data` — only 0 overlapping days after factor join


### ONDS

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.1692 (adjusted = 0.1585)
- Alpha (annualized): **+209.45%** (daily = +0.008312, t = +2.14, p = 0.0332)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6015 | +3.90 | 0.0001 *** |
| SMB | +1.5978 | +2.26 | 0.0242 * |
| HML | -0.5837 | -0.92 | 0.3600  |
| RMW | -2.3522 | -3.02 | 0.0027 ** |
| CMA | -1.0153 | -1.23 | 0.2212  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Aggressive investment; Significant positive alpha; Modest factor fit_

### ON

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.4348 (adjusted = 0.4276)
- Alpha (annualized): **-18.81%** (daily = -0.000746, t = -0.57, p = 0.5690)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.8123 | +13.10 | 0.0000 *** |
| SMB | +0.6329 | +2.66 | 0.0081 ** |
| HML | -0.0197 | -0.09 | 0.9268  |
| RMW | -0.2099 | -0.80 | 0.4242  |
| CMA | +1.0611 | +3.80 | 0.0002 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### SO

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.0842 (adjusted = 0.0724)
- Alpha (annualized): **+1.97%** (daily = +0.000078, t = +0.15, p = 0.8844)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.1024 | +1.80 | 0.0728  |
| SMB | -0.2338 | -2.39 | 0.0173 * |
| HML | +0.4762 | +5.40 | 0.0000 *** |
| RMW | -0.0429 | -0.40 | 0.6912  |
| CMA | +0.1195 | +1.04 | 0.2983  |

_Interpretation: Modest factor fit_

### WEN

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.1995 (adjusted = 0.1892)
- Alpha (annualized): **-49.11%** (daily = -0.001949, t = -1.88, p = 0.0607)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5967 | +5.45 | 0.0000 *** |
| SMB | +0.7963 | +4.23 | 0.0000 *** |
| HML | +0.2343 | +1.38 | 0.1682  |
| RMW | +0.3443 | +1.66 | 0.0982  |
| CMA | +0.8990 | +4.07 | 0.0001 *** |

_Interpretation: Small-cap tilt; Conservative investment; Modest factor fit_

### SMCI

- Period: `2024-08-30` to `2026-03-31` (396 obs)
- R² = 0.2503 (adjusted = 0.2407)
- Alpha (annualized): **-7.12%** (daily = -0.000283, t = -0.10, p = 0.9191)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1985 | +4.08 | 0.0001 *** |
| SMB | +0.2443 | +0.48 | 0.6286  |
| HML | -2.0542 | -4.51 | 0.0000 *** |
| RMW | -2.0463 | -3.67 | 0.0003 *** |
| CMA | +1.9816 | +3.35 | 0.0009 *** |

_Interpretation: Growth tilt; Weak profitability; Conservative investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._