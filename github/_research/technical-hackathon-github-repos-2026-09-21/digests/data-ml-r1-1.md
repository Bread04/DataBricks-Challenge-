# Data & ML hackathon accelerators: digest r1-1 (2026-09-21)

Legend for notes: **[E]** means the slug or status is backed by a source fetched or searched this session. **[U]** means the slug comes from prior knowledge and has not been verified this session, so the lead should check it. Star counts are the figures the cited sources report, not live values.

## Candidates

| category | owner/repo | one-line hackathon use | evidence URL | notes |
|---|---|---|---|---|
| LLM agents | langchain-ai/langgraph | Stateful graph agents with tool calls and human-in-the-loop | https://dreaming.press/posts/ai-agent-frameworks-github-ranked-by-stars-2026.html | [E] ~40.2k stars (Aug 21 2026); 1.0 GA Oct 2025 |
| LLM agents | langchain-ai/langchain | Integrations glue for models, retrievers and tools | https://florinelchis.medium.com/top-10-rag-frameworks-on-github-by-stars-january-2026-e6edff1e0d91 | ~125k stars (Jan 2026); slug [U] |
| LLM agents | crewAIInc/crewAI | Role-based multi-agent crews, fast to demo | https://dreaming.press/posts/ai-agent-frameworks-github-ranked-by-stars-2026.html | [E] ~57.4k, active |
| LLM agents / RAG | run-llama/llama_index | Document-centric agents and RAG over your data | same | [E] ~51.8k, active |
| LLM agents | agno-agi/agno | Lightweight Python agents (formerly Phidata) | same | [E] ~41.8k, active |
| LLM agents | huggingface/smolagents | Minimal code-as-action agents on HF models | same | [E] ~28.9k |
| LLM agents | openai/openai-agents-python | First-party OpenAI agent SDK with handoffs and guardrails | same | [E] ~28.8k |
| LLM agents | mastra-ai/mastra | TypeScript-native agents and workflows for JS teams | same | [E] ~27.3k |
| LLM agents | google/adk-python | Gemini/Google Cloud agent kit | same | [E] ~21.2k |
| LLM agents | pydantic/pydantic-ai | Type-safe agents with structured outputs | same | [E] ~19.4k |
| LLM agents | microsoft/agent-framework | Successor to AutoGen and Semantic Kernel (Python/.NET) | same | [E] ~13.0k; 1.0 GA Apr 2 2026 |
| LLM agents | anthropics/claude-agent-sdk-python | Claude agent loop with tools | same | [E] ~7.9k |
| LLM agents (AVOID) | microsoft/autogen | Do not start new work here | https://www.langchain.com/resources/langchain-vs-autogen | [E] Maintenance mode, community-managed; README points to Agent Framework |
| LLM agents | ag2ai/ag2 | Community fork of AutoGen 0.2 | — | [U] status not checked this run |
| LLM agents | stanfordnlp/dspy | Programmatic prompt optimization | — | [U] |
| LLM agents | vercel/ai | TS AI SDK for streaming chat UIs | — | [U] |
| RAG / ingestion | docling-project/docling | PDF/DOCX/PPTX to structured Markdown/JSON with tables | https://github.com/topics/docling?l=python | slug [U] (org moved from DS4SD); scored 4.5/5 vs Crawl4AI on olud.ai |
| RAG / ingestion | microsoft/markitdown | Convert any office file to Markdown for LLMs | https://www.firecrawl.dev/blog/best-open-source-web-scraping-libraries | ~47.3k stars; slug [U] |
| RAG / ingestion | unclecode/crawl4ai | Local-first LLM-friendly crawler that outputs markdown | https://github.com/unclecode/crawl4ai | [E] slug; >68k stars per Firecrawl blog |
| RAG / ingestion | firecrawl/firecrawl | Crawl/scrape to clean markdown via API or self-hosted | https://github.com/firecrawl | [E] org; ~68k+ stars claimed in its own blog (vendor source) |
| RAG / ingestion | Unstructured-IO/unstructured | Broad file partitioning for ETL | — | [U] |
| RAG engine | infiniflow/ragflow | Turnkey RAG with deep document understanding and a UI | https://florinelchis.medium.com/top-10-rag-frameworks-on-github-by-stars-january-2026-e6edff1e0d91 | ~70k (Jan 2026); slug [U] |
| RAG engine | HKUDS/LightRAG | Graph-based RAG from HKU research | https://www.firecrawl.dev/blog/best-open-source-rag-frameworks | slug [U] |
| RAG engine | microsoft/graphrag | Knowledge-graph RAG pipeline | — | [U] |
| RAG framework | deepset-ai/haystack | Mature production RAG pipelines | https://florinelchis.medium.com/top-10-rag-frameworks-on-github-by-stars-january-2026-e6edff1e0d91 | ~24k (Jan 2026); slug [U] |
| Vector DB | qdrant/qdrant | Rust vector DB with a good free tier and sparse/ColBERT support | https://dreaming.press/posts/best-open-source-vector-database-2026.html | [E] Apache-2.0 |
| Vector DB | weaviate/weaviate | Hybrid vector+BM25 search | same | [E] BSD-3, v1.37 in 2026 |
| Vector DB | pgvector/pgvector | Vectors inside Postgres (Supabase/Neon friendly) | same | [E] 0.8.x |
| Vector DB | milvus-io/milvus | Billion-scale vectors (overkill for hackathons) | same | Milvus 3.0 "lake-native" shipped Jul 2026; slug [U] |
| Vector DB | chroma-core/chroma | Zero-config embedded vector store for prototypes | same | Chroma Cloud still in preview; slug [U] |
| Vector DB | lancedb/lancedb | Serverless, local-first multimodal vectors | https://www.firecrawl.dev/blog/best-vector-databases | slug [U] |
| Search | meilisearch/meilisearch | Instant typo-tolerant search plus hybrid search | — | [U] |
| Search | typesense/typesense | Fast search with a vector option | — | [U] |
| Local models | ollama/ollama | One-command local LLMs with an OpenAI-compatible API | https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1 | [E] 130k+ (July 2026); v0.19 added an MLX backend |
| Local models | ggml-org/llama.cpp | CPU/GPU GGUF inference engine | https://www.storagereview.com/best/local-llm-tools | 100k stars in Mar 2026; dev.to gives the old slug ggerganov/llama.cpp, so the lead should confirm the redirect |
| Serving | vllm-project/vllm | High-throughput multi-user serving | dev.to guide (above) | [E] 50k+ |
| Serving | sgl-project/sglang | Serving with RadixAttention for shared-prefix RAG and agents | dev.to guide (above) | [E] 18k+, fast-growing |
| Local models | janhq/jan | Offline desktop ChatGPT alternative | dev.to guide (above) | [E] 42k+ |
| Local models | nomic-ai/gpt4all | Desktop local LLM | dev.to guide (above) | [E] 73k+; activity not checked |
| Local models | ml-explore/mlx | Apple Silicon ML/LLM | dev.to guide (above) | [E] 21k+ |
| Serving (AVOID) | huggingface/text-generation-inference | Do not start on TGI | dev.to guide (above) | [E] Maintenance mode since Mar 21 2026; redirects users to vLLM, SGLang, llama.cpp and MLX. Slug [U] |
| Local UI | open-webui/open-webui | ChatGPT-style UI over Ollama/OpenAI | https://www.storagereview.com/best/local-llm-tools | listed in the dev-UX layer; slug [U] |
| Local models | mudler/LocalAI | OpenAI-compatible local API | — | [U] |
| Low-code | langgenius/dify | Visual LLM app/agent builder with RAG | https://dreaming.press/posts/ai-agent-frameworks-github-ranked-by-stars-2026.html (search snippet) | ~144k per search snippet; ~114k in Jan 2026 per Medium; slug [U] |
| Low-code | n8n-io/n8n | Workflow automation with AI nodes | https://huggingface.co/blog/daya-shankar/n8n-vs-flowise-vs-langflow-enterprises | 182k+ in one source, 90k in another (conflict); slug [U] |
| Low-code | langflow-ai/langflow | Drag-and-drop LangChain flows | same | slug [U] |
| Low-code | FlowiseAI/Flowise | Drag-and-drop agent builder | https://newsroom.workday.com/2025-08-14-Workday-Acquires-Flowise,-Bringing-Powerful-AI-Agent-Builder-Capabilities-to-the-Workday-Platform | [E] Acquired by Workday Aug 14 2025; 42k+ stars; open-source status after the deal not verified |
| Demo UI | gradio-app/gradio | Model demo in a few lines; HF Spaces hosting | https://pynions.com/streamlit-vs-gradio | ~43–45k; slug [U] |
| Demo UI | streamlit/streamlit | Data apps and dashboards | same | ~43–45k; slug [U] |
| Demo UI | marimo-team/marimo | Reactive notebook that deploys as an app | https://github.com/marimo-team/marimo?locale=en-US | [E] 18k+; a security advisory was exploited quickly (cybernews), so keep it patched |
| Demo UI | reflex-dev/reflex | Full-stack web apps in pure Python | https://github.com/reflex-dev/reflex | [E] 20k+ |
| Demo UI (CAUTION) | Chainlit/chainlit | Chat UI for LLM apps | https://heyclau.de/compare/ml-app-ui-frameworks | ~11.9k; founding team stepped back May 2025, now community-maintained, 2 high-severity CVEs in late 2025 |
| Demo UI | holoviz/panel | Dashboards | — | [U] |
| Classic data | pola-rs/polars | Fast DataFrames | https://docs.pola.rs/user-guide/ecosystem/ | slug [U]; scikit-learn accepts Polars I/O |
| Classic data | duckdb/duckdb | In-process SQL analytics on CSV/Parquet | https://www.opensourceforu.com/2026/03/polars-duckdb-the-new-power-combo-for-in-process-analytics/ | slug [U] |
| Classic ML | scikit-learn/scikit-learn | Baseline models and pipelines | https://docs.pola.rs/user-guide/ecosystem/ | [U] slug |
| Classic ML | dmlc/xgboost | Tabular gradient boosting | — | [U] |
| Classic ML | microsoft/LightGBM | Fast tabular GBDT | — | [U] |
| Classic ML | Lightning-AI/pytorch-lightning | Training-loop boilerplate removal | — | [U] |
| HF stack | huggingface/transformers | Pretrained models | — | [U] |
| HF stack | huggingface/datasets | Dataset loading | — | [U] |
| HF stack | huggingface/diffusers | Image/video generation pipelines | — | [U] |
| Vision | ultralytics/ultralytics | YOLO detection/segmentation in a few lines | — | [U]; AGPL-3.0 per prior knowledge, verify licensing |
| Labeling | HumanSignal/label-studio | Fast data labeling UI | — | [U] |
| MLOps | mlflow/mlflow | Experiment tracking, now with LLM eval | https://inference.net/content/llm-evaluation-tools-comparison/ | listed as Apache/MIT eval tool; slug [U] |
| MLOps | wandb/wandb | Experiment tracking client | — | [U] |
| Monitoring | evidentlyai/evidently | Data drift and model/LLM eval reports | https://inference.net/content/llm-evaluation-tools-comparison/ | slug [U] |
| Speech | SYSTRAN/faster-whisper | 4x faster Whisper transcription | https://localaimaster.com/blog/faster-whisper-guide | slug [U] |
| Speech | m-bain/whisperX | Word timestamps plus diarization | https://github.com/m-bain/whisperX | [E] slug |
| Speech | openai/whisper | Reference ASR | — | [U] |
| Vision | facebookresearch/sam3 | Text-prompted segmentation and tracking in images and video | https://github.com/facebookresearch/sam3 | [E] SAM 3.1 released, ~7x multi-object speedup; SAM License (not OSI) |
| Vision | google-ai-edge/mediapipe | On-device face, hand and pose detection | — | [U] slug |
| Vision | opencv/opencv | Classic CV | — | [U] |
| Gen media | comfyanonymous/ComfyUI | Node-graph diffusion workflows; SAM 3.1 supported natively | https://docs.comfy.org/tutorials/utility/video-segment-sam3 | slug [U] (may now be under the Comfy-Org org) |
| Eval/obs | langfuse/langfuse | Tracing, evals and prompt management; self-hostable | https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability | [E] Acquired by ClickHouse Jan 2026; stays OSS and self-hostable |
| Eval | promptfoo/promptfoo | Prompt/model comparison and red-teaming in CI | https://inference.net/content/llm-evaluation-tools-comparison/ | Acquired by OpenAI early 2026; CLI still ships under the same license. Slug [U] |
| Eval | vibrantlabsai/ragas | RAG metrics (faithfulness, context recall) | https://github.com/vibrantlabsai/ragas | [E] moved from explodinggradients; development "visibly slowed" in 2026 per inference.net |
| Eval | confident-ai/deepeval | Pytest-style LLM evals | https://agentscamp.com/guides/evaluation/best-llm-eval-tools-2026 | slug [U] |
| Eval/obs | Arize-ai/phoenix | Tracing plus evals, self-host | https://inference.net/content/llm-evaluation-tools-comparison/ | ELv2 source-available, not OSI; slug [U] |
| Eval/obs | comet-ml/opik | OSS eval and tracing | same | Apache/MIT per source; slug [U] |
| Obs | traceloop/openllmetry | OpenTelemetry for LLMs | — | [U] |
| Datasets | awesomedata/awesome-public-datasets | Find a dataset fast | https://awesome.ecosyste.ms/projects/github.com/awesomedata/awesome-public-datasets | [E] ~76k stars, last pushed Jun 2026 |

Count: 79 rows (about 45 with [E] evidence, the rest [U]).

## Findings

1. As of Aug 21 2026 the agent-framework star ranking is AutoGen ~60.6k, CrewAI ~57.4k, LlamaIndex ~51.8k, Agno ~41.8k, LangGraph ~40.2k, smolagents ~28.9k, OpenAI Agents SDK ~28.8k, Mastra ~27.3k, Google ADK ~21.2k, Pydantic AI ~19.4k, MS Agent Framework ~13.0k and Claude Agent SDK ~7.9k | https://dreaming.press/posts/ai-agent-frameworks-github-ranked-by-stars-2026.html | dreaming.press (AI-authored byline) | 2026-08-21 | accessed 2026-09-21 | medium (the source says it used a live GitHub API pull, but the byline is an AI model) | metric
2. AutoGen went into maintenance mode (bug fixes and security only, community-managed) and its README points new users to Microsoft Agent Framework. MAF reached 1.0 GA on Apr 2 2026 | https://www.langchain.com/resources/langchain-vs-autogen ; https://agentmarketcap.ai/blog/2026/04/13/microsoft-autogen-maintenance-mode-agent-framework-sunset-2026 | LangChain (competitor), AgentMarketCap | 2026 | accessed 2026-09-21 | high (several sources agree) | status/avoid
3. The start date of AutoGen's maintenance mode is given as Oct 2025 by some sources and tied to the April 2026 MAF GA by others | atlan.com, analyticsinsight (search snippets) | various | 2026 | accessed 2026-09-21 | medium | status
4. LangGraph 1.0 went GA in Oct 2025 | dreaming.press (above) | — | 2026-08-21 | accessed 2026-09-21 | medium | fact
5. Hugging Face TGI moved to maintenance mode on Mar 21 2026 and redirects users to vLLM, SGLang, llama.cpp and MLX | https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1 | DEV Community (Sreeraj Sreenivasan) | 2026-07-19 | accessed 2026-09-21 | medium-high | status/avoid
6. July 2026 star counts: Ollama 130k+, GPT4All 73k+, vLLM 50k+, Jan 42k+, MLX 21k+, SGLang 18k+. Ollama v0.19 (Mar 2026) added an MLX backend | same | same | 2026-07-19 | accessed 2026-09-21 | medium (the llama.cpp figure of 85k in this source conflicts with #7) | metric
7. llama.cpp passed 100k GitHub stars in March 2026 | https://www.storagereview.com/best/local-llm-tools | StorageReview | 2026 | accessed 2026-09-21 | medium | metric
8. SGLang reports about 29% higher throughput than vLLM on shared-context workloads (RadixAttention) | storagereview (search snippet) | StorageReview | 2026 | accessed 2026-09-21 | low-medium (vendor-neutral claim, but no benchmark was fetched) | performance
9. Workday acquired Flowise on Aug 14 2025 | https://newsroom.workday.com/2025-08-14-Workday-Acquires-Flowise,-Bringing-Powerful-AI-Agent-Builder-Capabilities-to-the-Workday-Platform | Workday (primary) | 2025-08-14 | accessed 2026-09-21 | high | ownership
10. ClickHouse acquired Langfuse in Jan 2026. Langfuse stays open source and self-hostable, and Langfuse Cloud keeps running | https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability | ClickHouse (primary) | 2026-01 | accessed 2026-09-21 | high | ownership
11. OpenAI acquired Promptfoo in early 2026, and the OSS CLI keeps shipping under its existing license | https://inference.net/content/llm-evaluation-tools-comparison/ | Inference.net | 2026 | accessed 2026-09-21 | medium (secondary source) | ownership
12. Ragas now lives at vibrantlabsai/ragas (Vibrant Labs, Apache-2.0), and one comparison says its development "visibly slowed" in 2026 | https://github.com/vibrantlabsai/ragas ; inference.net | GitHub / Inference.net | 2026 | accessed 2026-09-21 | medium | rename/status
13. Arize Phoenix is ELv2 source-available, not OSI open source. Langfuse has an MIT core plus enterprise directories | inference.net | Inference.net | 2026 | accessed 2026-09-21 | medium | license
14. Chainlit's founding team stepped back in May 2025 (pivoting to Summon, a YC startup), the project is community-maintained, and two high-severity vulnerabilities were reported in late 2025 | https://heyclau.de/compare/ml-app-ui-frameworks (search snippet) | HeyClaude | 2026 | accessed 2026-09-21 | medium | status/caution
15. Gradio and Streamlit are both at ~43–45k stars, Chainlit ~11.9k, Marimo 18k+, Reflex 20k+ | search snippets (pynions, heyclau.de, reflex.dev) | various | 2026 | accessed 2026-09-21 | low-medium | metric
16. In Jan 2026 the RAG star ranking was LangChain ~125k, Dify ~114k, RAGFlow ~70k, LlamaIndex ~46.5k, Haystack ~24k | https://florinelchis.medium.com/top-10-rag-frameworks-on-github-by-stars-january-2026-e6edff1e0d91 | Medium (florinelchis) | 2026-01 | accessed 2026-09-21 | medium | metric
17. Crawl4AI has more than 68k stars and MarkItDown ~47.3k | https://www.firecrawl.dev/blog/best-open-source-web-scraping-libraries | Firecrawl (a competitor, so possible bias) | 2026 | accessed 2026-09-21 | medium | metric
18. Milvus 3.0 shipped in Jul 2026 as "lake-native", Weaviate is at v1.37, pgvector at 0.8.x, and Chroma Cloud is still in preview | https://dreaming.press/posts/best-open-source-vector-database-2026.html | dreaming.press | 2026-08-19 | accessed 2026-09-21 | medium | status
19. Recommended vector DBs by fit: Chroma for prototyping, LanceDB for local/multimodal, Qdrant for free tier and filtering, Weaviate for hybrid search, pgvector for Postgres | https://www.firecrawl.dev/blog/best-vector-databases (snippet) | Firecrawl | 2026 | accessed 2026-09-21 | medium | guidance
20. SAM 3.1 checkpoints were released with ~7x multi-object tracking speedup over SAM 3 (Nov 2025), under the SAM License. ComfyUI supports SAM 3.1 natively | https://github.com/facebookresearch/sam3 ; https://docs.comfy.org/tutorials/utility/video-segment-sam3 | Meta / Comfy | 2026 | accessed 2026-09-21 | high | release
21. awesome-public-datasets has ~76k stars and 11.5k forks and was last pushed in Jun 2026 | https://awesome.ecosyste.ms/projects/github.com/awesomedata/awesome-public-datasets | ecosyste.ms | 2026 | accessed 2026-09-21 | medium-high | metric/activity
22. n8n star counts conflict across sources (182k+ vs 90k+), and Dify is reported at ~144k (search snippet) | HF blog / search snippets | various | 2026 | accessed 2026-09-21 | low (the lead should verify) | metric
23. A marimo security advisory was exploited quickly after disclosure (cybernews headline), so pin to the latest release | https://cybernews.com/ai-news/python-notebook-flaw-marimo-hackers-advisories-glasswing/ (title only) | Cybernews | 2026 | accessed 2026-09-21 | low (headline only, article not read) | security

## Leads not chased / not found
- AG2 (ag2ai/ag2) current activity, DSPy, the Vercel AI SDK slug and stars were not searched.
- Star counts and slugs for the classic data/ML stack were not found in any 2026 source: Polars, DuckDB, scikit-learn, XGBoost, LightGBM, Lightning, HF transformers/datasets/diffusers, Ultralytics (check its AGPL license), Label Studio, MLflow, W&B, Evidently. They are all very likely healthy, but that is unverified this run.
- The llama.cpp canonical slug (ggml-org vs ggerganov) and the ggml/HF relationship were not verified.
- Flowise: whether the repo is still active and Apache-licensed after the Workday deal was not checked.
- ComfyUI slug (comfyanonymous vs Comfy-Org), MediaPipe org, faster-whisper activity and whisper.cpp were not checked.
- The majesticlabs Aug 2026 eval comparison fetch timed out. DeepEval, OpenLLMetry and Opik status were not verified.
- Unstructured, LlamaParse alternatives (e.g. MinerU, marker), Meilisearch, Typesense, Panel, LocalAI and Open WebUI licensing were not checked.
- No github.com repo pages were fetched (the budget went to searches), so every [U] slug needs the lead's metric check.
