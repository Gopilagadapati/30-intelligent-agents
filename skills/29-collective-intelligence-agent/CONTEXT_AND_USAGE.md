# Collective Intelligence Agent — Context & Usage

**Agent #29 · Chapter 15: Education and Knowledge Agents · class `CollectiveIntelligenceAgent` · file `29_collective_intelligence_agent.py`**

## Chapter context

Agents for learning and collective reasoning: adaptive tutoring and multi-agent consensus.

## This agent

- **Does:** Aggregates multiple agents' votes into a confidence-weighted consensus.
- **Use when:** You want robustness via ensemble/consensus across several agents or models.
- **Not for:** single-perspective tasks.
- **Inputs:** a list of Voter agents, a question
- **Keywords:** consensus, ensemble, voting, multi-agent, collective, aggregation, swarm
- **Example task:** Decide loan approval by majority of weighted voters.

## Techniques (from the book)

propose/critique/synthesize; weighted consensus; adversarial critic rotation; cross-pollination

## Real-world use case (from the book)

LearnPath - builds grading rubrics via multi-agent consensus.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 15 (Education and Knowledge Agents) of the mirrored repo:

- README: [`../../book-repo/chapter15/README.md`](../../book-repo/chapter15/README.md)
- Use case: [`../../book-repo/chapter15/USECASE.md`](../../book-repo/chapter15/USECASE.md)
- Agents notes: [`../../book-repo/chapter15/AGENTS.md`](../../book-repo/chapter15/AGENTS.md)
- Notebook: [`../../book-repo/chapter15/ch15_education_and_knowledge_agents.ipynb`](../../book-repo/chapter15/ch15_education_and_knowledge_agents.ipynb)

## Run the built-in demo

```bash
python ../../29_collective_intelligence_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(29)   # CollectiveIntelligenceAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Decide loan approval by majority of weighted voters."
```
