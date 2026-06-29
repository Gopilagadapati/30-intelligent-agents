---
name: 11-verification-validation-agent
description: Verification and Validation Agent (Chapter 8, Data Analysis and Reasoning Agents). Splits a statement into claims and checks each against a knowledge base (fact-checking). Use when: You need to verify factual consistency of a statement against trusted evidence. Triggers: verification, validation, fact-check, factual, factually, consistency, claim, claims, accurate, correct, verify, truth, audit.
---

# Skill 11 — Verification and Validation Agent

*Chapter 8: Data Analysis and Reasoning Agents*

## What it does

Splits a statement into claims and checks each against a knowledge base (fact-checking).

## When to use this skill

You need to verify factual consistency of a statement against trusted evidence.

## When NOT to use

generating new content; it only validates.

## Inputs required

a knowledge base (list of facts), a statement to verify

## Triggers / keywords

verification, validation, fact-check, factual, factually, consistency, claim, claims, accurate, correct, verify, truth, audit

## Example task

Verify 'The Eiffel Tower is in Paris; built 1889.'

## Techniques (from the book)

claim extraction; trusted-DB retrieval; BART-MNLI NLI; confidence scoring; source comparison

## Real-world use case (from the book)

CanadaFirst News - fact-checks statistical claims before publication.

## Book reference (official code)

- Chapter 8: Data Analysis and Reasoning Agents
- README: [`../../book-repo/chapter08/README.md`](../../book-repo/chapter08/README.md)
- Use case: [`../../book-repo/chapter08/USECASE.md`](../../book-repo/chapter08/USECASE.md)
- Agents notes: [`../../book-repo/chapter08/AGENTS.md`](../../book-repo/chapter08/AGENTS.md)
- Notebook: [`../../book-repo/chapter08/ch08_data_analysis_reasoning_agents.ipynb`](../../book-repo/chapter08/ch08_data_analysis_reasoning_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 11_verification_validation_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(11)   # VerificationValidationAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
