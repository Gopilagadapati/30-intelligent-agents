"""Agent 27 - Legal Intelligence Agent (Chapter 14).

Pattern: legal knowledge-base integration with hallucination-proofing -- every
answer must cite a retrieved clause/precedent or explicitly say it cannot find
support. Demonstrated with contract-clause analysis.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Tuple

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.memory import SemanticMemory
from common.llm import MockLLM


class LegalIntelligenceAgent(BaseAgent):
    def __init__(self, corpus: List[Dict[str, str]], min_score: float = 0.2, llm=None):
        super().__init__(
            name="LegalIntelligenceAgent",
            system_prompt="Answer only with cited authority. If no source supports it, say so.",
            llm=llm,
        )
        self.min_score = min_score
        self.index = SemanticMemory()
        for c in corpus:
            self.index.store(c["text"], cite=c["cite"])
        self._corpus = {c["text"]: c["cite"] for c in corpus}

    def run(self, question: str) -> AgentResult:
        self.trace = []
        hits = self.index.retrieve(question, k=2)
        self._log(f"retrieved: {hits}")
        grounded = [(t, s) for t, s in hits if s >= self.min_score]
        if not grounded:
            return AgentResult(output="No supporting authority found; cannot answer.",
                               trace=list(self.trace), metadata={"citations": []})
        sources = "\n".join(f"- {t} (cite: {self._corpus[t]})" for t, _ in grounded)
        answer = self.think(f"SOURCES:\n{sources}\nQUESTION: {question}\nCited answer:")
        return AgentResult(output=answer, trace=list(self.trace),
                           metadata={"citations": [self._corpus[t] for t, _ in grounded]})


if __name__ == "__main__":
    corpus = [
        {"text": "Either party may terminate this agreement with 30 days written notice.", "cite": "Sec 8.1"},
        {"text": "Confidential information must be protected for five years post-termination.", "cite": "Sec 9.2"},
    ]
    llm = MockLLM().add_rule(r"Cited answer:", "You may terminate with 30 days' written notice (Sec 8.1).")
    agent = LegalIntelligenceAgent(corpus, llm=llm)
    result = agent.run("How can the contract be terminated?")
    print("Answer:", result.output)
    print("Citations:", result.metadata["citations"])
