# Scientific Discovery Agent — Context & Usage

**Agent #25 · Chapter 13: Healthcare and Scientific Agents · class `ScientificDiscoveryAgent` · file `25_scientific_discovery_agent.py`**

## Chapter context

Domain agents for biomedical research and care: Bayesian clinical decision support and hypothesis-driven scientific discovery (educational only).

## This agent

- **Does:** Hypothesis->experiment->evaluate loop over a candidate space (active discovery).
- **Use when:** You search a candidate/parameter space using a (simulated) experiment objective.
- **Not for:** literature review (use Scientific Research Agent).
- **Inputs:** candidate list, an objective function, a budget
- **Keywords:** discovery, experiment, optimization, materials, active learning, search, hypothesis
- **Example task:** Find the material parameters maximizing conductivity.

## Techniques (from the book)

fault-tolerant multi-source literature scanning; knowledge-gap detection; abductive hypothesis generation; closed-loop experimental feedback

## Real-world use case (from the book)

NovaMateria Labs - finds cross-disciplinary polymer breakthroughs faster.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 13 (Healthcare and Scientific Agents) of the mirrored repo:

- README: [`../../book-repo/chapter13/README.md`](../../book-repo/chapter13/README.md)
- Use case: [`../../book-repo/chapter13/USECASE.md`](../../book-repo/chapter13/USECASE.md)
- Agents notes: [`../../book-repo/chapter13/AGENTS.md`](../../book-repo/chapter13/AGENTS.md)
- Notebook: [`../../book-repo/chapter13/ch13_healthcare_scientific_agents.ipynb`](../../book-repo/chapter13/ch13_healthcare_scientific_agents.ipynb)

## Run the built-in demo

```bash
python ../../25_scientific_discovery_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(25)   # ScientificDiscoveryAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Find the material parameters maximizing conductivity."
```

> Educational demonstration only — not professional advice.
