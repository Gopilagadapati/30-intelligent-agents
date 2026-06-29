"""Agent 23 - Explainable Agent (Chapter 12).

Pattern: reasoning transparency. The agent produces a decision together with a
structured explanation -- the factors considered, their weights, and a
counterfactual ("what would change the outcome"). Mirrors SHAP/LIME-style
feature attributions in a model-agnostic way.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Tuple

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class ExplainableAgent(BaseAgent):
    def __init__(self, weights: Dict[str, float], threshold: float = 0.5, llm=None):
        super().__init__(
            name="ExplainableAgent",
            system_prompt="You make decisions and explain the contributing factors transparently.",
            llm=llm,
        )
        self.weights = weights
        self.threshold = threshold

    def score(self, features: Dict[str, float]) -> Tuple[float, List[Tuple[str, float]]]:
        contributions = [(f, round(self.weights.get(f, 0.0) * v, 3)) for f, v in features.items()]
        total = round(sum(c for _, c in contributions), 3)
        contributions.sort(key=lambda x: abs(x[1]), reverse=True)
        return total, contributions

    def counterfactual(self, features: Dict[str, float], contributions: List[Tuple[str, float]]) -> str:
        # the single feature whose removal most moves the score toward the boundary
        top = contributions[0][0] if contributions else None
        return f"Had '{top}' been different, the decision would likely change."

    def run(self, features: Dict[str, float]) -> AgentResult:
        self.trace = []
        total, contributions = self.score(features)
        decision = "APPROVE" if total >= self.threshold else "DENY"
        self._log(f"score={total} decision={decision} factors={contributions}")
        cf = self.counterfactual(features, contributions)
        narrative = self.think(
            f"DECISION: {decision}\nSCORE: {total}\nFACTORS: {contributions}\nExplain plainly:"
        )
        return AgentResult(
            output={"decision": decision, "score": total, "factors": contributions,
                    "counterfactual": cf, "narrative": narrative},
            trace=list(self.trace),
        )


if __name__ == "__main__":
    weights = {"credit_score": 0.6, "income": 0.3, "debt_ratio": -0.4}
    llm = MockLLM().add_rule(r"Explain plainly:", "Approved mainly due to a strong credit score; high debt was the main negative.")
    agent = ExplainableAgent(weights, threshold=0.4)
    agent.llm = llm
    result = agent.run({"credit_score": 0.9, "income": 0.5, "debt_ratio": 0.6})
    print("Decision:", result.output["decision"])
    print("Factors:", result.output["factors"])
    print("Counterfactual:", result.output["counterfactual"])
