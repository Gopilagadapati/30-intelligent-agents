"""Agent 24 - Healthcare Intelligence Agent (Chapter 13).

Pattern: clinical decision support using Bayesian reasoning over symptoms/findings.
The agent updates the probability of a condition given evidence and likelihood
ratios, then recommends next steps. Educational demo only -- not medical advice.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class HealthcareIntelligenceAgent(BaseAgent):
    def __init__(self, prior: float, likelihood_ratios: Dict[str, float], llm=None):
        super().__init__(
            name="HealthcareIntelligenceAgent",
            system_prompt="You provide clinical decision support. Always advise clinician confirmation.",
            llm=llm,
        )
        self.prior = prior
        self.lrs = likelihood_ratios

    def posterior(self, findings: Dict[str, bool]) -> float:
        # odds-form Bayesian update across independent findings
        odds = self.prior / (1 - self.prior)
        for finding, present in findings.items():
            lr = self.lrs.get(finding, 1.0)
            odds *= lr if present else (1.0 / lr if lr else 1.0)
        return round(odds / (1 + odds), 3)

    def run(self, findings: Dict[str, bool]) -> AgentResult:
        self.trace = []
        p = self.posterior(findings)
        self._log(f"posterior probability = {p}")
        risk = "high" if p >= 0.6 else "moderate" if p >= 0.3 else "low"
        rec = self.think(f"Posterior probability {p} ({risk} risk). Recommend next step:")
        return AgentResult(output={"probability": p, "risk": risk, "recommendation": rec},
                           trace=list(self.trace))


if __name__ == "__main__":
    # Sepsis-style screening demo
    lrs = {"fever": 2.0, "elevated_lactate": 4.0, "low_bp": 3.0, "high_wbc": 2.5}
    llm = MockLLM().add_rule(r"Recommend next step:", "Initiate sepsis bundle and obtain blood cultures; confirm with clinician.")
    agent = HealthcareIntelligenceAgent(prior=0.1, likelihood_ratios=lrs, llm=llm)
    result = agent.run({"fever": True, "elevated_lactate": True, "low_bp": True, "high_wbc": False})
    print("Probability:", result.output["probability"], "Risk:", result.output["risk"])
    print("Recommendation:", result.output["recommendation"])
