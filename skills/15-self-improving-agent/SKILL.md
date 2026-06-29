---
name: 15-self-improving-agent
description: Self-Improving Agent (Chapter 9, Software Development Agents). Adapts future answers from user feedback (online learning of style/lessons). Use when: You want behavior to improve over time from ratings/feedback. Triggers: learning, feedback, adaptive, improve, online learning, rlhf.
---

# Skill 15 — Self-Improving Agent

*Chapter 9: Software Development Agents*

## What it does

Adapts future answers from user feedback (online learning of style/lessons).

## When to use this skill

You want behavior to improve over time from ratings/feedback.

## When NOT to use

static, one-off responses with no feedback loop.

## Inputs required

a question; feedback via give_feedback()

## Triggers / keywords

learning, feedback, adaptive, improve, online learning, rlhf

## Example task

Give more detailed answers after a low rating.

## Techniques (from the book)

execute->observe->learn->adapt; critic/planner/learning layers; rollback

## Real-world use case (from the book)

VaultPay - improves support chatbot resolution rate over time.

## Book reference (official code)

- Chapter 9: Software Development Agents
- README: [`../../book-repo/chapter09/README.md`](../../book-repo/chapter09/README.md)
- Use case: [`../../book-repo/chapter09/USECASE.md`](../../book-repo/chapter09/USECASE.md)
- Agents notes: [`../../book-repo/chapter09/AGENTS.md`](../../book-repo/chapter09/AGENTS.md)
- Notebook: [`../../book-repo/chapter09/ch09_software_dev_agents.ipynb`](../../book-repo/chapter09/ch09_software_dev_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 15_self_improving_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(15)   # SelfImprovingAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
