---
name: 03-memory-augmented-agent
description: Memory-Augmented Agent (Chapter 5, Foundational Cognitive Architectures). Answers using working, episodic and semantic memory to personalize and stay consistent. Use when: The task needs recall of prior facts/interactions or personalization across turns. Triggers: memory, recall, personalization, history, context retention.
---

# Skill 03 — Memory-Augmented Agent

*Chapter 5: Foundational Cognitive Architectures*

## What it does

Answers using working, episodic and semantic memory to personalize and stay consistent.

## When to use this skill

The task needs recall of prior facts/interactions or personalization across turns.

## When NOT to use

stateless one-off questions with no prior context.

## Inputs required

a user message; pre-loaded facts via remember_fact()

## Triggers / keywords

memory, recall, personalization, history, context retention

## Example task

Answer a patient question while remembering their penicillin allergy.

## Techniques (from the book)

working/episodic/semantic memory; vector-similarity retrieval

## Real-world use case (from the book)

ConnectWave Telecom - remembers prior calls, fixes, and customer history.

## Book reference (official code)

- Chapter 5: Foundational Cognitive Architectures
- README: [`../../book-repo/chapter05/README.md`](../../book-repo/chapter05/README.md)
- Use case: [`../../book-repo/chapter05/USECASE.md`](../../book-repo/chapter05/USECASE.md)
- Agents notes: [`../../book-repo/chapter05/AGENTS.md`](../../book-repo/chapter05/AGENTS.md)
- Notebook: [`../../book-repo/chapter05/ch05_foundational_architectures.ipynb`](../../book-repo/chapter05/ch05_foundational_architectures.ipynb)

## How to run

```bash
# from the 30agents/ root
python 03_memory_augmented_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(3)   # MemoryAugmentedAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
