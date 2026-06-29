---
name: 28-education-intelligence-agent
description: Education Intelligence Agent (Chapter 15, Education and Knowledge Agents). Adaptive tutor: tracks mastery and picks next item in the zone of proximal development. Use when: You build a tutor that adapts difficulty to a learner's skill level. Triggers: education, tutor, adaptive learning, curriculum, mastery, edtech, personalized.
---

# Skill 28 — Education Intelligence Agent

*Chapter 15: Education and Knowledge Agents*

## What it does

Adaptive tutor: tracks mastery and picks next item in the zone of proximal development.

## When to use this skill

You build a tutor that adapts difficulty to a learner's skill level.

## When NOT to use

content creation or generic Q&A.

## Inputs required

skills, an item bank (id/skill/difficulty); optional last result

## Triggers / keywords

education, tutor, adaptive learning, curriculum, mastery, edtech, personalized

## Example task

Pick the next exercise after a correct 'loops' answer.

## Techniques (from the book)

POMDP tutor; Bayesian Knowledge Tracing; IRT 2PL placement; ZPD Gaussian curriculum; SM-2 spaced repetition; misconception detection

## Real-world use case (from the book)

LearnPath - adaptive placement raises course completion (52% -> 78%).

## Book reference (official code)

- Chapter 15: Education and Knowledge Agents
- README: [`../../book-repo/chapter15/README.md`](../../book-repo/chapter15/README.md)
- Use case: [`../../book-repo/chapter15/USECASE.md`](../../book-repo/chapter15/USECASE.md)
- Agents notes: [`../../book-repo/chapter15/AGENTS.md`](../../book-repo/chapter15/AGENTS.md)
- Notebook: [`../../book-repo/chapter15/ch15_education_and_knowledge_agents.ipynb`](../../book-repo/chapter15/ch15_education_and_knowledge_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 28_education_intelligence_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(28)   # EducationIntelligenceAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
