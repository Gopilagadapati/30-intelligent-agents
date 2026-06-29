"""Agent 22 - Ethical Reasoning Agent (Chapter 12).

Pattern: value-alignment framework. A proposed action is evaluated against a set
of ethical principles; conflicts are surfaced and the agent recommends approve,
revise, or reject with justification.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM

PRINCIPLES = {
    "non_maleficence": "Do not cause harm.",
    "autonomy": "Respect user choice and consent.",
    "fairness": "Avoid bias and discrimination.",
    "transparency": "Be honest about capabilities and limitations.",
    "privacy": "Protect personal data.",
}


class EthicalReasoningAgent(BaseAgent):
    def __init__(self, principles: Dict[str, str] = None, llm=None):
        super().__init__(
            name="EthicalReasoningAgent",
            system_prompt="You evaluate actions against ethical principles and flag conflicts.",
            llm=llm,
        )
        self.principles = principles or PRINCIPLES

    def evaluate(self, action: str) -> Dict[str, str]:
        verdicts = {}
        for name, desc in self.principles.items():
            verdicts[name] = self.think(
                f"PRINCIPLE: {desc}\nACTION: {action}\nDoes the action comply? Answer COMPLY or VIOLATE with reason:"
            )
        return verdicts

    def run(self, action: str) -> AgentResult:
        self.trace = []
        verdicts = self.evaluate(action)
        violations = [k for k, v in verdicts.items() if "VIOLATE" in v.upper()]
        for k, v in verdicts.items():
            self._log(f"{k}: {v}")
        decision = "REJECT" if violations else "APPROVE"
        return AgentResult(output={"decision": decision, "violations": violations, "detail": verdicts},
                           trace=list(self.trace))


if __name__ == "__main__":
    llm = MockLLM().add_rule(
        r"COMPLY or VIOLATE",
        lambda p: "VIOLATE - sells data without consent" if "personal data" in p.lower() and "sell" in p.lower() else "COMPLY",
    )
    agent = EthicalReasoningAgent(llm=llm)
    result = agent.run("Sell users' location data to advertisers without asking.")
    print("Decision:", result.output["decision"])
    print("Violations:", result.output["violations"])
