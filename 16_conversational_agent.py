"""Agent 16 - Conversational Agent (Chapter 10).

Pattern: multi-turn dialog management with persona modeling and state tracking.
Maintains conversation history, tracks simple dialog state (slots), and responds
in a configured persona.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult, Message
from common.llm import MockLLM


class ConversationalAgent(BaseAgent):
    def __init__(self, persona: str = "a friendly support agent", slots: List[str] = None, llm=None):
        super().__init__(
            name="ConversationalAgent",
            system_prompt=f"You are {persona}. Be helpful and stay in character.",
            llm=llm,
        )
        self.persona = persona
        self.history: List[Message] = []
        self.slots: Dict[str, str] = {s: "" for s in (slots or [])}

    def _update_slots(self, text: str) -> None:
        for slot in self.slots:
            if slot in text.lower() and not self.slots[slot]:
                # naive slot fill: capture the word after the slot name
                words = text.lower().split()
                if slot in words:
                    idx = words.index(slot)
                    if idx + 1 < len(words):
                        self.slots[slot] = words[idx + 1]

    def run(self, user_turn: str) -> AgentResult:
        self.trace = []
        self.history.append(Message("user", user_turn))
        self._update_slots(user_turn)
        context = "\n".join(f"{m.role}: {m.content}" for m in self.history[-6:])
        reply = self.think(f"PERSONA: {self.persona}\nSLOTS: {self.slots}\n{context}\nassistant:")
        self.history.append(Message("assistant", reply))
        self._log(f"slots={self.slots}")
        return AgentResult(output=reply, trace=list(self.trace), metadata={"slots": dict(self.slots)})


if __name__ == "__main__":
    llm = MockLLM().add_rule(r"assistant:", "Happy to help! Could you share your order number?")
    agent = ConversationalAgent(persona="a cheerful support rep", slots=["order"], llm=llm)
    print(agent.run("Hi, I have a problem with order 12345").output)
    print(agent.run("It hasn't arrived").metadata)
