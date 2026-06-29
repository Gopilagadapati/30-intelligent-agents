---
name: 08-chain-of-agents-orchestrator
description: Chain-of-Agents Orchestrator (Chapter 7, Tool Manipulation and Orchestration Agents). Routes a task through specialist sub-agents in sequence, passing outputs along. Use when: A task benefits from a pipeline of specialists (e.g., research->write->edit). Triggers: orchestration, pipeline, multi-agent, delegation, routing, chain.
---

# Skill 08 — Chain-of-Agents Orchestrator

*Chapter 7: Tool Manipulation and Orchestration Agents*

## What it does

Routes a task through specialist sub-agents in sequence, passing outputs along.

## When to use this skill

A task benefits from a pipeline of specialists (e.g., research->write->edit).

## When NOT to use

single-agent tasks, or workflows needing human approval (use Agentic Workflow System).

## Inputs required

a list of Specialist agents, a task

## Triggers / keywords

orchestration, pipeline, multi-agent, delegation, routing, chain

## Example task

Produce polished copy via researcher->writer->editor.

## Techniques (from the book)

cooperation protocol; shared memory; manager agent; conflict scoring/resolution

## Real-world use case (from the book)

ShieldPoint Insurance - market-intelligence workflow with conflict detection.

## Book reference (official code)

- Chapter 7: Tool Manipulation and Orchestration Agents
- README: [`../../book-repo/chapter07/README.md`](../../book-repo/chapter07/README.md)
- Use case: [`../../book-repo/chapter07/USECASE.md`](../../book-repo/chapter07/USECASE.md)
- Agents notes: [`../../book-repo/chapter07/AGENTS.md`](../../book-repo/chapter07/AGENTS.md)
- Notebook: [`../../book-repo/chapter07/ch07_tool_orchestration.ipynb`](../../book-repo/chapter07/ch07_tool_orchestration.ipynb)

## How to run

```bash
# from the 30agents/ root
python 08_chain_of_agents_orchestrator.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(8)   # ChainOfAgentsOrchestrator
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
