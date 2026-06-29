# Domain-Transforming Integration Agent — Context & Usage

**Agent #31 · Chapter 16: Embodied and Physical World Agents · class `DomainTransformingIntegrationAgent` · file `31_domain_transforming_integration_agent.py`**

## Chapter context

Agents that bridge digital intelligence and the physical world: embodied perception-action control and cross-domain integration.

## This agent

- **Does:** Cross-domain analogy: transfers patterns from one field to solve a problem in another.
- **Use when:** You want novel solutions by borrowing patterns across domains (biomimicry, etc.).
- **Not for:** straightforward single-domain tasks.
- **Inputs:** a map of domain->patterns, a problem, a target domain
- **Keywords:** cross-domain, analogy, synthesis, innovation, biomimicry, transfer, integration
- **Example task:** Use ant-colony routing to balance data-center load.

## Techniques (from the book)

typed knowledge graph; weighted breadth-first influence propagation; cross-domain cascade analysis; constraint assembler

## Real-world use case (from the book)

ArcticWing Aerial - detects a power outage blocks road access to a flight site.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 16 (Embodied and Physical World Agents) of the mirrored repo:

- README: [`../../book-repo/chapter16/README.md`](../../book-repo/chapter16/README.md)
- Use case: [`../../book-repo/chapter16/USECASE.md`](../../book-repo/chapter16/USECASE.md)
- Agents notes: [`../../book-repo/chapter16/AGENTS.md`](../../book-repo/chapter16/AGENTS.md)
- Notebook: [`../../book-repo/chapter16/ch16_embodied_agents.ipynb`](../../book-repo/chapter16/ch16_embodied_agents.ipynb)

## Run the built-in demo

```bash
python ../../31_domain_transforming_integration_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(31)   # DomainTransformingIntegrationAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Use ant-colony routing to balance data-center load."
```
