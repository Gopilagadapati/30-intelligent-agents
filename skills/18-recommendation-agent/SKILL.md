---
name: 18-recommendation-agent
description: Recommendation Agent (Chapter 10, Conversational and Content Creation Agents). Hybrid recommender (content + popularity) with LLM-explained suggestions. Use when: You need to recommend items from a catalog given a user profile/preferences. Triggers: recommendation, recommender, personalization, ranking, suggest, catalog.
---

# Skill 18 — Recommendation Agent

*Chapter 10: Conversational and Content Creation Agents*

## What it does

Hybrid recommender (content + popularity) with LLM-explained suggestions.

## When to use this skill

You need to recommend items from a catalog given a user profile/preferences.

## When NOT to use

open-ended generation; it ranks existing items.

## Inputs required

a catalog (item->description), optional popularity, a user profile

## Triggers / keywords

recommendation, recommender, personalization, ranking, suggest, catalog

## Example task

Recommend books to a sci-fi fan and explain why.

## Techniques (from the book)

hybrid recommender (content-based + collaborative/popularity); preference modeling; explanation generation

## Real-world use case (from the book)

MindBridge Health - personalized content/resource recommendations.

## Book reference (official code)

- Chapter 10: Conversational and Content Creation Agents
- README: [`../../book-repo/chapter10/README.md`](../../book-repo/chapter10/README.md)
- Use case: [`../../book-repo/chapter10/USECASE.md`](../../book-repo/chapter10/USECASE.md)
- Agents notes: [`../../book-repo/chapter10/AGENTS.md`](../../book-repo/chapter10/AGENTS.md)
- Notebook: [`../../book-repo/chapter10/ch10_conversational_and_content_creation_agents.ipynb`](../../book-repo/chapter10/ch10_conversational_and_content_creation_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 18_recommendation_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(18)   # RecommendationAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
