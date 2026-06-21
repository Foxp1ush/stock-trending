# Weekly Report — `all-stocks` — 2026-W25

Generated: 2026-06-21  ·  Source: `apewisdom:all-stocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W25.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| MSFT | -14.01% | +0.885 | -0.260 | -0.406 | +0.138 | -0.495 | 0.524 | 445 | Neutral profile |
| MU | +40.40% | +2.005 | -0.471 | -0.118 | -0.963 | +0.443 | 0.399 | 445 | Weak profitability |
| NVDA | +17.09% | +1.739 | -0.842 | -1.203 | -0.305 | +1.582 | 0.685 | 445 | Large-cap tilt; Growth tilt; Conservative investment |
| SNDK | +277.05% | +2.357 | -0.019 | +0.847 | -1.260 | -1.283 | 0.249 | 282 | Value tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| TSLA | +36.00% | +2.300 | -0.136 | -0.152 | -0.153 | -0.958 | 0.446 | 445 | Aggressive investment |
| AMD | +3.45% | +1.582 | -0.579 | -0.499 | -1.704 | -0.072 | 0.482 | 445 | Large-cap tilt; Weak profitability |
| ASTS | +145.20% | +1.458 | +1.571 | -1.485 | -2.655 | -0.071 | 0.285 | 445 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| DTE | +6.78% | +0.276 | -0.114 | +0.558 | -0.200 | +0.044 | 0.145 | 445 | Value tilt; Modest factor fit |
| NBIS | +171.20% | +1.642 | +0.745 | -2.284 | -2.007 | -0.014 | 0.295 | 360 | Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha |
| META | +7.05% | +1.374 | -0.119 | -0.613 | +0.504 | -0.616 | 0.512 | 445 | Growth tilt; Robust profitability; Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| SNDK | **93.33** | 30.00 | 33.33 | 30.00 | 0.270 | +1.731 | 0.9027 | 0.0549 | 195 |
| NBIS | **86.67** | 23.33 | 30.00 | 33.33 | 0.299 | +1.271 | 0.9213 | 0.0560 | 195 |
| MU | **76.67** | 26.67 | 26.67 | 23.33 | 0.289 | +0.511 | 0.5409 | 0.0329 | 195 |
| ASTS | **60.00** | 20.00 | 13.33 | 26.67 | 0.301 | +0.173 | 0.8883 | 0.0540 | 195 |
| DTE | **46.67** | 33.33 | 10.00 | 3.33 | 0.057 | +0.107 | 0.1546 | 0.0094 | 195 |
| AMD | **46.67** | 6.67 | 20.00 | 20.00 | 0.429 | +0.329 | 0.4836 | 0.0294 | 195 |
| META | **43.33** | 13.33 | 16.67 | 13.33 | 0.351 | +0.250 | 0.2943 | 0.0179 | 195 |
| TSLA | **40.00** | 16.67 | 6.67 | 16.67 | 0.346 | -0.098 | 0.3735 | 0.0227 | 195 |
| NVDA | **36.67** | 3.33 | 23.33 | 10.00 | 0.607 | +0.390 | 0.2210 | 0.0134 | 195 |
| MSFT | **20.00** | 10.00 | 3.33 | 6.67 | 0.426 | -0.450 | 0.1852 | 0.0113 | 195 |

## Per-ticker FF5 Detail

### MSFT

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.5236 (adjusted = 0.5181)
- Alpha (annualized): **-14.01%** (daily = -0.000556, t = -1.08, p = 0.2803)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8852 | +16.09 | 0.0000 *** |
| SMB | -0.2597 | -2.91 | 0.0038 ** |
| HML | -0.4061 | -4.82 | 0.0000 *** |
| RMW | +0.1382 | +1.30 | 0.1929  |
| CMA | -0.4951 | -4.66 | 0.0000 *** |

_Interpretation: Neutral profile_

### MU

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.3991 (adjusted = 0.3922)
- Alpha (annualized): **+40.40%** (daily = +0.001603, t = +1.09, p = 0.2755)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.0049 | +12.76 | 0.0000 *** |
| SMB | -0.4708 | -1.85 | 0.0651  |
| HML | -0.1184 | -0.49 | 0.6232  |
| RMW | -0.9627 | -3.18 | 0.0016 ** |
| CMA | +0.4435 | +1.46 | 0.1443  |

_Interpretation: Weak profitability_

### NVDA

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.6849 (adjusted = 0.6813)
- Alpha (annualized): **+17.09%** (daily = +0.000678, t = +0.82, p = 0.4152)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7391 | +19.54 | 0.0000 *** |
| SMB | -0.8418 | -5.84 | 0.0000 *** |
| HML | -1.2030 | -8.82 | 0.0000 *** |
| RMW | -0.3052 | -1.78 | 0.0756  |
| CMA | +1.5824 | +9.22 | 0.0000 *** |

_Interpretation: Large-cap tilt; Growth tilt; Conservative investment_

### SNDK

- Period: `2025-02-14` to `2026-03-31` (282 obs)
- R² = 0.2490 (adjusted = 0.2354)
- Alpha (annualized): **+277.05%** (daily = +0.010994, t = +3.31, p = 0.0011)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.3574 | +7.20 | 0.0000 *** |
| SMB | -0.0193 | -0.03 | 0.9748  |
| HML | +0.8466 | +1.41 | 0.1591  |
| RMW | -1.2601 | -1.98 | 0.0485 * |
| CMA | -1.2831 | -1.62 | 0.1062  |

_Interpretation: Value tilt; Weak profitability; Aggressive investment; Significant positive alpha_

### TSLA

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.4462 (adjusted = 0.4399)
- Alpha (annualized): **+36.00%** (daily = +0.001429, t = +1.01, p = 0.3127)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.3004 | +15.21 | 0.0000 *** |
| SMB | -0.1360 | -0.56 | 0.5791  |
| HML | -0.1522 | -0.66 | 0.5116  |
| RMW | -0.1531 | -0.53 | 0.5994  |
| CMA | -0.9577 | -3.28 | 0.0011 ** |

_Interpretation: Aggressive investment_

### AMD

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.4825 (adjusted = 0.4766)
- Alpha (annualized): **+3.45%** (daily = +0.000137, t = +0.11, p = 0.9123)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5821 | +11.88 | 0.0000 *** |
| SMB | -0.5788 | -2.68 | 0.0076 ** |
| HML | -0.4992 | -2.45 | 0.0148 * |
| RMW | -1.7037 | -6.65 | 0.0000 *** |
| CMA | -0.0724 | -0.28 | 0.7781  |

_Interpretation: Large-cap tilt; Weak profitability_

### ASTS

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.2846 (adjusted = 0.2764)
- Alpha (annualized): **+145.20%** (daily = +0.005762, t = +2.05, p = 0.0408)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4576 | +4.85 | 0.0000 *** |
| SMB | +1.5714 | +3.23 | 0.0013 ** |
| HML | -1.4849 | -3.23 | 0.0014 ** |
| RMW | -2.6547 | -4.59 | 0.0000 *** |
| CMA | -0.0710 | -0.12 | 0.9027  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### DTE

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.1447 (adjusted = 0.1350)
- Alpha (annualized): **+6.78%** (daily = +0.000269, t = +0.56, p = 0.5777)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2762 | +5.35 | 0.0000 *** |
| SMB | -0.1140 | -1.36 | 0.1740  |
| HML | +0.5584 | +7.06 | 0.0000 *** |
| RMW | -0.1998 | -2.01 | 0.0452 * |
| CMA | +0.0444 | +0.45 | 0.6561  |

_Interpretation: Value tilt; Modest factor fit_

### NBIS

- Period: `2024-10-22` to `2026-03-31` (360 obs)
- R² = 0.2953 (adjusted = 0.2854)
- Alpha (annualized): **+171.20%** (daily = +0.006794, t = +2.15, p = 0.0320)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6416 | +5.06 | 0.0000 *** |
| SMB | +0.7454 | +1.29 | 0.1966  |
| HML | -2.2842 | -4.49 | 0.0000 *** |
| RMW | -2.0070 | -3.24 | 0.0013 ** |
| CMA | -0.0135 | -0.02 | 0.9839  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Significant positive alpha_

### META

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.5122 (adjusted = 0.5066)
- Alpha (annualized): **+7.05%** (daily = +0.000280, t = +0.36, p = 0.7154)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3735 | +16.73 | 0.0000 *** |
| SMB | -0.1194 | -0.90 | 0.3702  |
| HML | -0.6134 | -4.88 | 0.0000 *** |
| RMW | +0.5039 | +3.19 | 0.0015 ** |
| CMA | -0.6161 | -3.89 | 0.0001 *** |

_Interpretation: Growth tilt; Robust profitability; Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._