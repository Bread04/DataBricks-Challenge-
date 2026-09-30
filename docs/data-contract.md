# DengueRadar data contract (DRAFT v0.1, 30 Sep 2026)

Owner: Braedon · Design: `docs/model-definitions.md` section 6d.

**One versioned schema, several views.** Each authority takes only the fields it needs. This is a **proposal**: we have no agreement with any agency, and the prototype sends nothing. All example values below are **ILLUSTRATIVE**, not model output.

## Schema (one row per planning area per week)

| Field | Type | Meaning | Notes |
|---|---|---|---|
| `contract_version` | string | Schema version, "0.1" | Bump on any change |
| `area_id` | string | URA planning area code | 55 areas |
| `area_name` | string | Planning area name | |
| `week` | date | Monday of the forecast week | ISO date |
| `band` | enum | `Low`, `Medium`, `High` | From the calibrated Rising probability |
| `band_change` | enum | `up`, `same`, `down`, `new` | Versus last week |
| `persistence` | enum | `new`, `persistent` | Ties to H3; limits alert fatigue |
| `top_drivers` | array of string | Up to 3 plain-words drivers | No feature names |
| `action_ids` | array of string | Up to 3 ids from `docs/action-library.md` | Deduplicated, ranked |
| `rank_cases`, `rank_rate` | int | Priority ranks (section 6a) | NEA view only |
| `confidence` | string or null | Backtest hit rate for this band | Null until measured |
| `coverage_flag` | enum | `ok`, `low_data` | |
| `tag` | enum or null | `HOMES`, `PUBLIC_PLACES`, `CONSTRUCTION_SITES`, null | NEA's breeding-source tag; sparse |
| `caveat` | string | "Forecast cluster activity, not a diagnosis. Cluster cases only." | Always present |
| `valid_until` | date | End of the forecast window | Forwarded messages must show it |

## Views

| Consumer | Fields | Format | Trigger |
|---|---|---|---|
| NEA weekly export | All fields | CSV or GeoJSON file | Weekly |
| NEA enforcement, NEA drain-cleansing and NParks record (NParks role unconfirmed) | `area_id`, `area_name`, `week`, `band`, `tag`, `top_drivers`, `action_ids`, `caveat`, `valid_until` | JSON, one record per event | Only when the trigger fires |
| Admin kit post | `area_name`, `band`, `band_change`, `top_drivers`, `action_ids` (resident and community text), `caveat`, `valid_until` | Plain text, WhatsApp and Telegram variants | Weekly, only on a band change |

Trigger rules: NEA enforcement when `tag = CONSTRUCTION_SITES`; NEA drain cleansing when band is High or rising and the H1 driver is present; NParks (role unconfirmed) when band is High and the H4 driver is present. The "sustained" flag threshold is tuned on validation years and frozen before the test year.

## Sample record (ILLUSTRATIVE, values invented for layout only)

```json
{
  "contract_version": "0.1",
  "area_id": "EXAMPLE",
  "area_name": "Example Area",
  "week": "2026-10-05",
  "band": "High",
  "band_change": "up",
  "persistence": "new",
  "top_drivers": ["Heavy rain 2 to 4 weeks ago, now warm", "A cluster close by"],
  "action_ids": ["A02", "A03"],
  "tag": null,
  "caveat": "Forecast cluster activity, not a diagnosis. Cluster cases only.",
  "valid_until": "2026-10-19"
}
```

## Open points

- `confidence`, ranks and thresholds stay empty until the backtest exists.
- **Town mapping caveat.** `analysis/data/hdb_property_information.csv` has a `bldg_contract_town` code per block, so a block-to-HDB-town mapping may be possible. That is not the same as Town Council or constituency boundaries, and it does not cover condos. It does not change the locked decision. It would only inform the roadmap item, after checking what the code means.
- Agency names and roles in the views are unconfirmed until the jurisdiction check is done.
