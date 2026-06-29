---
name: 01-autonomous-decision-agent
description: Autonomous Decision-Making Agent (Chapter 5, Foundational Cognitive Architectures). Runs a perceive->reason->act loop, independently choosing the next action until a goal is met. Use when: You have a goal and a discrete set of possible actions, and want the agent to drive itself with minimal human steps. Triggers: autonomy, loop, act, decision, goal-directed, self-driving.
---

# Skill 01 — Autonomous Decision-Making Agent

*Chapter 5: Foundational Cognitive Architectures*

## What it does

Runs a perceive->reason->act loop, independently choosing the next action until a goal is met.

## When to use this skill

You have a goal and a discrete set of possible actions, and want the agent to drive itself with minimal human steps.

## When NOT to use

single-shot Q&A, or when you need a multi-step ordered plan up front (use the Planning Agent).

## Inputs required

a goal string, a list of available actions

## Triggers / keywords

autonomy, loop, act, decision, goal-directed, self-driving

## Example task

Keep taking actions until a project proposal is produced.

## Techniques (from the book)

perceive->reason->act loop; strategy scoring; dependency-aware task DAGs; escalation thresholds

## Real-world use case (from the book)

ConnectWave Telecom - context-aware support decisions (outage/billing routing).

## Book reference (official code)

- Chapter 5: Foundational Cognitive Architectures
- README: [`../../book-repo/chapter05/README.md`](../../book-repo/chapter05/README.md)
- Use case: [`../../book-repo/chapter05/USECASE.md`](../../book-repo/chapter05/USECASE.md)
- Agents notes: [`../../book-repo/chapter05/AGENTS.md`](../../book-repo/chapter05/AGENTS.md)
- Notebook: [`../../book-repo/chapter05/ch05_foundational_architectures.ipynb`](../../book-repo/chapter05/ch05_foundational_architectures.ipynb)

## How to run

```bash
# from the 30agents/ root
python 01_autonomous_decision_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(1)   # AutonomousDecisionAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
