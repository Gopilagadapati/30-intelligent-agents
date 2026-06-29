# Verification and Validation Agent — Context & Usage

**Agent #11 · Chapter 8: Data Analysis and Reasoning Agents · class `VerificationValidationAgent` · file `11_verification_validation_agent.py`**

## Chapter context

Agents specialized in analyzing data and reasoning: data exploration, fact verification, and a domain-agnostic problem solver.

## This agent

- **Does:** Splits a statement into claims and checks each against a knowledge base (fact-checking).
- **Use when:** You need to verify factual consistency of a statement against trusted evidence.
- **Not for:** generating new content; it only validates.
- **Inputs:** a knowledge base (list of facts), a statement to verify
- **Keywords:** verification, validation, fact-check, factual, factually, consistency, claim, claims, accurate, correct, verify, truth, audit
- **Example task:** Verify 'The Eiffel Tower is in Paris; built 1889.'

## Techniques (from the book)

claim extraction; trusted-DB retrieval; BART-MNLI NLI; confidence scoring; source comparison

## Real-world use case (from the book)

CanadaFirst News - fact-checks statistical claims before publication.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 8 (Data Analysis and Reasoning Agents) of the mirrored repo:

- README: [`../../book-repo/chapter08/README.md`](../../book-repo/chapter08/README.md)
- Use case: [`../../book-repo/chapter08/USECASE.md`](../../book-repo/chapter08/USECASE.md)
- Agents notes: [`../../book-repo/chapter08/AGENTS.md`](../../book-repo/chapter08/AGENTS.md)
- Notebook: [`../../book-repo/chapter08/ch08_data_analysis_reasoning_agents.ipynb`](../../book-repo/chapter08/ch08_data_analysis_reasoning_agents.ipynb)

## Run the built-in demo

```bash
python ../../11_verification_validation_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(11)   # VerificationValidationAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Verify 'The Eiffel Tower is in Paris; built 1889.'"
```
