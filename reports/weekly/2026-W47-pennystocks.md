# Weekly Report — `pennystocks` — 2026-W47

Generated: 2026-11-16  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W47.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| NXXT | -113.68% | +0.968 | -0.139 | +1.682 | -1.696 | +0.480 | 0.052 | 342 | Value tilt; Weak profitability; Modest factor fit |
| OMH | +903.66% | -5.595 | +4.902 | -3.455 | +6.086 | +1.404 | 0.022 | 342 | Small-cap tilt; Growth tilt; Robust profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| VIVK | -156.79% | -0.106 | +0.565 | -0.366 | -1.747 | +0.762 | 0.011 | 342 | Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| PLCE | -54.03% | +1.717 | +2.357 | -0.070 | +0.665 | +0.127 | 0.159 | 342 | Small-cap tilt; Robust profitability; Modest factor fit |
| POAS | +168.61% | +1.693 | -1.981 | -2.159 | +1.935 | +4.483 | 0.039 | 93 | Large-cap tilt; Growth tilt; Robust profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| DTE | +5.89% | +0.336 | -0.199 | +0.567 | -0.200 | +0.082 | 0.165 | 342 | Value tilt; Modest factor fit |
| AVGO | +60.85% | +1.553 | -0.123 | -1.425 | +0.075 | -0.154 | 0.460 | 342 | Growth tilt |
| CC | +23.26% | +1.880 | +2.154 | +0.432 | +0.188 | +1.077 | 0.465 | 342 | Small-cap tilt; Conservative investment |
| MS | -1.43% | +1.436 | -0.203 | +0.814 | -0.477 | -0.071 | 0.691 | 342 | Value tilt |
| NVDA | +18.25% | +1.551 | -0.919 | -1.365 | -0.330 | +1.304 | 0.681 | 342 | Large-cap tilt; Growth tilt; Conservative investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| POAS | **83.33** | 33.33 | 20.00 | 30.00 | 0.044 | +0.005 | 3.1835 | 0.1209 | 92 |
| OMH | **63.33** | 26.67 | 10.00 | 26.67 | 0.075 | -0.588 | 1.8373 | 0.0698 | 92 |
| CC | **60.00** | 13.33 | 30.00 | 16.67 | 0.365 | +0.653 | 0.8721 | 0.0331 | 92 |
| VIVK | **60.00** | 23.33 | 3.33 | 33.33 | 0.098 | -2.270 | 4.4959 | 0.1708 | 92 |
| DTE | **56.67** | 30.00 | 23.33 | 3.33 | 0.067 | +0.036 | 0.2604 | 0.0099 | 92 |
| NXXT | **50.00** | 20.00 | 6.67 | 23.33 | 0.245 | -2.038 | 1.8062 | 0.0686 | 92 |
| PLCE | **50.00** | 16.67 | 13.33 | 20.00 | 0.262 | -0.160 | 1.2207 | 0.0464 | 92 |
| AVGO | **46.67** | 6.67 | 26.67 | 13.33 | 0.578 | +0.420 | 0.5033 | 0.0191 | 92 |
| NVDA | **43.33** | 3.33 | 33.33 | 6.67 | 0.672 | +0.666 | 0.3344 | 0.0127 | 92 |
| MS | **36.67** | 10.00 | 16.67 | 10.00 | 0.539 | -0.136 | 0.3451 | 0.0131 | 92 |

## Per-ticker FF5 Detail

### NXXT

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.0516 (adjusted = 0.0375)
- Alpha (annualized): **-113.68%** (daily = -0.004511, t = -1.12, p = 0.2643)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9677 | +2.32 | 0.0207 * |
| SMB | -0.1389 | -0.19 | 0.8519  |
| HML | +1.6816 | +2.44 | 0.0154 * |
| RMW | -1.6961 | -2.18 | 0.0299 * |
| CMA | +0.4799 | +0.55 | 0.5829  |

_Interpretation: Value tilt; Weak profitability; Modest factor fit_

### OMH

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.0223 (adjusted = 0.0078)
- Alpha (annualized): **+903.66%** (daily = +0.035860, t = +1.30, p = 0.1952)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -5.5948 | -1.96 | 0.0506  |
| SMB | +4.9024 | +0.96 | 0.3363  |
| HML | -3.4546 | -0.73 | 0.4656  |
| RMW | +6.0857 | +1.14 | 0.2542  |
| CMA | +1.4039 | +0.23 | 0.8145  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### VIVK

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.0115 (adjusted = -0.0033)
- Alpha (annualized): **-156.79%** (daily = -0.006222, t = -0.93, p = 0.3551)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.1063 | -0.15 | 0.8783  |
| SMB | +0.5650 | +0.46 | 0.6485  |
| HML | -0.3659 | -0.32 | 0.7505  |
| RMW | -1.7471 | -1.35 | 0.1784  |
| CMA | +0.7619 | +0.52 | 0.6007  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### PLCE

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.1588 (adjusted = 0.1463)
- Alpha (annualized): **-54.03%** (daily = -0.002144, t = -0.67, p = 0.5008)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7175 | +5.23 | 0.0000 *** |
| SMB | +2.3575 | +4.02 | 0.0001 *** |
| HML | -0.0704 | -0.13 | 0.8972  |
| RMW | +0.6646 | +1.08 | 0.2794  |
| CMA | +0.1275 | +0.19 | 0.8532  |

_Interpretation: Small-cap tilt; Robust profitability; Modest factor fit_

### POAS

- Period: `2025-11-14` to `2026-03-31` (93 obs)
- R² = 0.0394 (adjusted = -0.0159)
- Alpha (annualized): **+168.61%** (daily = +0.006691, t = +0.51, p = 0.6121)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6932 | +0.90 | 0.3723  |
| SMB | -1.9815 | -0.62 | 0.5392  |
| HML | -2.1587 | -0.76 | 0.4489  |
| RMW | +1.9351 | +0.72 | 0.4733  |
| CMA | +4.4829 | +0.99 | 0.3236  |

_Interpretation: Large-cap tilt; Growth tilt; Robust profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### DTE

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.1653 (adjusted = 0.1529)
- Alpha (annualized): **+5.89%** (daily = +0.000234, t = +0.44, p = 0.6629)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3363 | +6.08 | 0.0000 *** |
| SMB | -0.1992 | -2.02 | 0.0443 * |
| HML | +0.5666 | +6.18 | 0.0000 *** |
| RMW | -0.2003 | -1.94 | 0.0533  |
| CMA | +0.0821 | +0.71 | 0.4792  |

_Interpretation: Value tilt; Modest factor fit_

### AVGO

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.4604 (adjusted = 0.4523)
- Alpha (annualized): **+60.85%** (daily = +0.002415, t = +1.72, p = 0.0860)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5528 | +10.73 | 0.0000 *** |
| SMB | -0.1229 | -0.48 | 0.6347  |
| HML | -1.4253 | -5.94 | 0.0000 *** |
| RMW | +0.0753 | +0.28 | 0.7808  |
| CMA | -0.1543 | -0.51 | 0.6116  |

_Interpretation: Growth tilt_

### CC

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.4654 (adjusted = 0.4574)
- Alpha (annualized): **+23.26%** (daily = +0.000923, t = +0.56, p = 0.5730)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.8802 | +11.14 | 0.0000 *** |
| SMB | +2.1541 | +7.15 | 0.0000 *** |
| HML | +0.4324 | +1.54 | 0.1233  |
| RMW | +0.1879 | +0.60 | 0.5517  |
| CMA | +1.0771 | +3.04 | 0.0025 ** |

_Interpretation: Small-cap tilt; Conservative investment_

### MS

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.6914 (adjusted = 0.6868)
- Alpha (annualized): **-1.43%** (daily = -0.000057, t = -0.10, p = 0.9235)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4360 | +23.62 | 0.0000 *** |
| SMB | -0.2029 | -1.87 | 0.0624  |
| HML | +0.8142 | +8.08 | 0.0000 *** |
| RMW | -0.4767 | -4.20 | 0.0000 *** |
| CMA | -0.0706 | -0.55 | 0.5803  |

_Interpretation: Value tilt_

### NVDA

- Period: `2024-11-15` to `2026-03-31` (342 obs)
- R² = 0.6812 (adjusted = 0.6764)
- Alpha (annualized): **+18.25%** (daily = +0.000724, t = +0.80, p = 0.4252)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5513 | +16.58 | 0.0000 *** |
| SMB | -0.9188 | -5.50 | 0.0000 *** |
| HML | -1.3655 | -8.80 | 0.0000 *** |
| RMW | -0.3303 | -1.89 | 0.0598  |
| CMA | +1.3037 | +6.64 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._