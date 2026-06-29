---
name: 31-domain-transforming-integration-agent
description: Domain-Transforming Integration Agent (Chapter 16, Embodied and Physical World Agents). Cross-domain analogy: transfers patterns from one field to solve a problem in another. Use when: You want novel solutions by borrowing patterns across domains (biomimicry, etc.). Triggers: cross-domain, analogy, synthesis, innovation, biomimicry, transfer, integration.
---

# Skill 31 — Domain-Transforming Integration Agent

*Chapter 16: Embodied and Physical World Agents*

## What it does

Cross-domain analogy: transfers patterns from one field to solve a problem in another.

## When to use this skill

You want novel solutions by borrowing patterns across domains (biomimicry, etc.).

## When NOT to use

straightforward single-domain tasks.

## Inputs required

a map of domain->patterns, a problem, a target domain

## Triggers / keywords

cross-domain, analogy, synthesis, innovation, biomimicry, transfer, integration

## Example task

Use ant-colony routing to balance data-center load.

## Techniques (from the book)

typed knowledge graph; weighted breadth-first influence propagation; cross-domain cascade analysis; constraint assembler

## Real-world use case (from the book)

ArcticWing Aerial - detects a power outage blocks road access to a flight site.

## Book reference (official code)

- Chapter 16: Embodied and Physical World Agents
- README: [`../../book-repo/chapter16/README.md`](../../book-repo/chapter16/README.md)
- Use case: [`../../book-repo/chapter16/USECASE.md`](../../book-repo/chapter16/USECASE.md)
- Agents notes: [`../../book-repo/chapter16/AGENTS.md`](../../book-repo/chapter16/AGENTS.md)
- Notebook: [`../../book-repo/chapter16/ch16_embodied_agents.ipynb`](../../book-repo/chapter16/ch16_embodied_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 31_domain_transforming_integration_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(31)   # DomainTransformingIntegrationAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
