# 📖 Glossary: the words, in plain English

<!-- markdownlint-disable MD013 -->

> Every piece of jargon used in this toolkit, explained simply. Words are grouped by topic, and you can use Ctrl+F to find one.

---

## Hackathon basics

| Word | What it means |
| --- | --- |
| **Hackathon** | A short event (usually 24–48 hours) where teams build a working project from scratch, then pitch it to judges |
| **Demo** | Showing your project working, live, in front of the judges |
| **Pitch** | The short talk (usually 2–4 minutes) where you explain the problem, show the demo and say why it matters |
| **Judging rubric** | The list of things judges score you on (for example idea, design, technical difficulty, impact) |
| **Sponsor track / prize** | An extra prize from a company, usually for using their product in your project |
| **Devpost** | A website where many hackathons collect submissions (description, video, code link) |
| **MVP** (minimum viable product) | The smallest version of your idea that still works and impresses. At a hackathon, you only build the MVP |
| **Scope / cut line** | Deciding what you *won't* build. Features below the "cut line" are only for if you have spare time |
| **Walking skeleton** | A bare-bones version of the app that works end to end and is online. Build this first |
| **Mock / fake data** | Pretend data or a fake response used so the demo works even when the real thing is slow or unfinished |
| **Backup video** | A recording of your demo, in case the live demo breaks on stage |

## Building apps

| Word | What it means |
| --- | --- |
| **Frontend** | The part of the app people see and click (buttons, pages, layout) |
| **Backend** | The behind-the-scenes part: saving data, logins, talking to other services |
| **Full-stack** | Both frontend and backend |
| **Framework** | A ready-made foundation for building apps. **Next.js** is the one this guide uses |
| **Library / package** | Reusable code someone else wrote that you add to your project (for example a chart library) |
| **npm / npx** | The tools that install JavaScript packages (`npm install …`) or run one without installing it (`npx …`) |
| **Component** | A reusable piece of UI, like a button or a card |
| **Tailwind** | A way of styling apps by adding short class names (`p-4`, `text-lg`) instead of writing CSS files |
| **shadcn/ui** | A popular free collection of good-looking, accessible components you copy into your project |
| **Design tokens** | Named values for colours, spacing and fonts (for example `--color-accent`), so the whole app looks consistent |
| **Responsive** | The layout adapts to phones, tablets and desktops |
| **Accessibility (a11y)** | Making the app usable by everyone, including people using screen readers or keyboards only. **WCAG** is the standard |
| **PWA** | A website that can be "installed" on a phone's home screen like an app |
| **Expo / React Native** | Tools for building real mobile apps with JavaScript |

## Data and accounts

| Word | What it means |
| --- | --- |
| **Database** | Where your app stores information (users, posts, scores…) |
| **Supabase** | A free-tier service that gives you a database, logins and file storage in one place |
| **SQL** | The language used to talk to most databases |
| **Table** | Like a spreadsheet inside the database: rows of data with columns |
| **Migration** | A saved change to the database structure (for example "add a table"), so everyone's database matches |
| **Seed data** | Example data you load into the database so the app doesn't look empty during the demo |
| **Auth** (authentication) | Logging in: checking who a user is. **Clerk** and **Supabase Auth** do this for you |
| **RLS** (row level security) | A database rule that makes sure users can only see and change *their own* data |
| **GRANT** | A database permission that allows access to a table. Supabase now requires one per table (from 2026-10-30 for all projects) |

## Putting it online

| Word | What it means |
| --- | --- |
| **Deploy** | Putting your app on the internet so anyone can open it with a link |
| **Hosting / host** | The service that runs your app online (for example **Vercel**, **Railway**, **Render**) |
| **URL / domain** | Your app's web address |
| **Localhost** | Your app running only on your own computer (`http://localhost:3000`). Other people can't see it |
| **Tunnel** | A tool (like **cloudflared**) that temporarily gives your localhost a public link |
| **Environment variable / `.env`** | A settings file for secrets and configuration. **Never upload it to GitHub** |
| **API key** | A secret password that lets your app use a service (for example an AI model). Treat it like a password |
| **Cold start / sleeping** | Free hosts pause your app when nobody uses it; the first visit then takes a while to wake it up |
| **Free tier** | The free plan of a paid service, with usage limits |
| **CI** | Automatic checks that run whenever you upload code (for example running tests) |

## Code and teamwork

| Word | What it means |
| --- | --- |
| **Repo** (repository) | A project folder tracked by **git**, usually stored on **GitHub** |
| **Git / commit / push** | Git tracks changes. A *commit* saves a snapshot, and *push* uploads it to GitHub |
| **Branch** | A separate copy of the code to work on without affecting the main version |
| **PR** (pull request) | A request to merge a branch's changes into the main code, usually with a review |
| **Merge conflict** | When two people changed the same lines and git asks you which version to keep. How to fix one: [`01-hackathon-playbook/docs/git-for-teams.md`](01-hackathon-playbook/docs/git-for-teams.md) → Part 4 |
| **Open source** | Code anyone can use for free, published publicly |
| **License** | The rules for how you're allowed to use someone's code (MIT and Apache are very permissive) |
| **Stars ⭐** | GitHub "likes": a rough sign of how popular a project is |
| **Archived / stale** | A project that's no longer maintained. Avoid building on it |

## AI terms

| Word | What it means |
| --- | --- |
| **LLM** (large language model) | The AI behind chatbots, such as Claude, GPT or Gemini |
| **Model API** | A way for *your app* to send text to an AI and get an answer back (usually paid per use) |
| **Token** | A small chunk of text (about ¾ of a word). AI pricing is per million tokens |
| **Prompt** | The instructions you give an AI |
| **System prompt** | Hidden instructions that set how the AI behaves in your app |
| **Structured output** | Asking the AI to reply in a fixed format (like JSON) your code can read reliably |
| **RAG** (retrieval-augmented generation) | Letting the AI answer questions using *your own documents*: it looks up the relevant bits first, then answers |
| **Embedding / vector** | A way of turning text into numbers so similar meanings can be found. It powers RAG |
| **Vector database** | A database built to search embeddings (for example **pgvector**, which is built into Supabase) |
| **Local model / Ollama** | Running an AI model on your own computer, free and offline |
| **Agent** | An AI that takes several steps on its own (for example searching, then writing code, then testing). Building one into your app: [`04-ai-and-rag/docs/agents-and-tool-use.md`](04-ai-and-rag/docs/agents-and-tool-use.md) |
| **Tool call** | When the AI asks your code to run a function (search, look up a user, send an email), then reads the result |
| **Lethal trifecta** | Private data + untrusted content + a way to send data out, all in one AI. Together, one hidden instruction can leak your data, so never combine all three |
| **Hallucination** | When an AI confidently makes something up |

## Datathons & Data Science

| Word | What it means |
| --- | --- |
| **Datathon** | A data-focused hackathon where teams solve a real-world problem using datasets, machine learning and an interactive decision-support tool |
| **Baseline** | The simplest possible model or heuristic (like guessing the average) that any clever machine learning model must beat |
| **Cross-Validation (CV)** | Splitting data into multiple slices to train and test repeatedly, preventing lucky guesses and testing generalizability |
| **Overfitting** | When a model memorizes the training data answers instead of learning general patterns, causing it to fail on unseen data |
| **Target Leakage** | Accidental cheating: when information from the future or the answer key sneaks into the training features |
| **SHAP (Explainability)** | Game-theoretic proof showing *why* a machine learning model made a specific prediction (showing the receipts) |
| **Polars & DuckDB** | Modern, high-speed analytical engines that run in Rust/C++ across all CPU cores without memory crashes on large CSVs |

## AI coding tools

| Word | What it means |
| --- | --- |
| **AI coding assistant** | An AI that writes and edits code with you (for example **Claude Code**, Copilot, Cursor, Antigravity) |
| **Claude Code** | Anthropic's AI coding assistant that runs in your terminal. It needs a paid plan 💳 |
| **Terminal / CLI** | The text window where you type commands |
| **MCP** (Model Context Protocol) | A standard way to give your AI assistant **extra abilities**, such as reading a database, controlling a browser or searching docs |
| **MCP server** | One of those plug-in abilities (for example the "Playwright MCP" lets the AI use a web browser) |
| **Plugin / marketplace** | Ready-made bundles you can install into Claude Code with one command |
| **Skill** (`SKILL.md`) | A saved set of instructions Claude Code can load when relevant, like a cheat sheet |
| **Hook** | An automatic action that runs when the AI does something (for example "format code after every edit") |
| **Subagent** | A helper AI that Claude Code sends off to do one task in parallel |
| **Prompt injection** | A trick where hidden text (in a web page, file or tool) tries to make the AI do something harmful. See [`05-tools-and-mcp/docs/mcp-security.md`](05-tools-and-mcp/docs/mcp-security.md) |
| **BMad** (BMad Method) | The free, step-by-step workflow this toolkit runs on. It's a set of skills for Claude Code (`/bmad-brainstorming`, `/bmad-spec`, `/bmad-build`…) that take you from idea to pitch. Setup: [`01-hackathon-playbook/docs/setup-bmad.md`](01-hackathon-playbook/docs/setup-bmad.md) |
| **Story** | One small, buildable piece of the project, sized for one `bmad-build` session. Stories live in `stories.yaml`, ordered by demo value |
| **Spec** (`SPEC.md`) | The one-page plan `bmad-spec` writes: Why · Capabilities · Constraints · Non-goals · Success signal |
| **`project-context.md`** | The file at your repo root with the event rules and your stack. Almost every BMad skill reads it automatically |
| **Fresh chat** | A new Claude Code session. Run each BMad skill in its own, so earlier work doesn't confuse it |

## Other terms you'll see

| Word | What it means |
| --- | --- |
| **Web3 / smart contract** | Blockchain apps. A smart contract is code that runs on a blockchain (see [`03-backend/docs/web3.md`](03-backend/docs/web3.md)) |
| **Testnet** | A practice blockchain with free fake money |
| **Analytics** | Tracking how people use your app (for example **PostHog**) |
| **Core Web Vitals** | Google's measures of how fast and smooth a web page feels |
| **Rate limit** | A cap on how many requests you can make in a period of time |
| **OWASP** | A well-known list of the most common security mistakes |
