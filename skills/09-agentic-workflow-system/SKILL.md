---
name: 09-agentic-workflow-system
description: Agentic Workflow System (Chapter 7, Tool Manipulation and Orchestration Agents). Executes a multi-step workflow with human-in-the-loop approval checkpoints. Use when: A process has gated steps requiring human approval before continuing. Triggers: workflow, human-in-the-loop, approval, process, gating, checkpoints.
---

# Skill 09 — Agentic Workflow System

*Chapter 7: Tool Manipulation and Orchestration Agents*

## What it does

Executes a multi-step workflow with human-in-the-loop approval checkpoints.

## When to use this skill

A process has gated steps requiring human approval before continuing.

## When NOT to use

fully autonomous flows with no approval gates.

## Inputs required

a list of WorkflowStep objects, an approver callback, initial context

## Triggers / keywords

workflow, human-in-the-loop, approval, process, gating, checkpoints

## Example task

Draft->review (needs approval)->publish a report.

## Techniques (from the book)

state machine; guard conditions; human-in-the-loop gates; audit trail

## Real-world use case (from the book)

ShieldPoint Insurance - claims pipeline (intake->validation->risk->payout).

## Book reference (official code)

- Chapter 7: Tool Manipulation and Orchestration Agents
- README: [`../../book-repo/chapter07/README.md`](../../book-repo/chapter07/README.md)
- Use case: [`../../book-repo/chapter07/USECASE.md`](../../book-repo/chapter07/USECASE.md)
- Agents notes: [`../../book-repo/chapter07/AGENTS.md`](../../book-repo/chapter07/AGENTS.md)
- Notebook: [`../../book-repo/chapter07/ch07_tool_orchestration.ipynb`](../../book-repo/chapter07/ch07_tool_orchestration.ipynb)

## How to run

```bash
# from the 30agents/ root
python 09_agentic_workflow_system.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(9)   # AgenticWorkflowSystem
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
