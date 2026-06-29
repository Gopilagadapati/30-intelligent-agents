---
name: 30-embodied-intelligence-agent
description: Embodied Intelligence Agent (Chapter 16, Embodied and Physical World Agents). Perception-action loop for navigation/control in a (grid) physical environment. Use when: The task is robotic/embodied control: sense, plan a move, actuate, repeat. Triggers: robotics, embodied, navigation, control, perception-action, motion, grid.
---

# Skill 30 — Embodied Intelligence Agent

*Chapter 16: Embodied and Physical World Agents*

## What it does

Perception-action loop for navigation/control in a (grid) physical environment.

## When to use this skill

The task is robotic/embodied control: sense, plan a move, actuate, repeat.

## When NOT to use

pure information tasks with no physical state.

## Inputs required

obstacles set, a start and goal position

## Triggers / keywords

robotics, embodied, navigation, control, perception-action, motion, grid

## Example task

Navigate a robot around obstacles to a goal cell.

## Techniques (from the book)

four-layer control hierarchy; Unified Constraint Envelope; conservative all() safety fusion; fail-graceful external checks

## Real-world use case (from the book)

ArcticWing Aerial - deterministic go/no-go flight control in winter conditions.

## Book reference (official code)

- Chapter 16: Embodied and Physical World Agents
- README: [`../../book-repo/chapter16/README.md`](../../book-repo/chapter16/README.md)
- Use case: [`../../book-repo/chapter16/USECASE.md`](../../book-repo/chapter16/USECASE.md)
- Agents notes: [`../../book-repo/chapter16/AGENTS.md`](../../book-repo/chapter16/AGENTS.md)
- Notebook: [`../../book-repo/chapter16/ch16_embodied_agents.ipynb`](../../book-repo/chapter16/ch16_embodied_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 30_embodied_intelligence_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(30)   # EmbodiedIntelligenceAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
