"""Generate one skill per agent (31 skills) from the agent catalog.

For each agent this writes:
  skills/NN-<agent-slug>/SKILL.md               - skill definition + when to use
  skills/NN-<agent-slug>/CONTEXT_AND_USAGE.md   - chapter context + usage details
and a skills/README.md index grouped by chapter.

Run:  python generate_skills.py
"""
from __future__ import annotations

from pathlib import Path

from catalog import CATALOG, TECHNIQUES, USE_CASES, reference

ROOT = Path(__file__).resolve().parent
SKILLS = ROOT / "skills"

# Chapter-level context (title + concept) embedded into each agent's skill.
CHAPTERS = {
    5: ("Foundational Cognitive Architectures",
        "The core building-block agents every other agent composes from: an autonomous "
        "perceive-reason-act loop, explicit planning, and working/episodic/semantic memory."),
    6: ("Information Retrieval and Knowledge Agents",
        "Agents that ground an LLM in external information via advanced RAG, document "
        "intelligence pipelines, and scientific literature review."),
    7: ("Tool Manipulation and Orchestration Agents",
        "Agents that take action and coordinate others: tool/function calling, chain-of-"
        "agents orchestration, and human-in-the-loop workflows."),
    8: ("Data Analysis and Reasoning Agents",
        "Agents specialized in analyzing data and reasoning: data exploration, fact "
        "verification, and a domain-agnostic problem solver."),
    9: ("Software Development Agents",
        "Agents that build and safeguard software: program synthesis with tests, prompt-"
        "injection defense, and learning from feedback."),
    10: ("Conversational and Content Creation Agents",
         "Agents that manage dialog and generate content: persona-driven conversation, "
         "multi-format content creation, and hybrid recommendation."),
    11: ("Multi-Modal Perception Agents",
         "Agents that perceive non-text inputs: vision-language, audio/speech, and IoT "
         "physical-world sensing."),
    12: ("Ethical and Explainable Agents",
         "Agents that make AI trustworthy: ethical value-alignment and explainable "
         "decisioning. Prerequisites for the regulated-domain chapters."),
    13: ("Healthcare and Scientific Agents",
         "Domain agents for biomedical research and care: Bayesian clinical decision "
         "support and hypothesis-driven scientific discovery (educational only)."),
    14: ("Financial and Legal Domain Agents",
         "Agents for regulated industries: compliance-aware financial advisory and "
         "citation-grounded legal intelligence (educational only)."),
    15: ("Education and Knowledge Agents",
         "Agents for learning and collective reasoning: adaptive tutoring and multi-agent "
         "consensus."),
    16: ("Embodied and Physical World Agents",
         "Agents that bridge digital intelligence and the physical world: embodied "
         "perception-action control and cross-domain integration."),
}


def slug(spec) -> str:
    # 01_autonomous_decision_agent.py -> autonomous-decision-agent
    stem = spec.file[:-3]                      # drop .py
    stem = stem.split("_", 1)[1]               # drop leading NN_
    return stem.replace("_", "-")


def folder_name(spec) -> str:
    return f"{spec.num:02d}-{slug(spec)}"


def skill_md(spec) -> str:
    ch_title, ch_ctx = CHAPTERS[spec.chapter]
    desc = (
        f"{spec.name} (Chapter {spec.chapter}, {ch_title}). {spec.capability} "
        f"Use when: {spec.use_when} Triggers: {', '.join(spec.keywords)}."
    )
    L = []
    L.append("---")
    L.append(f"name: {folder_name(spec)}")
    L.append(f"description: {desc}")
    L.append("---")
    L.append("")
    L.append(f"# Skill {spec.num:02d} — {spec.name}")
    L.append("")
    L.append(f"*Chapter {spec.chapter}: {ch_title}*")
    L.append("")
    L.append("## What it does")
    L.append("")
    L.append(spec.capability)
    L.append("")
    L.append("## When to use this skill")
    L.append("")
    L.append(spec.use_when)
    L.append("")
    L.append("## When NOT to use")
    L.append("")
    L.append(spec.not_for)
    L.append("")
    L.append("## Inputs required")
    L.append("")
    L.append(spec.inputs)
    L.append("")
    L.append("## Triggers / keywords")
    L.append("")
    L.append(", ".join(spec.keywords))
    L.append("")
    L.append("## Example task")
    L.append("")
    L.append(spec.example_task)
    L.append("")
    L.append("## Techniques (from the book)")
    L.append("")
    L.append(TECHNIQUES[spec.num])
    L.append("")
    L.append("## Real-world use case (from the book)")
    L.append("")
    L.append(USE_CASES[spec.num])
    L.append("")
    ref = reference(spec.num, prefix="../../book-repo")
    L.append("## Book reference (official code)")
    L.append("")
    L.append(f"- Chapter {ref['chapter']}: {ref['chapter_title']}")
    L.append(f"- README: [`{ref['readme']}`]({ref['readme']})")
    L.append(f"- Use case: [`{ref['usecase']}`]({ref['usecase']})")
    L.append(f"- Agents notes: [`{ref['agents_md']}`]({ref['agents_md']})")
    L.append(f"- Notebook: [`{ref['notebook']}`]({ref['notebook']})")
    L.append("")
    L.append("## How to run")
    L.append("")
    L.append("```bash")
    L.append("# from the 30agents/ root")
    L.append(f"python {spec.file}                 # built-in demo")
    L.append('python meta_agent.py "<your task>"  # let the router pick this skill')
    L.append("```")
    L.append("")
    L.append("```python")
    L.append("import sys; sys.path.append('../..')   # path to 30agents/ root")
    L.append("from meta_agent import MetaAgent")
    L.append(f"AgentClass = MetaAgent.load({spec.num})   # {spec.cls}")
    L.append("# construct with the inputs above, then call .run(...)")
    L.append("```")
    L.append("")
    L.append("See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.")
    L.append("")
    if spec.chapter in (13, 14):
        L.append("> Educational demonstration only — not professional advice.")
        L.append("")
    return "\n".join(L)


def usage_md(spec) -> str:
    ch_title, ch_ctx = CHAPTERS[spec.chapter]
    L = []
    L.append(f"# {spec.name} — Context & Usage")
    L.append("")
    L.append(f"**Agent #{spec.num} · Chapter {spec.chapter}: {ch_title} · "
             f"class `{spec.cls}` · file `{spec.file}`**")
    L.append("")
    L.append("## Chapter context")
    L.append("")
    L.append(ch_ctx)
    L.append("")
    L.append("## This agent")
    L.append("")
    L.append(f"- **Does:** {spec.capability}")
    L.append(f"- **Use when:** {spec.use_when}")
    L.append(f"- **Not for:** {spec.not_for}")
    L.append(f"- **Inputs:** {spec.inputs}")
    L.append(f"- **Keywords:** {', '.join(spec.keywords)}")
    L.append(f"- **Example task:** {spec.example_task}")
    L.append("")
    L.append("## Techniques (from the book)")
    L.append("")
    L.append(TECHNIQUES[spec.num])
    L.append("")
    L.append("## Real-world use case (from the book)")
    L.append("")
    L.append(USE_CASES[spec.num])
    L.append("")
    ref = reference(spec.num, prefix="../../book-repo")
    L.append("## Book reference (official code)")
    L.append("")
    L.append(f"The authoritative implementation and narrative for this agent live in "
             f"Chapter {ref['chapter']} ({ref['chapter_title']}) of the mirrored repo:")
    L.append("")
    L.append(f"- README: [`{ref['readme']}`]({ref['readme']})")
    L.append(f"- Use case: [`{ref['usecase']}`]({ref['usecase']})")
    L.append(f"- Agents notes: [`{ref['agents_md']}`]({ref['agents_md']})")
    L.append(f"- Notebook: [`{ref['notebook']}`]({ref['notebook']})")
    L.append("")
    L.append("## Run the built-in demo")
    L.append("")
    L.append("```bash")
    L.append(f"python ../../{spec.file}")
    L.append("```")
    L.append("")
    L.append("## Use in code")
    L.append("")
    L.append("```python")
    L.append("import sys; sys.path.append('../..')")
    L.append("from meta_agent import MetaAgent")
    L.append(f"AgentClass = MetaAgent.load({spec.num})   # {spec.cls}")
    L.append("# Provide the Inputs listed above, then:")
    L.append("# result = AgentClass(...).run(...)")
    L.append("# print(result.output)")
    L.append("```")
    L.append("")
    L.append("## Route to this skill automatically")
    L.append("")
    L.append("```bash")
    L.append(f'python ../../meta_agent.py "{spec.example_task}"')
    L.append("```")
    L.append("")
    if spec.chapter in (13, 14):
        L.append("> Educational demonstration only — not professional advice.")
        L.append("")
    return "\n".join(L)


def index_md() -> str:
    L = []
    L.append("# Skills — one per agent (31 total)")
    L.append("")
    L.append("Every agent in the library is packaged as its own **skill**. Each skill "
             "folder contains a `SKILL.md` (definition + when to use) and a "
             "`CONTEXT_AND_USAGE.md` (chapter context + usage details). Point your "
             "assistant at a skill's `SKILL.md` and state your task, or let "
             "`../meta_agent.py` route a task to the right skill automatically.")
    L.append("")
    current = None
    for s in CATALOG:
        if s.chapter != current:
            current = s.chapter
            ch_title, _ = CHAPTERS[s.chapter]
            L.append("")
            L.append(f"## Chapter {s.chapter} — {ch_title}")
            L.append("")
            L.append("| # | Skill | Use when |")
            L.append("|---|-------|----------|")
        L.append(f"| {s.num} | [`{folder_name(s)}`]({folder_name(s)}/SKILL.md) | {s.use_when} |")
    L.append("")
    L.append(f"**Total:** {len(CATALOG)} skills across {len(CHAPTERS)} chapters.")
    L.append("")
    return "\n".join(L)


def main() -> None:
    if SKILLS.exists():
        for p in sorted(SKILLS.rglob("*"), reverse=True):
            p.unlink() if p.is_file() else p.rmdir()
    SKILLS.mkdir(exist_ok=True)
    for s in CATALOG:
        d = SKILLS / folder_name(s)
        d.mkdir(exist_ok=True)
        (d / "SKILL.md").write_text(skill_md(s), encoding="utf-8")
        (d / "CONTEXT_AND_USAGE.md").write_text(usage_md(s), encoding="utf-8")
    (SKILLS / "README.md").write_text(index_md(), encoding="utf-8")
    print(f"Generated {len(CATALOG)} agent skills under {SKILLS}")


if __name__ == "__main__":
    main()
