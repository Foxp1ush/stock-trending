# Weekly Report — `pennystocks` — 2026-W26

Generated: 2026-06-28  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W26.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| CXAI | -45.70% | -0.641 | +3.781 | -3.291 | -1.238 | +0.101 | 0.151 | 440 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| GETY | -76.85% | +1.291 | +1.634 | +0.179 | -0.323 | -0.064 | 0.232 | 440 | Small-cap tilt |
| WEN | -50.24% | +0.549 | +0.836 | +0.280 | +0.382 | +0.649 | 0.193 | 440 | Small-cap tilt; Conservative investment; Significant negative alpha; Modest factor fit |
| MGRX | -34.48% | +0.430 | +2.252 | -1.069 | -0.510 | +0.644 | 0.042 | 440 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| PR | +6.09% | +1.369 | +0.186 | +0.787 | +0.383 | +0.315 | 0.333 | 440 | Value tilt |
| OTLK | -103.23% | +0.348 | +1.792 | -1.578 | -0.247 | +0.036 | 0.053 | 440 | Small-cap tilt; Growth tilt; Modest factor fit |
| RS | -6.38% | +0.890 | +0.712 | +0.496 | +0.364 | +0.299 | 0.458 | 440 | Small-cap tilt |
| SUNE | -246.93% | +1.506 | +1.177 | -0.658 | +0.351 | +3.364 | 0.037 | 440 | Small-cap tilt; Growth tilt; Conservative investment; Low explanatory power — likely sentiment-driven |
| MSFT | -14.54% | +0.889 | -0.263 | -0.409 | +0.149 | -0.511 | 0.525 | 440 | Aggressive investment |
| AMD | +6.07% | +1.579 | -0.573 | -0.517 | -1.700 | -0.093 | 0.483 | 440 | Large-cap tilt; Growth tilt; Weak profitability |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| MGRX | **96.67** | 30.00 | 33.33 | 33.33 | 0.067 | +1.930 | 2.0451 | 0.1205 | 190 |
| SUNE | **70.00** | 26.67 | 16.67 | 26.67 | 0.090 | -0.678 | 1.3526 | 0.0797 | 190 |
| OTLK | **70.00** | 33.33 | 6.67 | 30.00 | 0.057 | -1.246 | 1.4722 | 0.0868 | 190 |
| PR | **56.67** | 23.33 | 23.33 | 10.00 | 0.188 | -0.165 | 0.3150 | 0.0186 | 190 |
| AMD | **53.33** | 6.67 | 30.00 | 16.67 | 0.424 | +0.347 | 0.5032 | 0.0297 | 190 |
| CXAI | **53.33** | 20.00 | 10.00 | 23.33 | 0.222 | -1.108 | 0.9457 | 0.0557 | 190 |
| RS | **43.33** | 10.00 | 26.67 | 6.67 | 0.366 | +0.102 | 0.2191 | 0.0129 | 190 |
| WEN | **40.00** | 13.33 | 13.33 | 13.33 | 0.298 | -0.852 | 0.3648 | 0.0215 | 190 |
| GETY | **40.00** | 16.67 | 3.33 | 20.00 | 0.283 | -1.283 | 0.6426 | 0.0379 | 190 |
| MSFT | **26.67** | 3.33 | 20.00 | 3.33 | 0.428 | -0.465 | 0.1918 | 0.0113 | 190 |

## Per-ticker FF5 Detail

### CXAI

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.1511 (adjusted = 0.1413)
- Alpha (annualized): **-45.70%** (daily = -0.001813, t = -0.49, p = 0.6248)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.6406 | -1.62 | 0.1055  |
| SMB | +3.7812 | +5.91 | 0.0000 *** |
| HML | -3.2911 | -5.43 | 0.0000 *** |
| RMW | -1.2382 | -1.62 | 0.1054  |
| CMA | +0.1013 | +0.13 | 0.8949  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### GETY

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.2315 (adjusted = 0.2227)
- Alpha (annualized): **-76.85%** (daily = -0.003050, t = -1.64, p = 0.1017)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2907 | +6.51 | 0.0000 *** |
| SMB | +1.6339 | +5.09 | 0.0000 *** |
| HML | +0.1793 | +0.59 | 0.5558  |
| RMW | -0.3228 | -0.84 | 0.3998  |
| CMA | -0.0641 | -0.17 | 0.8676  |

_Interpretation: Small-cap tilt_

### WEN

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.1926 (adjusted = 0.1833)
- Alpha (annualized): **-50.24%** (daily = -0.001994, t = -2.06, p = 0.0402)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5493 | +5.32 | 0.0000 *** |
| SMB | +0.8360 | +5.00 | 0.0000 *** |
| HML | +0.2804 | +1.77 | 0.0774  |
| RMW | +0.3817 | +1.91 | 0.0564  |
| CMA | +0.6491 | +3.24 | 0.0013 ** |

_Interpretation: Small-cap tilt; Conservative investment; Significant negative alpha; Modest factor fit_

### MGRX

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.0420 (adjusted = 0.0309)
- Alpha (annualized): **-34.48%** (daily = -0.001368, t = -0.29, p = 0.7685)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.4297 | +0.87 | 0.3860  |
| SMB | +2.2522 | +2.81 | 0.0052 ** |
| HML | -1.0688 | -1.41 | 0.1603  |
| RMW | -0.5098 | -0.53 | 0.5945  |
| CMA | +0.6441 | +0.67 | 0.5030  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### PR

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.3328 (adjusted = 0.3251)
- Alpha (annualized): **+6.09%** (daily = +0.000242, t = +0.25, p = 0.8049)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3686 | +13.13 | 0.0000 *** |
| SMB | +0.1861 | +1.10 | 0.2707  |
| HML | +0.7867 | +4.92 | 0.0000 *** |
| RMW | +0.3833 | +1.90 | 0.0576  |
| CMA | +0.3152 | +1.56 | 0.1197  |

_Interpretation: Value tilt_

### OTLK

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.0527 (adjusted = 0.0418)
- Alpha (annualized): **-103.23%** (daily = -0.004096, t = -1.14, p = 0.2569)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3476 | +0.90 | 0.3667  |
| SMB | +1.7918 | +2.88 | 0.0042 ** |
| HML | -1.5776 | -2.67 | 0.0078 ** |
| RMW | -0.2472 | -0.33 | 0.7396  |
| CMA | +0.0360 | +0.05 | 0.9616  |

_Interpretation: Small-cap tilt; Growth tilt; Modest factor fit_

### RS

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.4576 (adjusted = 0.4514)
- Alpha (annualized): **-6.38%** (daily = -0.000253, t = -0.42, p = 0.6763)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8899 | +13.77 | 0.0000 *** |
| SMB | +0.7124 | +6.81 | 0.0000 *** |
| HML | +0.4961 | +5.00 | 0.0000 *** |
| RMW | +0.3639 | +2.91 | 0.0038 ** |
| CMA | +0.2988 | +2.38 | 0.0176 * |

_Interpretation: Small-cap tilt_

### SUNE

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.0371 (adjusted = 0.0260)
- Alpha (annualized): **-246.93%** (daily = -0.009799, t = -1.50, p = 0.1348)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5064 | +2.16 | 0.0313 * |
| SMB | +1.1770 | +1.04 | 0.2976  |
| HML | -0.6579 | -0.61 | 0.5389  |
| RMW | +0.3512 | +0.26 | 0.7944  |
| CMA | +3.3639 | +2.49 | 0.0133 * |

_Interpretation: Small-cap tilt; Growth tilt; Conservative investment; Low explanatory power — likely sentiment-driven_

### MSFT

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.5252 (adjusted = 0.5197)
- Alpha (annualized): **-14.54%** (daily = -0.000577, t = -1.11, p = 0.2668)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8891 | +16.08 | 0.0000 *** |
| SMB | -0.2633 | -2.94 | 0.0035 ** |
| HML | -0.4086 | -4.81 | 0.0000 *** |
| RMW | +0.1493 | +1.40 | 0.1630  |
| CMA | -0.5109 | -4.76 | 0.0000 *** |

_Interpretation: Aggressive investment_

### AMD

- Period: `2024-06-28` to `2026-03-31` (440 obs)
- R² = 0.4833 (adjusted = 0.4774)
- Alpha (annualized): **+6.07%** (daily = +0.000241, t = +0.19, p = 0.8481)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5792 | +11.79 | 0.0000 *** |
| SMB | -0.5730 | -2.64 | 0.0086 ** |
| HML | -0.5173 | -2.52 | 0.0123 * |
| RMW | -1.7000 | -6.57 | 0.0000 *** |
| CMA | -0.0928 | -0.36 | 0.7212  |

_Interpretation: Large-cap tilt; Growth tilt; Weak profitability_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._