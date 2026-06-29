"""Agent 29 - Collective Intelligence Agent (Chapter 15).

Pattern: multi-agent collaboration with a consensus mechanism. Several agents
independently answer; their outputs are aggregated (majority vote / weighted
confidence) to produce an emergent decision more robust than any single agent.
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class Voter(BaseAgent):
    def __init__(self, name: str, confidence: float, llm=None):
        super().__init__(name=name, system_prompt="Answer the question with a single label.", llm=llm)
        self.confidence = confidence

    def vote(self, question: str) -> Tuple[str, float]:
        return self.think(question).strip(), self.confidence


class CollectiveIntelligenceAgent(BaseAgent):
    def __init__(self, voters: List[Voter], llm=None):
        super().__init__(name="CollectiveIntelligenceAgent", system_prompt="Aggregate member opinions into consensus.", llm=llm)
        self.voters = voters

    def run(self, question: str) -> AgentResult:
        self.trace = []
        weighted: Counter = Counter()
        votes = []
        for v in self.voters:
            label, conf = v.vote(question)
            weighted[label] += conf
            votes.append((v.name, label, conf))
            self._log(f"{v.name} -> {label} ({conf})")
        consensus, score = weighted.most_common(1)[0]
        agreement = round(score / sum(weighted.values()), 3)
        return AgentResult(output={"consensus": consensus, "agreement": agreement, "votes": votes},
                           trace=list(self.trace))


if __name__ == "__main__":
    voters = [
        Voter("A", 0.9, MockLLM().add_rule(r".*", "approve")),
        Voter("B", 0.6, MockLLM().add_rule(r".*", "approve")),
        Voter("C", 0.8, MockLLM().add_rule(r".*", "reject")),
    ]
    agent = CollectiveIntelligenceAgent(voters)
    result = agent.run("Should we approve this loan application?")
    print("Consensus:", result.output["consensus"], "Agreement:", result.output["agreement"])
