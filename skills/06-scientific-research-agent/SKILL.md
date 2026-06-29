---
name: 06-scientific-research-agent
description: Scientific Research Agent (Chapter 6, Information Retrieval and Knowledge Agents). Literature review + synthesis + testable hypothesis generation over a paper corpus. Use when: You need to survey literature on a topic and propose research hypotheses. Triggers: research, literature, papers, hypothesis, review, synthesis, science.
---

# Skill 06 — Scientific Research Agent

*Chapter 6: Information Retrieval and Knowledge Agents*

## What it does

Literature review + synthesis + testable hypothesis generation over a paper corpus.

## When to use this skill

You need to survey literature on a topic and propose research hypotheses.

## When NOT to use

running experiments (use Scientific Discovery Agent).

## Inputs required

a list of papers (title+abstract), a research topic

## Triggers / keywords

research, literature, papers, hypothesis, review, synthesis, science

## Example task

Review microbiome papers and propose a testable hypothesis.

## Techniques (from the book)

arXiv search; sentence-transformers; KMeans clustering; thematic synthesis

## Real-world use case (from the book)

Lexington Legal Partners - synthesizes expert reports and finds knowledge gaps.

## Book reference (official code)

- Chapter 6: Information Retrieval and Knowledge Agents
- README: [`../../book-repo/chapter06/README.md`](../../book-repo/chapter06/README.md)
- Use case: [`../../book-repo/chapter06/USECASE.md`](../../book-repo/chapter06/USECASE.md)
- Agents notes: [`../../book-repo/chapter06/AGENTS.md`](../../book-repo/chapter06/AGENTS.md)
- Notebook: [`../../book-repo/chapter06/ch06_knowledge_agents.ipynb`](../../book-repo/chapter06/ch06_knowledge_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 06_scientific_research_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(6)   # ScientificResearchAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
