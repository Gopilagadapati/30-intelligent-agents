# Self-Improving Agent — Context & Usage

**Agent #15 · Chapter 9: Software Development Agents · class `SelfImprovingAgent` · file `15_self_improving_agent.py`**

## Chapter context

Agents that build and safeguard software: program synthesis with tests, prompt-injection defense, and learning from feedback.

## This agent

- **Does:** Adapts future answers from user feedback (online learning of style/lessons).
- **Use when:** You want behavior to improve over time from ratings/feedback.
- **Not for:** static, one-off responses with no feedback loop.
- **Inputs:** a question; feedback via give_feedback()
- **Keywords:** learning, feedback, adaptive, improve, online learning, rlhf
- **Example task:** Give more detailed answers after a low rating.

## Techniques (from the book)

execute->observe->learn->adapt; critic/planner/learning layers; rollback

## Real-world use case (from the book)

VaultPay - improves support chatbot resolution rate over time.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 9 (Software Development Agents) of the mirrored repo:

- README: [`../../book-repo/chapter09/README.md`](../../book-repo/chapter09/README.md)
- Use case: [`../../book-repo/chapter09/USECASE.md`](../../book-repo/chapter09/USECASE.md)
- Agents notes: [`../../book-repo/chapter09/AGENTS.md`](../../book-repo/chapter09/AGENTS.md)
- Notebook: [`../../book-repo/chapter09/ch09_software_dev_agents.ipynb`](../../book-repo/chapter09/ch09_software_dev_agents.ipynb)

## Run the built-in demo

```bash
python ../../15_self_improving_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(15)   # SelfImprovingAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Give more detailed answers after a low rating."
```
