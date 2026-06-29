"""Agent 03 - Memory-Augmented Agent (Chapter 5).

Pattern: combine working, episodic and semantic memory so the agent can carry
context within a task, recall past interactions, and ground answers in durable
facts. Demonstrated with a personalized assistant flow.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.memory import WorkingMemory, EpisodicMemory, SemanticMemory
from common.llm import MockLLM


class MemoryAugmentedAgent(BaseAgent):
    def __init__(self, llm=None):
        super().__init__(
            name="MemoryAugmentedAgent",
            system_prompt="You are an assistant that uses retrieved memory to personalize answers.",
            llm=llm,
        )
        self.working = WorkingMemory(capacity=5)
        self.episodic = EpisodicMemory()
        self.semantic = SemanticMemory()

    def remember_fact(self, fact: str, **meta) -> None:
        self.semantic.store(fact, **meta)

    def run(self, observation: str) -> AgentResult:
        self.trace = []
        self.working.add(observation)
        recalled = self.semantic.retrieve(observation, k=2)
        self._log(f"semantic recall: {recalled}")
        context = "; ".join(f for f, _ in recalled) or "(no prior facts)"
        prompt = f"CONTEXT: {context}\nUSER: {observation}\nAnswer:"
        answer = self.think(prompt)
        self.episodic.record(f"Q:{observation} | A:{answer}", tags=("dialog",))
        self._log(f"episodic size now {len(self.episodic.recent(99))}")
        return AgentResult(
            output=answer,
            trace=list(self.trace),
            metadata={"recalled": recalled, "working_set": self.working.all()},
        )


if __name__ == "__main__":
    llm = MockLLM().add_rule(
        r"Answer:",
        lambda p: "Based on your allergy to penicillin, I recommend an alternative."
        if "penicillin" in p.lower() else "Here is a general answer.",
    )
    agent = MemoryAugmentedAgent(llm=llm)
    agent.remember_fact("The patient is allergic to penicillin.", source="intake")
    agent.remember_fact("The patient prefers email contact.")
    result = agent.run("What antibiotic can I take for a sinus infection?")
    print("Answer:", result.output)
    print("Recalled:", result.metadata["recalled"])
