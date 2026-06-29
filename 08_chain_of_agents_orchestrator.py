"""Agent 08 - Chain-of-Agents Orchestrator (Chapter 7).

Pattern: a coordinator routes a task to specialist sub-agents and delegates work
in sequence (or by routing rules), passing each output forward. Demonstrated
with a research -> writer -> editor chain.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable, Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class Specialist(BaseAgent):
    def __init__(self, name: str, role: str, llm=None):
        super().__init__(name=name, system_prompt=role, llm=llm)

    def handle(self, payload: str) -> str:
        return self.think(f"[{self.name}] {payload}")


class ChainOfAgentsOrchestrator(BaseAgent):
    def __init__(self, specialists: List[Specialist], llm=None):
        super().__init__(name="Orchestrator", system_prompt="Route and delegate tasks.", llm=llm)
        self.specialists = specialists

    def route(self, task: str) -> List[Specialist]:
        # Simple policy: run the full chain in order. A real router could pick
        # a subset based on task classification.
        return self.specialists

    def run(self, task: str) -> AgentResult:
        self.trace = []
        payload = task
        for spec in self.route(task):
            payload = spec.handle(payload)
            self._log(f"{spec.name} -> {payload!r}")
        return AgentResult(output=payload, trace=list(self.trace))


if __name__ == "__main__":
    researcher = Specialist("Researcher", "Gather key facts.",
                            MockLLM().add_rule(r".*", lambda p: "facts: EVs cut emissions 50%"))
    writer = Specialist("Writer", "Draft prose.",
                        MockLLM().add_rule(r".*", lambda p: "Draft: EVs reduce emissions significantly."))
    editor = Specialist("Editor", "Polish text.",
                        MockLLM().add_rule(r".*", lambda p: "Final: Electric vehicles cut emissions by ~50%."))
    orch = ChainOfAgentsOrchestrator([researcher, writer, editor])
    print(orch.run("Write a sentence about EV emissions.").output)
