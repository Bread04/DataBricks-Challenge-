# 1 Oct checkpoint (30 min) · run by Braedon

Revised 28 Sep 2026 after the correct-course pivot (`_bmad-output/planning-artifacts/sprint-change-proposal-2026-09-28.md`).

Goal: leave with a go/adjust decision on the trained per-area forecast, and everything Komal needs to draft the 3 slides on 2-3 Oct.

**The go/adjust test:** does the archived cluster data give a usable weekly signal for enough planning areas to train and test a 2-week forecast? If yes, keep the plan. If not, fall back to the explainable points score as the per-area layer (still a valid demo) and say so on the slides.

## Bring

| Who | Brings |
|---|---|
| Braedon | Free Edition results incl. the new incremental-ingestion check, draft Island view map, `docs/model-definitions.md`, weekly lag chart, architecture diagram, draft prescriptive rule table |
| Jingyi | Weather dataset list, weekly national rainfall and temperature CSV (`week_start, rain_mm`), station-to-planning-area map with gaps |
| Ziqi | Per-area training panel CSV (`area_id, week_start, cluster_cases`) and coverage table; reconciled 2020 case count; where post-2022 weekly cases are published |
| Komal | Sourced statistics with links, NEA-dashboard description and cluster definition, resident story, Island view, Area view and resident-alert mock-ups |

## Agenda

| Min | Item | Decision needed |
|---|---|---|
| 0-5 | What changed on 28 Sep: the pivot, the new locked line, the new users | Everyone can say the idea back |
| 5-12 | **Training panel coverage** (Ziqi): weeks and areas with signal, June to December 2020 gap | **Go** on the trained model, or fall back to the points score |
| 12-17 | Free Edition results incl. incremental ingestion (Braedon) | Auto Loader / streaming on slide 3, or MERGE fallback |
| 17-21 | Lag chart and hypotheses H1 to H4 | Which hypotheses to state; drop "more rain = more risk" if the weekly chart agrees |
| 21-26 | Prescriptive rule table: drivers, actions, owners, timing, source links | Lock wording; flag anything not backed by NEA advice |
| 26-30 | Slide handoff to Komal | Owners and deadlines for the 2 Oct draft |

## Free Edition check (28 Sep 2026, Braedon's workspace)

| Area | Test | Works? |
|---|---|---|
| Egress | pypi.org; data.gov.sg dataset download, datastore API, real-time rainfall API | Yes (4/4) |
| Unity Catalog + Delta | Create schema and table; Delta history / time travel | Yes (2/2) |
| Spatial | `st_dwithin` in SQL; H3; shapely fallback | Yes (3/3) |
| MLflow | Log a run + model; register model in Unity Catalog | Yes (2/2) |
| Lakeflow Jobs | Daily 21:00 schedule of `01_cluster_snapshot_job` | Yes: archive live since 28 Sep (day 1: 11 clusters, 117 cases) |
| AI/BI dashboard | Point map of today's clusters (draft Island view) | Yes (tip: latitude ~1.3, longitude ~103.8) |
| Genie | "Which cluster has the most cases?" | Yes: Taman Jurong, 80 cases |
| Databricks Apps | Streamlit template starts | Yes |
| Incremental ingestion | Structured Streaming to Delta; Auto Loader picks up only new files; MERGE fallback | **Not run yet** (added 28 Sep, `00_free_edition_check.py` section 5) |

## Lines for Komal (already checked against data)

- Dengue cases: the 2020 record year and 2022 (MOH weekly bulletin, data.gov.sg). The two docs disagreed on 2020; summing the weekly file on 30 Sep gives 35,261 (peak week W30, 1,791) and 32,130 for 2022. Use 35,261 once Ziqi confirms the source.
- NEA's live feed showed 11 clusters on 28 Sep; the largest (80 cases, Taman Jurong) surrounds Taman Jurong Market & Food Centre.
- Feasibility proof: Databricks components on slide 3 were tested on Free Edition on 28 Sep, and the daily NEA cluster archive has run since 28 Sep.
- NEA already forecasts national cases and maps 1 km2 risk yearly. Our gap: **weekly, per planning area, with the drivers, and a plan of action for residents and community leaders.**
- Pitch line: "NEA's public dashboard shows today's clusters; DengueRadar shows where risk is heading, why, and what to do."
- Extra-care line only: 768,800 residents aged 65+ live in households; 88,400 live alone (SingStat via data.gov.sg, 2025); 614,380 residents are 65+ (15.2%, Census 2020).

## Do not put on the slides

- "Two weeks early" as a proven fact: lead time is unmeasured until the backtest runs.
- "NEA does not predict" without "public cluster dashboard".
- "More rain means more dengue": our monthly chart does not support it.
- That the model predicts total dengue cases: it predicts cluster activity (the archive holds only cases inside clusters).
- Effect sizes for actions ("cleaning drains cuts risk by X%"). We have no evidence; any what-if is illustrative.
- "Parks or hawker centres predict dengue": say "places where people gather".
- More archive days than we actually have: say "running since 28 Sep", not "months of history".
