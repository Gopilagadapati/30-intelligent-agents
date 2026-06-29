# 30 Agents

[![CI](https://github.com/Gopilagadapati/30-intelligent-agents/actions/workflows/ci.yml/badge.svg)](https://github.com/Gopilagadapati/30-intelligent-agents/actions/workflows/ci.yml)

Runnable Python implementations of the **31 agent architectures** from the book
*30 Intelligent Agents Every AI Engineer Should Know* (Imran Ahmad, PhD — Packt, 2026),
spanning Chapters 5–16.

Each agent is a **self-contained module** that captures the book's architectural
pattern (cognitive loop, planning, memory, RAG, tool-calling, orchestration,
multi-modal perception, ethics/explainability, and domain-specific reasoning).

## Zero-setup / Simulation Mode

Every agent ships with a deterministic **`MockLLM`**, so they run with **no API
key and no network access** — mirroring the book's "Simulation Mode". If you set
`OPENAI_API_KEY` or `ANTHROPIC_API_KEY` (and install the SDK), `common.get_llm`
automatically routes to the live provider instead.

```bash
# Run any single agent's demo
python 01_autonomous_decision_agent.py

# Run all 31 agents and get a pass/fail report
python run_all.py
```

Requires only **Python 3.10+** (standard library). No third-party packages.

## Official book repository (full reference)

The complete official code from the book is mirrored under **`book-repo/`** for
reference (source: <https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build>).
It contains everything from the upstream repo *except* the `.git` history and a
stray 61 MB Git installer `.exe`:

- `book-repo/chapter01` … `chapter17` — per-chapter `README.md`, `USECASE.md`,
  five pre-executed notebook variants, reference `.py` modules, and
  `requirements*.txt` / `.env.template` files.
- `book-repo/supporting`, `book-repo/Errata`, `ERRATA.md`,
  `LLM_COMPARISON_SUMMARY.md`, `outline.docx`, `LICENSE`, `README.md`.

This is the authoritative source material. The agent modules in this folder
(`01_…`–`31_…`) are original, compact re-implementations of the same architectural
patterns; consult `book-repo/` for the book's full notebooks, use cases, and
provider-specific code.

## The MetaAgent — one agent built out of all 31

`meta_agent.py` is a single agent that **knows the context of usage of every
agent** (defined in `catalog.py`) and decides **which agent to use** for a task.

**`AGENT.md`** (in [`agents/AGENT.md`](agents/AGENT.md)) is the human/LLM-readable
version of that same knowledge: point any assistant at it, state your task, and it
has everything needed to pick the right agent, gather inputs, and run it. It contains
the role/routing rules, a quick selection index, and the full context-of-usage for
all 31 agents — each entry enriched with the **Techniques**, **real-world use case**,
and **links into `book-repo/`** (chapter README / USECASE / notebook) drawn from the
official book code. Regenerate it from the catalog with `python generate_agent_md.py`.

For each agent the catalog records: capability, **use-when** (the context of
usage), required inputs, anti-signals (`not_for`), keywords and an example task.

```bash
# Ask which agent to use for a task
python meta_agent.py "extract the total and date from this invoice"
#   -> #5 Document Intelligence Agent  (with use-when, inputs, and alternatives)

# No args -> runs a set of demo routings
python meta_agent.py
```

In code you can route **and run** the selected agent:

```python
from meta_agent import MetaAgent
meta = MetaAgent()

result = meta.run("answer questions from our help-center articles")
best = result.metadata["best"]          # {'num':4, 'name':'Knowledge Retrieval Agent', ...}

AgentClass = MetaAgent.load(best["num"])  # dynamically import the chosen agent
agent = AgentClass(corpus=["..."])        # construct with the inputs it needs
agent.run("What is the refund window?")
```

Selection is **fully offline**: it scores each agent by overlap between the task
and the agent's context-of-usage (bag-of-words cosine + keyword boosts), and
adds an LLM-written justification when a provider key is configured.

## Per-agent skills (31)

Every agent is also packaged as its own **skill** under `skills/NN-<agent-slug>/`
(31 skills, grouped by chapter in the index):

- **`SKILL.md`** — skill definition with `name`/`description` frontmatter, the
  agent's chapter context, *when to use* / *when not to use*, required inputs,
  triggers, run/code snippets, the book **Techniques**, real-world **use case**,
  and reference links into `book-repo/`.
- **`CONTEXT_AND_USAGE.md`** — chapter context, full usage detail, book techniques,
  use case, and links to the official chapter README / USECASE / notebook.

See [`skills/README.md`](skills/README.md) for the index. Regenerate them from the
catalog with `python generate_skills.py`.

## Layout

```
30agents/
├── common/                 # shared scaffolding
│   ├── llm.py              # LLM interface + MockLLM + provider routing
│   ├── base.py             # BaseAgent (perceive -> reason -> act cognitive loop)
│   ├── memory.py           # Working / Episodic / Semantic memory
│   └── tools.py            # Tool registry + function-calling
├── catalog.py              # context-of-usage + book techniques/use-cases/refs for all 31 agents
├── meta_agent.py           # MetaAgent: routes a task to the right agent
├── generate_agent_md.py    # regenerates agents/AGENT.md from the catalog
├── generate_skills.py      # regenerates the 31 per-agent skills from the catalog
├── agents/AGENT.md         # MetaAgent instruction file (enriched with book-repo refs)
├── skills/NN-<slug>/       # 31 per-agent skills (SKILL.md + CONTEXT_AND_USAGE.md)
├── book-repo/              # full official book code mirror (chapter01..17)
├── tests/                  # pytest suite (agents, catalog, routing, book refs)
├── 01_…_agent.py … 31_…_agent.py
├── run_all.py              # quick pass/fail runner for all 31 demos
├── pyproject.toml          # project metadata + optional extras + pytest config
├── requirements.txt        # (everything runs offline; only optional extras listed)
├── .gitignore
└── LICENSE                 # MIT, with attribution to the Packt upstream
```

## Development & tests

The repository is self-contained and runs offline. To validate it:

```bash
python run_all.py                 # 31/31 agents pass (no extra deps)

pip install pytest                # or: pip install ".[dev]"
pytest                            # 163 tests: agent demos, catalog integrity,
                                  # routing, and book-reference link checks
```

Regenerate the derived docs after editing `catalog.py`:

```bash
python generate_agent_md.py       # rewrites agents/AGENT.md
python generate_skills.py         # rewrites the 31 skills under skills/
```

`catalog.py` is the **single source of truth** — `AGENT.md` and every skill are
generated from it, so there is no duplicated agent metadata to keep in sync.

## License

MIT (see [`LICENSE`](LICENSE)). The agent patterns, use cases, and the mirrored
`book-repo/` are derived from *30 Intelligent Agents Every AI Engineer Should Know*
(Imran Ahmad, Packt) and its MIT-licensed companion repository, Copyright (c) 2025
Packt. Upstream attribution is retained in `LICENSE` and `book-repo/LICENSE`. The
Healthcare, Financial, and Legal agents are **educational demonstrations only** and
are not professional advice.

## The 31 agents

| # | Ch | Agent | Pattern |
|---|----|-------|---------|
| 1 | 5 | Autonomous Decision-Making Agent | cognitive loop: perceive → reason → act |
| 2 | 5 | Planning Agent | tree-of-thought hierarchical decomposition |
| 3 | 5 | Memory-Augmented Agent | working / episodic / semantic memory |
| 4 | 6 | Knowledge Retrieval Agent | advanced RAG: retrieve → rerank → generate |
| 5 | 6 | Document Intelligence Agent | five-stage document pipeline |
| 6 | 6 | Scientific Research Agent | literature review + hypothesis generation |
| 7 | 7 | Tool-Using Agent | function-calling selection funnel |
| 8 | 7 | Chain-of-Agents Orchestrator | task routing and delegation |
| 9 | 7 | Agentic Workflow System | human-in-the-loop workflow engine |
| 10 | 8 | Data Analysis Agent | profiling + visualization recommendation |
| 11 | 8 | Verification & Validation Agent | factual consistency checking |
| 12 | 8 | General Problem Solver | means-ends analysis search |
| 13 | 9 | Code-Generation Agent | program synthesis with generate-test-repair |
| 14 | 9 | Security-Hardened Agent | prompt-injection defense (defense-in-depth) |
| 15 | 9 | Self-Improving Agent | learning from feedback |
| 16 | 10 | Conversational Agent | dialog management + persona + slots |
| 17 | 10 | Content Creation Agent | outline → draft → multi-format adapt |
| 18 | 10 | Recommendation Agent | hybrid recommender |
| 19 | 11 | Vision-Language Agent | image understanding |
| 20 | 11 | Audio Processing Agent | speech transcription + sentiment |
| 21 | 11 | Physical World Sensing Agent | IoT anomaly detection |
| 22 | 12 | Ethical Reasoning Agent | value-alignment framework |
| 23 | 12 | Explainable Agent | feature attribution + counterfactual |
| 24 | 13 | Healthcare Intelligence Agent | Bayesian clinical decision support |
| 25 | 13 | Scientific Discovery Agent | hypothesis-driven discovery loop |
| 26 | 14 | Financial Advisory Agent | risk profiling + compliance guardrails |
| 27 | 14 | Legal Intelligence Agent | citation-grounded (hallucination-proof) |
| 28 | 15 | Education Intelligence Agent | adaptive learning (ZPD) |
| 29 | 15 | Collective Intelligence Agent | multi-agent consensus |
| 30 | 16 | Embodied Intelligence Agent | perception-action loop (grid navigation) |
| 31 | 16 | Domain-Transforming Integration Agent | cross-domain knowledge synthesis |

> These are original, compact implementations of the *architectural patterns*
> described in the book — intended for learning and as starting points, not as a
> copy of the book's source. The official book code lives at
> https://github.com/PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build
>
> The healthcare, financial, and legal agents are educational demonstrations
> only and are **not** professional advice.
