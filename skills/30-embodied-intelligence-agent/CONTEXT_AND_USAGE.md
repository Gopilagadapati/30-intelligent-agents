# Embodied Intelligence Agent — Context & Usage

**Agent #30 · Chapter 16: Embodied and Physical World Agents · class `EmbodiedIntelligenceAgent` · file `30_embodied_intelligence_agent.py`**

## Chapter context

Agents that bridge digital intelligence and the physical world: embodied perception-action control and cross-domain integration.

## This agent

- **Does:** Perception-action loop for navigation/control in a (grid) physical environment.
- **Use when:** The task is robotic/embodied control: sense, plan a move, actuate, repeat.
- **Not for:** pure information tasks with no physical state.
- **Inputs:** obstacles set, a start and goal position
- **Keywords:** robotics, embodied, navigation, control, perception-action, motion, grid
- **Example task:** Navigate a robot around obstacles to a goal cell.

## Techniques (from the book)

four-layer control hierarchy; Unified Constraint Envelope; conservative all() safety fusion; fail-graceful external checks

## Real-world use case (from the book)

ArcticWing Aerial - deterministic go/no-go flight control in winter conditions.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 16 (Embodied and Physical World Agents) of the mirrored repo:

- README: [`../../book-repo/chapter16/README.md`](../../book-repo/chapter16/README.md)
- Use case: [`../../book-repo/chapter16/USECASE.md`](../../book-repo/chapter16/USECASE.md)
- Agents notes: [`../../book-repo/chapter16/AGENTS.md`](../../book-repo/chapter16/AGENTS.md)
- Notebook: [`../../book-repo/chapter16/ch16_embodied_agents.ipynb`](../../book-repo/chapter16/ch16_embodied_agents.ipynb)

## Run the built-in demo

```bash
python ../../30_embodied_intelligence_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(30)   # EmbodiedIntelligenceAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Navigate a robot around obstacles to a goal cell."
```
