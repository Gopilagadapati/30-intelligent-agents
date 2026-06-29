# Autonomous Decision-Making Agent — Context & Usage

**Agent #1 · Chapter 5: Foundational Cognitive Architectures · class `AutonomousDecisionAgent` · file `01_autonomous_decision_agent.py`**

## Chapter context

The core building-block agents every other agent composes from: an autonomous perceive-reason-act loop, explicit planning, and working/episodic/semantic memory.

## This agent

- **Does:** Runs a perceive->reason->act loop, independently choosing the next action until a goal is met.
- **Use when:** You have a goal and a discrete set of possible actions, and want the agent to drive itself with minimal human steps.
- **Not for:** single-shot Q&A, or when you need a multi-step ordered plan up front (use the Planning Agent).
- **Inputs:** a goal string, a list of available actions
- **Keywords:** autonomy, loop, act, decision, goal-directed, self-driving
- **Example task:** Keep taking actions until a project proposal is produced.

## Techniques (from the book)

perceive->reason->act loop; strategy scoring; dependency-aware task DAGs; escalation thresholds

## Real-world use case (from the book)

ConnectWave Telecom - context-aware support decisions (outage/billing routing).

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 5 (Foundational Cognitive Architectures) of the mirrored repo:

- README: [`../../book-repo/chapter05/README.md`](../../book-repo/chapter05/README.md)
- Use case: [`../../book-repo/chapter05/USECASE.md`](../../book-repo/chapter05/USECASE.md)
- Agents notes: [`../../book-repo/chapter05/AGENTS.md`](../../book-repo/chapter05/AGENTS.md)
- Notebook: [`../../book-repo/chapter05/ch05_foundational_architectures.ipynb`](../../book-repo/chapter05/ch05_foundational_architectures.ipynb)

## Run the built-in demo

```bash
python ../../01_autonomous_decision_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(1)   # AutonomousDecisionAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Keep taking actions until a project proposal is produced."
```
