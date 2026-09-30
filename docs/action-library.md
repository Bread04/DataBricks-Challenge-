# DengueRadar action library (DRAFT v0.1, 30 Sep 2026)

Owner: Braedon · Reviewer: Komal (wording) · Feeds: `area_action_card` (`docs/model-definitions.md` section 6b) and the admin kit (section 6d).

**Status: every row is DRAFT.** Wording and `source_url` must be checked against NEA's public dengue prevention advice before any slide, message or demo uses it (**CONFIRM**). Links added 30 Sep come from a web search; the pages themselves could not all be fetched, so Komal must read each one. Rows still saying CONFIRM have no source yet. Timings are recommended windows, not predictions. No row names a Town Council, RC or MCST (locked decision).

## Actions

| action_id | Driver tags | Resident text | Community checklist text | Timing (days) | owner_agency (CONFIRM) | source_url |
|---|---|---|---|---|---|---|
| A01 | H1 | Lift and empty flower-pot plates, overturn pails and wipe their rims, and change water in vases | Remind neighbours to do the same on balconies and corridors | 7 | Residents | https://www.nea.gov.sg/dengue-zika/stop-dengue-now (B-L-O-C-K, search summary only) |
| A02 | H1 | Keep roof gutters clear and add BTI insecticide as NEA advises (gully traps are not confirmed in the sources found) | Check and clear roof gutters and common-area standing water; report blocked public drains | 7 | Residents; NEA (Department of Public Cleanliness cleans public drains) | https://www.nea.gov.sg/dengue-zika/stop-dengue-now (roof gutters, search summary only) |
| A03 | H2 (cluster nearby) | Apply repellent regularly, wear long sleeves and long pants, and spray insecticide in dark corners (NEA's S-A-W). See a doctor early if you have a fever (**advice not confirmed in the sources found**) | Share the repellent and fever reminder with neighbours in the blocks around the cluster | 3 | Residents | https://www.nea.gov.sg/dengue-zika/stop-dengue-now (S-A-W, search summary only) |
| A04 | H2 (cluster nearby) | Check your home and corridor for standing water today | Remind neighbours in the blocks around the cluster; share the checklist | 3 | Community volunteers | CONFIRM |
| A05 | H2 (neighbour rising) | Do your usual weekly checks and stay alert | Pre-check known problem spots; watch the neighbouring area's forecast | 7 | Community volunteers | CONFIRM |
| A06 | H3 | Keep up your routine weekly checks | Scheduled walk-through of spots that had breeding before | 14 | Residents | CONFIRM |
| A07 | H3 | (none) | Walk known recurring spots and note any standing water | 14 | Community volunteers | CONFIRM |
| A08 | H4 | Use repellent before outdoor meals or exercise, and check plant pot plates | (none) | 7 | Residents | CONFIRM |
| A09 | H4 | (none) | Check drains, bins and stagnant water in nearby parks and eating areas; report to NEA (NParks' role unconfirmed) | 7 | NEA; NParks (unconfirmed) | CONFIRM |
| A10 | Axis 2: `CONSTRUCTION_SITES` | (none) | Enforcement referral: locality, case size and date go to NEA, which regulates construction-site mosquito control | 3 | NEA (BCA role not found) | https://www.nea.gov.sg/our-services/pest-control/mosquito-control/mosquito-control-in-construction-sites (search summary only) |
| A11 | Extra-care flag (top third 65+ share) | Check on older neighbours and family members | Check on older neighbours | 7 | Residents | CONFIRM |

Dedupe rule: when two top-3 drivers map to the same `action_id`, show it once. Rank by the driver's SHAP size, cap at 3. A01 and A02 often co-occur (both H1); the card may merge them into one line.

## Feature to plain words

Feature names never appear on a card or post.

| Feature(s) | Plain words |
|---|---|
| `rain_lag2..4` with `hot_days_31c` | "Heavy rain 2 to 4 weeks ago, now warm" |
| `temp_lag`, `hot_days_31c` | "A warm spell" |
| `humidity_lag` | "Humid weather" (drop if the weekly chart does not support it) |
| `flushing_days` | "Recent days of heavy rain" |
| `cluster_cases_adjacent`, `dist_to_nearest_cluster_km` | "A cluster close by" or "Cases rising in a neighbouring area" |
| `cluster_weeks_last_52`, `median_block_age` | "Clusters here in the past year" or "Older blocks" |
| `green_space_share` | "Lots of green space nearby" |
| `pop_density` | "A densely populated estate" |

## Coverage check (done when)

- Every H1 to H4 driver maps to at least one action: H1 (A01, A02), H2 (A03 to A05), H3 (A06, A07), H4 (A08, A09), Axis 2 tag (A10), extra-care (A11).
- Komal has reviewed the wording, and each `source_url` is either verified or the row is removed.
