"""Agent 28 - Education Intelligence Agent (Chapter 15).

Pattern: adaptive learning. The agent tracks a learner's mastery per skill,
selects the next item using a difficulty-matching policy (zone of proximal
development), and updates mastery from responses.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class EducationIntelligenceAgent(BaseAgent):
    def __init__(self, skills: List[str], items: List[Dict[str, object]], llm=None):
        super().__init__(
            name="EducationIntelligenceAgent",
            system_prompt="You are an adaptive tutor matching tasks to the learner's level.",
            llm=llm,
        )
        self.mastery = {s: 0.3 for s in skills}
        self.items = items  # each: {id, skill, difficulty}

    def next_item(self) -> Dict[str, object]:
        # pick the item whose difficulty is closest just above current mastery
        def gap(item):
            m = self.mastery.get(item["skill"], 0.0)
            target = m + 0.15  # zone of proximal development
            return abs(item["difficulty"] - target)
        return min(self.items, key=gap)

    def update(self, skill: str, correct: bool) -> None:
        delta = 0.1 if correct else -0.05
        self.mastery[skill] = max(0.0, min(1.0, self.mastery[skill] + delta))

    def run(self, last_result: Dict[str, object] = None) -> AgentResult:
        self.trace = []
        if last_result:
            self.update(last_result["skill"], last_result["correct"])
            self._log(f"updated {last_result['skill']} -> {self.mastery[last_result['skill']]:.2f}")
        nxt = self.next_item()
        self._log(f"next item: {nxt}")
        coaching = self.think(f"MASTERY: {self.mastery}\nNEXT: {nxt}\nEncourage the learner:")
        return AgentResult(output={"next_item": nxt, "mastery": dict(self.mastery), "coaching": coaching},
                           trace=list(self.trace))


if __name__ == "__main__":
    items = [
        {"id": "q1", "skill": "loops", "difficulty": 0.4},
        {"id": "q2", "skill": "loops", "difficulty": 0.7},
        {"id": "q3", "skill": "functions", "difficulty": 0.5},
    ]
    llm = MockLLM().add_rule(r"Encourage the learner:", "Great progress — let's try a slightly harder one!")
    agent = EducationIntelligenceAgent(["loops", "functions"], items, llm=llm)
    result = agent.run({"skill": "loops", "correct": True})
    print("Next item:", result.output["next_item"]["id"])
    print("Mastery:", result.output["mastery"])
