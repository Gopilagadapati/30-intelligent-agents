"""Agent 25 - Scientific Discovery Agent (Chapter 13).

Pattern: hypothesis-driven discovery loop -- propose candidate hypotheses, design
a (simulated) experiment, evaluate results, and update beliefs. Demonstrated with
a materials-discovery style search over a candidate space.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable, Dict, List, Tuple

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class ScientificDiscoveryAgent(BaseAgent):
    def __init__(self, candidates: List[Dict[str, float]], objective: Callable[[Dict[str, float]], float],
                 budget: int = 5, llm=None):
        super().__init__(
            name="ScientificDiscoveryAgent",
            system_prompt="You drive scientific discovery by proposing and testing hypotheses.",
            llm=llm,
        )
        self.candidates = candidates
        self.objective = objective  # simulated experiment
        self.budget = budget

    def run(self, goal: str) -> AgentResult:
        self.trace = []
        tested: List[Tuple[Dict[str, float], float]] = []
        # greedy active-learning: test highest-uncertainty/unseen candidates
        for cand in self.candidates[: self.budget]:
            score = self.objective(cand)
            tested.append((cand, score))
            self._log(f"tested {cand} -> {round(score,3)}")
        tested.sort(key=lambda x: x[1], reverse=True)
        best, best_score = tested[0]
        summary = self.think(f"GOAL: {goal}\nBest candidate {best} scored {round(best_score,3)}.\nConclusion:")
        return AgentResult(output={"best": best, "score": round(best_score, 3), "conclusion": summary},
                           trace=list(self.trace), metadata={"experiments": len(tested)})


if __name__ == "__main__":
    candidates = [
        {"temp": 300, "ratio": 0.2},
        {"temp": 450, "ratio": 0.5},
        {"temp": 600, "ratio": 0.8},
    ]
    # simulated material conductivity objective
    objective = lambda c: c["ratio"] * 100 - abs(c["temp"] - 450) * 0.1
    llm = MockLLM().add_rule(r"Conclusion:", "Higher ratio near 450C maximizes conductivity; recommend follow-up synthesis.")
    agent = ScientificDiscoveryAgent(candidates, objective, llm=llm)
    result = agent.run("Maximize material conductivity")
    print("Best:", result.output["best"], "Score:", result.output["score"])
    print("Conclusion:", result.output["conclusion"])
