---
name: 19-vision-language-agent
description: Vision-Language Agent (Chapter 11, Multi-Modal Perception Agents). Answers questions about images by fusing visual perception with language reasoning. Use when: The task involves images / visual question answering. Triggers: vision, image, visual, vqa, multimodal, picture, perception.
---

# Skill 19 — Vision-Language Agent

*Chapter 11: Multi-Modal Perception Agents*

## What it does

Answers questions about images by fusing visual perception with language reasoning.

## When to use this skill

The task involves images / visual question answering.

## When NOT to use

text-only or audio tasks.

## Inputs required

an image id (swap MockVisionEncoder for a real model), a question

## Triggers / keywords

vision, image, visual, vqa, multimodal, picture, perception

## Example task

Is there a pedestrian in this street image?

## Techniques (from the book)

ViT visual encoder; cross-modal attention; LLaVA 1.5; chain-of-thought prompting

## Real-world use case (from the book)

Meridian Facilities - occupancy analysis and after-hours intrusion detection.

## Book reference (official code)

- Chapter 11: Multi-Modal Perception Agents
- README: [`../../book-repo/chapter11/README.md`](../../book-repo/chapter11/README.md)
- Use case: [`../../book-repo/chapter11/USECASE.md`](../../book-repo/chapter11/USECASE.md)
- Agents notes: [`../../book-repo/chapter11/AGENTS.md`](../../book-repo/chapter11/AGENTS.md)
- Notebook: [`../../book-repo/chapter11/ch11_multimodal_agents.ipynb`](../../book-repo/chapter11/ch11_multimodal_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 19_vision_language_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(19)   # VisionLanguageAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
