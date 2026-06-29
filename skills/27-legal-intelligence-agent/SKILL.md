---
name: 27-legal-intelligence-agent
description: Legal Intelligence Agent (Chapter 14, Financial and Legal Domain Agents). Answers only from cited authority (hallucination-proof) over a legal corpus. Use when: Legal/contract questions that must be grounded in cited clauses/precedent. Triggers: legal, law, contract, clause, citation, precedent, compliance.
---

# Skill 27 — Legal Intelligence Agent

*Chapter 14: Financial and Legal Domain Agents*

## What it does

Answers only from cited authority (hallucination-proof) over a legal corpus.

## When to use this skill

Legal/contract questions that must be grounded in cited clauses/precedent.

## When NOT to use

creative drafting or non-legal Q&A.

## Inputs required

a corpus of {text, cite}, a question

## Triggers / keywords

legal, law, contract, clause, citation, precedent, compliance

## Example task

How can this contract be terminated? (cite the clause)

## Techniques (from the book)

hybrid retrieval; authority-weighted ranking (0.5 similarity + 0.3 authority + 0.2 recency); issue extraction; citation-verification gate

## Real-world use case (from the book)

Cartwright Legal Group - speeds research and blocks fabricated citations.

## Book reference (official code)

- Chapter 14: Financial and Legal Domain Agents
- README: [`../../book-repo/chapter14/README.md`](../../book-repo/chapter14/README.md)
- Use case: [`../../book-repo/chapter14/USECASE.md`](../../book-repo/chapter14/USECASE.md)
- Agents notes: [`../../book-repo/chapter14/AGENTS.md`](../../book-repo/chapter14/AGENTS.md)
- Notebook: [`../../book-repo/chapter14/ch14_financial_legal_agents.ipynb`](../../book-repo/chapter14/ch14_financial_legal_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 27_legal_intelligence_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(27)   # LegalIntelligenceAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.

> Educational demonstration only — not professional advice.
