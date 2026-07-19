# Weekly Report — `Shortsqueeze` — 2026-W29

Generated: 2026-07-19  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W29.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **9 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| GRPN | -6.91% | +0.646 | +1.060 | -0.313 | -1.923 | +0.612 | 0.157 | 426 | Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit |
| CRM | -21.61% | +0.801 | +0.263 | -0.348 | -0.435 | -0.055 | 0.326 | 426 | Neutral profile |
| ES | +2.82% | +0.350 | -0.102 | +0.486 | -0.111 | +0.263 | 0.083 | 426 | Modest factor fit |
| NOW | -25.90% | +0.967 | -0.087 | -0.436 | -0.554 | -0.046 | 0.308 | 426 | Weak profitability |
| MU | +54.81% | +1.961 | -0.334 | -0.131 | -1.043 | +0.377 | 0.405 | 426 | Weak profitability |
| IQ | -58.81% | +0.993 | +0.177 | +0.135 | -0.738 | +0.258 | 0.131 | 426 | Weak profitability; Modest factor fit |
| IT | -62.45% | +0.871 | +0.380 | -0.134 | +0.233 | -0.066 | 0.156 | 426 | Significant negative alpha; Modest factor fit |
| IP | -19.25% | +1.105 | +0.411 | +0.570 | +0.325 | +0.900 | 0.323 | 426 | Value tilt; Conservative investment |
| CC | +1.79% | +1.769 | +1.972 | +0.327 | +0.196 | +1.221 | 0.451 | 426 | Small-cap tilt; Conservative investment |
| PS | — | — | — | — | — | — | — | — | _insufficient_data_ |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| MU | **81.48** | 18.52 | 33.33 | 29.63 | 0.330 | +0.714 | 0.5795 | 0.0330 | 176 |
| GRPN | **70.37** | 22.22 | 14.81 | 33.33 | 0.267 | -0.780 | 0.6000 | 0.0341 | 176 |
| IQ | **70.37** | 29.63 | 22.22 | 18.52 | 0.137 | -0.160 | 0.4963 | 0.0282 | 176 |
| ES | **62.96** | 33.33 | 25.93 | 3.70 | 0.067 | -0.142 | 0.2808 | 0.0160 | 176 |
| CC | **62.96** | 11.11 | 29.63 | 22.22 | 0.418 | +0.240 | 0.5516 | 0.0314 | 176 |
| IT | **59.26** | 25.93 | 7.41 | 25.93 | 0.209 | -1.559 | 0.5552 | 0.0316 | 176 |
| IP | **48.15** | 14.81 | 18.52 | 14.81 | 0.355 | -0.393 | 0.3666 | 0.0209 | 176 |
| NOW | **22.22** | 7.41 | 3.70 | 11.11 | 0.431 | -1.683 | 0.3268 | 0.0186 | 176 |
| CRM | **22.22** | 3.70 | 11.11 | 7.41 | 0.456 | -1.534 | 0.2891 | 0.0164 | 176 |

## Per-ticker FF5 Detail

### GRPN

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.1571 (adjusted = 0.1470)
- Alpha (annualized): **-6.91%** (daily = -0.000274, t = -0.12, p = 0.9067)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6461 | +2.61 | 0.0094 ** |
| SMB | +1.0595 | +2.51 | 0.0123 * |
| HML | -0.3132 | -0.82 | 0.4142  |
| RMW | -1.9234 | -4.03 | 0.0001 *** |
| CMA | +0.6123 | +1.26 | 0.2073  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit_

### CRM

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.3263 (adjusted = 0.3183)
- Alpha (annualized): **-21.61%** (daily = -0.000857, t = -1.00, p = 0.3166)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8012 | +8.85 | 0.0000 *** |
| SMB | +0.2634 | +1.71 | 0.0882  |
| HML | -0.3481 | -2.48 | 0.0134 * |
| RMW | -0.4351 | -2.49 | 0.0131 * |
| CMA | -0.0547 | -0.31 | 0.7577  |

_Interpretation: Neutral profile_

### ES

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.0834 (adjusted = 0.0725)
- Alpha (annualized): **+2.82%** (daily = +0.000112, t = +0.15, p = 0.8792)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3502 | +4.49 | 0.0000 *** |
| SMB | -0.1022 | -0.77 | 0.4415  |
| HML | +0.4860 | +4.03 | 0.0001 *** |
| RMW | -0.1109 | -0.74 | 0.4612  |
| CMA | +0.2631 | +1.72 | 0.0853  |

_Interpretation: Modest factor fit_

### NOW

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.3081 (adjusted = 0.2998)
- Alpha (annualized): **-25.90%** (daily = -0.001028, t = -0.99, p = 0.3247)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9666 | +8.76 | 0.0000 *** |
| SMB | -0.0867 | -0.46 | 0.6446  |
| HML | -0.4358 | -2.55 | 0.0111 * |
| RMW | -0.5541 | -2.60 | 0.0095 ** |
| CMA | -0.0462 | -0.21 | 0.8309  |

_Interpretation: Weak profitability_

### MU

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.4046 (adjusted = 0.3976)
- Alpha (annualized): **+54.81%** (daily = +0.002175, t = +1.45, p = 0.1492)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9612 | +12.31 | 0.0000 *** |
| SMB | -0.3339 | -1.23 | 0.2191  |
| HML | -0.1307 | -0.53 | 0.5964  |
| RMW | -1.0428 | -3.39 | 0.0008 *** |
| CMA | +0.3771 | +1.21 | 0.2274  |

_Interpretation: Weak profitability_

### IQ

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.1306 (adjusted = 0.1203)
- Alpha (annualized): **-58.81%** (daily = -0.002334, t = -1.33, p = 0.1834)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9935 | +5.36 | 0.0000 *** |
| SMB | +0.1773 | +0.56 | 0.5746  |
| HML | +0.1345 | +0.47 | 0.6395  |
| RMW | -0.7380 | -2.06 | 0.0397 * |
| CMA | +0.2583 | +0.71 | 0.4772  |

_Interpretation: Weak profitability; Modest factor fit_

### IT

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.1564 (adjusted = 0.1463)
- Alpha (annualized): **-62.45%** (daily = -0.002478, t = -2.13, p = 0.0339)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8709 | +7.06 | 0.0000 *** |
| SMB | +0.3804 | +1.81 | 0.0705  |
| HML | -0.1343 | -0.70 | 0.4819  |
| RMW | +0.2327 | +0.98 | 0.3281  |
| CMA | -0.0661 | -0.27 | 0.7844  |

_Interpretation: Significant negative alpha; Modest factor fit_

### IP

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.3227 (adjusted = 0.3146)
- Alpha (annualized): **-19.25%** (daily = -0.000764, t = -0.80, p = 0.4232)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1052 | +10.95 | 0.0000 *** |
| SMB | +0.4108 | +2.39 | 0.0172 * |
| HML | +0.5699 | +3.65 | 0.0003 *** |
| RMW | +0.3252 | +1.67 | 0.0954  |
| CMA | +0.9004 | +4.56 | 0.0000 *** |

_Interpretation: Value tilt; Conservative investment_

### CC

- Period: `2024-07-19` to `2026-03-31` (426 obs)
- R² = 0.4509 (adjusted = 0.4443)
- Alpha (annualized): **+1.79%** (daily = +0.000071, t = +0.05, p = 0.9606)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7692 | +11.60 | 0.0000 *** |
| SMB | +1.9722 | +7.60 | 0.0000 *** |
| HML | +0.3270 | +1.39 | 0.1666  |
| RMW | +0.1959 | +0.67 | 0.5058  |
| CMA | +1.2211 | +4.09 | 0.0001 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### PS

Status: `insufficient_data` — price history only 55 days


---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._