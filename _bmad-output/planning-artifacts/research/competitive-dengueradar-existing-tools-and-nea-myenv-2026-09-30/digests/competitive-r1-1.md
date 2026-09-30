# Digest: competitive, round 1, assistant 1 (access date 2026-09-30)

Assistant read 5 sources (NEA clusters page, NEA community alert page, PMC6091171, arXiv 2601.12856, plus search summaries). The first fetch of the community alert page failed (ECONNRESET); the retry succeeded.

## Findings

1. NEA's cluster map is a current-state tool, not a forecast. It shows an interactive map and table of active clusters with localities and case counts. "Map data is updated at 1am." Page last updated 2026-09-30. The page contains no predictive information (confirmed by fetch). Source: https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters. Publisher: NEA. Confidence: high. Class: capability. Fetched.
2. Cluster definition and tiers: 2+ cases with onset within 14 days and within 150 m; Red = 10+ cases; Yellow = fewer than 10; Green = no new cases, monitored 21 days. Tiers are on the page (fetched). The 14 days / 150 m definition rests on a search summary only. Confidence: tiers high; definition medium. Class: capability.
3. The cluster GeoJSON is on data.gov.sg (https://data.gov.sg/datasets/d_dbfabf16158d1b0e1c420627c0819168/view). Seen only as a search-result listing, not fetched. Confidence: medium. Class: capability.
4. NEA Dengue Community Alert System: colour-coded banners (purple, red, yellow, green). Users get alerts on "high Aedes mosquito population and dengue clusters near you" via the myENV app or go.gov.sg/dengue-high-risk. Source: https://www.nea.gov.sg/dengue-zika/dengue/dengue-community-alert-system. Publisher: NEA. Page last updated 2026-04-13. Confidence: high (fetched). The page does not define the colours (purple presumably the Aedes-population level; unverified). No forward-looking projections on the page. Class: capability.
5. myENV push notifications: the search summary of NEA's step-by-step PDF says users add locations and enable "Dengue/Zika/Aedes" notifications, and are notified if a saved location has a higher Aedes population detected by Gravitraps. Source: https://www.nea.gov.sg/docs/default-source/default-document-library/aedes-myenv-app-v34e8eea8675eb456a822b53658431649b.pdf. PDF not fetched, date unknown. Search summary only. Confidence: medium. Class: capability. The "since when" question is unanswered. The MOH page "New Dengue Alert Map on MOH and NEA websites" (https://www.moh.gov.sg/newsroom/new-dengue-alert-map-on-moh-and-nea-websites/) appeared but was not read.
6. The Aedes-population signal comes from Gravitrap surveillance, which measures current mosquito counts, not future cases (search summary only). Confidence: medium. The alert pages are current-state. No yearly Aedes risk map or public national forecast was found (see not-found list).
7. NEA has an internal forecasting system. The Environment Health Institute (EHI) uses LASSO models; the 2018 BMC Med paper notes EHI "currently relying on" them. Forecasts are weekly, national, 1 to 12 weeks ahead, using 200+ variables (search summary of ehp.niehs.nih.gov/15-09981, Environ Health Perspect, Shi et al. 2016; details from the summary only). Confidence: medium. Class: positioning. It appears to be internal decision support with no public forecast; that is inferred from finding nothing public, not verified.
8. NEA's stated accuracy or hit rate: none found on NEA's own pages. Only academic figures exist (9, 10). Absence is a finding.
9. Neighbourhood-level research forecast: 1 km x 1 km grid, 315 neighbourhoods, up to 12 weeks ahead, AUC > 0.75 for all windows and > 0.80 within 5 weeks. Inputs: cases 2010 to 2016, mobile phone movement, weather, building age, NDVI, EZLink transit data, national cases. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC6091171/. Publisher: BMC Medicine, 2018-08-06. Confidence: high (fetched). Class: quantitative. A research paper, not a public tool.
10. Hotspot forecasting research: 323 subzones (about 1.35 km2 each), aggregated to 55 planning areas; predicts hotspot status 1 week ahead from 4 weeks of history. Average F-score 0.79 (2013 to 2018 and 2020); 0.83 during the circuit breaker. Learned spread networks matched commuting patterns. Code on GitHub, not positioned as a deployed tool. Source: https://arxiv.org/html/2601.12856. Publisher: arXiv preprint, Jan 2026 (from the ID; exact date unconfirmed). Confidence: high (fetched); preprint may not be peer reviewed. Class: quantitative.
11. NEA co-designed research adds serotype dynamics, improving forecasts up to 4 weeks ahead and outbreak detection at all lead times. Source: https://www.nature.com/articles/s41467-025-66411-6 (Nature Communications; PMC12727700). Search summary only; date likely late 2025, unverified. Confidence: medium-low. Class: quantitative.
12. User criticism of myENV is general, not dengue-specific. Reviews (via search summary of App Store and justuseapp pages) say the new version "has lost much of the functionality of previous versions" and cite crashes, a hard-to-navigate UI and "no connection" messages. Sources: https://apps.apple.com/sg/app/myenv/id444435182 and https://justuseapp.com/en/app/444435182/myenv/reviews. Review dates unknown. Confidence: low-medium. Class: positioning.

## Leads

- Fetch the myENV notification PDF and the MOH "New Dengue Alert Map" page to date the feature launch.
- Read Shi et al. 2016 (EHP, https://ehp.niehs.nih.gov/15-09981) for accuracy numbers and to confirm the forecast is national only.
- Check Nature Comms PMC12727700 for the NEA co-design details and date.
- Check Apple and Google Play review text for dengue-specific complaints.
- Look at data.gov.sg for Gravitrap or Aedes datasets (eight dengue datasets listed, not inspected).
- RPubs "Redesign of NEA Dengue Cluster Map" and the odimpact.org case study may give critiques.

## Not found

- Any NEA-published dengue forecast, risk map or hit rate on nea.gov.sg. Searches: "NEA dengue clusters map update daily", "NEA dengue forecast accuracy Environmental Health Institute early warning". The two alert pages are silent on forecasts.
- A yearly map of higher-Aedes areas: only alert banners and myENV notifications appeared.
- Any public app or dashboard offering a per-planning-area, two-week-ahead dengue forecast. SG Outbreak / SGCharts and other community projects were not searched (budget ran out); unverified either way.
- The launch date of myENV dengue alerts, and any Telegram or WhatsApp dengue channel (not searched).
- Dengue-specific public criticism: none found.

## Assistant's pitch caution

What is verifiable is that NEA's public pages show current clusters and Aedes-based alerts with no forecast. "NEA has no internal forecast" cannot be claimed, since EHI runs LASSO forecasts. "No public forecast exists" is supported only as "none found in this search".
