# Digest: D2 forecasting evidence, round 1, assistant 2 (accessed 2026-09-28)

## a. Published systems
- NEA operational model (Shi et al.): LASSO, weekly national notifications 1-12 weeks ahead, one submodel per horizon; recent cases, weather, vector surveillance, population (~226+ candidates); trained 2001-2010, validated 2011-2012, tested 2013. MAPE 17% (1 wk) to 24% (3 months); SARIMA/step-down 29% at 3 months; LASSO beat both except in the first 2-week window. | https://pmc.ncbi.nlm.nih.gov/articles/PMC5010413/ | Environ Health Perspect | 2016 | high | performance/method
- Shi model "integral part of Singapore's dengue control program"; informed bed planning, staffing, messaging in 2013; Nat Comms 2025 says Singapore still uses a LASSO model operationally. | PMC5010413; https://pmc.ncbi.nlm.nih.gov/articles/PMC12727700/ | EHP; Nature Communications | 2016; 2025-11-22 | high | method
- Shi limitation: ~60 predictors at 12 weeks, opposite-sign lags, hard to interpret. | PMC5010413 | 2016 | high | limitation
- Hii et al.: Poisson regression, temp/rain lags to 16 weeks + 6 weeks case AR; 16-week horizon; trained 2000-2010; SRMSE 0.30/0.32, R2 0.84; 96-98% outbreak-alert sensitivity, <3% false alarms (2011). | https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0001908 | PLOS NTD | 2012 | high | performance
- Finch et al.: Bayesian hierarchical (INLA), 2000-2022 weekly, expanding window after 8-year block, 0-8 week horizons; climate-only 54% better than seasonal baseline, 60% with serotype; still 32% better at 8 weeks; outbreak AUC 0.94; got 2020 and 2022 timing right but underpredicted size; code public. | PMC12727700 | Nature Communications | 2025-11-22 | high | performance/limitation
- Chen et al. 2020: RF, Poisson, logistic, ARIMA on 2000-2016; 4-week nMAE RF 0.40, Poisson 0.44, ARIMA 0.58; 12-week RF 0.62, Poisson 0.66, ARIMA 0.40; weather-only models poor (~0.58-0.61 at 4 wk); none captured the 2013-2014 trend. | https://pmc.ncbi.nlm.nih.gov/articles/PMC7567393/ | PLOS NTD | 2020-10 | medium | performance
- 2024 ML study: 2012-2022 weekly (583 weeks), 19 weather vars lags 1-12; XGBoost R2 0.83 only with time/trend features; weather-only R2 <= 0.50; random 80/20 split likely leaks. | https://pmc.ncbi.nlm.nih.gov/articles/PMC11055163/ | MDPI TMID | 2024-03 | medium | performance/limitation
- Lai, Fung & Chew: CNN lowest RMSE for 2019 weekly cases with weather + Google Trends; horizon not stated; preprint. | https://arxiv.org/abs/2407.00332 | arXiv | 2024-06 | low | performance

## b. Weather lags
- Xu et al. (2001-2009): absolute humidity most stable predictor, window 0-16 weeks, strongest at 1 week; mean temperature window 0-9 weeks, peak ~12 weeks; rainfall weak (<0.15); effects vary by serotype period. | https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0002805 | PLOS NTD | 2014 | high | method
- Shi: recent cases (1-5 wk) positive; temperature mostly dampening, more at 4-12 week horizons; absolute humidity positive ~1 month, negative 15-20 weeks. | PMC5010413 | 2016 | high | method
- Finch: best predictors 12-week rolling max temperature (no lag), dry days in last 12 weeks, Nino 3.4; humidity dropped (collinear). | PMC12727700 | 2025 | high | method
- Benedum et al.: rainfall non-linear; 5+ "flushing" events a week cut outbreak risk 16-70% for ~6 weeks. | https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0006935 | PLOS NTD | 2018 | high | method
- DLNM study: each 1 C above 31 C max temperature ~13% lower cumulative risk over 6 weeks (snippet only). | https://pubmed.ncbi.nlm.nih.gov/33618312 | PubMed | ~2021 | low | method

## c. Training length and horizon
- Published models use 8-17 years; no study tests whether ~6 years suffices. Chen et al. (Stat Med 2020) trained a GAM+AR(2) on 6 years (2006-2011) and detected 2013/2014/2016 outbreaks via EWMA over 312 weeks; they list 6 years as a limitation. | https://pmc.ncbi.nlm.nih.gov/articles/PMC7318238/ | Stat Med | 2020 | medium | data
- Accuracy decays with horizon (Shi 17% to 24%; Finch gain 32% at 8 wk; RF 0.40 to 0.62). | as above | high | performance

## d. Limitations and baselines
- Serotype switches drive year-to-year variation; forecasts underpredict peak size (2020, 2022). | PMC12727700 | 2025 | high | limitation
- Baselines used: seasonal average, SARIMA, step-down, ARIMA, MOH mean+2SD, CUSUM; no study reports a pure persistence baseline. | various | medium | method

## e. Spatial
- NEA/EHI (Ong et al.): random forest ranks risk on 1 km2 grid, 4 groups, regenerated yearly; inputs previous-year cases, population density, Aedes breeding %, vegetation, connectivity; trained 2006-2013, validated 2014-2016; rank correlation 0.86-0.88; ~90% of clusters in high-risk grids; used by vector control officers since 2015. | https://pmc.ncbi.nlm.nih.gov/articles/PMC6023234/ | PLOS NTD | 2018 | high | method/performance

## Assistant implication (not evidence)
2-week national forecast from recent cases + weather is credible; cases carry most skill; ~15-25% MAPE realistic vs seasonal and persistence baselines; rolling-origin validation; expect peak underprediction; keep model simple given ~6 years.

## Leads
- Optimal lead time paper (PMC3475667, CAPTCHA); Finch code github.com/EmilieFinch/dengue-singapore; Sci Rep 2025 sustained hotspots; arXiv 2601.12856; Viruses 2022; PMC9451123; DLNM heat paper.

## Not found
- NEA page on current operational model; test of 6-year sufficiency; Singapore persistence baseline or explicit 2-week accuracy; arXiv CNN horizon; peer-reviewed 2025-26 deep-learning study.
