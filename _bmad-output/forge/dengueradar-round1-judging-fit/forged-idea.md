# DengueRadar Round 1 — judging-fit forge: locked decisions

Goal: pressure-test the Round 1 submission against DAISI's rubric (Problem fit & social impact 30%, Solution quality & originality 30%, Data & technical feasibility 25%, Clarity 15%) against ~140 competing teams.

## Prescriptive action layer

- **No institutional routing claim.** Do not name a specific Town Council, RC, or MCST as the recipient — URA planning areas don't align with Town Council/electoral/MCST boundaries, and no dataset maps one to the other (`DATASETS.md` line 126). Every community-leader action is framed as a checklist **any engaged resident, RC volunteer, or MCST council member in a flagged area can read and act on or escalate themselves.**
- Rejected: full geographic institutional routing (acquiring Town Council/MCST boundary data and spatial-joining) — real scope, no clean open dataset likely exists, not a 2-week job.
- **Top 3 drivers → stacked, deduplicated, ranked actions**, not one "leading driver → one action." Fixes an internal contradiction in `docs/model-definitions.md` §6 (line 72 says top 3 drivers shown, line 74 says leading driver drives the action). Overlapping actions from different drivers collapse into one line.
- **Second, independent routing axis: cause, not just driver.** NEA's Dengue Clusters feed has `HOMES` / `PUBLIC_PLACES` / `CONSTRUCTION_SITES` breeding-source fields (`DATASETS.md` line 51). `CONSTRUCTION_SITES` → NEA/BCA enforcement referral (does *not* reopen the no-institutional-routing lock above — NEA/BCA jurisdiction is national, not planning-area-bound). `HOMES`/`PUBLIC_PLACES` feed the existing resident/leader checklist, block-level where HDB data allows.
  - Field is sparse: 2 of 11 clusters populated as of the 27 Sep check. Cause-routing is a bonus layer on top of driver-based actions, not the backbone. When absent, the Area view explicitly states "root cause not yet identified by NEA" rather than silently omitting it.
- **Action layer is deliberately deterministic/rule-based, not model-generated**, and this should be stated explicitly on the slide as a design principle (auditable, NEA-sourced health guidance vs. an unverified generated-text black box) — not left implicit for a judge to either miss or dock.

## What Round 1 can honestly claim about the model

- **No task exists before the 4 Oct submission to train the model, run SHAP, or compute a backtest** — that work is scheduled in the Build Sprint (12–26 Oct), gated on being shortlisted. Round 1 requires no code; the 25% feasibility line asks for "credible architecture, feasible in two weeks," not a finished result.
- **Locked: slide 3's proof point is the validation *methodology*** (rolling-origin/time-ordered testing, leave-areas-out `GroupKFold`, no-leakage rule, cost-matrix threshold weighting a missed rise 5x a false alarm, capped at 15% alert load) — cited to `github/08-datathon-handbook/03-modeling/cross-validation-guide.md` — not a fabricated or pre-empted accuracy/lead-time number.
- Rejected: presenting any specific backtest result or lead-time figure on the Round 1 slides. Directly violates the team's own rule ("do not claim 'two weeks early' until the backtest measures it").
- Open option not chosen: squeezing a rough first model fit on 1 Oct for one honest preliminary number. Not pursued — methodology-as-proof-point was locked instead.

## Idea-originality reframe

- **The forecast + map is not the differentiator** — the DAISI brief itself asks every one of ~140 teams for "a predictive model on an interactive map." Neither is SHAP/explainability — it's a standard technique, already in the generic datathon pitch blueprint the team itself uses.
- **Locked differentiator: official Singapore open data has no historical dengue record below the national level** — a real wall any competent team building a genuinely trained per-planning-area model will hit. DengueRadar's original contribution is **identifying and validating two independent, citable archives** (SGCharts, 256 snapshots, 2015–2020; Nature Scientific Data cluster CSV, 2022, 213 subzones mapped) to manufacture the per-area training history the brief requires, instead of faking a heuristic or quietly downgrading to national-only.
- Claim precisely as: "we found and solved the constraint with a citable, reproducible method" — not "nobody else could find this." Other capable teams may independently find the same archives; the claim doesn't depend on exclusivity.

## Whole-submission framing

- **Locked:** the pitch proves the idea, solution design, and execution capability are sound and original — it does not depend on a model accuracy number anywhere. No fabricated performance figures in the deck.
- Three pillars and their current state: **idea originality** (fixed by the data-wall reframe above), **solution soundness** (strong: validation methodology, honest sparsity handling, no-institutional-routing honesty, auditable-by-design actions), **execution credibility** (strong evidence exists — live Lakeflow archive running daily since 28 Sep, Free Edition capability check passed, real NEA field-level data already explored — but not yet drilled into for how it lands on the slide; open going into the next session).

## Two factual fixes, resolved (not just discussed)

- **2020 dengue case count = 35,261.** Independently reproduced by summing `analysis/data/weekly_idb.csv` (Dengue Fever rows, 2020-W01..W53) — matches `DATASETS.md`, and is directly citable as "our own aggregation of the MOH Weekly Infectious Disease Bulletin." Drop the competing 35,012 figure in `docs/checkpoint-1oct.md` — no traceable source found in the repo.
- **"Rising temperature and erratic rainfall extend the Aedes season"** (slide 1, "why now") — cite directly to the official DAISI A2 brief (`project-context.md`), not external research. Caution: the team's own research digest (`_bmad-output/planning-artifacts/research/technical-dengueradar-feasibility-2026-09-28`) found this is more nuanced than it sounds — temperature above 31°C is often *dampening*, and heavy "flushing" rain *lowers* risk — and H1 in `docs/model-definitions.md` already reflects the nuanced version. Don't let a naive "hot+rainy=worse" framing appear elsewhere and contradict it. This tension, stated honestly, is itself a small originality point: testing the brief's own premise against real data rather than accepting it at face value.

## Still open (not resolved in this session)

- Execution-credibility pillar: how the "already-running pipeline" evidence actually gets compressed onto a slide.
- Doc edits needed to match these locks: `docs/model-definitions.md` §6 (still says "Town council: clear drains and roof gutters"), `_bmad-output/planning-artifacts/sprint-change-proposal-2026-09-28.md` (same wording), `docs/checkpoint-1oct.md` (still cites 35,012).
