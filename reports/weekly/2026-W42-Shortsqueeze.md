# Weekly Report — `Shortsqueeze` — 2026-W42

Generated: 2026-10-18  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W42.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| AAPL | +3.39% | +1.352 | -0.157 | -0.046 | +0.757 | +0.202 | 0.554 | 362 | Robust profitability |
| ALL | -5.42% | +0.684 | -0.271 | +0.783 | +0.302 | -0.053 | 0.220 | 362 | Value tilt |
| AM | +21.92% | +0.610 | -0.348 | +0.386 | -0.291 | +0.127 | 0.195 | 362 | Modest factor fit |
| AMD | +9.48% | +1.588 | -0.584 | -0.418 | -1.665 | -0.279 | 0.476 | 362 | Large-cap tilt; Weak profitability |
| API | +54.50% | +0.212 | +0.944 | -1.391 | -1.214 | +0.492 | 0.098 | 362 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| ASTS | +100.05% | +1.290 | +0.984 | -1.186 | -2.924 | -0.341 | 0.315 | 362 | Small-cap tilt; Growth tilt; Weak profitability |
| BB | +15.42% | +1.015 | +0.200 | -0.471 | -1.232 | +0.822 | 0.278 | 362 | Weak profitability; Conservative investment |
| CC | +21.75% | +1.755 | +2.085 | +0.186 | +0.228 | +1.381 | 0.437 | 362 | Small-cap tilt; Conservative investment |
| ET | +5.71% | +0.762 | -0.257 | +0.364 | -0.362 | +0.450 | 0.336 | 362 | Neutral profile |
| EU | -23.03% | +0.856 | +1.510 | -1.221 | -0.994 | -0.127 | 0.174 | 362 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| EU | **80.00** | 16.67 | 33.33 | 30.00 | 0.300 | +1.328 | 0.9371 | 0.0413 | 112 |
| CC | **66.67** | 13.33 | 26.67 | 26.67 | 0.327 | +0.583 | 0.7384 | 0.0326 | 112 |
| AM | **63.33** | 33.33 | 20.00 | 10.00 | 0.046 | +0.127 | 0.2694 | 0.0119 | 112 |
| ASTS | **63.33** | 6.67 | 23.33 | 33.33 | 0.369 | +0.366 | 1.2883 | 0.0568 | 112 |
| API | **56.67** | 26.67 | 6.67 | 23.33 | 0.104 | -0.321 | 0.5860 | 0.0258 | 112 |
| AMD | **53.33** | 3.33 | 30.00 | 20.00 | 0.572 | +1.015 | 0.5615 | 0.0248 | 112 |
| ET | **46.67** | 30.00 | 13.33 | 3.33 | 0.088 | +0.012 | 0.2227 | 0.0098 | 112 |
| ALL | **46.67** | 23.33 | 10.00 | 13.33 | 0.240 | -0.268 | 0.2754 | 0.0121 | 112 |
| BB | **40.00** | 20.00 | 3.33 | 16.67 | 0.258 | -0.561 | 0.4507 | 0.0199 | 112 |
| AAPL | **33.33** | 10.00 | 16.67 | 6.67 | 0.352 | +0.090 | 0.2475 | 0.0109 | 112 |

## Per-ticker FF5 Detail

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

### ALL

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.2204 (adjusted = 0.2095)
- Alpha (annualized): **-5.42%** (daily = -0.000215, t = -0.29, p = 0.7748)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6837 | +8.83 | 0.0000 *** |
| SMB | -0.2710 | -1.98 | 0.0483 * |
| HML | +0.7829 | +6.46 | 0.0000 *** |
| RMW | +0.3021 | +2.05 | 0.0415 * |
| CMA | -0.0533 | -0.33 | 0.7382  |

_Interpretation: Value tilt_

### AM

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.1947 (adjusted = 0.1834)
- Alpha (annualized): **+21.92%** (daily = +0.000870, t = +1.19, p = 0.2364)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6103 | +8.07 | 0.0000 *** |
| SMB | -0.3478 | -2.60 | 0.0096 ** |
| HML | +0.3865 | +3.27 | 0.0012 ** |
| RMW | -0.2909 | -2.02 | 0.0444 * |
| CMA | +0.1273 | +0.82 | 0.4139  |

_Interpretation: Modest factor fit_

### AMD

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.4759 (adjusted = 0.4685)
- Alpha (annualized): **+9.48%** (daily = +0.000376, t = +0.26, p = 0.7931)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.5881 | +10.75 | 0.0000 *** |
| SMB | -0.5839 | -2.24 | 0.0259 * |
| HML | -0.4177 | -1.81 | 0.0717  |
| RMW | -1.6648 | -5.91 | 0.0000 *** |
| CMA | -0.2787 | -0.92 | 0.3602  |

_Interpretation: Large-cap tilt; Weak profitability_

### API

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.0984 (adjusted = 0.0857)
- Alpha (annualized): **+54.50%** (daily = +0.002163, t = +0.78, p = 0.4380)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.2120 | +0.74 | 0.4608  |
| SMB | +0.9439 | +1.86 | 0.0636  |
| HML | -1.3905 | -3.09 | 0.0021 ** |
| RMW | -1.2139 | -2.22 | 0.0273 * |
| CMA | +0.4924 | +0.83 | 0.4053  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### ASTS

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.3145 (adjusted = 0.3049)
- Alpha (annualized): **+100.05%** (daily = +0.003970, t = +1.43, p = 0.1530)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.2895 | +4.51 | 0.0000 *** |
| SMB | +0.9843 | +1.95 | 0.0521  |
| HML | -1.1855 | -2.65 | 0.0084 ** |
| RMW | -2.9244 | -5.37 | 0.0000 *** |
| CMA | -0.3406 | -0.58 | 0.5630  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### BB

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.2778 (adjusted = 0.2676)
- Alpha (annualized): **+15.42%** (daily = +0.000612, t = +0.39, p = 0.6992)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0145 | +6.22 | 0.0000 *** |
| SMB | +0.2001 | +0.69 | 0.4880  |
| HML | -0.4714 | -1.85 | 0.0657  |
| RMW | -1.2321 | -3.96 | 0.0001 *** |
| CMA | +0.8215 | +2.45 | 0.0149 * |

_Interpretation: Weak profitability; Conservative investment_

### CC

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.4369 (adjusted = 0.4289)
- Alpha (annualized): **+21.75%** (daily = +0.000863, t = +0.53, p = 0.5964)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.7554 | +10.46 | 0.0000 *** |
| SMB | +2.0846 | +7.03 | 0.0000 *** |
| HML | +0.1861 | +0.71 | 0.4790  |
| RMW | +0.2280 | +0.71 | 0.4768  |
| CMA | +1.3811 | +4.00 | 0.0001 *** |

_Interpretation: Small-cap tilt; Conservative investment_

### ET

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.3361 (adjusted = 0.3268)
- Alpha (annualized): **+5.71%** (daily = +0.000227, t = +0.34, p = 0.7336)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7616 | +11.11 | 0.0000 *** |
| SMB | -0.2572 | -2.12 | 0.0344 * |
| HML | +0.3643 | +3.40 | 0.0008 *** |
| RMW | -0.3616 | -2.77 | 0.0060 ** |
| CMA | +0.4505 | +3.19 | 0.0015 ** |

_Interpretation: Neutral profile_

### EU

- Period: `2024-10-18` to `2026-03-31` (362 obs)
- R² = 0.1735 (adjusted = 0.1619)
- Alpha (annualized): **-23.03%** (daily = -0.000914, t = -0.35, p = 0.7284)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8559 | +3.16 | 0.0017 ** |
| SMB | +1.5097 | +3.15 | 0.0018 ** |
| HML | -1.2208 | -2.88 | 0.0042 ** |
| RMW | -0.9936 | -1.92 | 0.0554  |
| CMA | -0.1274 | -0.23 | 0.8195  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._