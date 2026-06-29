# Agentic Workflow System — Context & Usage

**Agent #9 · Chapter 7: Tool Manipulation and Orchestration Agents · class `AgenticWorkflowSystem` · file `09_agentic_workflow_system.py`**

## Chapter context

Agents that take action and coordinate others: tool/function calling, chain-of-agents orchestration, and human-in-the-loop workflows.

## This agent

- **Does:** Executes a multi-step workflow with human-in-the-loop approval checkpoints.
- **Use when:** A process has gated steps requiring human approval before continuing.
- **Not for:** fully autonomous flows with no approval gates.
- **Inputs:** a list of WorkflowStep objects, an approver callback, initial context
- **Keywords:** workflow, human-in-the-loop, approval, process, gating, checkpoints
- **Example task:** Draft->review (needs approval)->publish a report.

## Techniques (from the book)

state machine; guard conditions; human-in-the-loop gates; audit trail

## Real-world use case (from the book)

ShieldPoint Insurance - claims pipeline (intake->validation->risk->payout).

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 7 (Tool Manipulation and Orchestration Agents) of the mirrored repo:

- README: [`../../book-repo/chapter07/README.md`](../../book-repo/chapter07/README.md)
- Use case: [`../../book-repo/chapter07/USECASE.md`](../../book-repo/chapter07/USECASE.md)
- Agents notes: [`../../book-repo/chapter07/AGENTS.md`](../../book-repo/chapter07/AGENTS.md)
- Notebook: [`../../book-repo/chapter07/ch07_tool_orchestration.ipynb`](../../book-repo/chapter07/ch07_tool_orchestration.ipynb)

## Run the built-in demo

```bash
python ../../09_agentic_workflow_system.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(9)   # AgenticWorkflowSystem
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Draft->review (needs approval)->publish a report."
```
