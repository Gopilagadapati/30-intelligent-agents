---
name: 26-financial-advisory-agent
description: Financial Advisory Agent (Chapter 14, Financial and Legal Domain Agents). Risk profiling + allocation with compliance/suitability guardrails (educational). Use when: Personalized financial planning framed with risk tolerance + suitability checks. Triggers: finance, investment, portfolio, risk, advisory, allocation, wealth, compliance.
---

# Skill 26 — Financial Advisory Agent

*Chapter 14: Financial and Legal Domain Agents*

## What it does

Risk profiling + allocation with compliance/suitability guardrails (educational).

## When to use this skill

Personalized financial planning framed with risk tolerance + suitability checks.

## When NOT to use

legal questions; this is a demo, not financial advice.

## Inputs required

a client profile dict (age, risk_tolerance, horizon)

## Triggers / keywords

finance, investment, portfolio, risk, advisory, allocation, wealth, compliance

## Example task

Recommend an asset allocation for a 35-year-old.

## Techniques (from the book)

LangGraph StateGraph; supervisor + specialist agents; yfinance/Finnhub/Tavily; composite risk scoring (0.40*vol + 0.35*drawdown + 0.25*VaR); compliance gate

## Real-world use case (from the book)

Meridian Wealth Partners - scales advice while preventing suitability violations.

## Book reference (official code)

- Chapter 14: Financial and Legal Domain Agents
- README: [`../../book-repo/chapter14/README.md`](../../book-repo/chapter14/README.md)
- Use case: [`../../book-repo/chapter14/USECASE.md`](../../book-repo/chapter14/USECASE.md)
- Agents notes: [`../../book-repo/chapter14/AGENTS.md`](../../book-repo/chapter14/AGENTS.md)
- Notebook: [`../../book-repo/chapter14/ch14_financial_legal_agents.ipynb`](../../book-repo/chapter14/ch14_financial_legal_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 26_financial_advisory_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(26)   # FinancialAdvisoryAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.

> Educational demonstration only — not professional advice.
