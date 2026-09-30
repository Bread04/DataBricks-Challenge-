---
title: 'competitive research: Existing dengue tools and NEA offerings vs DengueRadar'
type: 'competitive'
topic: 'Existing dengue tools and NEA offerings vs DengueRadar'
decision: 'What can the DAISI Round 1 slides truthfully claim about what already exists and about group-chat delivery and community messaging, and what should change'
source: 'native run'
status: complete
preset: 'quick'
validation: 'normal'
created: '2026-09-30'
updated: '2026-09-30'
---

# Competitive research: what already exists vs DengueRadar

**Decision this research serves:** what the Round 1 slides can truthfully claim about existing tools, and what to change.

## Executive summary

**Do:** keep the gap claim, but narrow it to what is verified, and stop implying nobody forecasts at planning-area level.

1. **The public NEA cluster map is current-state only.** It lists active clusters and case counts, updated at 1am, with no predictive information [1]. That supports "NEA's public cluster dashboard shows today's clusters".
2. **NEA already pushes alerts, so "residents find out too late" needs care.** The Dengue Community Alert System sends alerts about high Aedes population and clusters near a user through the myENV app, a web portal and banners [2][3]. Those alerts are about current conditions, not a forecast [2]. Our slide 1 must not read as if residents get no notice at all.
3. **Forecasting research at our exact level exists.** A 2026 preprint forecasts hotspots for 323 subzones aggregated to 55 planning areas, one week ahead, F-score 0.79 (not yet peer reviewed) [5]. A 2018 BMC Medicine paper forecast 1 km grids up to 12 weeks ahead with AUC above 0.75 [4]. NEA's Environment Health Institute also appears to run internal national forecasts (search summary only) [6]. So "no one forecasts by planning area" cannot be claimed. What we can say is that **none of this was found as a public, actionable tool**, which is a search result and not proof.
4. **Biggest caveat:** absence of a public forecast tool is inferred from a quick search. SG Outbreak / SGCharts and community projects were not searched.

## Dimension: offer and feature teardown

| Existing thing | What it does | Forecast? | Source |
|---|---|---|---|
| NEA cluster map and table | Active clusters, localities, case counts; tiers Red (10+ cases), Yellow (fewer than 10), Green (no new cases, monitored 21 days); updated at 1am | No | [1] |
| Dengue Community Alert System | Colour-coded banners; alerts about high Aedes population and clusters near you via myENV or go.gov.sg/dengue-high-risk | No forward-looking projection on the page | [2] |
| myENV notifications | Users save locations and enable Dengue/Zika/Aedes notifications, alerted if a saved location has higher Aedes population from Gravitraps (search summary only) | Current mosquito counts, not future cases | [3] |
| Cluster GeoJSON on data.gov.sg | Open data (listing seen only) | No | [1] |
| NEA EHI internal models | LASSO models, weekly national forecasts 1 to 12 weeks ahead (search summary only); appears internal | Internal | [6] |
| Research: neighbourhood forecast | 315 neighbourhoods, up to 12 weeks, AUC above 0.75 | Research | [4] |
| Research: hotspot forecast | 55 planning areas, 1 week ahead, F-score 0.79; preprint | Research | [5] |

## Dimension: positioning and messaging

Where DengueRadar still differs, as far as this search shows: **two weeks ahead per planning area, drivers explained, ranked by where limited effort goes first, and a ready-to-post message.** None of the sources describe a public tool that combines those. The differentiation is the decision and delivery layer, not the existence of a forecast.

## Dimension: their customers' voice

Only general complaints about myENV (lost functionality, crashes, navigation) from app-store reviews via search summaries; none dengue-specific; dates unknown [7]. Treat as weak.

## Cross-dimension insights

- NEA's own alert channel is **app and web based and current-state**. That leaves room for a forecast and for chats residents already read, but it also means the honest problem statement is "alerts describe the present; nothing public says where risk is heading", not "residents are not told anything".
- The planning-area research preprint [5] is both a **validation** (the level is meaningful and the method works at one week) and a **risk**: other teams can cite it too, so our originality has to come from the last-mile layer.

## Recommendations

1. **Reword slide 1** to: "NEA's public cluster map and alerts describe today's situation; nothing public shows where risk is heading over the next two weeks." Confidence: medium-high on the map [1], medium on "nothing public" (search-limited).
2. **Never say "NEA does not predict."** NEA's institute appears to run internal forecasts [6]. Keep "public cluster dashboard".
3. **Position against myENV explicitly** on slide 2: alerts today, forecast plus ready-to-post message tomorrow. Binds to the differentiation prompt.
4. **Cite the planning-area preprint [5] as related work** and say we forecast two weeks ahead and add ranking and delivery. Frame our numbers only against our own baselines.
5. **Do not claim** "no app forecasts by planning area" until SG Outbreak / SGCharts and community projects are checked.

## Open questions

- Does any public tool (SG Outbreak, community projects) forecast per planning area? Needs one more search round.
- When did myENV dengue alerts launch, and can a group admin paste or share an alert? Fetch the myENV PDF [3] and NEA's news page "Information on areas with higher mosquito population now available on myENV app".
- Does NEA publish a yearly higher-Aedes risk map? Not found in this search.
- Accuracy numbers for NEA's internal forecasts: read Shi et al. 2016 [6].

## Sources

| n | Supports | Publisher | Published | Accessed | Confidence |
|---|---|---|---|---|---|
| [1] | Cluster map is current-state, no forecast; tiers; GeoJSON on data.gov.sg | [NEA](https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters) | 2026-09-30 (page updated) | 2026-09-30 | high (fetched) |
| [2] | Community Alert System; myENV alerts; no forward-looking projection | [NEA](https://www.nea.gov.sg/dengue-zika/dengue/dengue-community-alert-system) | 2026-04-13 | 2026-09-30 | high (fetched) |
| [3] | myENV Dengue/Zika/Aedes notifications based on Gravitraps; NEA news item on myENV area information | [NEA](https://www.nea.gov.sg/docs/default-source/default-document-library/aedes-myenv-app-v34e8eea8675eb456a822b53658431649b.pdf) | unknown | 2026-09-30 | medium (search summary; second search confirmed NEA news title) |
| [4] | 1 km neighbourhood forecast, 12 weeks, AUC above 0.75 | [BMC Medicine](https://pmc.ncbi.nlm.nih.gov/articles/PMC6091171/) | 2018-08-06 | 2026-09-30 | high (fetched) |
| [5] | Planning-area hotspot forecast, 1 week, F-score 0.79 | [arXiv preprint](https://arxiv.org/html/2601.12856) | 2026-01 (from ID) | 2026-09-30 | medium (fetched; not peer reviewed) |
| [6] | NEA EHI internal LASSO forecasts | [EHP, Shi et al. 2016](https://ehp.niehs.nih.gov/15-09981) | 2016 | 2026-09-30 | medium-low (search summary) |
| [7] | myENV general user complaints | [App Store](https://apps.apple.com/sg/app/myenv/id444435182) | unknown | 2026-09-30 | low (search summary) |

## Staleness map

Pricing and features go stale within 3 months, so the alert-system claims [2][3] should be re-checked by **2026-12-30**; trajectory signals such as the preprint [5] within 6 months, by **2027-03-30**. The earliest re-check is 2026-12-30. Refresh handles this.

## Verification note

Normal validation: spot-checked at landing. [1] and [2] were confirmed by direct page fetch; a second, independent NEA search surfaced NEA news pages titled "Information On Areas With Higher Mosquito Population Now Available On MyENV App" and "New Dengue Alert Banners", corroborating the myENV alert claim. The semantic citation check by a fresh-context subagent was not run on this quick preset.
