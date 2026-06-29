---
name: 29-collective-intelligence-agent
description: Collective Intelligence Agent (Chapter 15, Education and Knowledge Agents). Aggregates multiple agents' votes into a confidence-weighted consensus. Use when: You want robustness via ensemble/consensus across several agents or models. Triggers: consensus, ensemble, voting, multi-agent, collective, aggregation, swarm.
---

# Skill 29 — Collective Intelligence Agent

*Chapter 15: Education and Knowledge Agents*

## What it does

Aggregates multiple agents' votes into a confidence-weighted consensus.

## When to use this skill

You want robustness via ensemble/consensus across several agents or models.

## When NOT to use

single-perspective tasks.

## Inputs required

a list of Voter agents, a question

## Triggers / keywords

consensus, ensemble, voting, multi-agent, collective, aggregation, swarm

## Example task

Decide loan approval by majority of weighted voters.

## Techniques (from the book)

propose/critique/synthesize; weighted consensus; adversarial critic rotation; cross-pollination

## Real-world use case (from the book)

LearnPath - builds grading rubrics via multi-agent consensus.

## Book reference (official code)

- Chapter 15: Education and Knowledge Agents
- README: [`../../book-repo/chapter15/README.md`](../../book-repo/chapter15/README.md)
- Use case: [`../../book-repo/chapter15/USECASE.md`](../../book-repo/chapter15/USECASE.md)
- Agents notes: [`../../book-repo/chapter15/AGENTS.md`](../../book-repo/chapter15/AGENTS.md)
- Notebook: [`../../book-repo/chapter15/ch15_education_and_knowledge_agents.ipynb`](../../book-repo/chapter15/ch15_education_and_knowledge_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 29_collective_intelligence_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(29)   # CollectiveIntelligenceAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
