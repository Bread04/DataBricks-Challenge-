# DengueRadar: hypotheses, model, metrics and prescriptive rules

Owner: Braedon · Status: **rewritten 28 Sep 2026** after the correct-course pivot (`_bmad-output/planning-artifacts/sprint-change-proposal-2026-09-28.md`) · Method: `github/08-datathon-handbook` (hypothesis framing, cross-validation guide, pitch guide) · Earlier version (senior-first points score and exposure x vulnerability matrix) is superseded; the forges in `_bmad-output/forge/` keep that history.

DengueRadar predicts, then prescribes. **Level 1 (context)** forecasts national weekly dengue cases 2 weeks ahead. **Level 2 (the product)** forecasts each planning area's dengue cluster risk 2 weeks ahead with a trained model, explains the top drivers, and maps each driver to an action for residents and community leaders.

---

## 1. The bottleneck and the hypotheses

**Real-world bottleneck.** NEA's public cluster dashboard reports clusters after cases exist. Prevention (clearing water, inspecting drains, door-to-door reminders) works best before clusters form, but nobody tells residents or town councils which areas to focus on this fortnight. The cost of a missed rising area (an outbreak that grows unchecked) is much higher than the cost of an extra reminder, so recall matters more than accuracy.

| ID | Hypothesis (domain factor, outcome, mechanism, test) | Features |
|---|---|---|
| **H1 Weather lag** | Warm periods, and rain 2 to 4 weeks earlier followed by dry spells, raise next-fortnight cluster activity, because they speed Aedes breeding and leave standing water. Our monthly chart supports temperature (+0.29 at 4 months) but not rain alone | `hot_days_31c`, `rain_lag2..4`, `temp_lag`, `humidity_lag`, `flushing_days` |
| **H2 Spatial spillover** | Clusters in neighbouring planning areas raise an area's own risk, because Aedes and people move across borders | `cluster_cases_adjacent`, `dist_to_nearest_cluster_km` |
| **H3 Recurrence** | Areas with clusters in the past year recur, especially with older housing stock | `cluster_weeks_last_52`, `median_block_age` |
| **H4 Green space** | Planning areas with a larger share of green space (parks and nature reserves) have higher next-fortnight cluster activity, **after controlling for population density**, because vegetation gives Aedes shade and resting sites and plant containers hold standing water. Test: add the feature to the H1 to H3 model, compare on unseen years and in the leave-areas-out check, and read the SHAP direction. Support only if recall or PR-AUC improves and the effect is consistently positive. Say "associated with", not "causes" | `green_space_share` (NParks park polygon area / planning-area land area), controlled with `pop_density`, `median_block_age` |

Say honestly on the slides which of these the data confirms and which it does not.

## 2. Data for the model

| Piece | Source | Notes |
|---|---|---|
| **Training panel (area x week)** | SGCharts archive (256 snapshots, 3 Jul 2015 to 6 Nov 2020) plus Nature Scientific Data (20 weekly snapshots, 28 Feb to 9 Jul 2020, 213 subzones mapped) | Cited, offline training only. Aggregate points to planning areas, then to weekly cluster cases |
| **Live inputs** | NEA Dengue Clusters (daily archive since 28 Sep), real-time rainfall and temperature | Same structure as the archive, so features match |
| **Weather features** | NEA historical rainfall, temperature, humidity (pre-aggregated daily per station) | Map stations to planning areas (nearest station or Voronoi) |
| **National context** | MOH weekly cases 2012 to 2022 | Level 1 feature: national trend and season |
| **Denominator and flag** | Census 2020 residents by planning area and age | Population per area; share 65+ for the extra-care flag |

**Target caveat (must appear on the slides).** The archive holds only cases inside NEA clusters. The model predicts **cluster activity** (new or growing cluster cases in a planning area over the next 2 weeks), not total dengue cases.

## 3. Targets, baselines and models

- **Regression target:** cluster cases in planning area A in weeks t+1 and t+2.
- **Classification target ("Rising"):** cases in the next 2 weeks are at least 20% above the area's 4-week average and above a minimum count (so tiny numbers do not flap).
- **Risk level shown to users:** Low, Medium, High from the calibrated Rising probability, with thresholds set in section 5.

| Name | Rule | Why |
|---|---|---|
| **B1 Persistence** (main) | Next 2 weeks = the last 4 weeks' average cluster cases in that area ("clusters carry on") | What a person reading NEA's dashboard would guess |
| **B2 Seasonal average** | Same week averaged over training years | Dengue is seasonal |
| **B3 Explainable points score** | Hand-set points: cluster size band, high-Aedes zone, national Rising, recent rain, hot days | The old Level 2 design; shows what the trained model adds |
| **M1 Trained model** | LightGBM (regression + Rising classifier) logged in MLflow; a Poisson or logistic model as the readable cross-check | Handbook default for tabular data |

Register the best model in Unity Catalog. If M1 does not beat B1 and B2, say so and present the explainable score with the honest result.

## 4. Validation (how we test honestly)

Following `github/08-datathon-handbook/03-modeling/cross-validation-guide.md`:

- **Time-ordered, never random.** Rolling origin: train 2015 to 2018, test 2019; train 2015 to 2019, test Jan to Jul 2020 (Nature fills the surge). Never shuffle weeks.
- **Leave-areas-out check (`GroupKFold` by planning area).** Confirms the model learns weather and spillover patterns, not each area's own history.
- **No leakage.** Features for week t use only data available before week t. NEA publishes cases about a week late, so use lags of 1 week or more. Fit imputers, scalers and encoders inside each fold.
- **Known weakness.** Published Singapore models catch the timing of peaks but underpredict their size. State it before a judge does.
- **Data gap and prospective test.** The training cluster archives end in Nov 2020 and the live feed starts in Sep 2026, so a rolling-origin backtest cannot say the model holds in the current regime. The MOH weekly file shows how much the disease can swing (5,251 cases in 2021, 32,130 in 2022). Treat the live daily snapshots (`bronze_cluster_snapshots`, since 28 Sep) as a **prospective, out-of-time test**: log each forecast with its date, then score it against the snapshots 2 weeks later. Report how many forecast dates it covers, and never blend it into the backtest numbers.
- **Coverage.** 2020 has dense snapshots to May, then monthly only, and cases outside clusters are missing. Report weeks and areas with usable data.

## 5. Metrics and the cost matrix

| Level | Metric | Plain meaning | Target |
|---|---|---|---|
| 2 | **Rising recall** and **precision** | Of real rises, how many we flagged; of our flags, how many were real | Recall first (missed rise costs more) |
| 2 | **PR-AUC** | Quality of the Rising probability when rises are rare | Above B1 and B3 |
| 2 | **Hit rate** | Share of new or growing clusters in the next 2 weeks that were in areas we rated High | Above B1; compare with NEA's ~90% for its 1 km2 map |
| 2 | **Lead time (weeks)** | How many weeks before an area's cluster cases crossed the alert size we first flagged it | Measure it; never claim it before measuring |
| 2 | **Alert load** | Share of areas rated High in a typical week | At most 15%, so leaders trust it |
| 2 | **MAE** (cluster cases per area per fortnight) | Average miss | Below B1 and B2 |
| 1 | **MAE / MAPE** (national cases per week) | Average national miss | Below B1 and B2; report beside NEA's published 17% (1 week) to 24% |

**Cost matrix and threshold.** Missing a rising area (false negative) is set at 5 times the cost of an unnecessary reminder or inspection (false positive), as a starting assumption. Choose the probability threshold that minimises expected cost on the validation years, then check alert load is at most 15%. If the cap binds, raise the threshold and report the lost recall. Change the 5x ratio with input from a town council or NEA contact if we can get one; until then it is an assumption, labelled as such.

## 6. Explainability and the prescriptive layer

**Design locked at the 30 Sep Round 1 judging-fit review.** Two independent routing axes decide what an area's action list says. Wording is a draft: **CONFIRM against NEA's public dengue prevention advice before any slide uses it.**

**Axis 1 - why it's rising (the backbone).** SHAP (or the B3 rule score) gives the top 3 drivers for each area and week. Each maps to an action below. The area gets up to 3 **ranked, deduplicated** actions, not one "leading driver". Actions that overlap across drivers collapse into one line.

**Axis 2 - who caused it (bonus layer).** NEA's Dengue Clusters feed tags the breeding source per cluster: `HOMES`, `PUBLIC_PLACES`, `CONSTRUCTION_SITES`. The field is sparse (2 of 11 clusters populated at the 27 Sep check), so it adds routing but is never the backbone. It is used only to route actions after a cluster exists, never as a model feature (that would leak the answer).

| Breeding-source tag | Routed action |
|---|---|
| `CONSTRUCTION_SITES` | NEA enforcement referral. NEA regulates mosquito control at construction sites nationally (BCA's role was not found in NEA's sources; see the jurisdiction check in 6d), so it does not depend on a planning-area boundary |
| `HOMES` / `PUBLIC_PLACES` | Feeds the resident and community checklist below, block-level where HDB data allows |
| Tag absent (~80% of clusters) | Falls back to Axis 1 driver actions. The Area view states "root cause not yet identified by NEA" instead of omitting it |

**LOCKED DECISION: no routing to a named Town Council, RC or MCST.** URA planning areas do not align with Town Council, electoral or MCST boundaries, and no open dataset maps one to the other. Naming an institution would imply a routing capability the data cannot support. Every community action is a **checklist any engaged resident, RC volunteer or MCST council member in a flagged area can read, act on or escalate**.

| Driver (Axis 1) | Resident action (this week) | Community checklist (anyone in the area can act or escalate) | Timing |
|---|---|---|---|
| Recent rain then warm spell (H1) | Empty flower-pot plates and containers, clear gully traps, cover storage | Check and clear drains, roof gutters and common-area standing water | Within 7 days |
| Active cluster nearby (H2) | Repellent, long sleeves at dawn and dusk, see a doctor early for fever (nearest CHAS clinic) | Remind neighbours in blocks around the cluster; share the checklist | Within 3 days |
| Neighbouring area rising (H2) | Heightened awareness; do the weekly checks | Pre-check known problem spots; watch the neighbouring area's forecast | Before next week |
| Recurrence, older blocks (H3) | Routine weekly checks | Scheduled walk-through of known recurring spots | Within 14 days |
| High green space with a rising forecast (H4), and places people gather, if validation keeps them | Repellent before outdoor meals or exercise; check plant pot plates | Check drains, bins and stagnant water in nearby parks and eating areas; report to NEA or NParks | Within 7 days |

**Extra-care flag.** Where an area's share of residents 65+ is in the top third, add: "check on older neighbours and family members." This is the only place seniors enter the product.

### 6a. Inspection priority ranking (decision layer)

Answers "we only have effort for K areas this week, which K?" It orders areas; it does **not** claim that acting there reduces cases.

- **Inputs per area and week:** `p` = calibrated Rising probability, `y_hat` = expected cluster cases over the next 2 weeks, `residents` = Census 2020 population.
- **Two lists, both shown (chosen 30 Sep, option C):**
  - **Most cases:** rank by `p x y_hat`. Favours large areas.
  - **Highest risk per resident:** rank by `p x y_hat / residents x 10,000`. Favours small areas with a sudden rise.
- **Budget slider K** ("teams available", 5 to 15). Default K = 8, about the 15% alert-load cap, so the two rules agree.
- **Metric: capture rate at K.** In the backtest, the share of the next 2 weeks' actual new cluster cases that fell inside the top K areas. Compute for M1 and for B1; the slide line uses only measured values (for example "top 8 areas covered X% of new cluster cases vs Y% for the last-4-weeks guess").
- **Guardrails:** state "cluster cases only" (target caveat); show **rank change vs last week** so the list does not flap; mark areas with poor data coverage "low data" instead of giving a confident rank.
- **Gold table `area_priority`:** `area_id, week, p, y_hat, rate_per_10k, rank_cases, rank_rate, rank_change, low_data_flag`.

### 6b. Weekly action card (one per area per week)

The Area view shows one plain-language card:

1. Area, risk level and **what changed since last week** (risk band and top drivers).
2. **Why it's rising:** top 3 drivers in plain words, from a feature-to-sentence lookup (for example `rain_lag2..4` + `hot_days_31c` becomes "heavy rain 2 to 4 weeks ago, now warm"). Feature names never appear.
3. **This week:** up to 3 ranked, deduplicated actions as a tick-box checklist, each with a recommended window.
4. **Root cause line (Axis 2):** routed action if a tag exists, otherwise "root cause not yet identified by NEA".
5. **Confidence line:** for this risk band, the share of backtest weeks where the area then rose. Shown only after the backtest is run, never before.
6. **Extra-care flag** where it applies, and the **source link** to NEA prevention advice.

**How it is built**

- **Action library:** one table, `action_id, resident_text, community_text, timing_days, source_url, driver_tags`. Each action is written and checked once (the CONFIRM step happens here).
- **Driver to action mapping:** each of the top 3 SHAP drivers points to action IDs; take the union, **dedupe by `action_id`**, order by the driver's SHAP size, cap at 3.
- **Timing** comes from the action, not the model: a recommended window, not a prediction.
- **Gold table `area_action_card`:** `area_id, week, risk_band, band_change, driver_1..3_text, action_id_1..3, root_cause_tag, confidence_text, extra_care_flag`.

**Rules:** no number appears that has not been measured; no named institution routing (locked decision above); wording stays under CONFIRM until checked against NEA advice.

**Flow in the demo:** Island view (map plus both ranked lists and the K slider) then click an area to open its card.

### 6c. Who gets what (audience-tiered views)

Hardened on 30 Sep with an assumption audit, a pre-mortem and a Shark Tank pass. **One forecast, three decisions.** Each audience sees only what feeds its decision. The split is by **relevance, not secrecy**: the cluster locations are already public, and a public prototype has no access control.

**Delivery model (decided 30 Sep): each audience gets the mode that fits how it already works.** Section 6d has the modes. The prototype sends nothing to anyone: the app **generates** each audience's real payload or post from the gold tables, and a person or the agency's own platform takes it from there. No slide may claim notification or an agreement with any agency.

**Three lenses only** (chosen with a "Who are you?" selector in the app):

| Lens | Decision | Sees | Does not see (by default) |
|---|---|---|---|
| **Resident** (reached mainly through their RC or constituency group chat, posted by an admin; the in-app view is the same content) | What do I do at home this week? | Own area's band, what changed, top 3 plain-language actions, extra-care line, and adjacent areas' bands | Probabilities, island ranking, model metrics |
| **Volunteer / group-chat admin** (RC volunteer, MCST council member, engaged resident) | What should our neighbourhood check, and what do I post? | The resident view plus the community checklist and the **admin kit** (section 6d): ready-to-post WhatsApp and Telegram text, planning-area picker, valid-until date, and a link to NEA's public cluster map for block level | Full island ranking |
| **NEA (comparison view)** | Where should limited effort go first? | Both priority lists (6a), K slider, drivers, Axis 2 tags, confidence and coverage, backtest scores | Resident-level content |

- **Construction referral:** a single conditional row in the NEA view for clusters tagged `CONSTRUCTION_SITES` (NEA), with an honest empty state ("no tagged construction clusters this week"). Only 2 of 11 clusters were tagged at the 27 Sep check.
- **Roadmap, not built:** an NParks park-checklist view, a Town Council view (would need a block-to-town mapping, which is unverified), and MOH or other agencies (see 6d).
- **NEA framing:** decision support to compare with NEA's own forecast, never "NEA does not predict".

**Escalation and alert fatigue**

| Band | Resident | Volunteer | NEA view |
|---|---|---|---|
| Low | Routine card ("Low is not zero") | Nothing | Nothing |
| Medium | Card with actions | Digest | Nothing |
| High | Alert message | Checklist | In the ranking |
| Sustained or tagged | Same | Same | Flag, or referral row |

- **Trigger rule for "sustained":** do not hard-code "2 consecutive weeks", because 2-week forecast windows overlap and two High weeks are not two independent signals. Tune the trigger on validation years and freeze it before scoring the test year (section 8).
- **New vs persistent flag:** each High area is marked "new" or "persistent" (ties to H3 recurrence) so recurring areas do not cry wolf. The backtest reports the distribution of weeks-in-High per area, and the 15% alert cap stays.

**Language rules:** in posts, lead with "higher than usual" and show the level (Low, Medium, High) second, so a chat does not panic at a bare "HIGH". Say "forecast cluster activity" and "prevention priority". Never "worst", "dangerous" or "safe". Every view carries the "cluster cases only" caveat, and the confidence line appears only once measured.

**Pitch rules (from the Shark Tank pass)**
1. Lead with the decision ("where do the first 8 teams go?"); the role views are the packaging.
2. One benefit sentence, filled only from the backtest: "the top 8 areas covered X% of new cluster cases vs Y% for the last-4-weeks guess". No number before it is measured.
3. One "who gets what" slide with three columns and one delivery line: "the app generates each audience's message; the people and platforms they already use send it".
4. Contingency: if capture rate at K does not beat B1, pitch the explainable B3 score with the honest result.
5. Data-limits line: cluster cases only, thin 2020 tags, and what was tested versus untested (the incremental-ingestion check and any Unity Catalog row or column security are **not verified** on Free Edition; the app selector is the mechanism).

**Demo resilience:** Free Edition apps can auto-stop after 24 hours. Restart the app before the demo and keep one pre-rendered fallback screenshot per lens.

### 6d. Authority routing and dissemination modes

Decided 30 Sep. **Route by who owns the action, not by geography.** National agencies need no match with planning areas, so they can be addressed directly. Boundary-based groups (Town Councils, RCs, MCSTs, GRC or constituency chats) are reached through the admin kit and are never named or routed by boundary (locked decision above). **CONFIRM each agency's jurisdiction against official sources before any slide uses it.**

| Authority | Owns | Trigger | Payload (minimum necessary) | **Mode** |
|---|---|---|---|---|
| **NEA** | Dengue control and inspection | Weekly; flag on sustained High | Both priority lists, drivers, confidence, coverage, tags | **Weekly export file** (CSV/GeoJSON from the gold table) plus a written data contract, for NEA's own platform to ingest |
| **NEA enforcement** (construction sites; the earlier "NEA/BCA" wording is not supported, see the jurisdiction check) | Construction-site breeding | `CONSTRUCTION_SITES` tag present | Locality, case size, date, tag | **Structured record per trigger** (JSON/CSV, sent only when the trigger fires) |
| **NEA drain cleansing (Department of Public Cleanliness)**; PUB does structural repairs and litter devices, not regular cleansing | Drain and canal cleansing | High or rising with the H1 rain-then-warm driver | Area, reason, recommended timing, caveat | **Structured record per trigger**, same schema |
| **NParks** (**role in dengue control unconfirmed**; no source found; sample record is illustrative only) | Parks and nature reserves | High with high green-space share (H4) | Area, reason, park checklist, timing | **Structured record per trigger**, same schema |
| **Residents, RCs, MCSTs, group-chat admins** | Community action | Weekly, only on a band change | Short forwardable post | **Admin kit with copy buttons** |
| **CDA and MOH** (health sector: dengue is notifiable within 24 hours; CDA publishes clinical guidance) | Clinical response and notification | Area rising | Aggregate band and timing only, no patient data | **Roadmap only** |
| HDB, JTC, SLA, others | Unverified | n/a | n/a | **Roadmap only** |

**Admin kit.** One post per planning area per week, only when the band changes. Contents: area name and "your estate may span a different boundary", band and what changed, up to 3 actions, source, **date and "valid until"** (forwarded messages live in chats for weeks), and "forecast, not diagnosis". Separate WhatsApp and Telegram versions (they format bold and line breaks differently), a multi-select planning-area picker, and no bot, token or stored user data. Extra languages (Chinese, Malay, Tamil) are a stretch, using cached AI translations that are disclosed and speaker-reviewed.

**One data contract, several views.** Publish one versioned schema and each authority takes only its fields: `area_id, week, band, band_change, top_drivers, action_ids, confidence, coverage_flag, tag, caveat, valid_until`. Add an `owner_agency` column to the action library so each action has an owner without naming a Town Council.

**Escalation across levels**

| Situation | Informed |
|---|---|
| Area goes High | Community admins (admin kit) |
| Sustained High or large rise | NEA digest flag |
| Tag present | Enforcement referral record |
| High with H1 rain driver | NEA drain-cleansing record |
| High with H4 green space | NParks record (role unconfirmed) |

**Jurisdiction check (30 Sep, web search; several direct page fetches failed, so most points rest on search summaries and need Komal to read the pages).**

| Claim | Result | Source |
|---|---|---|
| NEA enforces mosquito control at construction sites | **Supported.** NEA pages describe Stop Work Orders, court charges and the ECO Scheme. BCA did not appear. | https://www.nea.gov.sg/our-services/pest-control/mosquito-control/mosquito-control-in-construction-sites |
| PUB cleans public drains | **Not supported.** PUB's page (via search summary; direct fetch returned 403) says regular cleansing is done by NEA's Department of Public Cleanliness, and PUB does structural repairs and litter devices | https://www.pub.gov.sg/drainage/network/draincleansingmaintenance |
| NParks owns park dengue control | **Not found.** NParks appears in the One Health Framework and in gardening advice only | https://gardeningsg.nparks.gov.sg/page-index/housekeeping/keeping-gardens-mosquito-free/ |
| MOH is the health-sector body | **Partly.** The Communicable Diseases Agency (CDA) gives dengue clinical guidance and the notification rule (within 24 hours of diagnosis; page fetched) | https://www.cda.gov.sg/professionals/diseases/dengue-fever/ |
| NEA advice: B-L-O-C-K (break up hardened soil, lift and empty flowerpot plates, overturn pails and wipe rims, change water in vases, keep roof gutters clear and add BTI) and S-A-W (spray insecticide in dark corners, apply repellent, wear long sleeves and long pants) | **Supported by search summary only** | https://www.nea.gov.sg/dengue-zika/stop-dengue-now |

Town Councils do work with NEA on vector control (NEA press release), which supports keeping community actions as a checklist that any local actor can pick up.

**Guardrails.** Advisory, not orders: wording like "forecast suggests prioritising..." and decisions stay with the agency. Aggregate and public data only, no personal or case-level data. Send only on trigger. No acknowledgement loop is built (roadmap: an "actioned" reply so response could be measured). Not verified: any real agency channel; the data contract is a proposal.

**Demo depth (decided):** the app renders each audience's generated payload and copy text from the gold tables. Nothing is sent externally, so there is no Telegram token, egress or opt-in risk.

**What-if.** Any "what if households act" slider is illustrative only. We have no evidence for effect sizes, so we never show a percentage reduction as fact.

## 7. Outputs

- **Island view:** 55 planning areas coloured Low, Medium, High, with the forecast date and the target caveat, plus the two priority lists (most cases, highest risk per resident) and the K slider (section 6a).
- **Area view:** the weekly action card (section 6b): risk, what changed, top 3 drivers in plain words, ranked checklist, root-cause line and confidence line. Genie answers plain-English questions on the same gold tables.
- **Admin kit and payloads (section 6d):** for a flagged area, the ready-to-post WhatsApp and Telegram text, the NEA weekly export file, and one sample record each for the NEA enforcement referral, the NEA drain-cleansing record and NParks (role unconfirmed). All generated in the app; nothing is sent to anyone.
- **2020 replay:** the model trained before 2020 flags the areas that later grew.

## 8. Thresholds and assumptions to test

Rising = 20% above the 4-week average, the minimum count, the 15% alert cap, the 5x cost ratio and the risk-level cut-offs are starting values. Tune them on validation years, then freeze them before scoring the test year.
