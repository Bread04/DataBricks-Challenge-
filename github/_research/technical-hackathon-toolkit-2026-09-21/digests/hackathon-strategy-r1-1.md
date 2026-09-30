# Digest: Hackathon strategy & pitching (r1-1)

Dimension: strategy, judging, pitch, AI-tool rules, repos. Accessed 2026-09-21. Tool budget ~20 calls; 11 pages/APIs fetched + 5 searches.

## Findings

1. At judging, a strong project with a confusing demo loses to a simpler project the judges understand; do one thing well rather than five halfway, since feature creep leads to unfinished demos. | https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/ | JetBrains Blog (Katherine Druckman, collecting judges' quotes) | 2026-06 | accessed 2026-09-21 | high | strategy
2. Show something working within about 90 seconds of the pitch. Lead with the problem so the judges share your frustration (Jono Bacon, Avi Press). | same JetBrains URL | JetBrains Blog | 2026-06 | accessed 2026-09-21 | med (one publisher, several named judges) | pitch
3. A working demo matters more than code quality. Colin Lowenberg (Nebius): "Mock everything you can and make sure all your forms are filled". Use tools and teammates you already know to cut down unknowns. | same JetBrains URL | JetBrains Blog | 2026-06 | accessed 2026-09-21 | med | strategy
4. Read the rules before you start and don't write code until you understand the problem space (Wortmann, JetBrains). Start from a real frustration, not "the coolest new tool" (Bonnie Xu, OpenAI). Visualize the winning demo and work backwards from it. Rehearse and time the pitch. | same JetBrains URL | JetBrains Blog | 2026-06 | accessed 2026-09-21 | med | strategy
5. Named Devpost judges list these as submission killers: over-indexing on one criterion, backend-heavy projects with no UI (Moot, Square), ambiguity (Bajza-Terlouw, Databricks), little change from provided templates (Boateng, Google), recycled projects and large teams with unequal contribution (Yarotska, NEAR), rehashed or overly simple ideas (Marusiak, Atlassian). | https://info.devpost.com/blog/hackathon-judging-tips | Devpost blog | undated | accessed 2026-09-21 | med | judging
6. Some judges look at visual appeal first (Boateng: "The first thing we look at is how visually appealing the project is"). Others look for a startup mindset (Yarotska) or ask "would I want to use it" (Marusiak). Judges review slide decks and written descriptions seriously. | same Devpost URL | Devpost blog | undated | accessed 2026-09-21 | med | judging
7. Devpost lists six common criteria: technological implementation (use of required tech), ease of use, demonstration, potential impact, quality of idea (originality), and design. It gives no weights. It stresses checking eligibility, required tools and video length limits before building. | https://info.devpost.com/blog/understanding-hackathon-submission-and-judging-criteria | Devpost blog | undated | accessed 2026-09-21 | high | judging
8. Devpost video advice: leave at least 2–3 hours before the deadline to polish, record and upload. Write your own script ("rather than relying on AI"). Cover what it does, the problem and how it works, starting with the pitch. Most hackathons require videos under 3 minutes. Use tools you already know (OBS, Canva, PowerPoint). Upload to YouTube and mark it "Not for Kids". | https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video | Devpost blog | undated | accessed 2026-09-21 | high | pitch
9. On YouTube you get the video link before the upload finishes, so you can submit to Devpost without waiting. You are judged on the application, not on production quality. (From search-result snippets of Devpost help pages; the pages themselves were not fetched.) | https://help.devpost.com/article/84-video-making-best-practices | Devpost Help Center | undated | accessed 2026-09-21 | low-med | pitch
10. ETHGlobal (Tokyo 2026) finalist format: 7 minutes per team, 4 min demo plus 3 min Q&A. Partner prizes are judged only on written materials. Criteria: Technicality, Originality, Practicality, Usability (UI/UX/DX), WOW Factor. The same format appears on several ETHGlobal event pages. | https://ethglobal.com/events/tokyo2026/info/details | ETHGlobal | 2026 (event Sep 2026) | accessed 2026-09-21 | high | judging
11. ETHGlobal demo video spec: 2–4 min, at least 720p, intro of 20 seconds at most, show live functionality and edit out waiting, no more than 4 bullets per slide. Prohibited: phone recording, text-to-speech or AI voiceovers, sped-up footage, music with text overlays instead of narration. | same ETHGlobal URL | ETHGlobal | 2026 | accessed 2026-09-21 | high | pitch
12. ETHGlobal AI rule: document in the submission where and how AI tools were used, down to specific files and generated assets. AI should assist, "not to create the entire project". Projects built entirely by AI may lose eligibility. Large single commits or missing git history may be disqualified. Prior code is not allowed in the Classic track. | same ETHGlobal URL | ETHGlobal | 2026 | accessed 2026-09-21 | high | tooling
13. MLH standard rules: AI is allowed for code completion, code generation and image generation, but teams must be honest and transparent about the AI tools they used. An idea from before the event is fine; code or materials from before it are not. Open-sourcing code before the event just to reuse it is not allowed. Digital events require a demo video of 2 minutes or less that names the hackathon at the start. | https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md | MLH (GitHub, repo pushed 2026-09-21) | living doc | accessed 2026-09-21 | high | tooling
14. MLH organizer guide recommends science-fair judging with about 3 minutes per team (pitch plus questions), with judges stack-ranking their top 3 rather than using a detailed rubric. The guide's philosophy is "learning over profit". | https://guide.mlh.com/general-information/judging-and-submissions/judging-plan | MLH Hackathon Organizer Guide | undated | accessed 2026-09-21 | high | judging
15. CONTRADICTION: A search snippet quoting MLH guidance says code quality, pitch quality, idea quality and real-world usefulness should NOT be judged at MLH events. Sponsor and industry judges (findings 1–6) weight pitch, problem framing and impact heavily. Rubrics differ by event type (learning-first student events vs sponsor/prize events), so read each event's rubric. The snippet was not verified on the fetched page. | https://guide.mlh.io/general-information/judging-and-submissions (snippet) | MLH | undated | accessed 2026-09-21 | low | judging
16. Unverified secondary claims (SEO snippets, not fetched): one "widely used 2026 rubric" is 20% innovation / 25% technical / 25% impact / rest presentation, and "90%+ of developers use AI coding tools daily" with winners "hand-writing the 20% of logic that makes it different". These are unsourced figures, so downgrade them. | https://www.masaischool.com/blog/how-to-win-an-ai-hackathon-in-2026-full-guide/ | Masai School blog | 2026 | accessed 2026-09-21 | low | judging/tooling

## Repos

| repo | URL | stars | last push | why useful |
|---|---|---|---|---|
| sahat/hackathon-starter | https://github.com/sahat/hackathon-starter | 35,254 | 2026-09-21 | Actively maintained Node.js boilerplate (auth, APIs) built for hackathons |
| dribdat/awesome-hackathon | https://github.com/dribdat/awesome-hackathon | 301 | 2026-05-05 | Curated platforms, tools and guides, aimed at organizers; useful for judging/format docs |
| MLH/mlh-policies | https://github.com/MLH/mlh-policies | 191 | 2026-09-21 | Source of the MLH standard hackathon rules (AI, prior code, video) for docs/standards |
| HappyHackingSpace/awesome-hackathon | https://github.com/HappyHackingSpace/awesome-hackathon | 90 | 2026-05-06 | "Tools and resources to help you build, design, and win hackathons", aimed at participants |
| geekcamp-ph/awesome-hackathon-starters | https://github.com/geekcamp-ph/awesome-hackathon-starters | 37 | 2016-07-17 | STALE, leave it out (listed only so nobody re-researches it) |

Also surfaced but not API-checked: TheAmazingPT/awesome-hackathons and mbiesiad/awesome-hackathons (event lists, low value for the toolkit), and Olanetsoft/awesome-hackathon-projects (example projects).

## Practical material

**Pre-event / T-minus checklist**
- Read the rules and rubric first: required tech, prior-code policy, AI disclosure, video length, whether the video must name the hackathon. [4, 7, 12, 13]
- Use a stack and tools you already know. Don't learn new video or editing tools during the event. [3, 8]
- An idea from before the event is allowed (MLH), but pre-written code is not. Don't pre-open-source code to reuse it. [13]
- Commit little and often. A single giant commit can get you disqualified (ETHGlobal). [12]
- Keep an AI-usage log from the start (tool, files, generated assets) so the disclosure section is ready. [12, 13]

**During the build**
- Choose one core feature and one "wow" moment. Cut anything that endangers the demo. [1, 10]
- Build the demo path first. Mock slow or flaky APIs and pre-fill forms. [3]
- Ship a visible UI. Judges penalize backend-only work and barely-changed templates. [5, 6]
- Hard stop on features 2–3 hours before the deadline, then script, record and upload. [8]

**Pitch structure (3 min live / 2–4 min video)**
1. Hook plus problem, 20 seconds at most, making judges feel the frustration. [2, 11]
2. What it does, in one sentence. [8]
3. Live demo, working by about the 90-second mark, with waiting edited out. [2, 11]
4. How it works: the tech and required sponsor tools, with 4 bullets per slide at most. [7, 11]
5. Impact / who uses it today (practicality). [7, 10]
6. Close; for ETHGlobal-style finals, prepare for 3 min of Q&A. [10]
- Time-box variants: MLH science fair about 3 min including questions [14]; MLH digital video 2 min or less [13]; Devpost usually under 3 min [8]; ETHGlobal 4 + 3 min Q&A [10].

**Backup video rules**
- Record your own narration. ETHGlobal bans AI voiceover and text-to-speech; Devpost advises writing your own script. [8, 11]
- Use the best mic, at least 720p, no phone recording, no sped-up footage. [8, 11]
- YouTube, unlisted or public, marked "Not for Kids". Grab the link while it uploads. [8, 9]
- Say the hackathon's name at the start (MLH). [13]

**Rubric self-check prompt idea (for PROMPTS.md)**
- "Here is the event rubric [paste]. Score my project 1–5 on each criterion, say which one I'm over-indexing on, and name the single change that raises my weakest score within N hours." [5, 7, 10]
- "Write a 180-second demo script: problem in 20 s, one-sentence solution, live demo by 90 s, tech plus sponsor tools, impact, ask. Mark where to cut if I'm running long." [2, 8, 11]
- "Draft the AI-usage disclosure for my submission from this log [paste], listing tools, files and generated assets." [12, 13]

## Leads not chased / Looked for but not found

- A fetched primary source on AI tools actually used at 2025–2026 hackathons (Claude Code, Cursor, v0, Lovable, Bolt). Only an unfetched TAIKAI "5 AI vibe coding tools" post (https://taikai.network/en/blog/5-ai-vibe-coding-tools-for-hackathons) turned up. Gap.
- HackYeah "use AI responsibly" page returned 404.
- The explicit four MLH criteria weighted equally were mentioned in a snippet but not found on the fetched judging-plan page. The "what is not judged" list is unverified.
- Winner retrospectives with concrete hour-by-hour time allocation were not found. Team-role splits (builder / demo-owner / pitcher) were not evidenced by any fetched source.
- Devpost posts are undated, so freshness is unknown.
- No pitch-template repo was found or checked.
- Not API-checked: Olanetsoft/awesome-hackathon-projects, TheAmazingPT/awesome-hackathons.
