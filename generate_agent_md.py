"""Generate agents/AGENT.md (the MetaAgent instruction file) from the catalog.

The file is enriched from the official book code mirrored under book-repo/:
each agent entry carries the concrete Techniques, a Real-world use case, and
links into the relevant chapter README / USECASE / notebook.

Run:  python generate_agent_md.py
"""
from __future__ import annotations

from pathlib import Path

from catalog import (
    CATALOG,
    CHAPTER_TITLES,
    TECHNIQUES,
    USE_CASES,
    by_number,
    reference,
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "agents" / "AGENT.md"

# AGENT.md lives in agents/, so links into the repo mirror are one level up.
REF_PREFIX = "../book-repo"

EDU_CHAPTERS = {13, 14}


def header() -> str:
    return """# AGENT.md — The 30-Agents MetaAgent

> Single entry point to a library of **31 specialized agents** (from *30 Intelligent
> Agents Every AI Engineer Should Know*, Packt 2026). Point your assistant at this
> file, then state your task. The agent uses the **context of usage** below to pick
> the right specialist, gather the inputs it needs, and run it.

---

## Role

You are the **MetaAgent**. You do not solve every task yourself — you **route** each
request to the best-fit specialized agent in the catalog, then orchestrate its
execution. Always:

1. **Understand the task** the user states.
2. **Select** the single best agent using the `Use when` / `Keywords` fields. If two
   fit, prefer the more specific one; respect each agent's `Not for` anti-signals.
3. **Check inputs**: confirm you have what the chosen agent's `Inputs` requires; ask
   the user only for what is missing.
4. **Run** it (see *How to run* below) and return the result plus which agent was used
   and why. Offer 1–2 alternatives when the match is close.
5. For multi-part tasks, chain agents (e.g., Planning -> Tool-Using -> Verification).

All agents run **offline by default** via a built-in `MockLLM` (no API key). Set
`OPENAI_API_KEY` or `ANTHROPIC_API_KEY` to use a live model.

---

## How to use this file

**Option A — let the router pick (recommended):**
```bash
python meta_agent.py "<your task in plain English>"
```
It prints the chosen agent, its `Use when`, required `Inputs`, and alternatives.

**Option B — call a specific agent directly:** open its file (column *File*) and run it,
or import its *Class* and call `.run(...)`.

**Option C — route and run in code:**
```python
from meta_agent import MetaAgent
meta = MetaAgent()
best = meta.run("answer questions from our help-center docs").metadata["best"]
AgentClass = MetaAgent.load(best["num"])   # dynamically import the chosen agent
agent = AgentClass(corpus=[...])           # provide the inputs it needs
print(agent.run("What is the refund window?").output)
```

> Paths in this file are relative to the `30agents/` project root (run commands), or
> to this `agents/` folder for the clickable book-reference links (`../book-repo/...`).

---

## Reference material (official book code)

The full, authoritative source for every agent is mirrored under
[`../book-repo/`](../book-repo/) — the official repo
*30-Agents-Every-AI-Engineer-Must-Build* (Packt). Each chapter folder contains:

- `README.md` — chapter narrative and agent walkthrough
- `USECASE.md` — the real-world business scenario the agent solves
- `AGENTS.md` — implementation notes and design decisions
- `chNN_*.ipynb` — the runnable reference notebook (plus per-LLM `__RUN_*` variants)
- `*_core.py`, `mock_llm.py`, `synthetic_data.py` — supporting code

When you need ground-truth detail (exact algorithm, thresholds, prompts), open the
chapter files linked in each agent's **Book reference** below. The local `NN_*.py`
modules in this project are faithful, self-contained re-implementations that run
offline; the notebooks are the canonical originals.

---
"""


def quick_index() -> str:
    L = ["## Quick selection index", "",
         "| # | Agent | Use when | File | Class |",
         "|---|-------|----------|------|-------|"]
    for s in CATALOG:
        L.append(f"| {s.num} | {s.name} | {s.use_when} | `{s.file}` | `{s.cls}` |")
    L.append("")
    L.append("---")
    L.append("")
    return "\n".join(L)


def agent_entry(num: int) -> str:
    s = by_number(num)
    ref = reference(num, prefix=REF_PREFIX)
    L = []
    L.append(f"### {s.num}. {s.name}  (Chapter {s.chapter} — {CHAPTER_TITLES[s.chapter]})")
    L.append("")
    L.append(f"- **Does:** {s.capability}")
    L.append(f"- **Use when:** {s.use_when}")
    L.append(f"- **Inputs:** {s.inputs}")
    L.append(f"- **Not for:** {s.not_for}")
    L.append(f"- **Keywords:** {', '.join(s.keywords)}")
    L.append(f"- **Example task:** {s.example_task}")
    L.append(f"- **Techniques (book):** {TECHNIQUES[num]}")
    L.append(f"- **Real-world use case:** {USE_CASES[num]}")
    L.append(f"- **Run:** `python {s.file}`  ·  class `{s.cls}`")
    L.append(f"- **Book reference:** "
             f"[README]({ref['readme']}) · "
             f"[USECASE]({ref['usecase']}) · "
             f"[AGENTS]({ref['agents_md']}) · "
             f"[notebook]({ref['notebook']})")
    if num in EDU_CHAPTERS or s.chapter in EDU_CHAPTERS:
        L.append("- > Educational demonstration only — not professional advice.")
    L.append("")
    return "\n".join(L)


def footer() -> str:
    return """---

## Notes

- The Healthcare, Financial, and Legal agents are **educational demonstrations only**,
  not professional advice.
- Vision/Audio agents use mock encoders; swap in CLIP/Whisper/GPT-4o-vision for production.
- Run the whole suite with `python run_all.py` (expect `31/31 agents passed`).
- Every agent is also packaged as a standalone skill under
  [`../skills/`](../skills/), and the official source notebooks live under
  [`../book-repo/`](../book-repo/).
"""


def build() -> str:
    parts = [header(), "", quick_index(),
             "## Agent reference (full context of usage)", ""]
    for s in CATALOG:
        parts.append(agent_entry(s.num))
    parts.append(footer())
    return "\n".join(parts)


def main() -> None:
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(build(), encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
