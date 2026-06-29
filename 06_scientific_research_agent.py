"""Agent 06 - Scientific Research Agent (Chapter 6).

Pattern: research workflow as a cognitive loop -- search literature, synthesize
findings, identify gaps, and generate testable hypotheses. Demonstrated with a
small in-memory literature corpus.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.memory import SemanticMemory
from common.llm import MockLLM


class ScientificResearchAgent(BaseAgent):
    def __init__(self, papers: List[Dict[str, str]], llm=None):
        super().__init__(
            name="ScientificResearchAgent",
            system_prompt="You are a research assistant performing literature review and hypothesis generation.",
            llm=llm,
        )
        self.papers = papers
        self.index = SemanticMemory()
        for p in papers:
            self.index.store(f"{p['title']}. {p['abstract']}", title=p["title"])

    def review(self, topic: str, k: int = 3) -> List[str]:
        hits = self.index.retrieve(topic, k=k)
        return [t for t, _ in hits]

    def synthesize(self, findings: List[str]) -> str:
        joined = "\n".join(f"- {f}" for f in findings)
        return self.think(f"Synthesize these findings:\n{joined}\nSynthesis:")

    def hypothesize(self, synthesis: str) -> str:
        return self.think(f"Given: {synthesis}\nPropose one testable hypothesis:")

    def run(self, topic: str) -> AgentResult:
        self.trace = []
        findings = self.review(topic)
        self._log(f"reviewed {len(findings)} papers")
        synthesis = self.synthesize(findings)
        hypothesis = self.hypothesize(synthesis)
        return AgentResult(
            output={"synthesis": synthesis, "hypothesis": hypothesis},
            trace=list(self.trace),
            metadata={"papers": findings},
        )


if __name__ == "__main__":
    papers = [
        {"title": "Gut microbiome and immunity", "abstract": "Microbiome diversity correlates with immune resilience."},
        {"title": "Diet effects on gut flora", "abstract": "High-fiber diets increase microbial diversity."},
        {"title": "Probiotics review", "abstract": "Probiotic supplementation shows mixed immune outcomes."},
    ]
    llm = (
        MockLLM()
        .add_rule(r"Synthesis:", "Diet-driven microbiome diversity may strengthen immunity.")
        .add_rule(r"testable hypothesis", "A 12-week high-fiber diet increases immune marker IgA vs control.")
    )
    agent = ScientificResearchAgent(papers, llm=llm)
    result = agent.run("microbiome diversity and immune function")
    print("Hypothesis:", result.output["hypothesis"])
