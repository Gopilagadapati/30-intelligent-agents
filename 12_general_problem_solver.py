"""Agent 12 - General Problem Solver (Chapter 8).

Pattern: domain-agnostic reasoning via means-ends analysis. Given a start state,
a goal state and a set of operators, the agent searches for a sequence of
operators that reduces the difference between current and goal states.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable, Dict, List, Optional, Set, Tuple

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class Operator:
    def __init__(self, name: str, precondition: Callable[[frozenset], bool],
                 effect: Callable[[frozenset], frozenset]):
        self.name = name
        self.precondition = precondition
        self.effect = effect


class GeneralProblemSolver(BaseAgent):
    def __init__(self, operators: List[Operator], max_depth: int = 10, llm=None):
        super().__init__(name="GeneralProblemSolver", system_prompt="Solve problems by means-ends analysis.", llm=llm)
        self.operators = operators
        self.max_depth = max_depth

    def solve(self, start: Set[str], goal: Set[str]) -> Optional[List[str]]:
        start_f, goal_f = frozenset(start), frozenset(goal)
        seen: Set[frozenset] = {start_f}
        frontier: List[Tuple[frozenset, List[str]]] = [(start_f, [])]
        while frontier:
            state, path = frontier.pop(0)
            if goal_f <= state:
                return path
            if len(path) >= self.max_depth:
                continue
            for op in self.operators:
                if op.precondition(state):
                    nxt = op.effect(state)
                    if nxt not in seen:
                        seen.add(nxt)
                        frontier.append((nxt, path + [op.name]))
        return None

    def run(self, problem: Dict[str, Set[str]]) -> AgentResult:
        self.trace = []
        plan = self.solve(problem["start"], problem["goal"])
        self._log(f"plan: {plan}")
        return AgentResult(output=plan, trace=list(self.trace),
                           metadata={"solved": plan is not None})


if __name__ == "__main__":
    ops = [
        Operator("buy_flour", lambda s: "money" in s, lambda s: s | {"flour"}),
        Operator("bake", lambda s: "flour" in s, lambda s: s | {"cake"}),
    ]
    solver = GeneralProblemSolver(ops)
    result = solver.run({"start": {"money"}, "goal": {"cake"}})
    print("Plan:", result.output)
