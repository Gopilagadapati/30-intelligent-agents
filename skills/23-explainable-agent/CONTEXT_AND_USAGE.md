# Explainable Agent — Context & Usage

**Agent #23 · Chapter 12: Ethical and Explainable Agents · class `ExplainableAgent` · file `23_explainable_agent.py`**

## Chapter context

Agents that make AI trustworthy: ethical value-alignment and explainable decisioning. Prerequisites for the regulated-domain chapters.

## This agent

- **Does:** Makes a weighted decision and explains it with factor attributions + a counterfactual.
- **Use when:** A decision needs transparency: which factors drove it and what would flip it.
- **Not for:** ethical acceptability judgments (use Ethical Reasoning).
- **Inputs:** feature weights, a feature dict
- **Keywords:** explainability, transparency, shap, lime, attribution, counterfactual, interpretability
- **Example task:** Explain why a loan was approved/denied.

## Techniques (from the book)

LIME; SHAP; counterfactual analysis; confidence calibration (temperature scaling); audience-adapted explanations

## Real-world use case (from the book)

ClearPath Health - explains clinical predictions so doctors trust them.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 12 (Ethical and Explainable Agents) of the mirrored repo:

- README: [`../../book-repo/chapter12/README.md`](../../book-repo/chapter12/README.md)
- Use case: [`../../book-repo/chapter12/USECASE.md`](../../book-repo/chapter12/USECASE.md)
- Agents notes: [`../../book-repo/chapter12/AGENTS.md`](../../book-repo/chapter12/AGENTS.md)
- Notebook: [`../../book-repo/chapter12/ch12_02_explainable_agent.ipynb`](../../book-repo/chapter12/ch12_02_explainable_agent.ipynb)

## Run the built-in demo

```bash
python ../../23_explainable_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(23)   # ExplainableAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Explain why a loan was approved/denied."
```
