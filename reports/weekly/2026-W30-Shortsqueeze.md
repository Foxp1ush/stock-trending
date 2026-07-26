# Weekly Report — `Shortsqueeze` — 2026-W30

Generated: 2026-07-26  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W30.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| WEN | -47.27% | +0.559 | +0.769 | +0.242 | +0.383 | +0.717 | 0.180 | 421 | Small-cap tilt; Conservative investment; Modest factor fit |
| SMCI | -31.39% | +1.190 | +0.308 | -2.115 | -2.114 | +2.009 | 0.266 | 421 | Growth tilt; Weak profitability; Conservative investment |
| SLS | +99.08% | +0.247 | +0.606 | +0.193 | -1.873 | -1.015 | 0.080 | 421 | Small-cap tilt; Weak profitability; Aggressive investment; Modest factor fit |
| PLTR | +85.68% | +1.620 | -0.761 | -0.092 | -2.329 | -0.806 | 0.451 | 421 | Large-cap tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| SMA | -10.84% | +0.296 | +0.707 | -0.197 | +0.151 | +0.586 | 0.193 | 249 | Small-cap tilt; Conservative investment; Modest factor fit |
| AM | +19.35% | +0.618 | -0.254 | +0.381 | -0.256 | +0.057 | 0.195 | 421 | Modest factor fit |
| ASTS | +133.96% | +1.468 | +1.516 | -1.494 | -2.778 | +0.086 | 0.295 | 421 | Small-cap tilt; Growth tilt; Weak profitability |
| API | +65.42% | +0.145 | +0.737 | -1.321 | -1.564 | +0.647 | 0.069 | 421 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| BATL | +264.54% | +0.013 | +0.765 | -1.809 | +2.658 | -0.382 | 0.008 | 421 | Small-cap tilt; Growth tilt; Robust profitability; Low explanatory power — likely sentiment-driven |
| ES | +0.81% | +0.364 | -0.094 | +0.460 | -0.090 | +0.254 | 0.084 | 421 | Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SLS | **83.33** | 20.00 | 33.33 | 30.00 | 0.141 | +0.624 | 0.9741 | 0.0549 | 171 |
| BATL | **70.00** | 33.33 | 3.33 | 33.33 | 0.018 | -1.084 | 4.0331 | 0.2274 | 171 |
| AM | **63.33** | 30.00 | 30.00 | 3.33 | 0.055 | +0.283 | 0.2211 | 0.0125 | 171 |
| ASTS | **56.67** | 6.67 | 23.33 | 26.67 | 0.324 | +0.105 | 0.9722 | 0.0548 | 171 |
| ES | **53.33** | 26.67 | 16.67 | 10.00 | 0.064 | -0.126 | 0.2871 | 0.0162 | 171 |
| API | **53.33** | 23.33 | 10.00 | 20.00 | 0.136 | -0.184 | 0.4891 | 0.0276 | 171 |
| PLTR | **46.67** | 3.33 | 26.67 | 16.67 | 0.501 | +0.154 | 0.4000 | 0.0226 | 171 |
| SMCI | **46.67** | 10.00 | 13.33 | 23.33 | 0.280 | -0.164 | 0.7368 | 0.0415 | 171 |
| SMA | **40.00** | 13.33 | 20.00 | 6.67 | 0.267 | -0.097 | 0.2523 | 0.0142 | 171 |
| WEN | **36.67** | 16.67 | 6.67 | 13.33 | 0.264 | -0.886 | 0.3890 | 0.0219 | 171 |

## Per-ticker FF5 Detail

### WEN

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.1803 (adjusted = 0.1704)
- Alpha (annualized): **-47.27%** (daily = -0.001876, t = -1.89, p = 0.0601)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5587 | +5.31 | 0.0000 *** |
| SMB | +0.7694 | +4.26 | 0.0000 *** |
| HML | +0.2419 | +1.48 | 0.1385  |
| RMW | +0.3829 | +1.89 | 0.0591  |
| CMA | +0.7174 | +3.49 | 0.0005 *** |

_Interpretation: Small-cap tilt; Conservative investment; Modest factor fit_

### SMCI

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.2658 (adjusted = 0.2569)
- Alpha (annualized): **-31.39%** (daily = -0.001246, t = -0.47, p = 0.6420)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1896 | +4.20 | 0.0000 *** |
| SMB | +0.3083 | +0.63 | 0.5260  |
| HML | -2.1153 | -4.82 | 0.0000 *** |
| RMW | -2.1136 | -3.88 | 0.0001 *** |
| CMA | +2.0085 | +3.63 | 0.0003 *** |

_Interpretation: Growth tilt; Weak profitability; Conservative investment_

### SLS

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.0797 (adjusted = 0.0686)
- Alpha (annualized): **+99.08%** (daily = +0.003932, t = +1.50, p = 0.1354)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2467 | +0.89 | 0.3756  |
| SMB | +0.6064 | +1.27 | 0.2042  |
| HML | +0.1931 | +0.45 | 0.6541  |
| RMW | -1.8727 | -3.50 | 0.0005 *** |
| CMA | -1.0154 | -1.87 | 0.0623  |

_Interpretation: Small-cap tilt; Weak profitability; Aggressive investment; Modest factor fit_

### PLTR

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.4511 (adjusted = 0.4445)
- Alpha (annualized): **+85.68%** (daily = +0.003400, t = +2.27, p = 0.0237)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6202 | +10.23 | 0.0000 *** |
| SMB | -0.7613 | -2.80 | 0.0053 ** |
| HML | -0.0923 | -0.38 | 0.7070  |
| RMW | -2.3292 | -7.65 | 0.0000 *** |
| CMA | -0.8061 | -2.61 | 0.0095 ** |

_Interpretation: Large-cap tilt; Weak profitability; Aggressive investment; Significant positive alpha_

### SMA

- Period: `2025-04-03` to `2026-03-31` (249 obs)
- R² = 0.1935 (adjusted = 0.1769)
- Alpha (annualized): **-10.84%** (daily = -0.000430, t = -0.47, p = 0.6390)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2961 | +3.27 | 0.0012 ** |
| SMB | +0.7074 | +4.14 | 0.0000 *** |
| HML | -0.1967 | -1.10 | 0.2720  |
| RMW | +0.1508 | +0.83 | 0.4095  |
| CMA | +0.5857 | +2.50 | 0.0132 * |

_Interpretation: Small-cap tilt; Conservative investment; Modest factor fit_

### AM

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.1946 (adjusted = 0.1848)
- Alpha (annualized): **+19.35%** (daily = +0.000768, t = +1.14, p = 0.2547)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6180 | +8.68 | 0.0000 *** |
| SMB | -0.2544 | -2.08 | 0.0378 * |
| HML | +0.3808 | +3.45 | 0.0006 *** |
| RMW | -0.2560 | -1.87 | 0.0621  |
| CMA | +0.0567 | +0.41 | 0.6835  |

_Interpretation: Modest factor fit_

### ASTS

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.2953 (adjusted = 0.2868)
- Alpha (annualized): **+133.96%** (daily = +0.005316, t = +1.85, p = 0.0646)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4677 | +4.84 | 0.0000 *** |
| SMB | +1.5163 | +2.91 | 0.0038 ** |
| HML | -1.4944 | -3.18 | 0.0016 ** |
| RMW | -2.7778 | -4.76 | 0.0000 *** |
| CMA | +0.0859 | +0.14 | 0.8848  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### API

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.0687 (adjusted = 0.0575)
- Alpha (annualized): **+65.42%** (daily = +0.002596, t = +0.81, p = 0.4163)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.1447 | +0.43 | 0.6684  |
| SMB | +0.7371 | +1.27 | 0.2036  |
| HML | -1.3215 | -2.53 | 0.0118 * |
| RMW | -1.5644 | -2.41 | 0.0163 * |
| CMA | +0.6472 | +0.98 | 0.3268  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### BATL

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.0083 (adjusted = -0.0037)
- Alpha (annualized): **+264.54%** (daily = +0.010498, t = +1.26, p = 0.2083)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.0125 | +0.01 | 0.9887  |
| SMB | +0.7651 | +0.51 | 0.6129  |
| HML | -1.8094 | -1.33 | 0.1855  |
| RMW | +2.6579 | +1.57 | 0.1174  |
| CMA | -0.3816 | -0.22 | 0.8247  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Low explanatory power — likely sentiment-driven_

### ES

- Period: `2024-07-26` to `2026-03-31` (421 obs)
- R² = 0.0841 (adjusted = 0.0731)
- Alpha (annualized): **+0.81%** (daily = +0.000032, t = +0.04, p = 0.9651)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3638 | +4.65 | 0.0000 *** |
| SMB | -0.0937 | -0.70 | 0.4847  |
| HML | +0.4598 | +3.80 | 0.0002 *** |
| RMW | -0.0900 | -0.60 | 0.5496  |
| CMA | +0.2544 | +1.67 | 0.0964  |

_Interpretation: Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._