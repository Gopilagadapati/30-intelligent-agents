---
name: 12-general-problem-solver
description: General Problem Solver (Chapter 8, Data Analysis and Reasoning Agents). Domain-agnostic means-ends search from a start state to a goal state via operators. Use when: The problem can be framed as states + operators and you need a sequence of steps. Triggers: planning, search, means-ends, state space, solver, operators, reasoning.
---

# Skill 12 — General Problem Solver

*Chapter 8: Data Analysis and Reasoning Agents*

## What it does

Domain-agnostic means-ends search from a start state to a goal state via operators.

## When to use this skill

The problem can be framed as states + operators and you need a sequence of steps.

## When NOT to use

natural-language tasks that can't be modeled as discrete states.

## Inputs required

start state, goal state, a list of Operator objects

## Triggers / keywords

planning, search, means-ends, state space, solver, operators, reasoning

## Example task

From {money} reach {cake} using buy/bake operators.

## Techniques (from the book)

decompose->analogize->hypothesize->test->meta-learn

## Real-world use case (from the book)

CanadaFirst News - cross-domain investigation (immigration, housing, health, economics).

## Book reference (official code)

- Chapter 8: Data Analysis and Reasoning Agents
- README: [`../../book-repo/chapter08/README.md`](../../book-repo/chapter08/README.md)
- Use case: [`../../book-repo/chapter08/USECASE.md`](../../book-repo/chapter08/USECASE.md)
- Agents notes: [`../../book-repo/chapter08/AGENTS.md`](../../book-repo/chapter08/AGENTS.md)
- Notebook: [`../../book-repo/chapter08/ch08_data_analysis_reasoning_agents.ipynb`](../../book-repo/chapter08/ch08_data_analysis_reasoning_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 12_general_problem_solver.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(12)   # GeneralProblemSolver
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
