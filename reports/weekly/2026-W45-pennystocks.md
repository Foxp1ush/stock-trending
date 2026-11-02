# Weekly Report — `pennystocks` — 2026-W45

Generated: 2026-11-02  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W45.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| NRXP | +68.84% | +0.507 | +0.376 | -0.090 | -1.571 | +0.193 | 0.045 | 352 | Weak profitability; Low explanatory power — likely sentiment-driven |
| AAPL | +2.94% | +1.355 | -0.154 | -0.029 | +0.771 | +0.183 | 0.554 | 352 | Robust profitability |
| AMD | +13.11% | +1.603 | -0.601 | -0.375 | -1.647 | -0.303 | 0.481 | 352 | Large-cap tilt; Weak profitability |
| ALL | -3.21% | +0.677 | -0.277 | +0.768 | +0.303 | -0.051 | 0.215 | 352 | Value tilt |
| CC | +23.12% | +1.758 | +2.089 | +0.184 | +0.214 | +1.387 | 0.436 | 352 | Small-cap tilt; Conservative investment |
| BBAI | +112.93% | +1.093 | +0.977 | -2.069 | -3.810 | +0.916 | 0.269 | 352 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment |
| AVGO | +53.01% | +1.600 | -0.094 | -1.278 | +0.086 | -0.253 | 0.457 | 352 | Growth tilt |
| IBKR | +17.81% | +1.658 | -0.529 | +0.514 | -1.084 | -0.017 | 0.553 | 352 | Large-cap tilt; Value tilt; Weak profitability |
| INTC | +27.92% | +1.545 | -0.418 | +1.284 | -1.769 | +0.417 | 0.281 | 352 | Value tilt; Weak profitability |
| MU | +80.63% | +1.982 | -0.288 | -0.116 | -0.951 | +0.159 | 0.403 | 352 | Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| NRXP | **90.00** | 33.33 | 23.33 | 33.33 | 0.221 | +0.598 | 1.1988 | 0.0490 | 102 |
| MU | **80.00** | 20.00 | 33.33 | 26.67 | 0.386 | +1.116 | 0.8787 | 0.0359 | 102 |
| INTC | **66.67** | 16.67 | 26.67 | 23.33 | 0.392 | +0.908 | 0.8341 | 0.0341 | 102 |
| CC | **66.67** | 26.67 | 20.00 | 20.00 | 0.340 | +0.550 | 0.8163 | 0.0334 | 102 |
| AMD | **53.33** | 6.67 | 30.00 | 16.67 | 0.564 | +1.000 | 0.6181 | 0.0253 | 102 |
| BBAI | **46.67** | 13.33 | 3.33 | 30.00 | 0.486 | -0.307 | 1.0562 | 0.0432 | 102 |
| ALL | **43.33** | 30.00 | 6.67 | 6.67 | 0.250 | -0.271 | 0.3059 | 0.0125 | 102 |
| AAPL | **40.00** | 23.33 | 13.33 | 3.33 | 0.386 | +0.149 | 0.2547 | 0.0104 | 102 |
| AVGO | **40.00** | 10.00 | 16.67 | 13.33 | 0.561 | +0.458 | 0.4662 | 0.0191 | 102 |
| IBKR | **23.33** | 3.33 | 10.00 | 10.00 | 0.683 | -0.029 | 0.3571 | 0.0146 | 102 |

## Per-ticker FF5 Detail

### NRXP

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.0447 (adjusted = 0.0309)
- Alpha (annualized): **+68.84%** (daily = +0.002732, t = +0.74, p = 0.4612)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5068 | +1.34 | 0.1807  |
| SMB | +0.3757 | +0.56 | 0.5763  |
| HML | -0.0896 | -0.15 | 0.8806  |
| RMW | -1.5705 | -2.18 | 0.0299 * |
| CMA | +0.1926 | +0.25 | 0.8052  |

_Interpretation: Weak profitability; Low explanatory power — likely sentiment-driven_

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

### BBAI

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.2690 (adjusted = 0.2584)
- Alpha (annualized): **+112.93%** (daily = +0.004481, t = +1.20, p = 0.2293)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0928 | +2.88 | 0.0043 ** |
| SMB | +0.9769 | +1.45 | 0.1489  |
| HML | -2.0692 | -3.46 | 0.0006 *** |
| RMW | -3.8098 | -5.26 | 0.0000 *** |
| CMA | +0.9157 | +1.17 | 0.2438  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment_

### AVGO

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.4567 (adjusted = 0.4488)
- Alpha (annualized): **+53.01%** (daily = +0.002104, t = +1.53, p = 0.1264)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6000 | +11.42 | 0.0000 *** |
| SMB | -0.0936 | -0.38 | 0.7074  |
| HML | -1.2783 | -5.79 | 0.0000 *** |
| RMW | +0.0855 | +0.32 | 0.7491  |
| CMA | -0.2533 | -0.88 | 0.3820  |

_Interpretation: Growth tilt_

### IBKR

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.5530 (adjusted = 0.5465)
- Alpha (annualized): **+17.81%** (daily = +0.000707, t = +0.70, p = 0.4843)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6577 | +16.09 | 0.0000 *** |
| SMB | -0.5288 | -2.89 | 0.0041 ** |
| HML | +0.5135 | +3.16 | 0.0017 ** |
| RMW | -1.0839 | -5.52 | 0.0000 *** |
| CMA | -0.0169 | -0.08 | 0.9367  |

_Interpretation: Large-cap tilt; Value tilt; Weak profitability_

### INTC

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.2815 (adjusted = 0.2711)
- Alpha (annualized): **+27.92%** (daily = +0.001108, t = +0.59, p = 0.5561)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5449 | +8.05 | 0.0000 *** |
| SMB | -0.4181 | -1.23 | 0.2211  |
| HML | +1.2839 | +4.24 | 0.0000 *** |
| RMW | -1.7687 | -4.84 | 0.0000 *** |
| CMA | +0.4172 | +1.05 | 0.2931  |

_Interpretation: Value tilt; Weak profitability_

### MU

- Period: `2024-11-01` to `2026-03-31` (352 obs)
- R² = 0.4034 (adjusted = 0.3947)
- Alpha (annualized): **+80.63%** (daily = +0.003200, t = +1.89, p = 0.0597)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.9820 | +11.47 | 0.0000 *** |
| SMB | -0.2877 | -0.94 | 0.3498  |
| HML | -0.1159 | -0.43 | 0.6709  |
| RMW | -0.9509 | -2.89 | 0.0041 ** |
| CMA | +0.1590 | +0.45 | 0.6563  |

_Interpretation: Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._