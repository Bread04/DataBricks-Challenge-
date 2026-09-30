---

> **Note, 28 Sep 2026 (correct-course pivot):** the positioning below (senior-weighted, block-level, carer-facing) is superseded. The evidence still holds: NEA already forecasts nationally and maps 1 km2 risk yearly, so our claim must be scoped to NEA's *public cluster dashboard* and to what we add: a weekly, per-planning-area, explained forecast with a prescriptive action plan for residents and community leaders. See `sprint-change-proposal-2026-09-28.md`.

title: 'technical research: DengueRadar feasibility on Databricks Free Edition'
type: 'technical'
topic: 'DengueRadar feasibility on Databricks Free Edition'
decision: 'Go/no-go: can DengueRadar be built on Databricks Free Edition in a 2-week sprint by 4 students?'
source: 'native run'
status: complete
preset: 'quick'
validation: 'normal'
claims_verified: 3
claims_unverified: 8
created: '2026-09-28'
updated: '2026-09-28'
---

# Technical research: DengueRadar feasibility on Databricks Free Edition

**Decision this research serves:** Go/no-go: can DengueRadar be built on Databricks Free Edition in a 2-week sprint by 4 students?

## Executive summary

**Verdict: GO, with three conditions.** Every component of DengueRadar has documented support on Databricks Free Edition, and a 2-week-ahead national dengue forecast matches published Singapore practice. The idea is buildable in a 2-week sprint if the team treats three findings as hard constraints:

1. **Outbound internet is restricted on Free Edition.** Notebooks reach only a limited, unpublished set of trusted domains; LinkedIn identity verification unlocks outbound access but not all limits [1][2]. Whether data.gov.sg is reachable is unknown until tested. This is the biggest risk: the daily Lakeflow archive, the core "why Databricks" answer, depends on it. **Test it on day one.**
2. **Quotas are real but unpublished.** Exceeding them stops compute for the rest of the day, in extreme cases the month [1]. The ~30 GB of raw 5-minute weather must be pre-aggregated outside Databricks and uploaded as small daily tables (UI uploads cap at 5 GB per file) [1][8].
3. **NEA already forecasts dengue and maps risk.** NEA runs a LASSO national forecast 1 to 12 weeks ahead (MAPE 17% to 24%) and has used a random-forest 1 km² risk map since 2015 [10][18]. DengueRadar cannot claim forecasting itself as new. Its originality must rest on what NEA's tools do not do: a **weekly, senior-weighted, block-level visit list for carers, with root causes routed to their owners**.

Biggest caveat: **recent case counts carry most of the forecast skill; weather alone is weak** [13][14][15], and two forge rules conflict with the literature (hot days above 31 °C and heavy rain both tend to *lower* risk) [10][16][19]. They need redesign before the pitch uses them as "reasons".

## D1. Free Edition platform: capabilities and limits

Free Edition is serverless-only and replaced the retired Community Edition; it is for learning and non-commercial use [1]. Jobs are available with at most **5 concurrent job tasks** per account; Lakeflow pipelines allow **one active pipeline per type**; there is **one SQL warehouse at 2X-Small**; **Databricks Apps are capped at 3 and stop 24 hours after start**, with manual restart [1] (medium: single official source). Model Serving exists with no GPU, no provisioned throughput and no batch inference [1]. Unity Catalog, Genie, Lakeflow and dashboards are listed as included [1][20]; no page confirms MLflow tracking, the model registry or lineage individually (open question).

**Network:** outbound access is "restricted to a limited set of trusted domains"; staff confirm there is no public allowlist and it may vary by region; pypi.org works, wikipedia.org does not [1][2] (high, verified). LinkedIn verification raises limits including outbound access, but does not remove all limits [1]. An older thread shows general `requests.get` calls failing by design [3] (medium, pre-dates verification).

**Libraries and runtime:** notebook-scoped `%pip install` from PyPI works [9] (medium). Serverless has no RDDs, `cache()` and `persist()` fail, UDFs cannot reach the internet and are capped at 1 GB, and libraries are reinstalled each session [4] (high).

## D2. Forecasting evidence (Singapore)

**A 2-week national forecast is supported by the literature.** NEA's operational LASSO model forecasts weekly national cases 1 to 12 weeks ahead with MAPE 17% at 1 week and 24% at 3 months, beating SARIMA except in the first two weeks [10] (high, verified). A 2025 Bayesian model on 2000 to 2022 data was 54% better than a seasonal baseline, still 32% better at 8 weeks, and caught the *timing* of the 2020 and 2022 peaks while underpredicting their *size* [11] (medium). Hii et al. reached 96 to 98% outbreak-alert sensitivity with under 3% false alarms [12] (older, foundational).

**What drives skill:** recent cases (1 to 5 weeks) are the strongest predictors; weather-only models perform poorly (nMAE about 0.6 at 4 weeks; R² at most 0.50) [13][14]. Absolute humidity is the most stable weather predictor; rainfall correlation is weak [15]. Rainfall is non-linear: heavy "flushing" rain cuts outbreak risk by 16 to 70% for about 6 weeks [16]. Temperature is mostly dampening at high values [10]; one study links each 1 °C above 31 °C to about 13% lower risk (low confidence, snippet only) [19].

**Training length:** published models use 8 to 17 years; one used 6 years and listed it as a limitation [17]. The weather-overlap window of 2017 to 2022 (~310 weeks) is short, so the model should stay simple (regularised or Poisson regression, or a small tree model with few lags), use all 2012 to 2022 case history, and be evaluated with rolling-origin validation, never a random split (a 2024 study's random split likely inflated its R² of 0.83) [14]. No Singapore study reports a pure persistence baseline or accuracy exactly at 2 weeks (open question).

**Spatial:** NEA's random-forest risk map ranks 1 km² grids into 4 groups each January, trained on 2006 to 2013; about 90% of clusters fell in high-risk grids; used operationally since 2015 [18] (high, verified).

## D3. Implementation reality: geospatial and data volume

Spatial SQL (GEOMETRY and 90+ ST_ functions such as `st_contains`, `st_buffer`, `st_dwithin`) became GA on 2026-06-11 for Databricks SQL and Runtime 17.1+, together with AI/BI Maps [5][6]; H3 functions run on all compute except classic SQL warehouses [7]. Free Edition is not named in either source (medium), but serverless is not a classic warehouse, and `shapely`/`geopandas` via `%pip` is a working fallback [9]. The 332-subzone joins and 200 m buffers are small workloads.

Files: UI uploads cap at 5 GB per file; larger files go through the SDK, CLI or Files API [8]. Downloading from the web inside a notebook depends on egress (D1). Pre-aggregating the 5-minute weather outside Databricks fits the upload path and protects the unpublished quota.

## Cross-dimension insights

- **The egress limit threatens the "why Databricks" story, not just ingestion.** The forge locked "scheduled Lakeflow jobs building our own cluster archive" as the core platform answer. If data.gov.sg is not on the trusted list and LinkedIn verification does not open it, the daily snapshot must run elsewhere (for example a scheduled script uploading via the Files API), which weakens that answer. Test before the slides promise it.
- **NEA's existing tools sharpen the idea rather than kill it.** NEA's map is yearly, 1 km², and built for vector-control officers; its forecast is national and built for planners [10][18]. Neither is weekly, senior-weighted, block-level, or aimed at carers. DengueRadar's positioning becomes "the last mile of NEA's science, delivered to the people who visit seniors", and the pitch can cite NEA's models as proof the approach works.
- **The evidence changes two forge rules.** "Hot days above 31 °C" and "+1 for above-normal rain" conflict with [10][16][19]. Let Level 1 learn weather directions from data, and in Level 2 replace the rain point with an evidence-backed signal (for example humidity, or rain without flushing events) or drop it in favour of the Aedes hotspot layer.

## Contrary evidence

Red-team pass was off for this run. The strongest counter-signal found incidentally: Finch et al. note authorities need about two months to mitigate an outbreak [11], which suggests a 2-week lead time may be too short for agencies. It is less of a problem for carers, whose actions (removing breeding sites, fever checks) take days, not months.

## Recommendations

1. **Test egress first.** From a Free Edition notebook, call the data.gov.sg API with and without LinkedIn verification, before the Round 1 slides promise a daily Databricks archive. Feeds: architecture constraint. Confidence: high that the limit exists [1][2]; unknown whether data.gov.sg is allowed.
2. **Keep Databricks light.** Pre-aggregate weather to daily per-station tables outside Databricks; keep every table small; serve the demo from Delta, never live APIs; restart Apps before demos. Feeds: architecture spine. Confidence: high [1][8].
3. **Level 1 design.** Forecast national cases at t+2 with lagged cases as core features plus humidity, temperature and rain lags; baselines are seasonal average and persistence; rolling-origin validation; report MAPE and outbreak detection; state peak underprediction openly. Feeds: spec and stories. Confidence: high for the approach [10][11][13]; medium for any accuracy number until measured.
4. **Reposition in the Round 1 slides.** Acknowledge NEA's national forecast and 1 km² map, and claim the gap: weekly, senior-weighted, block-level, carer-facing, with root-cause routing. Feeds: brief and pitch. Confidence: high [10][18].
5. **Revise the two weather rules** in the risk matrix before they appear as "reasons". Feeds: spec. Confidence: medium (several studies, mixed strength) [15][16][19].

## Open questions

- Is data.gov.sg on Free Edition's trusted-domain list, and does LinkedIn verification open it? Answer: a 5-minute notebook test.
- Numeric daily quotas and storage caps are unpublished. Answer: monitor usage during the sprint.
- Do MLflow registry, Unity Catalog lineage, AI/BI Maps and ST_/H3 functions run on Free Edition? Answer: try each in the workspace in the first hour.
- Accuracy at exactly 2 weeks with ~6 years of weather has no published figure. Answer: our own backtest.

## Source appendix

| n | Supports | Publisher | Pub date | Accessed | Confidence |
|---|---|---|---|---|---|
| 1 | Free Edition limits: egress, quotas, jobs, pipelines, warehouse, apps, serving | [Databricks docs via Microsoft Learn](https://learn.microsoft.com/en-us/azure/databricks/getting-started/free-edition-limitations) | 2026-09-11 | 2026-09-28 | high |
| 2 | No public allowlist; pypi allowed, wikipedia blocked | [Databricks Community, staff answer](https://community.databricks.com/t5/databricks-free-edition-help/whitelist-for-outbound-network-access/td-p/146591) | 2026-02-02 | 2026-09-28 | high |
| 3 | General outbound requests blocked by design | [Databricks Community](https://community.databricks.com/t5/data-engineering/free-edition-outbound-internet-suddenly-blocked-error/td-p/121832) | 2025-06 | 2026-09-28 | medium |
| 4 | Serverless runtime limitations | [Databricks docs via Microsoft Learn](https://learn.microsoft.com/en-us/azure/databricks/compute/serverless/limitations) | 2026-09-11 | 2026-09-28 | high |
| 5 | Spatial SQL GA, AI/BI Maps | [Databricks blog](https://www.databricks.com/blog/geospatial-unbounded-spatial-sql-ga-aibi-maps-delta-sharing-and-iceberg-v3) | 2026-06-11 | 2026-09-28 | high |
| 6 | ST_ function list and runtime | [Databricks docs via Microsoft Learn](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/sql-ref-st-geospatial-functions) | 2026-09-11 | 2026-09-28 | high |
| 7 | H3 functions and compute support | [Databricks docs via Microsoft Learn](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/sql-ref-h3-geospatial-functions) | 2026-09-11 | 2026-09-28 | medium |
| 8 | 5 GB upload cap; SDK/CLI for larger | [Databricks docs via Microsoft Learn](https://learn.microsoft.com/en-us/azure/databricks/volumes/volume-files) | 2026-09-15 | 2026-09-28 | high |
| 9 | %pip works on Free Edition | [Databricks Community](https://community.databricks.com/t5/databricks-free-edition-help/is-it-possible-to-install-python-libraries-or-any-python-wheels/td-p/125594) | 2025-07-17 | 2026-09-28 | medium |
| 10 | NEA LASSO forecast, MAPE 17-24%, weather effects | [Environ Health Perspect (Shi et al.)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5010413/) | 2016 | 2026-09-28 | high |
| 11 | Bayesian model vs seasonal baseline; peak underprediction; 2-month mitigation need | [Nature Communications (Finch et al.)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12727700/) | 2025-11-22 | 2026-09-28 | medium |
| 12 | Outbreak-alert sensitivity 96-98% | [PLOS NTD (Hii et al.)](https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0001908) | 2012 | 2026-09-28 | medium |
| 13 | Weather-only models weak; RF vs Poisson vs ARIMA | [PLOS NTD (Chen et al.)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7567393/) | 2020-10 | 2026-09-28 | medium |
| 14 | ML on 2012-2022; random-split caution | [Trop Med Infect Dis](https://pmc.ncbi.nlm.nih.gov/articles/PMC11055163/) | 2024-03 | 2026-09-28 | medium |
| 15 | Humidity most stable; rainfall weak | [PLOS NTD (Xu et al.)](https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0002805) | 2014 | 2026-09-28 | medium |
| 16 | Flushing rain lowers outbreak risk | [PLOS NTD (Benedum et al.)](https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0006935) | 2018 | 2026-09-28 | medium |
| 17 | 6-year training flagged as limitation | [Statistics in Medicine (Chen et al.)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7318238/) | 2020 | 2026-09-28 | medium |
| 18 | NEA 1 km² risk map operational since 2015 | [PLOS NTD (Ong et al.)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6023234/) | 2018 | 2026-09-28 | high |
| 19 | Heat above 31 °C lowers risk | [PubMed 33618312](https://pubmed.ncbi.nlm.nih.gov/33618312) | ~2021 | 2026-09-28 | low |
| 20 | Free Edition feature list | [Databricks](https://www.databricks.com/learn/free-edition) | undated | 2026-09-28 | medium |

## Staleness map

Platform limits [1][3][4][9] and version or feature claims [5][6][7][8][20] age fastest (technical pack: versions within 1 month, ecosystem within 6 months). **Earliest re-check: 2026-10-28**, before Demo Day: re-read the Free Edition limitations page. Forecasting method claims [10] to [19] are pattern-class (within 2 years): re-check by 2027-09.
