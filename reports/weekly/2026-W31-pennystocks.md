# Weekly Report — `pennystocks` — 2026-W31

Generated: 2026-08-02  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W31.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| DFNS | +488.08% | -2.142 | -0.762 | -3.270 | -1.369 | +2.897 | 0.006 | 416 | Large-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| OTLK | -108.10% | +0.395 | +1.505 | -1.532 | -0.145 | -0.044 | 0.043 | 416 | Small-cap tilt; Growth tilt; Low explanatory power — likely sentiment-driven |
| CXAI | -32.38% | -0.803 | +4.502 | -3.386 | -1.216 | -0.006 | 0.164 | 416 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| WU | -10.63% | +0.704 | +0.577 | +0.217 | +0.516 | +0.322 | 0.230 | 416 | Small-cap tilt; Robust profitability |
| LVWR | +21.87% | +2.220 | +2.932 | -0.638 | +0.902 | +1.581 | 0.094 | 416 | Small-cap tilt; Growth tilt; Robust profitability; Conservative investment; Modest factor fit |
| XRX | -109.31% | +1.647 | +1.599 | +0.284 | +0.689 | +0.675 | 0.277 | 416 | Small-cap tilt; Robust profitability; Conservative investment; Significant negative alpha |
| GOSS | -10.34% | +1.143 | +0.284 | +0.670 | -2.451 | +0.094 | 0.115 | 416 | Value tilt; Weak profitability; Modest factor fit |
| IP | -21.33% | +1.125 | +0.443 | +0.567 | +0.329 | +0.929 | 0.330 | 416 | Value tilt; Conservative investment |
| ES | -2.18% | +0.373 | -0.105 | +0.455 | -0.111 | +0.332 | 0.091 | 416 | Modest factor fit |
| DTE | +1.43% | +0.308 | -0.199 | +0.548 | -0.207 | +0.083 | 0.151 | 416 | Value tilt; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| OTLK | **73.33** | 33.33 | 6.67 | 33.33 | 0.059 | -1.445 | 1.6420 | 0.0912 | 166 |
| DFNS | **70.00** | 23.33 | 16.67 | 30.00 | 0.153 | -1.018 | 1.5047 | 0.0836 | 166 |
| ES | **66.67** | 30.00 | 30.00 | 6.67 | 0.063 | -0.153 | 0.2930 | 0.0163 | 166 |
| DTE | **63.33** | 26.67 | 33.33 | 3.33 | 0.069 | +0.053 | 0.1671 | 0.0093 | 166 |
| WU | **53.33** | 20.00 | 23.33 | 10.00 | 0.169 | -0.524 | 0.3093 | 0.0172 | 166 |
| LVWR | **46.67** | 13.33 | 10.00 | 23.33 | 0.185 | -1.157 | 1.2722 | 0.0707 | 166 |
| GOSS | **46.67** | 16.67 | 3.33 | 26.67 | 0.177 | -1.549 | 1.4158 | 0.0786 | 166 |
| IP | **43.33** | 3.33 | 26.67 | 13.33 | 0.350 | -0.223 | 0.3553 | 0.0197 | 166 |
| XRX | **43.33** | 6.67 | 20.00 | 16.67 | 0.259 | -0.696 | 0.6429 | 0.0357 | 166 |
| CXAI | **43.33** | 10.00 | 13.33 | 20.00 | 0.218 | -1.038 | 1.0473 | 0.0582 | 166 |

## Per-ticker FF5 Detail

### DFNS

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.0056 (adjusted = -0.0066)
- Alpha (annualized): **+488.08%** (daily = +0.019368, t = +0.95, p = 0.3451)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -2.1422 | -0.99 | 0.3227  |
| SMB | -0.7625 | -0.21 | 0.8373  |
| HML | -3.2702 | -0.97 | 0.3308  |
| RMW | -1.3685 | -0.33 | 0.7427  |
| CMA | +2.8971 | +0.67 | 0.5014  |

_Interpretation: Large-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### OTLK

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.0427 (adjusted = 0.0310)
- Alpha (annualized): **-108.10%** (daily = -0.004290, t = -1.13, p = 0.2595)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3949 | +0.98 | 0.3255  |
| SMB | +1.5046 | +2.19 | 0.0293 * |
| HML | -1.5317 | -2.46 | 0.0143 * |
| RMW | -0.1454 | -0.19 | 0.8508  |
| CMA | -0.0438 | -0.05 | 0.9563  |

_Interpretation: Small-cap tilt; Growth tilt; Low explanatory power — likely sentiment-driven_

### CXAI

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.1643 (adjusted = 0.1541)
- Alpha (annualized): **-32.38%** (daily = -0.001285, t = -0.33, p = 0.7401)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.8032 | -1.97 | 0.0501  |
| SMB | +4.5018 | +6.42 | 0.0000 *** |
| HML | -3.3860 | -5.34 | 0.0000 *** |
| RMW | -1.2156 | -1.54 | 0.1233  |
| CMA | -0.0059 | -0.01 | 0.9942  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### WU

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.2300 (adjusted = 0.2206)
- Alpha (annualized): **-10.63%** (daily = -0.000422, t = -0.53, p = 0.5966)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7042 | +8.38 | 0.0000 *** |
| SMB | +0.5767 | +4.00 | 0.0001 *** |
| HML | +0.2167 | +1.66 | 0.0975  |
| RMW | +0.5159 | +3.19 | 0.0015 ** |
| CMA | +0.3219 | +1.92 | 0.0550  |

_Interpretation: Small-cap tilt; Robust profitability_

### LVWR

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.0939 (adjusted = 0.0829)
- Alpha (annualized): **+21.87%** (daily = +0.000868, t = +0.16, p = 0.8697)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2200 | +3.98 | 0.0001 *** |
| SMB | +2.9316 | +3.06 | 0.0023 ** |
| HML | -0.6383 | -0.74 | 0.4617  |
| RMW | +0.9020 | +0.84 | 0.4018  |
| CMA | +1.5811 | +1.42 | 0.1553  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Conservative investment; Modest factor fit_

### XRX

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.2770 (adjusted = 0.2681)
- Alpha (annualized): **-109.31%** (daily = -0.004338, t = -2.47, p = 0.0139)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6471 | +8.88 | 0.0000 *** |
| SMB | +1.5986 | +5.03 | 0.0000 *** |
| HML | +0.2840 | +0.99 | 0.3245  |
| RMW | +0.6892 | +1.93 | 0.0543  |
| CMA | +0.6746 | +1.83 | 0.0683  |

_Interpretation: Small-cap tilt; Robust profitability; Conservative investment; Significant negative alpha_

### GOSS

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.1154 (adjusted = 0.1046)
- Alpha (annualized): **-10.34%** (daily = -0.000410, t = -0.13, p = 0.8972)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1431 | +3.41 | 0.0007 *** |
| SMB | +0.2841 | +0.49 | 0.6214  |
| HML | +0.6699 | +1.29 | 0.1988  |
| RMW | -2.4512 | -3.80 | 0.0002 *** |
| CMA | +0.0939 | +0.14 | 0.8882  |

_Interpretation: Value tilt; Weak profitability; Modest factor fit_

### IP

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.3298 (adjusted = 0.3216)
- Alpha (annualized): **-21.33%** (daily = -0.000846, t = -0.87, p = 0.3833)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1249 | +10.99 | 0.0000 *** |
| SMB | +0.4435 | +2.53 | 0.0119 * |
| HML | +0.5672 | +3.57 | 0.0004 *** |
| RMW | +0.3292 | +1.67 | 0.0957  |
| CMA | +0.9286 | +4.56 | 0.0000 *** |

_Interpretation: Value tilt; Conservative investment_

### ES

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.0914 (adjusted = 0.0803)
- Alpha (annualized): **-2.18%** (daily = -0.000086, t = -0.12, p = 0.9074)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3734 | +4.77 | 0.0000 *** |
| SMB | -0.1053 | -0.78 | 0.4335  |
| HML | +0.4549 | +3.74 | 0.0002 *** |
| RMW | -0.1115 | -0.74 | 0.4601  |
| CMA | +0.3324 | +2.13 | 0.0335 * |

_Interpretation: Modest factor fit_

### DTE

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.1509 (adjusted = 0.1405)
- Alpha (annualized): **+1.43%** (daily = +0.000057, t = +0.12, p = 0.9081)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3075 | +5.94 | 0.0000 *** |
| SMB | -0.1991 | -2.24 | 0.0254 * |
| HML | +0.5484 | +6.82 | 0.0000 *** |
| RMW | -0.2068 | -2.07 | 0.0386 * |
| CMA | +0.0828 | +0.80 | 0.4220  |

_Interpretation: Value tilt; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._