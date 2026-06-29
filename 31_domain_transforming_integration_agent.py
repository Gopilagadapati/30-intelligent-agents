"""Agent 31 - Domain-Transforming Integration Agent (Chapter 16).

Pattern: cross-domain knowledge synthesis. The agent draws analogies between a
source domain and a target domain, transferring proven patterns to generate
novel solutions for complex-systems modeling.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.memory import SemanticMemory
from common.llm import MockLLM


class DomainTransformingIntegrationAgent(BaseAgent):
    def __init__(self, domain_patterns: Dict[str, List[str]], llm=None):
        super().__init__(
            name="DomainTransformingIntegrationAgent",
            system_prompt="You synthesize cross-domain analogies to solve novel problems.",
            llm=llm,
        )
        self.domain_patterns = domain_patterns
        self.index = SemanticMemory()
        for domain, patterns in domain_patterns.items():
            for p in patterns:
                self.index.store(p, domain=domain)

    def find_analogies(self, problem: str, k: int = 3) -> List[str]:
        return [t for t, _ in self.index.retrieve(problem, k=k)]

    def run(self, problem: str, target_domain: str) -> AgentResult:
        self.trace = []
        analogies = self.find_analogies(problem)
        self._log(f"analogies: {analogies}")
        solution = self.think(
            f"PROBLEM ({target_domain}): {problem}\n"
            f"ANALOGOUS PATTERNS: {analogies}\nTransferred solution:"
        )
        return AgentResult(output={"solution": solution, "analogies": analogies},
                           trace=list(self.trace))


if __name__ == "__main__":
    patterns = {
        "biology": ["ant colonies use pheromone trails for distributed routing",
                    "immune systems detect anomalies via pattern matching"],
        "economics": ["markets balance supply and demand via price signals"],
    }
    llm = MockLLM().add_rule(
        r"Transferred solution:",
        "Model network traffic routing on ant-colony pheromone trails for adaptive load balancing.",
    )
    agent = DomainTransformingIntegrationAgent(patterns, llm=llm)
    result = agent.run("Balance load across a data-center network dynamically", target_domain="distributed systems")
    print("Solution:", result.output["solution"])
    print("Drawn from:", result.output["analogies"])
