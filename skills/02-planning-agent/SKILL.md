---
name: 02-planning-agent
description: Planning Agent (Chapter 5, Foundational Cognitive Architectures). Decomposes a goal into an ordered plan using tree-of-thought evaluation of alternatives. Use when: You need an explicit, ordered breakdown of a complex goal into sub-tasks before execution. Triggers: plan, decompose, subtasks, tree-of-thought, strategy, breakdown.
---

# Skill 02 — Planning Agent

*Chapter 5: Foundational Cognitive Architectures*

## What it does

Decomposes a goal into an ordered plan using tree-of-thought evaluation of alternatives.

## When to use this skill

You need an explicit, ordered breakdown of a complex goal into sub-tasks before execution.

## When NOT to use

executing the steps (it only plans), or trivial single-step tasks.

## Inputs required

a goal string

## Triggers / keywords

plan, decompose, subtasks, tree-of-thought, strategy, breakdown

## Example task

Break 'launch a predictive-maintenance pilot' into ordered steps.

## Techniques (from the book)

hierarchical task decomposition; phased task trees; adaptive replanning

## Real-world use case (from the book)

ConnectWave Telecom - orchestrates multi-step fiber migration and monitoring.

## Book reference (official code)

- Chapter 5: Foundational Cognitive Architectures
- README: [`../../book-repo/chapter05/README.md`](../../book-repo/chapter05/README.md)
- Use case: [`../../book-repo/chapter05/USECASE.md`](../../book-repo/chapter05/USECASE.md)
- Agents notes: [`../../book-repo/chapter05/AGENTS.md`](../../book-repo/chapter05/AGENTS.md)
- Notebook: [`../../book-repo/chapter05/ch05_foundational_architectures.ipynb`](../../book-repo/chapter05/ch05_foundational_architectures.ipynb)

## How to run

```bash
# from the 30agents/ root
python 02_planning_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(2)   # PlanningAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
