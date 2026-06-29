# Tool-Using Agent — Context & Usage

**Agent #7 · Chapter 7: Tool Manipulation and Orchestration Agents · class `ToolUsingAgent` · file `07_tool_using_agent.py`**

## Chapter context

Agents that take action and coordinate others: tool/function calling, chain-of-agents orchestration, and human-in-the-loop workflows.

## This agent

- **Does:** Selects and calls the right tool/function for a request via a selection funnel.
- **Use when:** The task needs external actions/APIs/functions (calculations, lookups, side effects).
- **Not for:** pure reasoning with no tools to call.
- **Inputs:** a ToolRegistry of callables, a request
- **Keywords:** tools, function calling, api, actions, plugins, invoke
- **Example task:** Answer 'weather in Ottawa?' by calling the weather tool.

## Techniques (from the book)

Think/Plan/Act; tool registry; @graceful_fallback; tool-discovery funnel

## Real-world use case (from the book)

ShieldPoint Insurance - safe tool/analytics orchestration on campaign data.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 7 (Tool Manipulation and Orchestration Agents) of the mirrored repo:

- README: [`../../book-repo/chapter07/README.md`](../../book-repo/chapter07/README.md)
- Use case: [`../../book-repo/chapter07/USECASE.md`](../../book-repo/chapter07/USECASE.md)
- Agents notes: [`../../book-repo/chapter07/AGENTS.md`](../../book-repo/chapter07/AGENTS.md)
- Notebook: [`../../book-repo/chapter07/ch07_tool_orchestration.ipynb`](../../book-repo/chapter07/ch07_tool_orchestration.ipynb)

## Run the built-in demo

```bash
python ../../07_tool_using_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(7)   # ToolUsingAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Answer 'weather in Ottawa?' by calling the weather tool."
```
