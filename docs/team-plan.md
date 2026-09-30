# DengueRadar Team Plan

Sep 26, 2026 · @yanherngggg · **Revised 28 Sep 2026 (correct-course pivot)**

We submit the Round 1 three-slide PDF on Devpost by Oct 4, 2026, two days before the 6 Oct deadline. **The idea, as of 28 Sep:** NEA's public dashboards are reactive, so DengueRadar forecasts dengue risk for every planning area two weeks ahead, explains why, and tells Singapore's residents and community leaders what to do about it. The problem statement is **DengueRadar: Real-time outbreak forecasting** (A2).

Why we changed: we had narrowed the product to senior vulnerability and Active Ageing Centre staff, and only the national level was a trained model. The brief asks for a forward-looking forecast by planning area, a near-real-time pipeline with incremental ingestion, and a predictive model on a map. Full reasoning and file-by-file edits: `_bmad-output/planning-artifacts/sprint-change-proposal-2026-09-28.md`. The four earlier forges that pressure-tested the superseded senior-first design were removed on 30 Sep once the pivot made them obsolete.

Full dataset findings: `DATASETS.md`. Model details: `docs/model-definitions.md`.

## Decisions (28 Sep)

Our answer to "why not NEA's map?" is locked: **"NEA's public dashboard shows today's clusters; DengueRadar shows where risk is heading in the next two weeks, why, and what to do."** Replace "two weeks" with the lead time our backtest measures before Demo Day. Never say "NEA does not predict" without "public cluster dashboard": NEA publishes national forecasts and a yearly risk map.

| Area | Decision | Why |
| --- | --- | --- |
| Problem | NEA's public cluster dashboard is reactive: it shows clusters after people are sick. Nobody shows residents and community leaders where risk is heading | Matches the brief; gives one clear gap |
| Model | Level 2 (the product): a **trained** 2-week risk forecast per planning area (LightGBM in MLflow) from lagged clusters, weather and spatial features, trained on the archived cluster data and tested on unseen years. Level 1 (context): national weekly forecast from MOH cases 2012 to 2022. Explainable points score kept as a baseline | Official open data has no per-area case history, but the cited SGCharts and Nature archives give a weekly per-area cluster panel. Target is cluster activity, not total cases; say so |
| Data | Official sources (data.gov.sg, SingStat, NEA) run the product. Archived cluster data (SGCharts 2015 to 2020; Nature Scientific Data 2022) is now **training data**, cited | Rules allow cited public data (daisi.online). The live product does not depend on a third-party archive |
| Users | Residents (a personal action list) and community leaders: town councils, RCs, condo MCSTs (inspection and outreach priorities). NEA is the partner who acts on some causes. Seniors: an "extra care" line for areas with a high 65+ share, not the headline | The brief's audience is Singapore's communities. Track A is "Caring for an Ageing Singapore", so seniors stay visible |
| Prescriptive | Each forecast shows its top 3 drivers (SHAP) and maps the leading driver to actions with an owner and a timing (rule table in `docs/model-definitions.md`). No invented effect sizes | Prediction without action is another dashboard |
| Outputs | Island view: planning areas Low, Medium, High. Area view: risk, drivers, actions. Resident alert (mock). 2020 replay | One map, one drill-down, one story |
| Ingestion | Daily Lakeflow archive of NEA clusters (live since 28 Sep) plus incremental loading of 5-minute weather. Streaming or Auto Loader tested in `notebooks/00_free_edition_check.py` (section 5); fallback is a MERGE watermark. Clusters update daily, weather every 5 minutes: never call clusters "live streaming" | Brief asks for streaming or incremental ingestion |
| Why Databricks | Incremental ingestion, Delta bronze/silver/gold in Unity Catalog with lineage, MLflow, AI/BI map, Genie, Apps | Laptop cannot run a daily archive; it started 28 Sep |
| Method | Handbook: 4 hypotheses (weather lag, spatial spillover, recurrence, green space), time-ordered validation plus leave-areas-out check, cost-matrix threshold, SHAP, pitch blueprint | `github/08-datathon-handbook` |
| Privacy | Outputs planning areas and public places only | No personal data allowed |

Open risks: lead time not yet measured; thin per-area training window (weekly to May 2020, monthly after); target is clusters only; streaming on Free Edition untested until the notebook runs; NEA-dashboard wording and the action wording unconfirmed; nobody has spoken to a town council, RC or NEA contact; our own archive is about 30 days deep by Demo Day.

## Roles

Roles shift by phase. In Round 1, Jingyi and Ziqi both gather data, split by source so they never duplicate work. In the sprint, Ziqi moves to the demo. Braedon owns the platform, pipeline and model throughout, and leads the team.

| Person | Role | Round 1 job (now to 4 Oct) | Sprint job (12 to 26 Oct) |
| --- | --- | --- | --- |
| Braedon | Team lead + Platform & Data Architect + ML Modeler | Workspace and Free Edition tests (incl. incremental ingestion); architecture diagram; lag chart; hypotheses, baselines, metrics and prescriptive rule table | Ingestion and bronze/silver/gold tables, weekly area feature table, LightGBM forecast in MLflow, SHAP drivers, action rules, backtest |
| Jingyi | Data: weather | Verify and download rainfall, temperature, humidity (real-time and 2016 to 2024) and weather station locations; map stations to planning areas | Keep collecting and checking data; then take the silver cleaning tables from Braedon |
| Ziqi | Data: dengue & places, then Demo Engineer | Verify and download dengue cases, clusters, boundaries, population; **build the weekly per-planning-area training panel from the archives and report coverage** | Moves to the demo: Island view and Area view (AI/BI dashboard or App), Genie space, resident alert mock, 2020 replay screen, 30-second backup video |
| Komal | Story & Pitch Lead | Sourced statistics on dengue burden, evidence that NEA's public dashboard is reactive, a resident story, Island view and Area view and resident-alert mock-ups, 3 slides, Devpost submission | Mentor questions, demo script, rehearsals, judge Q&A answers |

Handover rule: Ziqi hands any unfinished data work to Jingyi at sprint kickoff (12 Oct) and starts the demo on a fake forecast table. Once all raw data is delivered (target 13 Oct), Jingyi takes the silver cleaning tables so Braedon can focus on the model.

## Round 1 schedule

No code is required for Round 1, but a real weather-versus-cases chart, a per-area training panel and a verified dataset list make the feasibility score (25%) much stronger. The 1 Oct checkpoint is the last cheap moment to change the idea.

| Date | Who | Task | BMad skill |
| --- | --- | --- | --- |
| 27 Sep (Sun) | All | Kickoff call: confirm roles, walk through the brainstorm result, agree this plan |  |
| 27 Sep | Braedon | Stress-test the earlier idea | /bmad-forge-idea |
| 28 Sep | Braedon | Create the Databricks workspace and invite everyone |  |
| 28 Sep (10pm) | All | **Pivot meeting**: agree the new problem, users and tasks | /bmad-correct-course |
| 28 to 30 Sep | Jingyi | Verify and download weather datasets; station-to-area mapping | /bmad-deep-recon |
| 28 to 30 Sep | Ziqi | Verify dengue, boundary and population datasets; build the per-area training panel | /bmad-deep-recon |
| 28 to 30 Sep | Komal | Research and cite statistics; draft the resident story | /bmad-deep-recon |
| 28 Sep to 1 Oct | Braedon | Run the incremental-ingestion check; architecture diagram; weekly lag chart; hypotheses, baselines, metrics, action rules |  |
| 30 Sep to 1 Oct | Komal | Island view, Area view and resident-alert mock-ups |  |
| 1 Oct (Thu) | All | Checkpoint: does the archive give a usable per-area signal? Adjust now if not |  |
| 2 to 3 Oct | Komal (lead), all feed in | Draft the 3 slides from the official template | /bmad-cis-storytelling, /bmad-cis-agent-presentation-master |
| 3 Oct (Sat) | All | Mock judging: scores plus the hardest questions | /bmad-party-mode (judges panel) |
| 4 Oct (Sun) | Komal | Final polish, export PDF, submit on Devpost | /bmad-review |
| 5 to 6 Oct |  | Buffer. Deadline is 6 Oct, 11:59pm SGT |  |

## Round 1 tasks by person

Every task has a due date and a "done when" test, so everyone knows when to hand off. Tick items here as you finish them.

### Everyone

- [ ] Read project-context.md and github/08-datathon-handbook/first-datathon.md before kickoff (27 Sep)
- [ ] Attend the 27 Sep kickoff call; confirm your role or ask to swap
- [ ] Attend the 28 Sep pivot meeting; read `_bmad-output/planning-artifacts/sprint-change-proposal-2026-09-28.md`
- [ ] Send Komal your name, institution, course, year and email (28 Sep)
- [ ] Create a Databricks Free Edition account (28 Sep); Braedon will add you to the workspace
- [ ] Post blockers in the team chat the same day; do not wait for the checkpoint
- [ ] Attend the 1 Oct checkpoint and the 3 Oct mock judging
- [ ] Review the final PDF before Komal submits (4 Oct)

### Braedon: Team lead + Platform & Data Architect + ML Modeler

- [x] Run the 27 Sep kickoff: walk through the brainstorm result and this plan (30 min)
- [x] Run /bmad-forge-idea on the earlier idea; share the verdict with the team (27 Sep)
- [x] Create the team Databricks Free Edition workspace and invite everyone (28 Sep)
- [x] Confirm which of Lakeflow, Unity Catalog, MLflow, AI/BI dashboards, Genie and Databricks Apps work on Free Edition (28 Sep). Done: yes/no list posted below
- [x] Start the daily Lakeflow job that saves the NEA Dengue Clusters GeoJSON into a Delta table (28 Sep). Live since 28 Sep
- [x] Draw the architecture diagram for slide 3 (updated 28 Sep for the new design: `pitch/assets/architecture.png`, source `pitch/architecture_diagram.py`)
- [x] Define the baseline, metrics and model (rewritten 28 Sep: `docs/model-definitions.md`)
- [ ] Run the new incremental-ingestion check (`notebooks/00_free_edition_check.py`, section 5: Structured Streaming, Auto Loader, MERGE fallback) and post pass or fail (29 Sep). Done when: three yes/no lines in this doc
- [ ] Build the weekly lag chart (30 Sep) from Ziqi's case CSV and Jingyi's rainfall CSV: weekly cases against weekly weather, shifted 0 to 8 weeks. Done when: one chart shows which lag lines up best for temperature, rain and humidity (tests H1)
- [ ] Turn the prescriptive rule table into a one-page draft for Komal and a neutral reviewer (1 Oct). Done when: every action has a timing, a resident or community checklist wording (no named Town Council, RC or MCST) and a source link to NEA's prevention advice
- [ ] Write the action library (1 Oct): 8 to 10 actions with `action_id, resident_text, community_text, timing_days, source_url, driver_tags`, plus the feature-to-plain-words lookup. Done when: every H1 to H4 driver maps to at least one action and Komal has reviewed the wording. **Draft written 30 Sep: `docs/action-library.md` (11 actions, all `source_url` still CONFIRM); awaiting Komal review and source links**
- [ ] Build the `area_priority` gold table and the capture rate at K (15 to 19 Oct, **after Round 1, sprint only (if shortlisted); not needed for the slides**), after the backtest: both ranked lists (most cases, highest risk per resident), rank change, low-data flag. Done when: capture rate at K = 8 is reported for M1 and B1 on unseen years
- [ ] Build the `area_action_card` gold table (15 to 19 Oct, **after Round 1, sprint only (if shortlisted); not needed for the slides**): top 3 drivers to deduplicated ranked actions, what-changed, root-cause line, confidence line per risk band. Done when: one card renders for a real flagged area and a 2020 replay week
- [ ] Add the K slider, an alert-threshold slider, the two priority lists and the action card to the Island and Area views (19 to 24 Oct, **after Round 1, sprint only (if shortlisted); not needed for the slides**), with Ziqi. The two sliders are the honest interactive core (capture rate and alert load update live; no effect sizes). Done when: the demo goes Island view, then click an area, then its card, in under 60 seconds
- [ ] Add the "Who are you?" selector with three lenses (Resident, Volunteer, NEA) to the app (19 to 24 Oct, **after Round 1, sprint only (if shortlisted); not needed for the slides**), with Ziqi. Done when: one area shows three different views, and the NEA view has the conditional construction-referral row with its empty state
- [ ] Add the new-vs-persistent flag and the weeks-in-High distribution to the backtest (15 to 19 Oct, **after Round 1, sprint only (if shortlisted); not needed for the slides**). Also log out-of-fold predictions to MLflow (hackathon guide, Standard 3). Done when: the distribution is reported and the "sustained" escalation trigger is tuned on validation years and frozen before the test year
- [ ] Give Komal the slide text in `pitch/round1-outline.md` (2 Oct): the one-sentence template, the mock post, one hypothesis line, the targets-not-claims impact wording and the cut list. Done when: Komal has it and the language rules (no "worst", "dangerous", "safe"); the "who gets what" matrix stays off the three slides
- [ ] Write the data contract and the weekly export (schema drafted; the export is sprint work, 15 to 19 Oct, **after Round 1, sprint only (if shortlisted); not needed for the slides**): one versioned schema (`area_id, week, band, band_change, top_drivers, action_ids, confidence, coverage_flag, tag, caveat, valid_until`), the NEA weekly CSV/GeoJSON export from the gold table, and an `owner_agency` column in the action library. Done when: the export file opens cleanly and the schema is written in `docs/`. **Schema drafted 30 Sep: `docs/data-contract.md`; the export waits for the gold table**
- [ ] Build the admin kit (19 to 24 Oct, **after Round 1, sprint only (if shortlisted); not needed for the slides**), with Ziqi: WhatsApp and Telegram versions of the weekly post, multi-select planning-area picker, "valid until" date, copy buttons. Done when: one flagged area produces both versions and a teammate can paste them into a chat
- [ ] Generate the agency records (19 to 24 Oct, **after Round 1, sprint only (if shortlisted); not needed for the slides**): one sample structured record each for the NEA enforcement referral, the NEA drain-cleansing record and NParks (role unconfirmed), from the trigger rules. Done when: each renders in the app and an empty state shows when no trigger fires
- [ ] Confirm agency jurisdictions (2 Oct), with Komal: check each named agency's role against official sources. Done when: every agency on the routing slide has a source link, or is moved to the roadmap. **First pass done 30 Sep (results in `docs/model-definitions.md` 6d): construction sites are NEA, drain cleansing is NEA's Department of Public Cleanliness (not PUB), NParks' role is not found, CDA is the health-sector body. Komal still needs to read the source pages**
- [ ] Prepare demo fallbacks (25 Oct, **after Round 1, sprint only (if shortlisted); not needed for the slides**): a 60-second screen recording of the working journey, a local run from a cached gold-table snapshot (Free Edition apps can auto-stop), and one screenshot per lens. Done when: fallbacks are in `pitch/assets/`
- [ ] Optional, Round 1 (2 Oct): compute the status-quo baseline's capture rate at K = 8 from the archive ("top 8 areas by last-4-weeks cases" against the next fortnight's cases), once Ziqi's per-area panel exists. Done when: one number with its date range, or dropped from the slide
- [ ] Update `pitch/assets/architecture.png` for slide 3 (2 Oct): add the admin-kit and weekly-export outputs and name each Databricks component's job in at most 4 bullets
- [ ] Hand the diagram and lag chart to Komal as PNGs (1 Oct)
- [ ] Run the 1 Oct checkpoint: go or adjust, based on the training-panel coverage
- [ ] Run /bmad-party-mode with the judges panel on 3 Oct; list the top 5 judge questions and our answers
- [ ] **Have one real conversation** with an RC volunteer, MCST council member or group-chat admin (2 Oct), anyone on the team who knows one. Script, interview kit (two draft posts and an answer card) and slide use are in `pitch/round1-outline.md`; the reasoning is in `_bmad-output/design-thinking-2026-09-30.md`. Done when: one anonymised, permitted quote is on slide 2, or the slot is removed. Never invent or paraphrase a quote
- [ ] **Re-import the hardened `notebooks/01_cluster_snapshot_job.py` into the workspace (1 Oct), run it once, and turn on the job's failure email.** The repo copy is updated but the scheduled job still runs the old copy until you re-import. It now writes `bronze_snapshot_runs` (ok, empty or failed per day) and stops on a renamed field or all-zero case counts. Done when: the runs table shows today's row and a failed run sends an email
- [ ] Keep the daily snapshot job healthy (check daily, 30 Sep to 6 Oct). Done when: the slide can say "N days of live snapshots collected" with N = `days_of_history` from `bronze_snapshot_runs` (status ok or empty), read on the day, and no day is missing
- [ ] Cold-judge check (3 Oct): someone outside the team reads the three slides once and explains the idea back; fix anything unclear

#### Braedon's update (28 Sep)

Everything we plan to use works on Databricks Free Edition, and the daily NEA cluster archive has been live since 28 Sep (day 1: 11 clusters, 117 cases). Incremental ingestion (Structured Streaming and Auto Loader) is newly added to the check and not yet run.

| Area | Test | Works? |
| --- | --- | --- |
| Egress | Notebook reaches data.gov.sg: dataset download, datastore API, real-time rainfall API | Yes |
| Unity Catalog + Delta | Own schema and tables; Delta history (time travel) | Yes |
| Lakeflow Jobs | Daily 21:00 SGT snapshot job | Yes |
| Spatial SQL | st_dwithin (200 m checks), H3; shapely fallback | Yes |
| MLflow | Log runs; register a model in Unity Catalog | Yes |
| AI/BI dashboards | Point map of today's clusters (draft Island view) | Yes |
| Genie | "Which cluster has the most cases?" answered Taman Jurong, 80 | Yes |
| Databricks Apps | Streamlit template starts | Yes |
| Incremental ingestion | Structured Streaming, Auto Loader, MERGE watermark | Not run yet |

- Lag chart (monthly for now): rain alone barely lines up with cases; warmer months come before more dengue, humid months before fewer. Weekly version once Jingyi's rainfall CSV lands.
- Problem statement code for slide 1: **A2 DengueRadar** (Track A: Caring for an Ageing Singapore). Confirm the track wording the Devpost form uses.

### Komal: Story & Pitch Lead

- [ ] Download the PowerPoint template; register the team on Devpost; pick the team name with everyone (27 Sep, still open)
- [ ] Confirm the DAISI problem statement code and track wording for slide 1 (27 Sep)
- [ ] Find and cite these numbers (30 Sep). Done when: each has a number, a source link and a year
  - [ ] Dengue cases in the 2020 and 2022 outbreaks: 35,261 and 32,130 (computed 30 Sep from the MOH weekly file; cite the source) and how many residents were affected
  - [ ] How NEA's public dengue dashboard works today (clusters only, updated daily) and NEA's cluster definition, with the page link
  - [ ] Evidence that rising temperature and erratic rain lengthen the Aedes season in Singapore (NEA, a study, or the brief)
  - [ ] The cost of dengue to Singapore (economic burden study) or hospitalisation numbers, if a sourced number exists
  - [ ] Share of residents 65+ now and projected for 2030, and how much more severe dengue is in older adults (for the extra-care line only)
- [ ] Write the resident story in 3 sentences for slide 1 (30 Sep): a family in a block that becomes a cluster two weeks later, and what an early alert would have let them do
- [ ] Mock up the Island view: planning areas coloured Low, Medium, High (1 Oct). Label it illustrative
- [ ] Mock up the Area view: risk level, top 3 drivers, and the action list for residents and leaders (1 Oct)
- [ ] Mock up the **admin-kit post** as a phone screen in Canva (1 Oct): the hero visual for slide 2, layout in `pitch/round1-outline.md`. Label it illustrative. Earlier example: "Dengue risk in Bedok is forecast HIGH for the next 2 weeks (warm spell, a cluster nearby). This week: empty plates and containers, use repellent, see a doctor early for fever."
- [ ] Put the draft text and visuals into the template; cut every answer to its shortest form (2 Oct)
- [ ] Fix the slides after mock judging (3 Oct)
- [ ] Export PDF, add all member details, submit on Devpost, screenshot the confirmation (4 Oct)

### Ziqi: Data, dengue & places (Demo Engineer in the sprint)
- [x] Find each dataset and add it to the team dataset table (`DATASETS.md`, 17 datasets) with: name, link, format, date range, granularity, update frequency (30 Sep)
- [x] Inspect the archived cluster data: SGCharts (256 clean snapshots, 3 Jul 2015 to 6 Nov 2020) and the Nature Scientific Data cluster CSV (20 weekly snapshots, 28 Feb to 9 Jul 2020; 213 subzone IDs mapped). Both free with attribution
- [x] Give Braedon weekly dengue cases as a CSV for the lag chart (29 Sep)
- [x] Give Komal the planning-area boundary GeoJSON or image for the map mock-up (29 Sep)
- [ ] **Build the weekly per-planning-area training panel** (1 Oct). Steps: assign each archive point to a planning area (URA boundaries); sum cluster cases per area per week; list weeks and areas with data. Done when: a CSV `area_id, week_start, cluster_cases` plus a coverage table (weeks per year, areas with any cases, gaps) is in `analysis/data/`, and you report whether June to December 2020 can be used
- [ ] Reconcile the 2020 dengue case count (35,261 in `DATASETS.md` vs 35,012 in the checkpoint doc) and pick one with its source (1 Oct). **Braedon summed `weekly_dengue_ziqi.csv` on 30 Sep: 2020 = 35,261 (peak week W30, 1,791), 2022 = 32,130; use 35,261. Ziqi confirms the file is the MOH bulletin and gives the link**
- [ ] Find where dengue cases after Dec 2022 are published (Communicable Diseases Agency weekly bulletins) and note the format (1 Oct)
- [ ] Hand Komal the dengue and population dataset lines for slide 2 (1 Oct)
- [ ] Before the sprint: explore AI/BI dashboards, Genie and Apps in the workspace; note which is fastest for the Island view and Area view, with reasons (by 11 Oct). Desk view so far: dashboard first for the walking skeleton on 15 Oct, App for the final demo if time allows, Genie on the same gold table

Older items now closed as not needed: seniors living alone by area (national only, 88,400), Active Ageing Centre locations (not openly available).

### Jingyi: Data, weather

- [ ] Set up your rows in the team dataset table (`DATASETS.md`: dataset, owner, link, format, date range, granularity, update frequency, notes) (28 Sep)
- [ ] Find each weather dataset and add it to the table (30 Sep)
  - [ ] Real-time rainfall, air temperature and relative humidity APIs (data.gov.sg)
  - [ ] Historical daily rainfall and temperature, 2016 to 2024
  - [ ] Weather station locations (dataset #18 in `DATASETS.md`)
  - [ ] Stretch: school holiday and public holiday calendars
- [ ] Pull one sample from each real-time API with the datastore URL pattern to prove it works; save the response (30 Sep)
- [ ] Give Braedon weekly national rainfall and temperature as a CSV for the lag chart (29 Sep)
- [ ] **Map each weather station to a planning area** (nearest station, or a Voronoi split) and list planning areas with no station within a few kilometres (1 Oct). Done when: a CSV `station_id, planning_area` and a note on gaps
- [ ] Hand Komal the weather dataset line for slide 2 (1 Oct)

## Round 1 slide draft

These answers follow the official template prompts word for word; every prompt must be answered. VERIFY marks a fact that needs a cited source before submission. Submission: 3 slides, PDF, on Devpost, with every member's name, institution, course, year and email.

### Slide 1: Problem & why it matters

| Template prompt | Draft answer | Owner |
| --- | --- | --- |
| Team name | To decide | All |
| Problem statement | A2 DengueRadar: Real-time outbreak forecasting (VERIFY code and track wording) | Komal |
| The problem in one sentence | NEA's public cluster map and alerts show where dengue is now; nothing public shows where risk is heading over the next two weeks, so prevention starts late. (Deep Recon 30 Sep: the map is current-state; myENV alerts are current-state; say "we found none" for forecasts.) | Komal |
| Who is affected, and how badly (a number from open data) | Dengue cases in the 2020 and 2022 outbreaks (MOH weekly bulletin; VERIFY the 2020 figure); the number of NEA clusters active today (live feed) | Komal |
| Why it matters now | Rising temperatures and erratic rainfall extend the Aedes breeding season (VERIFY source). NEA says the Aedes life cycle can be as short as seven days (https://www.nea.gov.sg/dengue-zika/stop-dengue-now, VERIFY by reading the page), so a 2-week warning spans two breeding cycles. | Komal |

### Slide 2: Solution & data

| Template prompt | Draft answer | Owner |
| --- | --- | --- |
| Your solution in one sentence | DengueRadar lets a group-chat admin post a two-week dengue warning for their planning area in one tap: what is rising, why, and what to do. Behind it, a forecast for every planning area two weeks ahead with the drivers explained. | Braedon |
| Who uses it, and what decision it changes | Residents, reached through the community chats admins already run (a proposed channel; the field check is pending), decide what to check at home this week. The admin or volunteer who runs the chat decides what to post, and NEA can compare a budgeted ranking ("where do the first 8 teams go?") with its own forecast. No named Town Council, RC or MCST is routed to (boundaries do not match planning areas). | Braedon |
| Datasets (name + source) | 1. NEA Dengue Clusters, daily (data.gov.sg). 2. NEA real-time and historical rainfall, air temperature, relative humidity (data.gov.sg). 3. MOH Weekly Infectious Disease Bulletin, 2012 to 2022 (data.gov.sg). 4. URA Master Plan 2019 boundaries and SingStat Census 2020 (data.gov.sg). Training data, cited: SG Outbreak (SGCharts) cluster archive 2015 to 2020; Nature Scientific Data 2022 (doi 10.1038/s41597-022-01666-y, CC BY 4.0). VERIFY links and date ranges | Jingyi, Ziqi |
| What makes it different from a generic dashboard | NEA's cluster map and myENV alerts describe today. We predict the next two weeks for each planning area, rank where limited effort should go first, explain the drivers, and hand the admin a ready-to-post message for the chats residents already use. We test four hypotheses (weather lag, spatial spillover, recurrence, green space); early monthly data supports temperature lag and not rain alone (VERIFY with the weekly chart). | Braedon |

Visual for slide 2: the mock post as a phone screen (hero), with a small Island view (Komal). Slide-ready text and the cut list: `pitch/round1-outline.md`.

### Slide 3: Databricks architecture & impact

| Template prompt | Draft answer | Owner |
| --- | --- | --- |
| Pipeline (name the Databricks components) | data.gov.sg APIs, then Lakeflow Jobs (daily NEA cluster archive, already running) and incremental weather loading, then Delta tables (bronze, silver, gold) governed in Unity Catalog with lineage, then a trained per-area forecast tracked in MLflow with SHAP drivers and an action-rule table, then an AI/BI map or Databricks App with Genie. Why a platform: NEA's cluster feed keeps no history, so the scheduled job builds it, and that history doubles as our out-of-time test | Braedon |
| The user-facing output you will demo | Island view: planning areas Low, Medium, High. Area view: why, and what to do. A 2020 replay: the model trained before 2020 flags areas that later grew. | Ziqi |
| Measurable impact if it worked | Stated as targets we will measure, not claims. Capture rate at K = 8: share of the next fortnight's new cluster cases inside our top 8 areas, against the last-4-weeks baseline. Lead time in weeks from the 2020 replay. Alert load: at most 15% of areas High. Optional, only if measured: the baseline's own capture rate from the 2015 to 2020 archive. A prospective check of our forecasts against live snapshots since 28 Sep, because the training archives end Nov 2020. | Braedon |
| What you can realistically finish in two weeks | Daily cluster archive, incremental weather ingestion, per-area training panel, trained 2-week forecast in MLflow with SHAP, the budgeted ranking, the admin kit with copy buttons, Island and Area views, Genie space, 2020 replay. Out of scope: sending anything to real people, agency agreements, causal effect sizes for the actions. | Braedon |

Visual for slide 3: architecture diagram (Braedon); lag chart as backup evidence (Braedon).

## Build sprint (if shortlisted)

The core demo must work end to end by 19 Oct; anything behind schedule after that gets cut, not rushed. Top 10 is announced 9 Oct.

| Date | Milestone | BMad skill |
| --- | --- | --- |
| 9 to 11 Oct | Turn the idea into a spec and stories, with the MoSCoW list as the cut line; agree table designs and folder ownership | /bmad-spec, /bmad-architecture |
| 12 Oct | Kickoff with mentor. Ask: who would act on a 2-week area forecast, and what would make the action list credible? |  |
| 15 Oct | Walking skeleton: real data flows load, baseline forecast, rough map. Ugly is fine | /bmad-build |
| 19 Oct | All MUST items working. Midpoint check; cut what is behind | /bmad-correct-course, /bmad-checkpoint-preview |
| 20 to 24 Oct | SHOULD items: 2020 replay polish, resident alert, extra features (humidity, block age, gathering places) | /bmad-build |
| 25 Oct | Feature freeze, code review, record the 30-second backup video | /bmad-code-review |
| 26 Oct | Rehearse the pitch five times with a stopwatch | /bmad-party-mode (judges panel) |
| 27 Oct, 4 to 7pm | Demo Day |  |

MUST (the core): daily cluster archive running; incremental weather ingestion; per-planning-area training panel; trained 2-week area forecast that beats the "clusters carry on" and seasonal baselines in MLflow on unseen years; SHAP top drivers; prescriptive action table; Island view and Area view; measured lead time and hit rate.

SHOULD: national MOH forecast as context; 2020 replay screen; Genie space; resident alert mock; parks and hawker centres if validation keeps them.

COULD: block-level detail near clusters; nearest CHAS clinic; threshold alerts.

## Handoff contracts

Agree these table names and columns on day one of the sprint. Each person can then start on fake data shaped like the contract and swap in the real table when it lands. Column names are a starting draft for /bmad-architecture to confirm.

| From | To | Delivers | Key columns | Due |
| --- | --- | --- | --- | --- |
| Jingyi and Ziqi | Braedon | Raw files and API details for every dataset, with data-quality notes; per-area training panel; station-to-area map | Source link, date range, granularity per dataset; area_id, week_start, cluster_cases; station_id, planning_area | 13 Oct (panel and map earlier: 1 Oct) |
| Braedon | Braedon (model) | gold.area_week_features | area_id, week_start, cluster_cases, cluster_cases_adjacent, dist_to_nearest_cluster_km, rain_lag2, rain_lag3, rain_lag4, hot_days_31c, temp_lag, humidity_lag, cluster_weeks_last_52, median_block_age, pct_65plus, national_cases_lag | 15 Oct |
| Braedon | Ziqi | gold.area_risk | area_id, week_start, risk_level (Low/Med/High), rising_prob, forecast_cases, top_3_drivers, action_ids | 19 Oct (fake version with these columns by 12 Oct) |
| Braedon | Ziqi | gold.action_rules | action_id, driver, audience (resident or leader), owner, action_text, timing_days, source_url | 15 Oct |
| Ziqi | Komal | Live map or app URL + 30-second backup video |  | 25 Oct |

Rule for the forecast table: features for week W may only use data available before week W. Anything else leaks the future and makes the model look better than it is.

## Team rules

- One owner per notebook or folder. Two people editing one notebook causes merge conflicts.
- Save Databricks notebooks in .py source format so Git can merge them.
- Work on a branch; merge to main only when it runs.
- Keep data small on Free Edition. Exceeding quotas can lock compute for the rest of the day. Stop idle notebooks, jobs, apps and endpoints.
- No personal data and no credentials in the repo or workspace. The resident alert is a mock-up, never sent to real people.
- Credit every dataset, library and AI tool used, as the challenge rules require.
- Do not claim "two weeks early" or any lead time until the backtest measures it.

Guides in the toolkit repo: github/08-datathon-handbook/first-datathon.md (everyone reads it at kickoff), 01-playbook/hypothesis-and-problem-framing.md, 01-playbook/team-git-and-notebook-workflow.md, 03-modeling/cross-validation-guide.md, and 01-playbook/pitch-and-presentation-guide.md.

## Open questions

- [ ] Does everyone agree with the pivot (28 Sep meeting): trained per-area forecast, residents and community leaders as users, prescriptive action plan, seniors as a secondary flag?
- [ ] Does the per-area training panel have enough weeks and areas with signal? (Ziqi, 1 Oct)
- [ ] Do Structured Streaming and Auto Loader run on Free Edition? (Braedon, 29 Sep)
- [ ] What exactly does NEA's public dashboard show, and how is a cluster defined? (Komal, 30 Sep)
- [ ] Are the action wordings consistent with NEA's public prevention advice? (Braedon and Komal, 1 Oct)
- [ ] Can we speak to one town council, RC or NEA contact before Demo Day to sanity-check the actions?
- [ ] Which track name does the Devpost form use?
- [ ] Which weekly time works for a 30-minute team check-in?
- [ ] Where do we keep shared files: GitHub repo, Databricks workspace, or both?
