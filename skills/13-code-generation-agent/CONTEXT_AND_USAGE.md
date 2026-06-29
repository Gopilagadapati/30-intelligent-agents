# Code-Generation Agent — Context & Usage

**Agent #13 · Chapter 9: Software Development Agents · class `CodeGenerationAgent` · file `13_code_generation_agent.py`**

## Chapter context

Agents that build and safeguard software: program synthesis with tests, prompt-injection defense, and learning from feedback.

## This agent

- **Does:** Synthesizes a function from a spec with a generate->test->repair loop until tests pass.
- **Use when:** You need code written/fixed and have unit tests to validate it.
- **Not for:** prose generation or tasks without verifiable tests.
- **Inputs:** a spec string, a tests callable that asserts on the produced namespace
- **Keywords:** code, programming, synthesis, tests, debug, repair, developer
- **Example task:** Write add(a,b) that passes the provided assertions.

## Techniques (from the book)

LangGraph test-driven generation; generate->test->refine loop; iteration limit

## Real-world use case (from the book)

VaultPay - test-first feature delivery for a fintech platform.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 9 (Software Development Agents) of the mirrored repo:

- README: [`../../book-repo/chapter09/README.md`](../../book-repo/chapter09/README.md)
- Use case: [`../../book-repo/chapter09/USECASE.md`](../../book-repo/chapter09/USECASE.md)
- Agents notes: [`../../book-repo/chapter09/AGENTS.md`](../../book-repo/chapter09/AGENTS.md)
- Notebook: [`../../book-repo/chapter09/ch09_software_dev_agents.ipynb`](../../book-repo/chapter09/ch09_software_dev_agents.ipynb)

## Run the built-in demo

```bash
python ../../13_code_generation_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(13)   # CodeGenerationAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Write add(a,b) that passes the provided assertions."
```
