# Planning Agent — Context & Usage

**Agent #2 · Chapter 5: Foundational Cognitive Architectures · class `PlanningAgent` · file `02_planning_agent.py`**

## Chapter context

The core building-block agents every other agent composes from: an autonomous perceive-reason-act loop, explicit planning, and working/episodic/semantic memory.

## This agent

- **Does:** Decomposes a goal into an ordered plan using tree-of-thought evaluation of alternatives.
- **Use when:** You need an explicit, ordered breakdown of a complex goal into sub-tasks before execution.
- **Not for:** executing the steps (it only plans), or trivial single-step tasks.
- **Inputs:** a goal string
- **Keywords:** plan, decompose, subtasks, tree-of-thought, strategy, breakdown
- **Example task:** Break 'launch a predictive-maintenance pilot' into ordered steps.

## Techniques (from the book)

hierarchical task decomposition; phased task trees; adaptive replanning

## Real-world use case (from the book)

ConnectWave Telecom - orchestrates multi-step fiber migration and monitoring.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 5 (Foundational Cognitive Architectures) of the mirrored repo:

- README: [`../../book-repo/chapter05/README.md`](../../book-repo/chapter05/README.md)
- Use case: [`../../book-repo/chapter05/USECASE.md`](../../book-repo/chapter05/USECASE.md)
- Agents notes: [`../../book-repo/chapter05/AGENTS.md`](../../book-repo/chapter05/AGENTS.md)
- Notebook: [`../../book-repo/chapter05/ch05_foundational_architectures.ipynb`](../../book-repo/chapter05/ch05_foundational_architectures.ipynb)

## Run the built-in demo

```bash
python ../../02_planning_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(2)   # PlanningAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Break 'launch a predictive-maintenance pilot' into ordered steps."
```
