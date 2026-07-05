# Weekly Report — `pennystocks` — 2026-W27

Generated: 2026-07-05  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W27.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| LGO | -25.34% | +1.399 | +0.385 | +0.644 | -1.447 | -0.055 | 0.157 | 436 | Value tilt; Weak profitability; Modest factor fit |
| CXAI | -47.83% | -0.676 | +3.828 | -3.299 | -1.296 | +0.208 | 0.153 | 436 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| CWD | -3.79% | +0.530 | -2.199 | +1.370 | -3.954 | -1.367 | 0.017 | 436 | Large-cap tilt; Value tilt; Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven |
| SLS | +91.05% | +0.279 | +0.394 | +0.138 | -1.882 | -0.963 | 0.077 | 436 | Weak profitability; Aggressive investment; Modest factor fit |
| SURG | -37.91% | +0.565 | +1.191 | -0.325 | -0.602 | -0.432 | 0.046 | 436 | Small-cap tilt; Weak profitability; Low explanatory power — likely sentiment-driven |
| RS | -6.14% | +0.890 | +0.708 | +0.490 | +0.368 | +0.298 | 0.456 | 436 | Small-cap tilt |
| CABA | -19.17% | +0.761 | +1.805 | -0.873 | -2.457 | +0.487 | 0.161 | 436 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| SRFM | +49.01% | +1.207 | +0.986 | -1.310 | -3.594 | +1.392 | 0.132 | 436 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| VIVS | +34.85% | +0.459 | +1.145 | -0.034 | +2.080 | -0.489 | 0.007 | 436 | Small-cap tilt; Robust profitability; Low explanatory power — likely sentiment-driven |
| YRD | -46.85% | +0.757 | +0.010 | +0.235 | -0.916 | +0.354 | 0.065 | 436 | Weak profitability; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| VIVS | **90.00** | 33.33 | 26.67 | 30.00 | 0.013 | +0.531 | 1.4969 | 0.0871 | 186 |
| CWD | **80.00** | 30.00 | 16.67 | 33.33 | 0.035 | -0.256 | 4.6494 | 0.2706 | 186 |
| LGO | **70.00** | 16.67 | 33.33 | 20.00 | 0.180 | +0.969 | 0.9840 | 0.0573 | 186 |
| SLS | **63.33** | 20.00 | 30.00 | 13.33 | 0.132 | +0.723 | 0.9307 | 0.0542 | 186 |
| SURG | **60.00** | 26.67 | 23.33 | 10.00 | 0.087 | +0.464 | 0.8875 | 0.0517 | 186 |
| SRFM | **50.00** | 13.33 | 10.00 | 26.67 | 0.218 | -1.084 | 1.0686 | 0.0622 | 186 |
| YRD | **43.33** | 23.33 | 13.33 | 6.67 | 0.094 | -0.532 | 0.6794 | 0.0395 | 186 |
| CXAI | **33.33** | 10.00 | 6.67 | 16.67 | 0.219 | -1.135 | 0.9653 | 0.0562 | 186 |
| CABA | **33.33** | 6.67 | 3.33 | 23.33 | 0.258 | -1.156 | 1.0274 | 0.0598 | 186 |
| RS | **26.67** | 3.33 | 20.00 | 3.33 | 0.357 | +0.103 | 0.2239 | 0.0130 | 186 |

## Per-ticker FF5 Detail

### LGO

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.1565 (adjusted = 0.1467)
- Alpha (annualized): **-25.34%** (daily = -0.001006, t = -0.43, p = 0.6693)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3988 | +5.59 | 0.0000 *** |
| SMB | +0.3846 | +0.95 | 0.3429  |
| HML | +0.6444 | +1.68 | 0.0944  |
| RMW | -1.4468 | -2.99 | 0.0029 ** |
| CMA | -0.0551 | -0.11 | 0.9100  |

_Interpretation: Value tilt; Weak profitability; Modest factor fit_

### CXAI

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.1534 (adjusted = 0.1435)
- Alpha (annualized): **-47.83%** (daily = -0.001898, t = -0.51, p = 0.6112)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.6760 | -1.70 | 0.0893  |
| SMB | +3.8285 | +5.96 | 0.0000 *** |
| HML | -3.2986 | -5.41 | 0.0000 *** |
| RMW | -1.2961 | -1.69 | 0.0916  |
| CMA | +0.2084 | +0.27 | 0.7877  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### CWD

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.0173 (adjusted = 0.0058)
- Alpha (annualized): **-3.79%** (daily = -0.000150, t = -0.02, p = 0.9865)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5304 | +0.56 | 0.5759  |
| SMB | -2.1989 | -1.43 | 0.1522  |
| HML | +1.3701 | +0.94 | 0.3468  |
| RMW | -3.9536 | -2.16 | 0.0312 * |
| CMA | -1.3672 | -0.74 | 0.4592  |

_Interpretation: Large-cap tilt; Value tilt; Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven_

### SLS

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.0771 (adjusted = 0.0664)
- Alpha (annualized): **+91.05%** (daily = +0.003613, t = +1.41, p = 0.1586)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2785 | +1.02 | 0.3068  |
| SMB | +0.3943 | +0.90 | 0.3712  |
| HML | +0.1378 | +0.33 | 0.7418  |
| RMW | -1.8818 | -3.58 | 0.0004 *** |
| CMA | -0.9628 | -1.82 | 0.0701  |

_Interpretation: Weak profitability; Aggressive investment; Modest factor fit_

### SURG

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.0463 (adjusted = 0.0353)
- Alpha (annualized): **-37.91%** (daily = -0.001504, t = -0.48, p = 0.6313)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5653 | +1.70 | 0.0906  |
| SMB | +1.1913 | +2.21 | 0.0277 * |
| HML | -0.3248 | -0.63 | 0.5261  |
| RMW | -0.6018 | -0.93 | 0.3503  |
| CMA | -0.4323 | -0.67 | 0.5059  |

_Interpretation: Small-cap tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

### RS

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.4561 (adjusted = 0.4498)
- Alpha (annualized): **-6.14%** (daily = -0.000243, t = -0.40, p = 0.6903)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8904 | +13.70 | 0.0000 *** |
| SMB | +0.7078 | +6.73 | 0.0000 *** |
| HML | +0.4898 | +4.91 | 0.0000 *** |
| RMW | +0.3675 | +2.93 | 0.0036 ** |
| CMA | +0.2978 | +2.35 | 0.0191 * |

_Interpretation: Small-cap tilt_

### CABA

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.1615 (adjusted = 0.1517)
- Alpha (annualized): **-19.17%** (daily = -0.000761, t = -0.24, p = 0.8127)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7609 | +2.23 | 0.0263 * |
| SMB | +1.8048 | +3.27 | 0.0012 ** |
| HML | -0.8734 | -1.67 | 0.0964  |
| RMW | -2.4571 | -3.73 | 0.0002 *** |
| CMA | +0.4866 | +0.73 | 0.4647  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### SRFM

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.1320 (adjusted = 0.1219)
- Alpha (annualized): **+49.01%** (daily = +0.001945, t = +0.42, p = 0.6768)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2069 | +2.43 | 0.0154 * |
| SMB | +0.9864 | +1.23 | 0.2198  |
| HML | -1.3098 | -1.72 | 0.0862  |
| RMW | -3.5940 | -3.75 | 0.0002 *** |
| CMA | +1.3924 | +1.44 | 0.1503  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### VIVS

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.0070 (adjusted = -0.0045)
- Alpha (annualized): **+34.85%** (daily = +0.001383, t = +0.21, p = 0.8362)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.4589 | +0.64 | 0.5194  |
| SMB | +1.1455 | +0.99 | 0.3204  |
| HML | -0.0341 | -0.03 | 0.9751  |
| RMW | +2.0803 | +1.51 | 0.1307  |
| CMA | -0.4887 | -0.35 | 0.7245  |

_Interpretation: Small-cap tilt; Robust profitability; Low explanatory power — likely sentiment-driven_

### YRD

- Period: `2024-07-05` to `2026-03-31` (436 obs)
- R² = 0.0646 (adjusted = 0.0537)
- Alpha (annualized): **-46.85%** (daily = -0.001859, t = -0.87, p = 0.3830)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7565 | +3.34 | 0.0009 *** |
| SMB | +0.0102 | +0.03 | 0.9777  |
| HML | +0.2351 | +0.68 | 0.4995  |
| RMW | -0.9162 | -2.09 | 0.0368 * |
| CMA | +0.3538 | +0.80 | 0.4230  |

_Interpretation: Weak profitability; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._