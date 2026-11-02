# Weekly Report — `Shortsqueeze` — 2026-W45

Generated: 2026-11-02  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W45.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| AAPL | +2.94% | +1.355 | -0.154 | -0.029 | +0.771 | +0.183 | 0.554 | 352 | Robust profitability |
| ALL | -3.21% | +0.677 | -0.277 | +0.768 | +0.303 | -0.051 | 0.215 | 352 | Value tilt |
| AM | +24.36% | +0.593 | -0.344 | +0.393 | -0.305 | +0.142 | 0.191 | 352 | Modest factor fit |
| AMD | +13.11% | +1.603 | -0.601 | -0.375 | -1.647 | -0.303 | 0.481 | 352 | Large-cap tilt; Weak profitability |
| API | +52.18% | +0.210 | +0.911 | -1.363 | -1.206 | +0.489 | 0.095 | 352 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| ASTS | +113.95% | +1.277 | +0.960 | -1.201 | -2.931 | -0.331 | 0.313 | 352 | Small-cap tilt; Growth tilt; Weak profitability |
| BB | +23.66% | +1.004 | +0.206 | -0.473 | -1.231 | +0.810 | 0.275 | 352 | Weak profitability; Conservative investment |
| CC | +23.12% | +1.758 | +2.089 | +0.184 | +0.214 | +1.387 | 0.436 | 352 | Small-cap tilt; Conservative investment |
| DTE | +2.21% | +0.297 | -0.224 | +0.535 | -0.238 | +0.122 | 0.149 | 352 | Value tilt; Modest factor fit |
| ES | -1.00% | +0.395 | -0.087 | +0.424 | -0.127 | +0.385 | 0.097 | 352 | Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| CC | **73.33** | 13.33 | 30.00 | 30.00 | 0.340 | +0.550 | 0.8163 | 0.0334 | 102 |
| ASTS | **70.00** | 10.00 | 26.67 | 33.33 | 0.372 | +0.309 | 1.4243 | 0.0582 | 102 |
| AM | **63.33** | 33.33 | 20.00 | 10.00 | 0.041 | +0.114 | 0.2967 | 0.0121 | 102 |
| ES | **60.00** | 30.00 | 13.33 | 16.67 | 0.068 | -0.170 | 0.4338 | 0.0177 | 102 |
| AMD | **60.00** | 3.33 | 33.33 | 23.33 | 0.564 | +1.000 | 0.6181 | 0.0253 | 102 |
| API | **56.67** | 23.33 | 6.67 | 26.67 | 0.108 | -0.309 | 0.6538 | 0.0267 | 102 |
| DTE | **46.67** | 26.67 | 16.67 | 3.33 | 0.069 | +0.025 | 0.2441 | 0.0100 | 102 |
| BB | **43.33** | 20.00 | 3.33 | 20.00 | 0.236 | -0.552 | 0.4968 | 0.0203 | 102 |
| ALL | **40.00** | 16.67 | 10.00 | 13.33 | 0.250 | -0.271 | 0.3059 | 0.0125 | 102 |
| AAPL | **36.67** | 6.67 | 23.33 | 6.67 | 0.386 | +0.149 | 0.2547 | 0.0104 | 102 |

## Per-ticker FF5 Detail

### AAPL

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.5543 (adjusted = 0.5479)
- Alpha (annualized): **+2.94%** (daily = +0.000117, t = +0.17, p = 0.8631)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3551 | +19.63 | 0.0000 *** |
| SMB | -0.1545 | -1.26 | 0.2088  |
| HML | -0.0293 | -0.27 | 0.7878  |
| RMW | +0.7706 | +5.86 | 0.0000 *** |
| CMA | +0.1825 | +1.28 | 0.2011  |

_Interpretation: Robust profitability_

### ALL

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.2148 (adjusted = 0.2034)
- Alpha (annualized): **-3.21%** (daily = -0.000127, t = -0.17, p = 0.8685)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6771 | +8.62 | 0.0000 *** |
| SMB | -0.2767 | -1.98 | 0.0483 * |
| HML | +0.7681 | +6.20 | 0.0000 *** |
| RMW | +0.3032 | +2.03 | 0.0436 * |
| CMA | -0.0505 | -0.31 | 0.7556  |

_Interpretation: Value tilt_

### AM

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.1911 (adjusted = 0.1795)
- Alpha (annualized): **+24.36%** (daily = +0.000967, t = +1.30, p = 0.1956)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5934 | +7.80 | 0.0000 *** |
| SMB | -0.3443 | -2.55 | 0.0113 * |
| HML | +0.3930 | +3.28 | 0.0012 ** |
| RMW | -0.3051 | -2.10 | 0.0361 * |
| CMA | +0.1419 | +0.90 | 0.3670  |

_Interpretation: Modest factor fit_

### AMD

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.4812 (adjusted = 0.4737)
- Alpha (annualized): **+13.11%** (daily = +0.000520, t = +0.36, p = 0.7189)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6028 | +10.88 | 0.0000 *** |
| SMB | -0.6010 | -2.29 | 0.0224 * |
| HML | -0.3745 | -1.61 | 0.1079  |
| RMW | -1.6473 | -5.86 | 0.0000 *** |
| CMA | -0.3026 | -0.99 | 0.3207  |

_Interpretation: Large-cap tilt; Weak profitability_

### API

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.0948 (adjusted = 0.0817)
- Alpha (annualized): **+52.18%** (daily = +0.002071, t = +0.73, p = 0.4685)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2103 | +0.72 | 0.4707  |
| SMB | +0.9115 | +1.76 | 0.0792  |
| HML | -1.3627 | -2.97 | 0.0032 ** |
| RMW | -1.2060 | -2.17 | 0.0305 * |
| CMA | +0.4894 | +0.81 | 0.4163  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### ASTS

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.3131 (adjusted = 0.3032)
- Alpha (annualized): **+113.95%** (daily = +0.004522, t = +1.59, p = 0.1119)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2773 | +4.41 | 0.0000 *** |
| SMB | +0.9600 | +1.86 | 0.0630  |
| HML | -1.2007 | -2.63 | 0.0089 ** |
| RMW | -2.9309 | -5.31 | 0.0000 *** |
| CMA | -0.3306 | -0.55 | 0.5806  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### BB

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.2750 (adjusted = 0.2645)
- Alpha (annualized): **+23.66%** (daily = +0.000939, t = +0.58, p = 0.5626)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0042 | +6.07 | 0.0000 *** |
| SMB | +0.2060 | +0.70 | 0.4838  |
| HML | -0.4726 | -1.81 | 0.0708  |
| RMW | -1.2312 | -3.91 | 0.0001 *** |
| CMA | +0.8103 | +2.37 | 0.0182 * |

_Interpretation: Weak profitability; Conservative investment_

### CC

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.4362 (adjusted = 0.4280)
- Alpha (annualized): **+23.12%** (daily = +0.000918, t = +0.55, p = 0.5835)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7578 | +10.30 | 0.0000 *** |
| SMB | +2.0892 | +6.89 | 0.0000 *** |
| HML | +0.1843 | +0.69 | 0.4937  |
| RMW | +0.2135 | +0.66 | 0.5120  |
| CMA | +1.3869 | +3.94 | 0.0001 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### DTE

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.1488 (adjusted = 0.1365)
- Alpha (annualized): **+2.21%** (daily = +0.000088, t = +0.16, p = 0.8719)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2975 | +5.35 | 0.0000 *** |
| SMB | -0.2244 | -2.27 | 0.0238 * |
| HML | +0.5351 | +6.10 | 0.0000 *** |
| RMW | -0.2377 | -2.24 | 0.0255 * |
| CMA | +0.1221 | +1.06 | 0.2883  |

_Interpretation: Value tilt; Modest factor fit_

### ES

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.0971 (adjusted = 0.0841)
- Alpha (annualized): **-1.00%** (daily = -0.000040, t = -0.05, p = 0.9625)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3949 | +4.60 | 0.0000 *** |
| SMB | -0.0870 | -0.57 | 0.5695  |
| HML | +0.4236 | +3.13 | 0.0019 ** |
| RMW | -0.1270 | -0.78 | 0.4387  |
| CMA | +0.3849 | +2.17 | 0.0308 * |

_Interpretation: Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._