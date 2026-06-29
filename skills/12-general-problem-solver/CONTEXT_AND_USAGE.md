# General Problem Solver — Context & Usage

**Agent #12 · Chapter 8: Data Analysis and Reasoning Agents · class `GeneralProblemSolver` · file `12_general_problem_solver.py`**

## Chapter context

Agents specialized in analyzing data and reasoning: data exploration, fact verification, and a domain-agnostic problem solver.

## This agent

- **Does:** Domain-agnostic means-ends search from a start state to a goal state via operators.
- **Use when:** The problem can be framed as states + operators and you need a sequence of steps.
- **Not for:** natural-language tasks that can't be modeled as discrete states.
- **Inputs:** start state, goal state, a list of Operator objects
- **Keywords:** planning, search, means-ends, state space, solver, operators, reasoning
- **Example task:** From {money} reach {cake} using buy/bake operators.

## Techniques (from the book)

decompose->analogize->hypothesize->test->meta-learn

## Real-world use case (from the book)

CanadaFirst News - cross-domain investigation (immigration, housing, health, economics).

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 8 (Data Analysis and Reasoning Agents) of the mirrored repo:

- README: [`../../book-repo/chapter08/README.md`](../../book-repo/chapter08/README.md)
- Use case: [`../../book-repo/chapter08/USECASE.md`](../../book-repo/chapter08/USECASE.md)
- Agents notes: [`../../book-repo/chapter08/AGENTS.md`](../../book-repo/chapter08/AGENTS.md)
- Notebook: [`../../book-repo/chapter08/ch08_data_analysis_reasoning_agents.ipynb`](../../book-repo/chapter08/ch08_data_analysis_reasoning_agents.ipynb)

## Run the built-in demo

```bash
python ../../12_general_problem_solver.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(12)   # GeneralProblemSolver
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "From {money} reach {cake} using buy/bake operators."
```
