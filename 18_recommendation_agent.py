"""Agent 18 - Recommendation Agent (Chapter 10).

Pattern: hybrid recommender combining content-based similarity and simple
collaborative signals, with an LLM layer that explains why each item is
recommended.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Tuple

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.memory import _tokens, _cosine
from common.llm import MockLLM


class RecommendationAgent(BaseAgent):
    def __init__(self, catalog: Dict[str, str], popularity: Dict[str, float] = None, llm=None):
        super().__init__(
            name="RecommendationAgent",
            system_prompt="You recommend items and explain the reasoning.",
            llm=llm,
        )
        self.catalog = catalog
        self.vectors = {item: _tokens(desc) for item, desc in catalog.items()}
        self.popularity = popularity or {k: 0.5 for k in catalog}

    def recommend(self, profile: str, k: int = 3) -> List[Tuple[str, float]]:
        pvec = _tokens(profile)
        scored = []
        for item, vec in self.vectors.items():
            content = _cosine(pvec, vec)
            hybrid = 0.7 * content + 0.3 * self.popularity.get(item, 0.0)
            scored.append((item, round(hybrid, 3)))
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:k]

    def run(self, profile: str, k: int = 3) -> AgentResult:
        self.trace = []
        recs = self.recommend(profile, k)
        self._log(f"recs: {recs}")
        top = recs[0][0] if recs else None
        why = self.think(f"User likes: {profile}\nRecommended: {top}\nExplain in one line:")
        return AgentResult(output=recs, trace=list(self.trace),
                           metadata={"explanation": why})


if __name__ == "__main__":
    catalog = {
        "Dune": "epic science fiction desert planet politics",
        "The Martian": "science fiction mars survival engineering",
        "Pride and Prejudice": "romance regency england society",
    }
    pop = {"Dune": 0.9, "The Martian": 0.7, "Pride and Prejudice": 0.6}
    llm = MockLLM().add_rule(r"Explain in one line:", "It matches your taste for sci-fi adventures.")
    agent = RecommendationAgent(catalog, pop, llm=llm)
    result = agent.run("loves science fiction space survival stories")
    print("Recommendations:", result.output)
    print("Why:", result.metadata["explanation"])
