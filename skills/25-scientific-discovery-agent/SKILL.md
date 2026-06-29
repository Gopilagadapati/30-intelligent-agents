---
name: 25-scientific-discovery-agent
description: Scientific Discovery Agent (Chapter 13, Healthcare and Scientific Agents). Hypothesis->experiment->evaluate loop over a candidate space (active discovery). Use when: You search a candidate/parameter space using a (simulated) experiment objective. Triggers: discovery, experiment, optimization, materials, active learning, search, hypothesis.
---

# Skill 25 — Scientific Discovery Agent

*Chapter 13: Healthcare and Scientific Agents*

## What it does

Hypothesis->experiment->evaluate loop over a candidate space (active discovery).

## When to use this skill

You search a candidate/parameter space using a (simulated) experiment objective.

## When NOT to use

literature review (use Scientific Research Agent).

## Inputs required

candidate list, an objective function, a budget

## Triggers / keywords

discovery, experiment, optimization, materials, active learning, search, hypothesis

## Example task

Find the material parameters maximizing conductivity.

## Techniques (from the book)

fault-tolerant multi-source literature scanning; knowledge-gap detection; abductive hypothesis generation; closed-loop experimental feedback

## Real-world use case (from the book)

NovaMateria Labs - finds cross-disciplinary polymer breakthroughs faster.

## Book reference (official code)

- Chapter 13: Healthcare and Scientific Agents
- README: [`../../book-repo/chapter13/README.md`](../../book-repo/chapter13/README.md)
- Use case: [`../../book-repo/chapter13/USECASE.md`](../../book-repo/chapter13/USECASE.md)
- Agents notes: [`../../book-repo/chapter13/AGENTS.md`](../../book-repo/chapter13/AGENTS.md)
- Notebook: [`../../book-repo/chapter13/ch13_healthcare_scientific_agents.ipynb`](../../book-repo/chapter13/ch13_healthcare_scientific_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 25_scientific_discovery_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(25)   # ScientificDiscoveryAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.

> Educational demonstration only — not professional advice.
