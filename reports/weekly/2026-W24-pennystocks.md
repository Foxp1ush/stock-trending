# Weekly Report — `pennystocks` — 2026-W24

Generated: 2026-06-14  ·  Source: `apewisdom:pennystocks`  ·  Lookback: 7 days

[← Back to dashboard](2026-W24.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| CXAI | -47.72% | -0.607 | +3.762 | -3.303 | -1.128 | +0.073 | 0.150 | 449 | Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit |
| GMM | +782.90% | +3.036 | -4.046 | -2.620 | +5.483 | -3.896 | 0.007 | 449 | Large-cap tilt; Growth tilt; Robust profitability; Aggressive investment; Low explanatory power — likely sentiment-driven |
| BATL | +243.44% | +0.022 | +0.934 | -1.898 | +2.743 | -0.418 | 0.009 | 449 | Small-cap tilt; Growth tilt; Robust profitability; Low explanatory power — likely sentiment-driven |
| OTLK | -101.70% | +0.324 | +1.750 | -1.557 | -0.354 | +0.108 | 0.053 | 449 | Small-cap tilt; Growth tilt; Modest factor fit |
| DFNS | +431.34% | -1.977 | -0.589 | -3.519 | -1.178 | +3.312 | 0.006 | 449 | Large-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| SPCE | -83.96% | +0.920 | +2.193 | -0.813 | -2.004 | -0.294 | 0.296 | 449 | Small-cap tilt; Growth tilt; Weak profitability |
| VSME | -58.12% | +0.808 | +1.294 | -0.771 | -0.847 | +1.201 | 0.028 | 449 | Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven |
| PR | +8.62% | +1.359 | +0.183 | +0.794 | +0.343 | +0.326 | 0.331 | 449 | Value tilt |
| DSS | -13.90% | -0.087 | +0.272 | +0.362 | -0.788 | -0.897 | 0.017 | 449 | Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven |
| HUBC | -298.93% | +2.101 | -1.131 | +0.868 | -0.425 | -0.067 | 0.044 | 449 | Large-cap tilt; Value tilt; Significant negative alpha; Low explanatory power — likely sentiment-driven |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| HUBC | **76.67** | 16.67 | 33.33 | 26.67 | 0.061 | +1.214 | 1.7101 | 0.1047 | 199 |
| BATL | **73.33** | 33.33 | 6.67 | 33.33 | 0.018 | -1.129 | 3.5511 | 0.2174 | 199 |
| VSME | **73.33** | 26.67 | 16.67 | 30.00 | 0.020 | -0.491 | 1.7901 | 0.1096 | 199 |
| DSS | **70.00** | 23.33 | 30.00 | 16.67 | 0.025 | +0.759 | 1.1038 | 0.0676 | 199 |
| GMM | **66.67** | 30.00 | 26.67 | 10.00 | 0.019 | +0.055 | 0.8236 | 0.0504 | 199 |
| OTLK | **46.67** | 20.00 | 3.33 | 23.33 | 0.052 | -1.313 | 1.3946 | 0.0854 | 199 |
| DFNS | **46.67** | 13.33 | 13.33 | 20.00 | 0.135 | -0.851 | 1.3191 | 0.0808 | 199 |
| PR | **33.33** | 10.00 | 20.00 | 3.33 | 0.187 | -0.209 | 0.3022 | 0.0185 | 199 |
| SPCE | **33.33** | 3.33 | 23.33 | 6.67 | 0.273 | -0.066 | 0.6250 | 0.0383 | 199 |
| CXAI | **30.00** | 6.67 | 10.00 | 13.33 | 0.217 | -1.057 | 0.9067 | 0.0555 | 199 |

## Per-ticker FF5 Detail

### CXAI

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.1498 (adjusted = 0.1402)
- Alpha (annualized): **-47.72%** (daily = -0.001893, t = -0.52, p = 0.6035)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.6071 | -1.56 | 0.1202  |
| SMB | +3.7620 | +5.97 | 0.0000 *** |
| HML | -3.3032 | -5.52 | 0.0000 *** |
| RMW | -1.1283 | -1.51 | 0.1327  |
| CMA | +0.0730 | +0.10 | 0.9229  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Modest factor fit_

### GMM

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.0074 (adjusted = -0.0038)
- Alpha (annualized): **+782.90%** (daily = +0.031067, t = +0.94, p = 0.3481)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +3.0358 | +0.86 | 0.3917  |
| SMB | -4.0459 | -0.71 | 0.4798  |
| HML | -2.6198 | -0.48 | 0.6299  |
| RMW | +5.4834 | +0.81 | 0.4206  |
| CMA | -3.8959 | -0.57 | 0.5697  |

_Interpretation: Large-cap tilt; Growth tilt; Robust profitability; Aggressive investment; Low explanatory power — likely sentiment-driven_

### BATL

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.0091 (adjusted = -0.0021)
- Alpha (annualized): **+243.44%** (daily = +0.009660, t = +1.23, p = 0.2182)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.0221 | +0.03 | 0.9790  |
| SMB | +0.9337 | +0.69 | 0.4911  |
| HML | -1.8975 | -1.47 | 0.1409  |
| RMW | +2.7429 | +1.70 | 0.0893  |
| CMA | -0.4179 | -0.26 | 0.7968  |

_Interpretation: Small-cap tilt; Growth tilt; Robust profitability; Low explanatory power — likely sentiment-driven_

### OTLK

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.0529 (adjusted = 0.0422)
- Alpha (annualized): **-101.70%** (daily = -0.004036, t = -1.14, p = 0.2556)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.3241 | +0.85 | 0.3935  |
| SMB | +1.7503 | +2.85 | 0.0045 ** |
| HML | -1.5572 | -2.67 | 0.0078 ** |
| RMW | -0.3539 | -0.49 | 0.6277  |
| CMA | +0.1080 | +0.15 | 0.8831  |

_Interpretation: Small-cap tilt; Growth tilt; Modest factor fit_

### DFNS

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.0062 (adjusted = -0.0050)
- Alpha (annualized): **+431.34%** (daily = +0.017117, t = +0.90, p = 0.3693)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -1.9767 | -0.97 | 0.3328  |
| SMB | -0.5890 | -0.18 | 0.8582  |
| HML | -3.5193 | -1.13 | 0.2612  |
| RMW | -1.1782 | -0.30 | 0.7637  |
| CMA | +3.3120 | +0.84 | 0.4014  |

_Interpretation: Large-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### SPCE

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.2964 (adjusted = 0.2885)
- Alpha (annualized): **-83.96%** (daily = -0.003332, t = -1.54, p = 0.1249)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.9196 | +3.96 | 0.0001 *** |
| SMB | +2.1926 | +5.85 | 0.0000 *** |
| HML | -0.8133 | -2.28 | 0.0228 * |
| RMW | -2.0036 | -4.50 | 0.0000 *** |
| CMA | -0.2940 | -0.66 | 0.5126  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability_

### VSME

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.0280 (adjusted = 0.0170)
- Alpha (annualized): **-58.12%** (daily = -0.002306, t = -0.42, p = 0.6742)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.8078 | +1.38 | 0.1694  |
| SMB | +1.2940 | +1.36 | 0.1730  |
| HML | -0.7709 | -0.86 | 0.3924  |
| RMW | -0.8467 | -0.75 | 0.4531  |
| CMA | +1.2011 | +1.06 | 0.2905  |

_Interpretation: Small-cap tilt; Growth tilt; Weak profitability; Conservative investment; Low explanatory power — likely sentiment-driven_

### PR

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.3312 (adjusted = 0.3237)
- Alpha (annualized): **+8.62%** (daily = +0.000342, t = +0.36, p = 0.7227)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3587 | +13.18 | 0.0000 *** |
| SMB | +0.1833 | +1.10 | 0.2716  |
| HML | +0.7938 | +5.02 | 0.0000 *** |
| RMW | +0.3431 | +1.73 | 0.0839  |
| CMA | +0.3263 | +1.64 | 0.1024  |

_Interpretation: Value tilt_

### DSS

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.0172 (adjusted = 0.0061)
- Alpha (annualized): **-13.90%** (daily = -0.000552, t = -0.21, p = 0.8326)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | -0.0869 | -0.31 | 0.7558  |
| SMB | +0.2715 | +0.60 | 0.5475  |
| HML | +0.3620 | +0.85 | 0.3985  |
| RMW | -0.7882 | -1.47 | 0.1423  |
| CMA | -0.8968 | -1.66 | 0.0974  |

_Interpretation: Weak profitability; Aggressive investment; Low explanatory power — likely sentiment-driven_

### HUBC

- Period: `2024-06-14` to `2026-03-31` (449 obs)
- R² = 0.0437 (adjusted = 0.0329)
- Alpha (annualized): **-298.93%** (daily = -0.011862, t = -2.48, p = 0.0137)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +2.1012 | +4.10 | 0.0000 *** |
| SMB | -1.1311 | -1.36 | 0.1730  |
| HML | +0.8677 | +1.10 | 0.2708  |
| RMW | -0.4251 | -0.43 | 0.6664  |
| CMA | -0.0665 | -0.07 | 0.9466  |

_Interpretation: Large-cap tilt; Value tilt; Significant negative alpha; Low explanatory power — likely sentiment-driven_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._