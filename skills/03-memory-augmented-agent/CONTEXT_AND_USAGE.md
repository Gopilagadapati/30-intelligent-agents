# Memory-Augmented Agent — Context & Usage

**Agent #3 · Chapter 5: Foundational Cognitive Architectures · class `MemoryAugmentedAgent` · file `03_memory_augmented_agent.py`**

## Chapter context

The core building-block agents every other agent composes from: an autonomous perceive-reason-act loop, explicit planning, and working/episodic/semantic memory.

## This agent

- **Does:** Answers using working, episodic and semantic memory to personalize and stay consistent.
- **Use when:** The task needs recall of prior facts/interactions or personalization across turns.
- **Not for:** stateless one-off questions with no prior context.
- **Inputs:** a user message; pre-loaded facts via remember_fact()
- **Keywords:** memory, recall, personalization, history, context retention
- **Example task:** Answer a patient question while remembering their penicillin allergy.

## Techniques (from the book)

working/episodic/semantic memory; vector-similarity retrieval

## Real-world use case (from the book)

ConnectWave Telecom - remembers prior calls, fixes, and customer history.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 5 (Foundational Cognitive Architectures) of the mirrored repo:

- README: [`../../book-repo/chapter05/README.md`](../../book-repo/chapter05/README.md)
- Use case: [`../../book-repo/chapter05/USECASE.md`](../../book-repo/chapter05/USECASE.md)
- Agents notes: [`../../book-repo/chapter05/AGENTS.md`](../../book-repo/chapter05/AGENTS.md)
- Notebook: [`../../book-repo/chapter05/ch05_foundational_architectures.ipynb`](../../book-repo/chapter05/ch05_foundational_architectures.ipynb)

## Run the built-in demo

```bash
python ../../03_memory_augmented_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(3)   # MemoryAugmentedAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Answer a patient question while remembering their penicillin allergy."
```
