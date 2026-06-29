# Ethical Reasoning Agent — Context & Usage

**Agent #22 · Chapter 12: Ethical and Explainable Agents · class `EthicalReasoningAgent` · file `22_ethical_reasoning_agent.py`**

## Chapter context

Agents that make AI trustworthy: ethical value-alignment and explainable decisioning. Prerequisites for the regulated-domain chapters.

## This agent

- **Does:** Evaluates an action against ethical principles and approves/rejects with reasons.
- **Use when:** You must check whether an action is ethically acceptable (value alignment).
- **Not for:** explaining model decisions (use Explainable Agent).
- **Inputs:** a proposed action string; optional custom principles
- **Keywords:** ethics, values, alignment, responsible ai, principles, compliance, harm
- **Example task:** Should we sell user location data without consent?

## Techniques (from the book)

deontic logic (obligation/permission/prohibition); IEEE EAD validators; EU AI Act compliance; four-fifths bias rule

## Real-world use case (from the book)

TalentForward - prevents biased hiring and produces compliance evidence.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 12 (Ethical and Explainable Agents) of the mirrored repo:

- README: [`../../book-repo/chapter12/README.md`](../../book-repo/chapter12/README.md)
- Use case: [`../../book-repo/chapter12/USECASE.md`](../../book-repo/chapter12/USECASE.md)
- Agents notes: [`../../book-repo/chapter12/AGENTS.md`](../../book-repo/chapter12/AGENTS.md)
- Notebook: [`../../book-repo/chapter12/ch12_01_ethical_reasoning_agent.ipynb`](../../book-repo/chapter12/ch12_01_ethical_reasoning_agent.ipynb)

## Run the built-in demo

```bash
python ../../22_ethical_reasoning_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(22)   # EthicalReasoningAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Should we sell user location data without consent?"
```
