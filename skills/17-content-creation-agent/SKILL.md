---
name: 17-content-creation-agent
description: Content Creation Agent (Chapter 10, Conversational and Content Creation Agents). Outline->draft->multi-format adaptation (blog, social, email) from one brief. Use when: You need marketing/content copy generated and adapted to multiple formats. Triggers: content, writing, copywriting, marketing, blog, social, creative.
---

# Skill 17 — Content Creation Agent

*Chapter 10: Conversational and Content Creation Agents*

## What it does

Outline->draft->multi-format adaptation (blog, social, email) from one brief.

## When to use this skill

You need marketing/content copy generated and adapted to multiple formats.

## When NOT to use

factual retrieval or data analysis.

## Inputs required

a content brief, target formats

## Triggers / keywords

content, writing, copywriting, marketing, blog, social, creative

## Example task

Announce a new app as a blog post and a social post.

## Techniques (from the book)

SMPA (Sense-Model-Plan-Act); CSP brand constraints; EditorAgent; CTR/analytics feedback

## Real-world use case (from the book)

MindBridge Health - brand/compliance-safe campus marketing content.

## Book reference (official code)

- Chapter 10: Conversational and Content Creation Agents
- README: [`../../book-repo/chapter10/README.md`](../../book-repo/chapter10/README.md)
- Use case: [`../../book-repo/chapter10/USECASE.md`](../../book-repo/chapter10/USECASE.md)
- Agents notes: [`../../book-repo/chapter10/AGENTS.md`](../../book-repo/chapter10/AGENTS.md)
- Notebook: [`../../book-repo/chapter10/ch10_conversational_and_content_creation_agents.ipynb`](../../book-repo/chapter10/ch10_conversational_and_content_creation_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 17_content_creation_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(17)   # ContentCreationAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
