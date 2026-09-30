# Research evidence

<!-- markdownlint-disable MD013 -->

> Where every claim in this toolkit comes from. Folder names follow the BMad Deep Recon convention, so `/bmad-deep-recon` → **Refresh** can find and update them. Don't rename them.

| Folder / file | What it is | Key output |
| --- | --- | --- |
| [`technical-hackathon-toolkit-2026-09-21/`](technical-hackathon-toolkit-2026-09-21/research.md) | Research run 1: hackathon strategy, frontend, backend, AI/RAG, MCP (56 sources) | `research.md`, which feeds folders 01–05 (and their `docs/evidence.md`) |
| [`technical-hackathon-github-repos-2026-09-21/`](technical-hackathon-github-repos-2026-09-21/research.md) | Research run 2: high-star GitHub repos, with 278 repos API-verified (34 sources) | `research.md` + `repo-tables.md`, which feed `06-repo-catalog/` and every folder's `docs/repos.md` |
| [`technical-agents-and-fullstack-practices-2026-09-23/`](technical-agents-and-fullstack-practices-2026-09-23/research.md) | Research run 3: AI agents and workflows, plus a backend/frontend currency check (123 sources) | `research.md`, which feeds `04-ai-and-rag/docs/agents-and-tool-use.md`, `skills/hackathon-ai`, the backend and frontend skills, and folders 02–05 `docs/evidence.md` (labels **A**) |
| [`technical-datathons-and-ml-solutions-2026-09-23/`](technical-datathons-and-ml-solutions-2026-09-23/research.md) | Research run 4: Datathons & ML hackathons, real-world data pipelines, rapid modeling, and last-mile solutions (14 key sources) | `research.md`, feeding the dedicated `Datathon-Playbook` repository |
| [`distribute.py`](distribute.py) | Splits both reports and `repo-tables.md` into each folder's `docs/evidence.md` and `docs/repos.md`. Run it from the toolkit root after a Refresh | Regenerated files |
| [`help-me-papi-import.md`](help-me-papi-import.md) | What was adapted from maxi-cmyk/help-me-papi, what was corrected, and what was left out | Import log |

Inside each run folder:

- `research.md`: the cited report
- `digests/`: raw findings from each researcher
- `imports/`: verified data, such as `github-metrics.json`
- `repo-tables.md` (run 2 only): the category tables, the source for every `docs/repos.md`
- `.memlog.md`: the append-only decision and claims log
