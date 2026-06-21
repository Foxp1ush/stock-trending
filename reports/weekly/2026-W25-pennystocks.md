# Weekly Report — `pennystocks` — 2026-W25

Generated: 2026-06-21  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W25.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **9 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| CXAI | -50.35% | -0.620 | +3.781 | -3.308 | -1.149 | +0.070 | 0.150 | 445 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| CTM | +159.51% | +0.734 | +1.257 | -0.855 | -1.182 | +0.359 | 0.035 | 445 | Small-cap tilt; Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven |
| OTLK | -104.86% | +0.341 | +1.796 | -1.572 | -0.277 | +0.061 | 0.053 | 445 | Small-cap tilt; Growth tilt; Modest factor fit |
| RS | -5.95% | +0.890 | +0.714 | +0.488 | +0.372 | +0.289 | 0.456 | 445 | Small-cap tilt |
| CRVO | -8.43% | +0.205 | -0.250 | +0.193 | -4.891 | +1.976 | 0.079 | 445 | Weak profitability; Conservative investment; Modest factor fit |
| PR | +8.20% | +1.361 | +0.189 | +0.790 | +0.355 | +0.324 | 0.331 | 445 | Value tilt |
| KITT | -131.24% | +1.615 | +0.705 | -1.040 | -2.946 | +1.914 | 0.082 | 445 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| CAST | — | — | — | — | — | — | — | — | _insufficient_data_ |
| WPRT | -66.70% | +0.893 | +0.460 | -0.035 | -0.234 | +0.446 | 0.149 | 445 | Modest factor fit |
| SLS | +87.26% | +0.247 | +0.416 | +0.142 | -1.961 | -0.832 | 0.078 | 445 | Weak profitability; Aggressive investment; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| WPRT | **74.07** | 33.33 | 29.63 | 11.11 | 0.050 | +0.253 | 0.5190 | 0.0316 | 195 |
| KITT | **74.07** | 25.93 | 14.81 | 33.33 | 0.076 | +0.062 | 1.9164 | 0.1165 | 195 |
| SLS | **74.07** | 18.52 | 33.33 | 22.22 | 0.141 | +0.830 | 0.8932 | 0.0543 | 195 |
| CRVO | **62.96** | 22.22 | 22.22 | 18.52 | 0.130 | +0.121 | 0.7245 | 0.0441 | 195 |
| OTLK | **62.96** | 29.63 | 3.70 | 29.63 | 0.053 | -1.323 | 1.4166 | 0.0861 | 195 |
| CTM | **51.85** | 11.11 | 25.93 | 14.81 | 0.204 | +0.200 | 0.6587 | 0.0401 | 195 |
| CXAI | **40.74** | 7.41 | 7.41 | 25.93 | 0.213 | -1.052 | 0.9220 | 0.0561 | 195 |
| PR | **33.33** | 14.81 | 11.11 | 7.41 | 0.187 | -0.209 | 0.3072 | 0.0187 | 195 |
| RS | **25.93** | 3.70 | 18.52 | 3.70 | 0.368 | +0.103 | 0.2102 | 0.0128 | 195 |

## Per-ticker FF5 Detail

### CXAI

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.1498 (adjusted = 0.1401)
- Alpha (annualized): **-50.35%** (daily = -0.001998, t = -0.54, p = 0.5867)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.6195 | -1.58 | 0.1157  |
| SMB | +3.7813 | +5.94 | 0.0000 *** |
| HML | -3.3076 | -5.49 | 0.0000 *** |
| RMW | -1.1493 | -1.52 | 0.1296  |
| CMA | +0.0695 | +0.09 | 0.9270  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### CTM

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.0355 (adjusted = 0.0245)
- Alpha (annualized): **+159.51%** (daily = +0.006330, t = +1.28, p = 0.2028)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7335 | +1.38 | 0.1679  |
| SMB | +1.2572 | +1.46 | 0.1448  |
| HML | -0.8548 | -1.05 | 0.2940  |
| RMW | -1.1817 | -1.16 | 0.2485  |
| CMA | +0.3592 | +0.35 | 0.7260  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Low explanatory power — likely sentiment-driven_

### OTLK

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.0533 (adjusted = 0.0425)
- Alpha (annualized): **-104.86%** (daily = -0.004161, t = -1.17, p = 0.2442)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3410 | +0.89 | 0.3724  |
| SMB | +1.7956 | +2.90 | 0.0039 ** |
| HML | -1.5720 | -2.69 | 0.0075 ** |
| RMW | -0.2768 | -0.38 | 0.7068  |
| CMA | +0.0610 | +0.08 | 0.9341  |

_Interpretation: Small-cap tilt; Growth tilt; Modest factor fit_

### RS

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.4565 (adjusted = 0.4503)
- Alpha (annualized): **-5.95%** (daily = -0.000236, t = -0.39, p = 0.6942)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8904 | +13.86 | 0.0000 *** |
| SMB | +0.7138 | +6.85 | 0.0000 *** |
| HML | +0.4877 | +4.95 | 0.0000 *** |
| RMW | +0.3719 | +3.01 | 0.0028 ** |
| CMA | +0.2885 | +2.33 | 0.0204 * |

_Interpretation: Small-cap tilt_

### CRVO

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.0794 (adjusted = 0.0690)
- Alpha (annualized): **-8.43%** (daily = -0.000335, t = -0.07, p = 0.9460)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2053 | +0.39 | 0.6976  |
| SMB | -0.2499 | -0.29 | 0.7704  |
| HML | +0.1932 | +0.24 | 0.8114  |
| RMW | -4.8910 | -4.81 | 0.0000 *** |
| CMA | +1.9758 | +1.94 | 0.0530  |

_Interpretation: Weak profitability; Conservative investment; Modest factor fit_

### PR

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.3310 (adjusted = 0.3234)
- Alpha (annualized): **+8.20%** (daily = +0.000325, t = +0.34, p = 0.7376)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3613 | +13.10 | 0.0000 *** |
| SMB | +0.1887 | +1.12 | 0.2631  |
| HML | +0.7903 | +4.97 | 0.0000 *** |
| RMW | +0.3545 | +1.77 | 0.0771  |
| CMA | +0.3245 | +1.62 | 0.1062  |

_Interpretation: Value tilt_

### KITT

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.0825 (adjusted = 0.0720)
- Alpha (annualized): **-131.24%** (daily = -0.005208, t = -0.90, p = 0.3679)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6149 | +2.61 | 0.0093 ** |
| SMB | +0.7053 | +0.70 | 0.4819  |
| HML | -1.0396 | -1.10 | 0.2730  |
| RMW | -2.9456 | -2.47 | 0.0137 * |
| CMA | +1.9144 | +1.60 | 0.1093  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### CAST

Status: `insufficient_data` — only 15 overlapping days after factor join


### WPRT

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.1493 (adjusted = 0.1396)
- Alpha (annualized): **-66.70%** (daily = -0.002647, t = -1.92, p = 0.0557)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8931 | +6.05 | 0.0000 *** |
| SMB | +0.4600 | +1.92 | 0.0552  |
| HML | -0.0346 | -0.15 | 0.8786  |
| RMW | -0.2344 | -0.82 | 0.4101  |
| CMA | +0.4463 | +1.57 | 0.1179  |

_Interpretation: Modest factor fit_

### SLS

- Period: `2024-06-21` to `2026-03-31` (445 obs)
- R² = 0.0780 (adjusted = 0.0675)
- Alpha (annualized): **+87.26%** (daily = +0.003463, t = +1.38, p = 0.1693)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2465 | +0.92 | 0.3602  |
| SMB | +0.4155 | +0.95 | 0.3413  |
| HML | +0.1419 | +0.34 | 0.7310  |
| RMW | -1.9608 | -3.78 | 0.0002 *** |
| CMA | -0.8324 | -1.60 | 0.1097  |

_Interpretation: Weak profitability; Aggressive investment; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._