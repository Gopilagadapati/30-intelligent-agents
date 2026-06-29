"""Agent 02 - Planning Agent (Chapter 5).

Pattern: hierarchical task decomposition with tree-of-thought style evaluation.
The agent breaks a goal into sub-tasks, optionally explores alternative
decompositions, scores them, and emits an ordered plan.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class PlanningAgent(BaseAgent):
    def __init__(self, branches: int = 2, llm=None):
        super().__init__(
            name="PlanningAgent",
            system_prompt=(
                "You are a planning agent. Decompose the goal into a numbered list "
                "of concrete, ordered sub-tasks."
            ),
            llm=llm,
        )
        self.branches = branches

    def decompose(self, goal: str, variant: int) -> List[str]:
        raw = self.think(f"GOAL: {goal}\nVariant #{variant}. Sub-tasks:")
        steps = [s.strip(" -.0123456789") for s in raw.splitlines() if s.strip()]
        return [s for s in steps if s]

    def score(self, plan: List[str]) -> float:
        # Tree-of-thought heuristic: prefer concrete, appropriately sized plans.
        if not plan:
            return 0.0
        size_score = 1.0 - abs(len(plan) - 4) / 10.0
        concreteness = sum(1 for s in plan if len(s.split()) >= 2) / len(plan)
        return round(0.5 * size_score + 0.5 * concreteness, 3)

    def run(self, goal: str) -> AgentResult:
        self.trace = []
        candidates = []
        for v in range(1, self.branches + 1):
            plan = self.decompose(goal, v)
            s = self.score(plan)
            candidates.append((s, plan))
            self._log(f"candidate v{v} score={s}: {plan}")
        candidates.sort(key=lambda x: x[0], reverse=True)
        best_score, best_plan = candidates[0]
        return AgentResult(
            output=best_plan,
            trace=list(self.trace),
            metadata={"goal": goal, "score": best_score, "explored": len(candidates)},
        )


def _demo_llm() -> MockLLM:
    plans = iter([
        "1. Define scope\n2. Collect data\n3. Build model\n4. Evaluate",
        "1. Start\n2. Stuff",
    ])

    def gen(_p: str) -> str:
        try:
            return next(plans)
        except StopIteration:
            return "1. Do the task"

    return MockLLM().add_rule(r"Sub-tasks:", gen)


if __name__ == "__main__":
    agent = PlanningAgent(branches=2, llm=_demo_llm())
    result = agent.run("Launch a predictive maintenance pilot")
    print("Chosen plan:")
    for i, step in enumerate(result.output, 1):
        print(f"  {i}. {step}")
    print("score:", result.metadata["score"])
