"""Agent 01 - Autonomous Decision-Making Agent (Chapter 5).

Pattern: the cognitive loop (perceive -> reason -> act) running until a goal is
reached or a step budget is exhausted. The agent independently chooses the next
action from a set of options without step-by-step human guidance.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class AutonomousDecisionAgent(BaseAgent):
    def __init__(self, goal: str, actions: List[str], max_steps: int = 6, llm=None):
        super().__init__(
            name="AutonomousDecisionAgent",
            system_prompt=(
                "You are an autonomous agent. Given the goal and current state, "
                "choose the single best next action. Reply with the action only."
            ),
            llm=llm,
        )
        self.goal = goal
        self.actions = actions
        self.max_steps = max_steps

    def decide(self, state: str) -> str:
        prompt = (
            f"GOAL: {self.goal}\nSTATE: {state}\n"
            f"AVAILABLE ACTIONS: {', '.join(self.actions)}\nNext action:"
        )
        choice = self.think(prompt).strip()
        # snap the (possibly noisy) LLM output onto a known action
        for a in self.actions:
            if a.lower() in choice.lower():
                return a
        return self.actions[-1]

    def run(self, observation: str) -> AgentResult:
        self.trace = []
        state = observation
        history: List[str] = []
        for step in range(1, self.max_steps + 1):
            action = self.decide(state)
            history.append(action)
            self._log(f"step {step}: state={state!r} -> action={action!r}")
            if action == "finish":
                break
            state = f"after {action} (step {step})"
        return AgentResult(
            output=history,
            trace=list(self.trace),
            metadata={"goal": self.goal, "steps": len(history)},
        )


def _demo_llm() -> MockLLM:
    scripted = iter(["gather_requirements", "draft_plan", "review", "finish"])

    def pick(_prompt: str) -> str:
        try:
            return next(scripted)
        except StopIteration:
            return "finish"

    return MockLLM().add_rule(r"Next action:", pick)


if __name__ == "__main__":
    agent = AutonomousDecisionAgent(
        goal="Produce a project proposal",
        actions=["gather_requirements", "draft_plan", "review", "finish"],
        llm=_demo_llm(),
    )
    result = agent.run("blank workspace")
    print("Action sequence:", result.output)
    print("\n".join(result.trace))
