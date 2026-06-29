# Legal Intelligence Agent — Context & Usage

**Agent #27 · Chapter 14: Financial and Legal Domain Agents · class `LegalIntelligenceAgent` · file `27_legal_intelligence_agent.py`**

## Chapter context

Agents for regulated industries: compliance-aware financial advisory and citation-grounded legal intelligence (educational only).

## This agent

- **Does:** Answers only from cited authority (hallucination-proof) over a legal corpus.
- **Use when:** Legal/contract questions that must be grounded in cited clauses/precedent.
- **Not for:** creative drafting or non-legal Q&A.
- **Inputs:** a corpus of {text, cite}, a question
- **Keywords:** legal, law, contract, clause, citation, precedent, compliance
- **Example task:** How can this contract be terminated? (cite the clause)

## Techniques (from the book)

hybrid retrieval; authority-weighted ranking (0.5 similarity + 0.3 authority + 0.2 recency); issue extraction; citation-verification gate

## Real-world use case (from the book)

Cartwright Legal Group - speeds research and blocks fabricated citations.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 14 (Financial and Legal Domain Agents) of the mirrored repo:

- README: [`../../book-repo/chapter14/README.md`](../../book-repo/chapter14/README.md)
- Use case: [`../../book-repo/chapter14/USECASE.md`](../../book-repo/chapter14/USECASE.md)
- Agents notes: [`../../book-repo/chapter14/AGENTS.md`](../../book-repo/chapter14/AGENTS.md)
- Notebook: [`../../book-repo/chapter14/ch14_financial_legal_agents.ipynb`](../../book-repo/chapter14/ch14_financial_legal_agents.ipynb)

## Run the built-in demo

```bash
python ../../27_legal_intelligence_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(27)   # LegalIntelligenceAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "How can this contract be terminated? (cite the clause)"
```

> Educational demonstration only — not professional advice.
