---
name: 22-ethical-reasoning-agent
description: Ethical Reasoning Agent (Chapter 12, Ethical and Explainable Agents). Evaluates an action against ethical principles and approves/rejects with reasons. Use when: You must check whether an action is ethically acceptable (value alignment). Triggers: ethics, values, alignment, responsible ai, principles, compliance, harm.
---

# Skill 22 — Ethical Reasoning Agent

*Chapter 12: Ethical and Explainable Agents*

## What it does

Evaluates an action against ethical principles and approves/rejects with reasons.

## When to use this skill

You must check whether an action is ethically acceptable (value alignment).

## When NOT to use

explaining model decisions (use Explainable Agent).

## Inputs required

a proposed action string; optional custom principles

## Triggers / keywords

ethics, values, alignment, responsible ai, principles, compliance, harm

## Example task

Should we sell user location data without consent?

## Techniques (from the book)

deontic logic (obligation/permission/prohibition); IEEE EAD validators; EU AI Act compliance; four-fifths bias rule

## Real-world use case (from the book)

TalentForward - prevents biased hiring and produces compliance evidence.

## Book reference (official code)

- Chapter 12: Ethical and Explainable Agents
- README: [`../../book-repo/chapter12/README.md`](../../book-repo/chapter12/README.md)
- Use case: [`../../book-repo/chapter12/USECASE.md`](../../book-repo/chapter12/USECASE.md)
- Agents notes: [`../../book-repo/chapter12/AGENTS.md`](../../book-repo/chapter12/AGENTS.md)
- Notebook: [`../../book-repo/chapter12/ch12_01_ethical_reasoning_agent.ipynb`](../../book-repo/chapter12/ch12_01_ethical_reasoning_agent.ipynb)

## How to run

```bash
# from the 30agents/ root
python 22_ethical_reasoning_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(22)   # EthicalReasoningAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
