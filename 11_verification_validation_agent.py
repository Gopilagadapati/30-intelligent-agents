"""Agent 11 - Verification and Validation Agent (Chapter 8).

Pattern: fact-check a claim against evidence and flag inconsistencies. The agent
decomposes a statement into atomic claims, checks each against a knowledge base,
and returns a verdict with support/contradiction evidence.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.memory import SemanticMemory
from common.llm import MockLLM


class VerificationValidationAgent(BaseAgent):
    def __init__(self, knowledge: List[str], llm=None):
        super().__init__(
            name="VerificationValidationAgent",
            system_prompt="Verify claims against evidence. Label each SUPPORTED, REFUTED or UNVERIFIED.",
            llm=llm,
        )
        self.kb = SemanticMemory()
        for fact in knowledge:
            self.kb.store(fact)

    def split_claims(self, statement: str) -> List[str]:
        return [c.strip() for c in re.split(r"[.;]\s*", statement) if c.strip()]

    def check(self, claim: str) -> Dict[str, object]:
        evidence = self.kb.retrieve(claim, k=1)
        if not evidence:
            return {"claim": claim, "verdict": "UNVERIFIED", "evidence": None}
        top, score = evidence[0]
        verdict = "SUPPORTED" if score >= 0.3 else "UNVERIFIED"
        return {"claim": claim, "verdict": verdict, "evidence": top, "score": score}

    def run(self, statement: str) -> AgentResult:
        self.trace = []
        results = [self.check(c) for c in self.split_claims(statement)]
        for r in results:
            self._log(f"{r['verdict']}: {r['claim']}")
        overall = "PASS" if all(r["verdict"] == "SUPPORTED" for r in results) else "REVIEW"
        return AgentResult(output={"verdict": overall, "claims": results}, trace=list(self.trace))


if __name__ == "__main__":
    kb = [
        "The Eiffel Tower is located in Paris, France.",
        "The Eiffel Tower was completed in 1889.",
    ]
    agent = VerificationValidationAgent(kb, llm=MockLLM())
    result = agent.run("The Eiffel Tower is in Paris. It was completed in 1889.")
    print("Overall:", result.output["verdict"])
    for c in result.output["claims"]:
        print(f"  {c['verdict']}: {c['claim']}")
