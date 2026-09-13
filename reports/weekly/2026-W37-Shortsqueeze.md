# Weekly Report — `Shortsqueeze` — 2026-W37

Generated: 2026-09-13  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W37.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| GOOGL | +40.50% | +1.012 | +0.193 | -0.528 | +0.495 | -0.746 | 0.438 | 387 | Growth tilt; Aggressive investment; Significant positive alpha |
| ASTS | +96.11% | +1.316 | +1.252 | -1.132 | -2.889 | -0.320 | 0.311 | 387 | Small-cap tilt; Growth tilt; Weak profitability |
| API | +85.06% | +0.081 | +0.653 | -1.369 | -1.613 | +0.810 | 0.064 | 387 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| PR | +21.04% | +1.385 | +0.133 | +0.809 | +0.354 | +0.388 | 0.328 | 387 | Value tilt |
| RDDT | +62.60% | +1.590 | -0.214 | -0.735 | -1.308 | -0.410 | 0.243 | 387 | Growth tilt; Weak profitability |
| RR | +124.84% | +1.142 | +1.894 | -1.516 | -4.146 | +1.458 | 0.195 | 387 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit |
| HOOD | +57.92% | +2.260 | -0.214 | +0.061 | -2.548 | -0.589 | 0.560 | 387 | Weak profitability; Aggressive investment |
| GME | +20.26% | +0.550 | +0.877 | -0.738 | -0.119 | +0.064 | 0.113 | 387 | Small-cap tilt; Growth tilt; Modest factor fit |
| FOR | -11.17% | +0.888 | +1.740 | +0.103 | +1.213 | +0.404 | 0.454 | 387 | Small-cap tilt; Robust profitability |
| FCF | -11.51% | +0.994 | +0.977 | +1.212 | +0.211 | -0.269 | 0.709 | 387 | Small-cap tilt; Value tilt |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| RR | **86.67** | 20.00 | 33.33 | 33.33 | 0.316 | +0.240 | 1.3785 | 0.0682 | 137 |
| ASTS | **73.33** | 16.67 | 26.67 | 30.00 | 0.347 | +0.096 | 1.1704 | 0.0579 | 137 |
| PR | **66.67** | 30.00 | 23.33 | 13.33 | 0.150 | -0.081 | 0.3723 | 0.0184 | 137 |
| GME | **63.33** | 26.67 | 20.00 | 16.67 | 0.179 | -0.125 | 0.4171 | 0.0206 | 137 |
| API | **63.33** | 33.33 | 10.00 | 20.00 | 0.125 | -0.337 | 0.5429 | 0.0268 | 137 |
| RDDT | **53.33** | 23.33 | 3.33 | 26.67 | 0.271 | -0.766 | 0.7054 | 0.0349 | 137 |
| GOOGL | **50.00** | 13.33 | 30.00 | 6.67 | 0.423 | +0.192 | 0.2694 | 0.0133 | 137 |
| HOOD | **36.67** | 6.67 | 6.67 | 23.33 | 0.589 | -0.463 | 0.5723 | 0.0283 | 137 |
| FOR | **33.33** | 10.00 | 13.33 | 10.00 | 0.453 | -0.176 | 0.3345 | 0.0165 | 137 |
| FCF | **23.33** | 3.33 | 16.67 | 3.33 | 0.696 | -0.127 | 0.1703 | 0.0084 | 137 |

## Per-ticker FF5 Detail

### GOOGL

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.4385 (adjusted = 0.4311)
- Alpha (annualized): **+40.50%** (daily = +0.001607, t = +2.17, p = 0.0306)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0118 | +12.97 | 0.0000 *** |
| SMB | +0.1926 | +1.43 | 0.1543  |
| HML | -0.5277 | -4.32 | 0.0000 *** |
| RMW | +0.4945 | +3.34 | 0.0009 *** |
| CMA | -0.7465 | -4.73 | 0.0000 *** |

_Interpretation: Growth tilt; Aggressive investment; Significant positive alpha_

### ASTS

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.3112 (adjusted = 0.3022)
- Alpha (annualized): **+96.11%** (daily = +0.003814, t = +1.42, p = 0.1560)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3159 | +4.66 | 0.0000 *** |
| SMB | +1.2521 | +2.56 | 0.0108 * |
| HML | -1.1322 | -2.56 | 0.0108 * |
| RMW | -2.8892 | -5.38 | 0.0000 *** |
| CMA | -0.3200 | -0.56 | 0.5757  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### API

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.0636 (adjusted = 0.0513)
- Alpha (annualized): **+85.06%** (daily = +0.003376, t = +0.98, p = 0.3263)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.0807 | +0.22 | 0.8237  |
| SMB | +0.6527 | +1.04 | 0.2975  |
| HML | -1.3692 | -2.42 | 0.0160 * |
| RMW | -1.6131 | -2.35 | 0.0195 * |
| CMA | +0.8101 | +1.11 | 0.2688  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### PR

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.3282 (adjusted = 0.3194)
- Alpha (annualized): **+21.04%** (daily = +0.000835, t = +0.78, p = 0.4359)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3850 | +12.28 | 0.0000 *** |
| SMB | +0.1331 | +0.68 | 0.4954  |
| HML | +0.8086 | +4.59 | 0.0000 *** |
| RMW | +0.3543 | +1.65 | 0.0989  |
| CMA | +0.3882 | +1.70 | 0.0894  |

_Interpretation: Value tilt_

### RDDT

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.2431 (adjusted = 0.2332)
- Alpha (annualized): **+62.60%** (daily = +0.002484, t = +1.08, p = 0.2794)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5905 | +6.58 | 0.0000 *** |
| SMB | -0.2141 | -0.51 | 0.6087  |
| HML | -0.7355 | -1.95 | 0.0523  |
| RMW | -1.3083 | -2.85 | 0.0046 ** |
| CMA | -0.4104 | -0.84 | 0.4013  |

_Interpretation: Growth tilt; Weak profitability_

### RR

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.1955 (adjusted = 0.1849)
- Alpha (annualized): **+124.84%** (daily = +0.004954, t = +1.10, p = 0.2725)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.1420 | +2.40 | 0.0167 * |
| SMB | +1.8943 | +2.31 | 0.0216 * |
| HML | -1.5156 | -2.04 | 0.0420 * |
| RMW | -4.1455 | -4.59 | 0.0000 *** |
| CMA | +1.4577 | +1.52 | 0.1298  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Modest factor fit_

### HOOD

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.5604 (adjusted = 0.5546)
- Alpha (annualized): **+57.92%** (daily = +0.002298, t = +1.44, p = 0.1511)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.2601 | +13.43 | 0.0000 *** |
| SMB | -0.2141 | -0.74 | 0.4624  |
| HML | +0.0609 | +0.23 | 0.8170  |
| RMW | -2.5478 | -7.97 | 0.0000 *** |
| CMA | -0.5889 | -1.73 | 0.0843  |

_Interpretation: Weak profitability; Aggressive investment_

### GME

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.1132 (adjusted = 0.1015)
- Alpha (annualized): **+20.26%** (daily = +0.000804, t = +0.49, p = 0.6258)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5499 | +3.17 | 0.0017 ** |
| SMB | +0.8769 | +2.92 | 0.0037 ** |
| HML | -0.7376 | -2.72 | 0.0069 ** |
| RMW | -0.1194 | -0.36 | 0.7175  |
| CMA | +0.0642 | +0.18 | 0.8550  |

_Interpretation: Small-cap tilt; Growth tilt; Modest factor fit_

### FOR

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.4536 (adjusted = 0.4465)
- Alpha (annualized): **-11.17%** (daily = -0.000443, t = -0.51, p = 0.6072)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8881 | +9.79 | 0.0000 *** |
| SMB | +1.7397 | +11.09 | 0.0000 *** |
| HML | +0.1031 | +0.73 | 0.4679  |
| RMW | +1.2129 | +7.04 | 0.0000 *** |
| CMA | +0.4044 | +2.20 | 0.0281 * |

_Interpretation: Small-cap tilt; Robust profitability_

### FCF

- Period: `2024-09-13` to `2026-03-31` (387 obs)
- R² = 0.7092 (adjusted = 0.7054)
- Alpha (annualized): **-11.51%** (daily = -0.000457, t = -0.92, p = 0.3604)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9935 | +18.90 | 0.0000 *** |
| SMB | +0.9767 | +10.75 | 0.0000 *** |
| HML | +1.2118 | +14.74 | 0.0000 *** |
| RMW | +0.2107 | +2.11 | 0.0355 * |
| CMA | -0.2688 | -2.53 | 0.0118 * |

_Interpretation: Small-cap tilt; Value tilt_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._