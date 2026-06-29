---
name: 23-explainable-agent
description: Explainable Agent (Chapter 12, Ethical and Explainable Agents). Makes a weighted decision and explains it with factor attributions + a counterfactual. Use when: A decision needs transparency: which factors drove it and what would flip it. Triggers: explainability, transparency, shap, lime, attribution, counterfactual, interpretability.
---

# Skill 23 — Explainable Agent

*Chapter 12: Ethical and Explainable Agents*

## What it does

Makes a weighted decision and explains it with factor attributions + a counterfactual.

## When to use this skill

A decision needs transparency: which factors drove it and what would flip it.

## When NOT to use

ethical acceptability judgments (use Ethical Reasoning).

## Inputs required

feature weights, a feature dict

## Triggers / keywords

explainability, transparency, shap, lime, attribution, counterfactual, interpretability

## Example task

Explain why a loan was approved/denied.

## Techniques (from the book)

LIME; SHAP; counterfactual analysis; confidence calibration (temperature scaling); audience-adapted explanations

## Real-world use case (from the book)

ClearPath Health - explains clinical predictions so doctors trust them.

## Book reference (official code)

- Chapter 12: Ethical and Explainable Agents
- README: [`../../book-repo/chapter12/README.md`](../../book-repo/chapter12/README.md)
- Use case: [`../../book-repo/chapter12/USECASE.md`](../../book-repo/chapter12/USECASE.md)
- Agents notes: [`../../book-repo/chapter12/AGENTS.md`](../../book-repo/chapter12/AGENTS.md)
- Notebook: [`../../book-repo/chapter12/ch12_02_explainable_agent.ipynb`](../../book-repo/chapter12/ch12_02_explainable_agent.ipynb)

## How to run

```bash
# from the 30agents/ root
python 23_explainable_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(23)   # ExplainableAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
