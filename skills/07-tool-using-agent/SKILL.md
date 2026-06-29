---
name: 07-tool-using-agent
description: Tool-Using Agent (Chapter 7, Tool Manipulation and Orchestration Agents). Selects and calls the right tool/function for a request via a selection funnel. Use when: The task needs external actions/APIs/functions (calculations, lookups, side effects). Triggers: tools, function calling, api, actions, plugins, invoke.
---

# Skill 07 — Tool-Using Agent

*Chapter 7: Tool Manipulation and Orchestration Agents*

## What it does

Selects and calls the right tool/function for a request via a selection funnel.

## When to use this skill

The task needs external actions/APIs/functions (calculations, lookups, side effects).

## When NOT to use

pure reasoning with no tools to call.

## Inputs required

a ToolRegistry of callables, a request

## Triggers / keywords

tools, function calling, api, actions, plugins, invoke

## Example task

Answer 'weather in Ottawa?' by calling the weather tool.

## Techniques (from the book)

Think/Plan/Act; tool registry; @graceful_fallback; tool-discovery funnel

## Real-world use case (from the book)

ShieldPoint Insurance - safe tool/analytics orchestration on campaign data.

## Book reference (official code)

- Chapter 7: Tool Manipulation and Orchestration Agents
- README: [`../../book-repo/chapter07/README.md`](../../book-repo/chapter07/README.md)
- Use case: [`../../book-repo/chapter07/USECASE.md`](../../book-repo/chapter07/USECASE.md)
- Agents notes: [`../../book-repo/chapter07/AGENTS.md`](../../book-repo/chapter07/AGENTS.md)
- Notebook: [`../../book-repo/chapter07/ch07_tool_orchestration.ipynb`](../../book-repo/chapter07/ch07_tool_orchestration.ipynb)

## How to run

```bash
# from the 30agents/ root
python 07_tool_using_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(7)   # ToolUsingAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
