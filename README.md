# DengueRadar — DAISI Challenge, Round 1

Real-time dengue outbreak forecasting by planning area, built on Databricks for the [Databricks AI Social Impact (DAISI) Challenge](https://daisi.online/), problem A2.

**The idea:** NEA's public cluster map and alerts show where dengue is now. Nothing public shows where risk is heading over the next two weeks. DengueRadar forecasts each planning area's cluster activity two weeks ahead from live cluster, weather and historical data, explains the top drivers, ranks where limited effort should go first, and hands a community group-chat admin a short, sourced, ready-to-post message.

**Status (30 Sep 2026):** design locked; Round 1 slides not yet built (only copy). The daily cluster-snapshot job has run since 28 Sep. No model has been trained and nothing about performance has been measured yet. See [`docs/DengueRadar-final-report.pdf`](docs/DengueRadar-final-report.pdf) for the full record.

## Start here

1. [`docs/DengueRadar-final-report.pdf`](docs/DengueRadar-final-report.pdf): everything we have done and decided, in one document.
2. [`pitch/round1-outline.md`](pitch/round1-outline.md): the three-slide copy, evidence, interview kit and claim guardrails.
3. [`docs/team-plan.md`](docs/team-plan.md): roles, tasks and the timeline to 6 Oct.

## Where things live

| Path | What's in it |
|---|---|
| [`project-context.md`](project-context.md) | Challenge brief, key dates, our angle, Databricks build path, judging criteria |
| [`DATASETS.md`](DATASETS.md) | Every dataset we use: source, tier, owner, how to pull it from data.gov.sg |
| [`docs/`](docs/README.md) | Model definitions, action library, data contract, team plan, ML explainer, checkpoint notes; `docs/archive/` holds superseded PDFs |
| `pitch/` | Round 1 slide copy, the official template (PDF and PPTX), architecture diagram source and images |
| `analysis/` | Analysis scripts (e.g. `lag_chart.py`); `analysis/data/` is working data and is gitignored |
| `notebooks/` | Databricks notebooks: Free Edition checks and the daily cluster-snapshot job |
| [`_bmad-output/`](_bmad-output/README.md) | BMad workflow records: brainstorm, forged ideas (history), the 28 Sep pivot, research reports, design thinking, judge-panel memory |
| `github/` and `.toolkit/` | Cloned hackathon playbook and datathon handbook (reference material, not our code; `.toolkit/` is a subset copy used by the BMad party-mode config) |
| `_bmad/`, `.claude/`, `.agent/`, `.agents/`, `.opencode/` | BMad and assistant tooling; do not edit by hand |

## Submission

Round 1 is a 3-slide PDF via Devpost, due 6 Oct 2026 11:59pm SGT (we are targeting 4 Oct). No working build is required. Timeline through Demo Day (27 Oct): [`project-context.md`](project-context.md).
