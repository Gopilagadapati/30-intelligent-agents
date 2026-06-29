# Financial Advisory Agent — Context & Usage

**Agent #26 · Chapter 14: Financial and Legal Domain Agents · class `FinancialAdvisoryAgent` · file `26_financial_advisory_agent.py`**

## Chapter context

Agents for regulated industries: compliance-aware financial advisory and citation-grounded legal intelligence (educational only).

## This agent

- **Does:** Risk profiling + allocation with compliance/suitability guardrails (educational).
- **Use when:** Personalized financial planning framed with risk tolerance + suitability checks.
- **Not for:** legal questions; this is a demo, not financial advice.
- **Inputs:** a client profile dict (age, risk_tolerance, horizon)
- **Keywords:** finance, investment, portfolio, risk, advisory, allocation, wealth, compliance
- **Example task:** Recommend an asset allocation for a 35-year-old.

## Techniques (from the book)

LangGraph StateGraph; supervisor + specialist agents; yfinance/Finnhub/Tavily; composite risk scoring (0.40*vol + 0.35*drawdown + 0.25*VaR); compliance gate

## Real-world use case (from the book)

Meridian Wealth Partners - scales advice while preventing suitability violations.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 14 (Financial and Legal Domain Agents) of the mirrored repo:

- README: [`../../book-repo/chapter14/README.md`](../../book-repo/chapter14/README.md)
- Use case: [`../../book-repo/chapter14/USECASE.md`](../../book-repo/chapter14/USECASE.md)
- Agents notes: [`../../book-repo/chapter14/AGENTS.md`](../../book-repo/chapter14/AGENTS.md)
- Notebook: [`../../book-repo/chapter14/ch14_financial_legal_agents.ipynb`](../../book-repo/chapter14/ch14_financial_legal_agents.ipynb)

## Run the built-in demo

```bash
python ../../26_financial_advisory_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(26)   # FinancialAdvisoryAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Recommend an asset allocation for a 35-year-old."
```

> Educational demonstration only — not professional advice.
