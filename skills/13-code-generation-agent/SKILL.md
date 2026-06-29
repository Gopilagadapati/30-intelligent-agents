---
name: 13-code-generation-agent
description: Code-Generation Agent (Chapter 9, Software Development Agents). Synthesizes a function from a spec with a generate->test->repair loop until tests pass. Use when: You need code written/fixed and have unit tests to validate it. Triggers: code, programming, synthesis, tests, debug, repair, developer.
---

# Skill 13 — Code-Generation Agent

*Chapter 9: Software Development Agents*

## What it does

Synthesizes a function from a spec with a generate->test->repair loop until tests pass.

## When to use this skill

You need code written/fixed and have unit tests to validate it.

## When NOT to use

prose generation or tasks without verifiable tests.

## Inputs required

a spec string, a tests callable that asserts on the produced namespace

## Triggers / keywords

code, programming, synthesis, tests, debug, repair, developer

## Example task

Write add(a,b) that passes the provided assertions.

## Techniques (from the book)

LangGraph test-driven generation; generate->test->refine loop; iteration limit

## Real-world use case (from the book)

VaultPay - test-first feature delivery for a fintech platform.

## Book reference (official code)

- Chapter 9: Software Development Agents
- README: [`../../book-repo/chapter09/README.md`](../../book-repo/chapter09/README.md)
- Use case: [`../../book-repo/chapter09/USECASE.md`](../../book-repo/chapter09/USECASE.md)
- Agents notes: [`../../book-repo/chapter09/AGENTS.md`](../../book-repo/chapter09/AGENTS.md)
- Notebook: [`../../book-repo/chapter09/ch09_software_dev_agents.ipynb`](../../book-repo/chapter09/ch09_software_dev_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 13_code_generation_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(13)   # CodeGenerationAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
