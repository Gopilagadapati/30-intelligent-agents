"""Agent 04 - Knowledge Retrieval Agent / advanced RAG (Chapter 6).

Pattern: retrieve -> rerank -> generate. A query is embedded (bag-of-words here),
the most relevant chunks are retrieved from a corpus, reranked, and used to
ground the generated answer with citations.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import List, Tuple

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.memory import SemanticMemory
from common.llm import MockLLM


class KnowledgeRetrievalAgent(BaseAgent):
    def __init__(self, corpus: List[str], top_k: int = 3, llm=None):
        super().__init__(
            name="KnowledgeRetrievalAgent",
            system_prompt="Answer strictly from the provided sources and cite them as [n].",
            llm=llm,
        )
        self.top_k = top_k
        self.index = SemanticMemory()
        for i, doc in enumerate(corpus):
            self.index.store(doc, doc_id=i)
        self._corpus = corpus

    def retrieve(self, query: str) -> List[Tuple[str, float]]:
        return self.index.retrieve(query, k=self.top_k)

    def rerank(self, query: str, hits: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
        # secondary signal: reward exact term overlap with the query head
        head = set(query.lower().split()[:5])
        def boost(text: str) -> float:
            return sum(1 for w in head if w in text.lower()) * 0.05
        return sorted(((t, s + boost(t)) for t, s in hits), key=lambda x: x[1], reverse=True)

    def run(self, query: str) -> AgentResult:
        self.trace = []
        hits = self.rerank(query, self.retrieve(query))
        self._log(f"retrieved {len(hits)} chunks")
        sources = "\n".join(f"[{i+1}] {t}" for i, (t, _) in enumerate(hits))
        answer = self.think(f"SOURCES:\n{sources}\n\nQUESTION: {query}\nGrounded answer:")
        return AgentResult(
            output=answer,
            trace=list(self.trace),
            metadata={"sources": [t for t, _ in hits]},
        )


if __name__ == "__main__":
    corpus = [
        "The refund policy allows returns within 30 days of purchase.",
        "Premium members get free shipping on all orders.",
        "Support is available 24/7 via chat and email.",
    ]
    llm = MockLLM().add_rule(
        r"Grounded answer:",
        "You can return items within 30 days of purchase [1].",
    )
    agent = KnowledgeRetrievalAgent(corpus, llm=llm)
    result = agent.run("What is the return window for purchases?")
    print("Answer:", result.output)
    print("Top source:", result.metadata["sources"][0])
