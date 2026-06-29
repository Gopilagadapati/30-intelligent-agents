# Chain-of-Agents Orchestrator — Context & Usage

**Agent #8 · Chapter 7: Tool Manipulation and Orchestration Agents · class `ChainOfAgentsOrchestrator` · file `08_chain_of_agents_orchestrator.py`**

## Chapter context

Agents that take action and coordinate others: tool/function calling, chain-of-agents orchestration, and human-in-the-loop workflows.

## This agent

- **Does:** Routes a task through specialist sub-agents in sequence, passing outputs along.
- **Use when:** A task benefits from a pipeline of specialists (e.g., research->write->edit).
- **Not for:** single-agent tasks, or workflows needing human approval (use Agentic Workflow System).
- **Inputs:** a list of Specialist agents, a task
- **Keywords:** orchestration, pipeline, multi-agent, delegation, routing, chain
- **Example task:** Produce polished copy via researcher->writer->editor.

## Techniques (from the book)

cooperation protocol; shared memory; manager agent; conflict scoring/resolution

## Real-world use case (from the book)

ShieldPoint Insurance - market-intelligence workflow with conflict detection.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 7 (Tool Manipulation and Orchestration Agents) of the mirrored repo:

- README: [`../../book-repo/chapter07/README.md`](../../book-repo/chapter07/README.md)
- Use case: [`../../book-repo/chapter07/USECASE.md`](../../book-repo/chapter07/USECASE.md)
- Agents notes: [`../../book-repo/chapter07/AGENTS.md`](../../book-repo/chapter07/AGENTS.md)
- Notebook: [`../../book-repo/chapter07/ch07_tool_orchestration.ipynb`](../../book-repo/chapter07/ch07_tool_orchestration.ipynb)

## Run the built-in demo

```bash
python ../../08_chain_of_agents_orchestrator.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(8)   # ChainOfAgentsOrchestrator
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Produce polished copy via researcher->writer->editor."
```
