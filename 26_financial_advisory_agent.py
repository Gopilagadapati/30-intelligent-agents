"""Agent 26 - Financial Advisory Agent (Chapter 14).

Pattern: market analysis + risk assessment + personalized planning, with
compliance guardrails baked into the architecture (suitability checks before any
recommendation). Educational demo only -- not financial advice.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM

RISK_ALLOCATIONS = {
    "conservative": {"bonds": 0.7, "stocks": 0.2, "cash": 0.1},
    "moderate": {"bonds": 0.4, "stocks": 0.5, "cash": 0.1},
    "aggressive": {"bonds": 0.1, "stocks": 0.85, "cash": 0.05},
}


class FinancialAdvisoryAgent(BaseAgent):
    def __init__(self, llm=None):
        super().__init__(
            name="FinancialAdvisoryAgent",
            system_prompt="You give compliant, suitability-checked financial guidance with disclaimers.",
            llm=llm,
        )

    def risk_profile(self, client: Dict[str, object]) -> str:
        score = 0
        score += {"low": 0, "medium": 1, "high": 2}.get(client.get("risk_tolerance", "low"), 0)
        score += 1 if client.get("horizon_years", 0) >= 10 else 0
        score += 1 if client.get("age", 99) < 40 else 0
        return ["conservative", "moderate", "aggressive"][min(score, 2)]

    def suitability_ok(self, client: Dict[str, object]) -> bool:
        # compliance guardrail: never recommend aggressive to near-retirement clients
        return not (client.get("age", 0) >= 60 and client.get("risk_tolerance") == "high")

    def run(self, client: Dict[str, object]) -> AgentResult:
        self.trace = []
        if not self.suitability_ok(client):
            self._log("suitability check failed; defaulting to conservative")
            profile = "conservative"
        else:
            profile = self.risk_profile(client)
        allocation = RISK_ALLOCATIONS[profile]
        self._log(f"profile={profile} allocation={allocation}")
        rationale = self.think(f"CLIENT: {client}\nPROFILE: {profile}\nExplain the allocation:")
        return AgentResult(
            output={"profile": profile, "allocation": allocation,
                    "rationale": rationale,
                    "disclaimer": "Educational only; consult a licensed advisor."},
            trace=list(self.trace),
        )


if __name__ == "__main__":
    llm = MockLLM().add_rule(r"Explain the allocation:", "A balanced mix suits your 15-year horizon and moderate tolerance.")
    agent = FinancialAdvisoryAgent(llm=llm)
    client = {"age": 35, "risk_tolerance": "medium", "horizon_years": 15}
    result = agent.run(client)
    print("Profile:", result.output["profile"])
    print("Allocation:", result.output["allocation"])
