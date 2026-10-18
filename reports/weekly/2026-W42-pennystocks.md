# Weekly Report — `pennystocks` — 2026-W42

Generated: 2026-10-18  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W42.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| TCRT | +56.79% | +0.176 | -0.438 | +0.560 | -1.874 | -0.767 | 0.027 | 362 | Value tilt; Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven |
| BETR | +80.41% | +0.896 | +0.878 | +0.743 | -2.790 | +0.077 | 0.134 | 362 | Small-cap tilt; Value tilt; Weak profitability; Modest factor fit |
| BEEM | -58.45% | +0.736 | +1.646 | -0.653 | -1.802 | -0.069 | 0.183 | 362 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| HTZ | +59.56% | +1.022 | +2.126 | +0.664 | +0.295 | +0.226 | 0.100 | 362 | Small-cap tilt; Value tilt; Modest factor fit |
| GENK | -84.15% | +1.480 | +1.069 | +0.152 | +0.392 | +0.322 | 0.174 | 362 | Small-cap tilt; Modest factor fit |
| IP | -19.46% | +1.153 | +0.469 | +0.563 | +0.332 | +0.991 | 0.325 | 362 | Value tilt; Conservative investment |
| IQ | -39.37% | +1.043 | +0.277 | +0.144 | -0.578 | +0.135 | 0.153 | 362 | Weak profitability; Modest factor fit |
| AAPL | +3.39% | +1.352 | -0.157 | -0.046 | +0.757 | +0.202 | 0.554 | 362 | Robust profitability |
| ES | +0.37% | +0.393 | -0.095 | +0.453 | -0.140 | +0.389 | 0.099 | 362 | Modest factor fit |
| AVGO | +49.11% | +1.602 | -0.080 | -1.278 | +0.098 | -0.264 | 0.459 | 362 | Growth tilt |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| HTZ | **66.67** | 26.67 | 13.33 | 26.67 | 0.126 | -0.255 | 1.0858 | 0.0479 | 112 |
| TCRT | **66.67** | 30.00 | 6.67 | 30.00 | 0.110 | -0.548 | 1.1200 | 0.0494 | 112 |
| GENK | **63.33** | 23.33 | 16.67 | 23.33 | 0.148 | -0.201 | 0.9011 | 0.0397 | 112 |
| ES | **60.00** | 33.33 | 20.00 | 6.67 | 0.063 | -0.155 | 0.3872 | 0.0171 | 112 |
| IQ | **60.00** | 20.00 | 23.33 | 16.67 | 0.204 | -0.011 | 0.5848 | 0.0258 | 112 |
| BEEM | **56.67** | 6.67 | 30.00 | 20.00 | 0.431 | +0.410 | 0.7776 | 0.0343 | 112 |
| BETR | **53.33** | 16.67 | 3.33 | 33.33 | 0.234 | -0.567 | 1.4883 | 0.0656 | 112 |
| AVGO | **46.67** | 3.33 | 33.33 | 10.00 | 0.578 | +0.516 | 0.4161 | 0.0184 | 112 |
| AAPL | **43.33** | 13.33 | 26.67 | 3.33 | 0.352 | +0.090 | 0.2475 | 0.0109 | 112 |
| IP | **33.33** | 10.00 | 10.00 | 13.33 | 0.419 | -0.291 | 0.4894 | 0.0216 | 112 |

## Per-ticker FF5 Detail

### TCRT

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.0269 (adjusted = 0.0132)
- Alpha (annualized): **+56.79%** (daily = +0.002254, t = +0.57, p = 0.5669)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.1764 | +0.44 | 0.6637  |
| SMB | -0.4378 | -0.61 | 0.5414  |
| HML | +0.5599 | +0.88 | 0.3780  |
| RMW | -1.8743 | -2.42 | 0.0158 * |
| CMA | -0.7667 | -0.92 | 0.3588  |

_Interpretation: Value tilt; Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven_

### BETR

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.1345 (adjusted = 0.1223)
- Alpha (annualized): **+80.41%** (daily = +0.003191, t = +0.93, p = 0.3516)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8962 | +2.54 | 0.0115 * |
| SMB | +0.8780 | +1.41 | 0.1597  |
| HML | +0.7427 | +1.35 | 0.1793  |
| RMW | -2.7900 | -4.15 | 0.0000 *** |
| CMA | +0.0773 | +0.11 | 0.9152  |

_Interpretation: Small-cap tilt; Value tilt; Weak profitability; Modest factor fit_

### BEEM

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.1828 (adjusted = 0.1714)
- Alpha (annualized): **-58.45%** (daily = -0.002319, t = -0.85, p = 0.3953)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7362 | +2.62 | 0.0092 ** |
| SMB | +1.6462 | +3.32 | 0.0010 ** |
| HML | -0.6526 | -1.48 | 0.1386  |
| RMW | -1.8018 | -3.36 | 0.0009 *** |
| CMA | -0.0695 | -0.12 | 0.9044  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### HTZ

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.0996 (adjusted = 0.0870)
- Alpha (annualized): **+59.56%** (daily = +0.002364, t = +0.73, p = 0.4632)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0219 | +3.08 | 0.0022 ** |
| SMB | +2.1263 | +3.63 | 0.0003 *** |
| HML | +0.6643 | +1.28 | 0.2015  |
| RMW | +0.2953 | +0.47 | 0.6410  |
| CMA | +0.2262 | +0.33 | 0.7407  |

_Interpretation: Small-cap tilt; Value tilt; Modest factor fit_

### GENK

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.1743 (adjusted = 0.1627)
- Alpha (annualized): **-84.15%** (daily = -0.003339, t = -1.56, p = 0.1186)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4802 | +6.73 | 0.0000 *** |
| SMB | +1.0689 | +2.75 | 0.0063 ** |
| HML | +0.1519 | +0.44 | 0.6594  |
| RMW | +0.3920 | +0.93 | 0.3509  |
| CMA | +0.3220 | +0.71 | 0.4776  |

_Interpretation: Small-cap tilt; Modest factor fit_

### IP

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.3249 (adjusted = 0.3154)
- Alpha (annualized): **-19.46%** (daily = -0.000772, t = -0.71, p = 0.4811)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1535 | +10.22 | 0.0000 *** |
| SMB | +0.4695 | +2.35 | 0.0191 * |
| HML | +0.5632 | +3.19 | 0.0016 ** |
| RMW | +0.3324 | +1.54 | 0.1235  |
| CMA | +0.9910 | +4.27 | 0.0000 *** |

_Interpretation: Value tilt; Conservative investment_

### IQ

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.1530 (adjusted = 0.1411)
- Alpha (annualized): **-39.37%** (daily = -0.001562, t = -0.88, p = 0.3769)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0427 | +5.73 | 0.0000 *** |
| SMB | +0.2773 | +0.86 | 0.3893  |
| HML | +0.1444 | +0.51 | 0.6126  |
| RMW | -0.5776 | -1.66 | 0.0971  |
| CMA | +0.1345 | +0.36 | 0.7198  |

_Interpretation: Weak profitability; Modest factor fit_

### AAPL

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.5543 (adjusted = 0.5480)
- Alpha (annualized): **+3.39%** (daily = +0.000134, t = +0.20, p = 0.8390)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3518 | +19.84 | 0.0000 *** |
| SMB | -0.1573 | -1.31 | 0.1922  |
| HML | -0.0460 | -0.43 | 0.6663  |
| RMW | +0.7573 | +5.83 | 0.0000 *** |
| CMA | +0.2016 | +1.44 | 0.1513  |

_Interpretation: Robust profitability_

### ES

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.0990 (adjusted = 0.0863)
- Alpha (annualized): **+0.37%** (daily = +0.000014, t = +0.02, p = 0.9860)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3926 | +4.61 | 0.0000 *** |
| SMB | -0.0946 | -0.63 | 0.5298  |
| HML | +0.4526 | +3.40 | 0.0008 *** |
| RMW | -0.1400 | -0.86 | 0.3891  |
| CMA | +0.3891 | +2.22 | 0.0270 * |

_Interpretation: Modest factor fit_

### AVGO

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.4586 (adjusted = 0.4510)
- Alpha (annualized): **+49.11%** (daily = +0.001949, t = +1.45, p = 0.1469)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6022 | +11.59 | 0.0000 *** |
| SMB | -0.0801 | -0.33 | 0.7430  |
| HML | -1.2783 | -5.91 | 0.0000 *** |
| RMW | +0.0980 | +0.37 | 0.7103  |
| CMA | -0.2635 | -0.93 | 0.3548  |

_Interpretation: Growth tilt_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._