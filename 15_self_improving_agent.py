"""Agent 15 - Self-Improving Agent (Chapter 9).

Pattern: learn from user feedback. The agent stores feedback on past answers and
adapts future behavior by retrieving relevant lessons and adjusting a policy
weight. Demonstrates a lightweight online-learning loop.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.memory import EpisodicMemory, SemanticMemory
from common.llm import MockLLM


class SelfImprovingAgent(BaseAgent):
    def __init__(self, llm=None):
        super().__init__(
            name="SelfImprovingAgent",
            system_prompt="You answer questions and incorporate prior feedback to improve.",
            llm=llm,
        )
        self.lessons = SemanticMemory()
        self.history = EpisodicMemory()
        self.style_weight = 0.5  # 0 = terse, 1 = detailed

    def answer(self, question: str) -> str:
        lessons = self.lessons.retrieve(question, k=2)
        hint = "; ".join(l for l, _ in lessons) or "(no lessons yet)"
        style = "detailed" if self.style_weight >= 0.5 else "concise"
        return self.think(f"LESSONS: {hint}\nSTYLE: {style}\nQ: {question}\nA:")

    def give_feedback(self, question: str, answer: str, rating: int, note: str) -> None:
        self.history.record(f"Q:{question} A:{answer} rating:{rating}")
        if rating < 3:
            self.lessons.store(f"For questions like '{question}': {note}")
            # adapt style based on feedback direction
            if "more detail" in note.lower():
                self.style_weight = min(1.0, self.style_weight + 0.25)
            elif "too long" in note.lower():
                self.style_weight = max(0.0, self.style_weight - 0.25)

    def run(self, question: str) -> AgentResult:
        self.trace = []
        ans = self.answer(question)
        self._log(f"answered with style_weight={self.style_weight}")
        return AgentResult(output=ans, trace=list(self.trace),
                           metadata={"style_weight": self.style_weight})


if __name__ == "__main__":
    llm = MockLLM().add_rule(
        r"\nA:",
        lambda p: "Detailed explanation..." if "detailed" in p else "Short answer.",
    )
    agent = SelfImprovingAgent(llm=llm)
    q = "How does TCP work?"
    first = agent.run(q)
    print("Before feedback:", first.output, "| weight", first.metadata["style_weight"])
    agent.give_feedback(q, first.output, rating=2, note="Please give more detail.")
    second = agent.run(q)
    print("After feedback:", second.output, "| weight", second.metadata["style_weight"])
