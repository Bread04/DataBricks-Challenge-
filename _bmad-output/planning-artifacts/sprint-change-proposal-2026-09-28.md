# Sprint Change Proposal: refocus DengueRadar on real-time forecasting and prescriptive action

Date: 2026-09-28 · Author: Bread (Braedon) with Claude · Mode: Batch · Status: **APPROVED 28 Sep 2026 and applied** (living docs, diagram, notebook check, forge banners, research note, memory; meeting PDF regenerated) · Scope: **Major** (replan of idea, audience and model design; Round 1 is idea-only so cost is documents, not code)

Note on inputs: the repo has no PRD or epics file. `docs/team-plan.md`, `project-context.md`, `docs/model-definitions.md`, `DATASETS.md` and the four forge records act as the PRD. No epics exist yet (sprint starts 12 Oct).

---

## 1. Issue summary

**Trigger (strategic pivot).** The team realised it had focused on the wrong thing. The official problem statement is **DengueRadar: Real-time outbreak forecasting**: a near-real-time pipeline that combines live dengue cluster data, weather station readings and geospatial data into a forward-looking risk forecast **by planning area**, with streaming or incremental ingestion, weather feature engineering and a predictive model on an interactive map. NEA cluster monitoring is largely reactive; predictive risk intelligence should let communities act 2 to 4 weeks ahead.

**What we built the plan around instead.** The 27 to 28 Sep forges narrowed the product to Active Ageing Centre (AAC) staff and senior vulnerability, and settled on a two-level design where only the national level is a trained model and the per-area level is a hand-set points score. That drifted from the brief in three ways:

| Brief says | Current plan says |
|---|---|
| Forecast **by planning area** with a predictive model | National model trained; per-area is an explainable score, not a trained forecast |
| Audience: the **Singapore public and communities** | Main user: AAC staff; families and NEA secondary |
| Emphasis on predict-then-**act** (prescriptive measures) | Emphasis on ranking seniors to visit; actions exist but sit under a score |
| Problem: **NEA dashboards are reactive and do not predict** | Problem: seniors are least likely to be tested in time |

**New direction (from the user, 28 Sep):**
1. Problem = NEA's public dashboards show what has already happened; nobody shows where dengue is *going*.
2. Solution = trained planning-area risk forecast, 2 weeks ahead, plus **prescriptive measures** driven by the forecast and by what is driving it.
3. Audience = the Singapore audience: residents, and the community members who act (engaged residents, RC volunteers, condo MCST council members). NEA is the partner who acts on some causes, not the user.
4. Use the hackathon handbook (`github/08-datathon-handbook`) as the method.

**Decisions taken in this session:** batch review; audience = residents plus community leaders; per-area forecast **trained on the archived cluster data**; forge records kept as history with a superseded banner.

**Evidence that the pivot is feasible.** Ziqi's archive inspection (28 Sep): SGCharts has 256 clean snapshots from 3 Jul 2015 to 6 Nov 2020 (56,976 rows, all coordinates valid), and the Nature dataset has 20 weekly snapshots (28 Feb to 9 Jul 2020) with all 213 subzone IDs mapped to URA subzones. The live NEA feed has the same structure, and our daily archive has run since 28 Sep. Free Edition egress, Delta, Lakeflow Jobs, spatial SQL, MLflow, AI/BI, Genie and Apps all passed on 28 Sep.

---

## 2. Impact analysis (checklist results)

| # | Checklist area | Status | Finding |
|---|---|---|---|
| 1 | Trigger and context | [x] Done | Strategic pivot; evidence above |
| 2 | Epic impact | [N/A] | No epics exist. The MUST list in `team-plan.md` is rewritten instead (section 4.2) |
| 3.1 | PRD conflict | [x] Done | Problem, user, solution, slides and MUST list all change |
| 3.2 | Architecture conflict | [!] Action-needed | Diagram changes (per-area trained model, incremental weather ingestion, prescriptive engine). Streaming/Auto Loader on Free Edition is **untested** |
| 3.3 | UX conflict | [!] Action-needed | Island view stays; Centre view (block list for AAC) is replaced by Area view (drivers and actions). Family Ping mock becomes a resident alert mock |
| 3.4 | Other artifacts | [x] Done | `DATASETS.md` tiers change; forges get banners; PDF pack and memory regenerate |
| 4 | Path forward | [x] Done | **Direct adjustment** of documents, no rollback. Notebooks and the running archive job are unaffected. MVP review: we keep the same MVP shape (map + forecast + explanation), change what it predicts and who it serves |
| 5 | Proposal components | [x] Done | This document |

**What survives unchanged:** the daily Lakeflow cluster archive; Free Edition results; MOH national model (now a Level 1 context feature); weather work by Jingyi; boundary and subzone data; the 2020 replay idea; baselines and rolling-origin validation; roles and schedule; team rules.

**What is demoted, not deleted:** seniors. Track A is "Caring for an Ageing Singapore", and problem fit is 30% of the score. Census 65+ share stays as an optional "extra care" flag on the Area view and as the population denominator. It is no longer the headline and no longer multiplies the score.

**What is removed:** AAC as the main user; the visit-first block list as the centrepiece; the exposure x vulnerability matrix; the "seniors living alone" work; the Active Ageing Centre location gap (16b) as a risk.

### Honest risks introduced by the pivot

| Risk | Why it matters | Mitigation |
|---|---|---|
| **Training target is clustered cases, not all cases.** The archive only holds cases inside NEA clusters; sporadic cases are missing | The model predicts "cluster activity in the next 2 weeks", not total dengue | Name the target exactly on the slides: "new or growing cluster cases in a planning area, next 2 weeks" |
| **Thin training window.** Weekly-ish 2015 to May 2020, then monthly; 55 areas | Small panel, honest error bars needed; June 2020 onward is sparse | Rolling origin: train 2015 to 2018, test 2019; train to 2019, test Jan to Jul 2020 (Nature fills the surge). Report the gap as a limitation |
| **"NEA does not predict" is too broad.** Our own feasibility research recorded that NEA publishes national forecasts and a yearly 1 km2 risk map | A judge who knows this will catch an overclaim | Scope the claim to the **public cluster dashboard**: reactive, current clusters only, no forward-looking planning-area risk. **CONFIRM wording against NEA pages before slide 1** |
| **Streaming ingestion untested on Free Edition** | Brief asks for streaming or incremental ingestion | Add a check: Auto Loader or a streaming table on rainfall. Fallback: scheduled incremental job with a watermark (already the pattern in `01_cluster_snapshot_job`) |
| **"Real-time" is daily for clusters** | NEA updates clusters daily; weather is 5-minute | Say: clusters daily, weather every 5 minutes, forecast refreshed daily. Do not say "live streaming" for clusters |
| **Prescriptive effect sizes unknown** | A slider that says "clean drains, cut risk 30%" would be invented | Prescriptive layer = evidence-based actions with an owner agency (national bodies only, never a named Town Council, RC or MCST) and timing, not quantified benefit. Any what-if is labelled illustrative |
| **Track A fit** | Dropping seniors may weaken fit with "Caring for an Ageing Singapore" | Keep the senior flag as a secondary lens; confirm with Komal which track wording the Devpost form requires |
| **Time.** 8 days to 6 Oct; senior work already done by Komal and Ziqi | Some effort is now secondary | Ziqi's Census work is reused as denominator and flag; Komal's story rewritten around residents |

---

## 3. Recommended approach

**Direct adjustment (recommended).** Rewrite the living docs and the diagram around the new problem, keep every piece of built infrastructure, and turn the per-area score into a trained, explainable forecast with a prescriptive rule layer on top. Effort: about one focused day of document changes (this proposal applies them), plus the model design work already planned for the sprint. Timeline impact: none on the 6 Oct deadline; the 1 Oct checkpoint becomes the go/adjust point for the new data-supported claim (does the archive give a usable per-area signal?). Risk: medium, mainly the thin training window, and it is measured, not hidden.

Rejected alternatives: *keep senior-first* (contradicts the brief and the new direction); *rollback* (nothing built needs reverting); *drop the trained per-area model* (safer but leaves the brief's "predictive model by planning area" unmet).

### New idea in one paragraph

**Problem.** NEA's public dashboards show where dengue clusters already are. By then people have fallen sick and Aedes have been breeding for weeks. Nobody shows Singapore residents and community leaders where risk is heading in the next 2 weeks, or what to do about it.

**Solution.** DengueRadar ingests the daily NEA cluster feed and 5-minute weather readings incrementally into Delta, engineers weather and spatial features, and forecasts each planning area's dengue risk (Low, Medium, High) two weeks ahead. Every forecast comes with its top drivers (SHAP) and a **prescriptive action plan**: what residents should do at home, what any engaged resident, RC volunteer or MCST council member in a flagged area should inspect or clear first (a checklist, not routing to a named institution), and by when.

**Why it beats a dashboard.** It predicts instead of reports, it explains why, and it says what to do.

### Hypotheses (handbook method: `01-playbook/hypothesis-and-problem-framing.md`)

| ID | Hypothesis | Testable feature |
|---|---|---|
| H1 Weather lag | Warm periods, and rain 2 to 4 weeks earlier followed by dry spells, raise next-fortnight cluster activity. Our monthly chart supports temperature (+0.29 at 4 months) but not rain alone | `hot_days_31c`, `rain_lag2..4`, `temp_lag`, `humidity_lag` |
| H2 Spatial spillover | Clusters in neighbouring planning areas raise an area's own risk | `cluster_cases_adjacent_areas`, `dist_to_nearest_cluster` |
| H3 Recurrence | Areas with clusters in the past year recur, especially in older housing | `cluster_weeks_last_52`, `median_block_age` |
| H4 Green space (added 30 Sep) | Areas with a larger share of green space have more next-fortnight cluster activity, after controlling for population density. Say "associated with", not "causes". Untested | `green_space_share` (NParks parks / planning-area land), `pop_density`, `median_block_age` |

Any of these may be disproven (H4 also needs the leave-areas-out check, because it never varies within an area); the handbook says to say so.

### Method (handbook: `03-modeling/cross-validation-guide.md`, `dashboard-design-patterns.md`, `pitch-and-presentation-guide.md`)

- **Target:** cluster cases in planning area A in weeks t+1 to t+2, and a binary "rising" label (at least 20% above the area's 4-week average).
- **Models:** baselines first (persistence: "current clusters carry on"; seasonal average), then LightGBM in MLflow; a Poisson or logistic model as the explainable check.
- **Validation:** time-ordered splits only (`TimeSeriesSplit` logic, rolling origin), plus a leave-areas-out check (`GroupKFold` by planning area) to test that it is not memorising areas. Features for week t use only data available before week t.
- **Threshold:** chosen from a cost matrix (a missed rise costs more than an extra reminder), with alert load capped so residents and leaders keep trusting it (start: at most 15% of areas High).
- **Explainability:** SHAP top 3 drivers per area, shown on the map and used to choose the prescriptive action.
- **Demo:** Streamlit or Databricks App per the handbook's template; AI/BI map as the walking skeleton. A "Who are you?" selector shows one area through three lenses (Resident, Volunteer or group-chat admin, NEA), and the app generates each audience's payload. Nothing is sent externally.

### Prescriptive layer (the new centre of the product)

**Updated 30 Sep to match the Round 1 judging-fit review (supersedes the single-driver table that was here).** Wording still to be checked against NEA's public prevention advice before it goes on a slide (**CONFIRM**). Full table: `docs/model-definitions.md` section 6.

Two independent routing axes:

- **Axis 1, why it's rising (backbone).** The top 3 SHAP (or B3 rule) drivers map to up to 3 ranked, deduplicated actions, not one "leading driver". Overlapping actions collapse into one line.
- **Axis 2, who caused it (bonus layer).** NEA's cluster feed tags `HOMES`, `PUBLIC_PLACES`, `CONSTRUCTION_SITES`, but the field is sparse (2 of 11 clusters at the 27 Sep check). `CONSTRUCTION_SITES` routes to an NEA enforcement referral (national jurisdiction; a BCA role was not found). `HOMES` / `PUBLIC_PLACES` feed the resident checklist. Tag absent (~80%) falls back to Axis 1, and the Area view says "root cause not yet identified by NEA". The tag is used only for routing after a cluster exists, never as a model feature.

**Locked decision: no routing to a named Town Council, RC or MCST.** URA planning areas do not align with those boundaries and no open dataset maps them. Every community action is a checklist any engaged resident, RC volunteer or MCST council member can act on or escalate.

| Driver (Axis 1) | Resident action (this week) | Community checklist | Timing |
|---|---|---|---|
| Recent rain then warm spell | Empty flower-pot plates, gully traps and containers; cover storage | Check and clear drains, roof gutters and common-area standing water | Within 7 days |
| Active cluster nearby | Use repellent, wear long sleeves in the morning and evening, check for fever and get tested early (nearest CHAS clinic) | Remind neighbours in the blocks around the cluster | Within 3 days |
| Recurrence (past-year clusters, older blocks) | Routine weekly checks | Scheduled walk-through of known recurring spots | Within 14 days |
| High risk in adjacent area | Heightened awareness | Pre-check known problem spots; watch the neighbouring forecast | Before next week |
| Green space and places where people gather | Repellent before outdoor meals or exercise; check plant pot plates | Check drains, bins and stagnant water nearby; report to NEA or NParks | Within 7 days |

Extra-care flag: where the share of residents 65+ is in the top third, add "check on older neighbours and family members".

**Added 30 Sep (full spec: `docs/model-definitions.md` sections 6a to 6d):**

- **Inspection priority ranking (6a).** Two lists, "most cases" (`p x y_hat`) and "highest risk per resident" (per 10,000), with a budget slider K (default 8, about the 15% alert cap). Metric: **capture rate at K** on the backtest versus B1, filled only from measured values. It orders areas and does not claim that acting reduces cases.
- **Weekly action card (6b).** Per area: band and what changed, top 3 drivers in plain words, up to 3 ranked deduplicated actions as a checklist, root-cause line, a confidence line (only after the backtest), extra-care flag and source link. Backed by an action library table and the `area_priority` and `area_action_card` gold tables.
- **Who gets what (6c).** One forecast, three lenses. Split by relevance, not secrecy. The trigger for "sustained" High is tuned on validation years and frozen before the test year, and a new-vs-persistent flag limits alert fatigue. Language rules: "forecast cluster activity", "prevention priority", "Low is not zero", never "worst", "dangerous" or "safe".
- **Dissemination modes (6d).** Routed by who owns the action, not by geography. Residents are reached through their existing RC or constituency group chats, so the community mode is an **admin kit** with WhatsApp and Telegram copy buttons, a planning-area picker, and a date and "valid until" line. NEA gets a **weekly export file** plus a data contract. NEA enforcement, NEA drain cleansing (Department of Public Cleanliness) and NParks (role unconfirmed) get a **structured record per trigger** under one schema. MOH and other agencies are roadmap only. Agency jurisdictions are **unconfirmed** until checked against official sources. The prototype generates payloads and sends nothing.

---

## 4. Detailed change proposals (batch)

### 4.1 `project-context.md` (Selected problem section)

**OLD:** "Real-time dengue outbreak forecasting by Singapore planning area ... 2-4 week predictive risk intelligence to help communities act earlier than reactive cluster monitoring." with the target demo listing map, two-week forecast, explainable Low/Medium/High, baseline comparison, and stretch items hawker/green space/alerts/MLflow.

**NEW:** Same official statement kept verbatim under "Official brief". Add "Our angle": NEA's public cluster dashboard is reactive; DengueRadar is a trained planning-area forecast for residents and community leaders with a prescriptive action plan. Stretch items become core where the brief asks (MLflow comparisons, threshold alerts as a resident alert mock). Key dates and rules unchanged.

**Rationale:** brief and our angle now agree.

### 4.2 `docs/team-plan.md`

| Section | OLD | NEW |
|---|---|---|
| Opening paragraph | "forecast the national dengue wave, rank areas and blocks by senior risk, ... AAC staff visit-first list" | "forecast dengue risk by planning area two weeks ahead, explain why, and tell residents and community leaders what to do" |
| Locked line | "NEA shows today's clusters; we warn seniors' carers up to two weeks early." | "**NEA's public dashboard shows today's clusters; DengueRadar shows where risk is heading in the next two weeks, why, and what to do.**" Replace "two weeks" with measured lead time before Demo Day |
| Forge decisions table | Model, Data, Main user, Outputs, Why Databricks, Privacy rows built around seniors and AAC | Model: Level 1 national context forecast (MOH 2012 to 2022) + **Level 2 trained per-planning-area forecast** on archived clusters + weather + spatial features; Data: archive is now **training data (cited)**, live NEA feed drives the product; Main users: residents and community leaders; Outputs: Island view, Area view (drivers + actions), resident alert mock; Why Databricks: incremental ingestion, Delta, Unity Catalog lineage, MLflow, Genie; Privacy: areas only |
| Roles | Braedon platform/model; Ziqi dengue and places then demo; Jingyi weather; Komal pitch | Unchanged. Braedon also owns the prescriptive rule table with Komal reviewing wording |
| Round 1 tasks | Komal: senior statistics, Uncle Tan story, Family Ping for parents. Ziqi: seniors living alone, AAC locations. Braedon: Senior Dengue Risk Index | Komal: dengue burden numbers (2020 and 2022 cases, share of Singapore affected), NEA-reactive evidence, a resident story (replaces Uncle Tan; a family in a flagged area), resident alert and Area view mock-ups. Ziqi: build the weekly per-planning-area training panel from SGCharts and Nature, report coverage by area and week. Braedon: Area risk definition, prescriptive rule table, streaming/Auto Loader check. Jingyi: unchanged, plus weather-to-planning-area mapping |
| Slide draft | Three slides, senior-first prompts | Rewritten in section 4.7 below |
| Handoff contracts | `gold.area_exposure`, `gold.senior_risk` with `pct_seniors`, `seniors_living_alone`, `top_3_reasons` | `gold.area_week_features` (area_id, week_start, cluster_cases, cluster_cases_adjacent, rain_lag2..4, hot_days, temp_lag, humidity_lag, cluster_weeks_last_52, median_block_age, pct_65plus), `gold.area_risk` (area_id, week_start, risk_level, score, rising_prob, top_3_drivers, action_ids), `gold.action_rules` |
| MUST list | Senior risk score, centre view, Family Ping | Daily cluster archive; incremental weather ingestion; per-area training panel; trained 2-week area forecast beating baselines in MLflow with rolling-origin test; SHAP drivers; prescriptive action table; Island view and Area view; measured lead time and hit rate |
| Open questions | AAC contact, seniors living alone, Gravitrap | Reword: can we reach any town council, RC or NEA contact to sanity-check the action table; confirm NEA-dashboard wording; confirm track wording |

### 4.3 `docs/model-definitions.md` (full rewrite)

- Keep: baselines B1, B2; rolling-origin validation; no-leakage rule; known-weakness statement; MAE/MAPE/rising recall/lead time; 2020 replay.
- Replace Level 2 "points score x vulnerability" with the **trained per-area model** described in section 3, keeping the explainable points score as the **fallback baseline** ("explainable score") so we can show the trained model beats it.
- Add: target definition, features by hypothesis, cost matrix and threshold rule, alert-load cap, GroupKFold spatial check, SHAP drivers, prescriptive rule table, and the honest target caveat (clustered cases only).
- Remove: exposure x vulnerability matrix, "seniors living alone" language.

### 4.4 `DATASETS.md`

| Dataset | OLD | NEW |
|---|---|---|
| #17 SGCharts and Nature archive | Tier **Validation**, "never feeds the live product" | Tier **Core (training)**, cited; trains the offline model; live product still runs on official feeds |
| #7 to 9 Historical rainfall, temperature, humidity | Core | Core (unchanged) |
| #10 Realtime Rainfall | Should | **Core** (incremental ingestion is in the brief) |
| Weather station locations | not listed as a dataset | Add: station-to-planning-area mapping (Jingyi) |
| #4 Census 2020 residents by age | Core, "Senior vulnerability" | **Should**: population denominator and 65+ extra-care flag |
| #11 Parks, #12 Hawker centres | Should, "Environment +1" | Should: candidate features and "places where people gather" actions; kept only if they improve validation |
| #16 CHAS clinics | Could | Should: "nearest subsidised test" in the resident action |
| #16b AAC locations gap | Decision text about the centre view | Remove; note "no longer needed" |
| Header | Owners and "Round 1: Ziqi ... " | Same owners; add training-panel task to Ziqi |

### 4.5 `pitch/architecture_diagram.py` and `pitch/assets/architecture.png`

Five boxes stay (Sources, Ingest, Store + govern, Model, Act); text changes:
- **Ingest:** "Daily NEA cluster archive" + "Incremental weather ingestion (5-minute readings, pre-aggregated)".
- **Model:** "Trained 2-week forecast per planning area (LightGBM in MLflow)" + "vs baselines, rolling-origin test" + "SHAP drivers".
- **Act:** "Island view: planning areas Low / Medium / High" + "Area view: why + what to do" + "Genie: ask in plain English" + "Prescriptive action plan by owner".
- Used-by line: "Residents and group-chat admins · community volunteers (RCs, condo MCST councils) · NEA (comparison view)".
Regenerate the PNG.

### 4.6 `docs/checkpoint-1oct.md`

New agenda: (1) the pivot and new locked line; (2) per-area training panel coverage from Ziqi (the go/adjust test: enough weeks and areas with signal?); (3) lag chart and H1 to H3; (4) prescriptive rule table review; (5) streaming/Auto Loader check result; (6) slide handoff. Replace the "Lines for Komal" with dengue-burden and NEA-reactive lines; keep the "do not put on slides" list and add: "'NEA does not predict' without the words 'public cluster dashboard'".

### 4.7 Round 1 slide draft (in `team-plan.md`)

| Slide | New answer |
|---|---|
| 1 Problem | *In one sentence:* "NEA's public dashboards show dengue clusters after people are already sick, so residents and community leaders find out too late to prevent them." *Who and how badly:* dengue cases in the 2020 and 2022 outbreaks (MOH bulletin; reconcile 35,012 vs 35,261), and the live count of NEA clusters. *Why now:* rising temperatures and erratic rainfall extend the Aedes season. Problem code A2 DengueRadar |
| 2 Solution and data | "DengueRadar forecasts dengue risk for every planning area two weeks ahead, explains the drivers, and tells residents and community leaders what to do, so action starts before clusters form." Users: residents and group-chat admins, RC and condo MCST volunteers; NEA as a comparison view (not routed by named institution). Datasets: NEA clusters (live), MOH weekly cases, NEA rainfall, temperature and humidity, URA boundaries, SingStat Census (denominator), cited archive for training. Difference from a dashboard: predicts, explains, prescribes |
| 3 Architecture and impact | Pipeline naming Lakeflow Jobs and incremental ingestion, Delta bronze/silver/gold in Unity Catalog, MLflow, SHAP, AI/BI map or App, Genie. Demo: Island view plus Area view with actions plus 2020 replay. Impact: lead time in weeks, hit rate vs "clusters carry on" baseline, alert load. Two-week scope list |

### 4.8 Other files

| File | Change |
|---|---|
| `notebooks/00_free_edition_check.py` | Add a check cell: incremental ingestion with Auto Loader or a streaming table on the rainfall data; record pass/fail |
| `notebooks/01_cluster_snapshot_job.py`, `analysis/lag_chart.py`, `analysis/data/*` | No change (still valid) |
| `_bmad-output/forge/*/forged-idea.md` and `forge-report.html` (4 forges) | Add banner: "Superseded on 28 Sep 2026 by sprint-change-proposal-2026-09-28. Kept as history." Content untouched |
| `docs/team-meeting-28sep.pdf` and `make_pdf.py` | Regenerate for tonight's meeting around the pivot: new problem, solution, hypotheses, prescriptive table, changed tasks, and the pivot as decision D1 |
| Claude Docs copy of the pack | Blocked earlier by a connector error; retry after the PDF is regenerated |
| Memory `project-dengueradar-status.md` | Update to record the pivot |
| `github/`, `.agent/`, `.claude/`, `_bmad/`, `.opencode/` | N/A: toolkit and tooling, not project content |

---

## 5. Implementation handoff

**Scope: Major**, routed to PM/Architect roles in BMad terms; in practice the team lead (Braedon) approves and executes because Round 1 is document-only.

| Recipient | Responsibility |
|---|---|
| Braedon | Approve this proposal; own model-definitions, prescriptive rule table, architecture diagram, streaming check |
| Ziqi | Weekly per-area training panel and coverage report (1 Oct); reconcile 2020 case count |
| Jingyi | Weekly rainfall/temperature CSV; station-to-area mapping |
| Komal | New statistics and resident story; NEA-dashboard wording check; mock-ups; slides |

**Success criteria**
1. Every living doc says the same problem, user and locked line (no leftover "AAC staff", "Uncle Tan", "Senior Dengue Risk Index").
2. By 1 Oct: training panel exists with coverage stats, weekly lag chart is done, and the streaming check has a pass or fail.
3. By 3 Oct: the claim "predicts N weeks ahead" is backed by a measured backtest, or reworded to what the data supports.
4. Slides submitted by 4 Oct (deadline 6 Oct, 11:59pm SGT).

**Open items that need a human answer (not decided here)**
- CONFIRM the exact NEA-dashboard wording and NEA's cluster definition.
- CONFIRM the action wording with NEA's public prevention advice.
- CONFIRM which track name the Devpost form uses.
- Reconcile 2020 case count (35,261 vs 35,012).
