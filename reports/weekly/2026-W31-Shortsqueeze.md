# Weekly Report — `Shortsqueeze` — 2026-W31

Generated: 2026-08-02  ·  Source: `apewisdom:Shortsqueeze`  ·  Lookback: 7 days

[← Back to dashboard](2026-W31.md)

## Part 1 — Orthodox FF5 Regression

Successful regressions: **10 / 10**

| Ticker | Alpha (ann %) | Mkt-RF β | SMB β | HML β | RMW β | CMA β | R² | N | Comment |
|--------|---------------|----------|-------|-------|-------|-------|------|------|---------|
| GRPN | +10.04% | +0.685 | +0.982 | -0.372 | -1.791 | +0.713 | 0.152 | 416 | Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit |
| AM | +21.07% | +0.623 | -0.276 | +0.352 | -0.239 | +0.098 | 0.195 | 416 | Modest factor fit |
| ET | +3.27% | +0.762 | -0.227 | +0.370 | -0.300 | +0.377 | 0.330 | 416 | Neutral profile |
| BE | +159.27% | +1.414 | -0.120 | -0.061 | -2.613 | -1.935 | 0.205 | 416 | Weak profitability; Aggressive investment; Significant positive alpha |
| PLTR | +86.23% | +1.617 | -0.756 | -0.081 | -2.326 | -0.840 | 0.449 | 416 | Large-cap tilt; Weak profitability; Aggressive investment; Significant positive alpha |
| WEN | -48.60% | +0.578 | +0.767 | +0.218 | +0.376 | +0.835 | 0.192 | 416 | Small-cap tilt; Conservative investment; Modest factor fit |
| ALL | -1.21% | +0.704 | -0.312 | +0.811 | +0.308 | -0.087 | 0.226 | 416 | Value tilt |
| AAPL | +1.61% | +1.315 | -0.129 | -0.059 | +0.771 | +0.149 | 0.537 | 416 | Robust profitability |
| DTE | +1.43% | +0.308 | -0.199 | +0.548 | -0.207 | +0.083 | 0.151 | 416 | Value tilt; Modest factor fit |
| GOOG | +29.56% | +1.024 | +0.230 | -0.502 | +0.485 | -0.721 | 0.454 | 416 | Growth tilt; Aggressive investment |

## Part 2 — Mania Index (within-subreddit ranking)

Quantile rank within this subreddit's pool (0~100). Higher score = more mania-like (poor factor fit, strong momentum, unstable betas).

| Ticker | **Mania** | invR² pt | UMD pt | BSE pt | R² | UMD β | mean_bse | idio_vol | N |
|--------|-----------|----------|--------|--------|------|-------|----------|----------|---|
| BE | **73.33** | 6.67 | 33.33 | 33.33 | 0.405 | +2.351 | 0.9530 | 0.0529 | 166 |
| AM | **70.00** | 33.33 | 26.67 | 10.00 | 0.055 | +0.164 | 0.2061 | 0.0114 | 166 |
| PLTR | **60.00** | 3.33 | 30.00 | 26.67 | 0.499 | +0.166 | 0.4117 | 0.0229 | 166 |
| GRPN | **53.33** | 16.67 | 6.67 | 30.00 | 0.271 | -0.835 | 0.6192 | 0.0344 | 166 |
| GOOG | **53.33** | 10.00 | 23.33 | 20.00 | 0.391 | +0.138 | 0.2488 | 0.0138 | 166 |
| ET | **50.00** | 26.67 | 16.67 | 6.67 | 0.082 | +0.075 | 0.1695 | 0.0094 | 166 |
| ALL | **50.00** | 23.33 | 10.00 | 16.67 | 0.198 | -0.193 | 0.2300 | 0.0128 | 166 |
| DTE | **46.67** | 30.00 | 13.33 | 3.33 | 0.069 | +0.053 | 0.1671 | 0.0093 | 166 |
| WEN | **46.67** | 20.00 | 3.33 | 23.33 | 0.265 | -0.922 | 0.3964 | 0.0220 | 166 |
| AAPL | **46.67** | 13.33 | 20.00 | 13.33 | 0.329 | +0.086 | 0.2174 | 0.0121 | 166 |

## Per-ticker FF5 Detail

### GRPN

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.1520 (adjusted = 0.1416)
- Alpha (annualized): **+10.04%** (daily = +0.000399, t = +0.17, p = 0.8659)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6850 | +2.75 | 0.0062 ** |
| SMB | +0.9824 | +2.30 | 0.0219 * |
| HML | -0.3721 | -0.96 | 0.3362  |
| RMW | -1.7914 | -3.74 | 0.0002 *** |
| CMA | +0.7127 | +1.44 | 0.1510  |

_Interpretation: Small-cap tilt; Weak profitability; Conservative investment; Modest factor fit_

### AM

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.1949 (adjusted = 0.1850)
- Alpha (annualized): **+21.07%** (daily = +0.000836, t = +1.23, p = 0.2179)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.6230 | +8.71 | 0.0000 *** |
| SMB | -0.2764 | -2.25 | 0.0248 * |
| HML | +0.3522 | +3.17 | 0.0016 ** |
| RMW | -0.2387 | -1.73 | 0.0839  |
| CMA | +0.0982 | +0.69 | 0.4909  |

_Interpretation: Modest factor fit_

### ET

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.3297 (adjusted = 0.3216)
- Alpha (annualized): **+3.27%** (daily = +0.000130, t = +0.21, p = 0.8315)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7624 | +11.86 | 0.0000 *** |
| SMB | -0.2271 | -2.06 | 0.0400 * |
| HML | +0.3704 | +3.71 | 0.0002 *** |
| RMW | -0.3001 | -2.42 | 0.0158 * |
| CMA | +0.3766 | +2.94 | 0.0034 ** |

_Interpretation: Neutral profile_

### BE

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.2055 (adjusted = 0.1958)
- Alpha (annualized): **+159.27%** (daily = +0.006320, t = +2.18, p = 0.0295)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.4141 | +4.63 | 0.0000 *** |
| SMB | -0.1197 | -0.23 | 0.8193  |
| HML | -0.0609 | -0.13 | 0.8978  |
| RMW | -2.6128 | -4.44 | 0.0000 *** |
| CMA | -1.9349 | -3.18 | 0.0016 ** |

_Interpretation: Weak profitability; Aggressive investment; Significant positive alpha_

### PLTR

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.4494 (adjusted = 0.4427)
- Alpha (annualized): **+86.23%** (daily = +0.003422, t = +2.26, p = 0.0245)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.6166 | +10.10 | 0.0000 *** |
| SMB | -0.7563 | -2.76 | 0.0061 ** |
| HML | -0.0815 | -0.33 | 0.7431  |
| RMW | -2.3262 | -7.55 | 0.0000 *** |
| CMA | -0.8397 | -2.64 | 0.0087 ** |

_Interpretation: Large-cap tilt; Weak profitability; Aggressive investment; Significant positive alpha_

### WEN

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.1925 (adjusted = 0.1826)
- Alpha (annualized): **-48.60%** (daily = -0.001929, t = -1.94, p = 0.0536)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.5783 | +5.50 | 0.0000 *** |
| SMB | +0.7674 | +4.26 | 0.0000 *** |
| HML | +0.2175 | +1.33 | 0.1835  |
| RMW | +0.3758 | +1.86 | 0.0643  |
| CMA | +0.8353 | +3.99 | 0.0001 *** |

_Interpretation: Small-cap tilt; Conservative investment; Modest factor fit_

### ALL

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.2263 (adjusted = 0.2169)
- Alpha (annualized): **-1.21%** (daily = -0.000048, t = -0.07, p = 0.9445)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +0.7040 | +9.69 | 0.0000 *** |
| SMB | -0.3123 | -2.51 | 0.0125 * |
| HML | +0.8108 | +7.19 | 0.0000 *** |
| RMW | +0.3084 | +2.21 | 0.0280 * |
| CMA | -0.0875 | -0.61 | 0.5453  |

_Interpretation: Value tilt_

### AAPL

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.5370 (adjusted = 0.5314)
- Alpha (annualized): **+1.61%** (daily = +0.000064, t = +0.10, p = 0.9166)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.3149 | +20.40 | 0.0000 *** |
| SMB | -0.1286 | -1.16 | 0.2453  |
| HML | -0.0586 | -0.59 | 0.5585  |
| RMW | +0.7713 | +6.22 | 0.0000 *** |
| CMA | +0.1492 | +1.16 | 0.2453  |

_Interpretation: Robust profitability_

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

### GOOG

- Period: `2024-08-02` to `2026-03-31` (416 obs)
- R² = 0.4539 (adjusted = 0.4473)
- Alpha (annualized): **+29.56%** (daily = +0.001173, t = +1.69, p = 0.0911)

Factor loadings:

| Factor | β | t-stat | p-value |
|--------|---|--------|---------|
| Mkt-RF | +1.0235 | +14.00 | 0.0000 *** |
| SMB | +0.2302 | +1.84 | 0.0670  |
| HML | -0.5024 | -4.43 | 0.0000 *** |
| RMW | +0.4851 | +3.45 | 0.0006 *** |
| CMA | -0.7212 | -4.96 | 0.0000 *** |

_Interpretation: Growth tilt; Aggressive investment_

---
### Methodology

- **Orthodox FF5**: 2y daily OLS on Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA). Excess return = R_i - RF.
- **Mania Index**: 1y daily 6-factor OLS adding Carhart UMD. Three instability metrics quantile-ranked within this subreddit pool: (1-R²), |UMD beta|, mean BSE of 5 factor betas. Each 0~33.33 pts → total 0~100.
- Factor data: Kenneth R. French Data Library. Price data: Yahoo Finance via yfinance.

### Disclaimer

_Research and educational use only. Not investment advice. Past performance does not predict future returns._