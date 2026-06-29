"""Agent 05 - Document Intelligence Agent (Chapter 6).

Pattern: the five-stage document intelligence pipeline:
ingest -> parse/segment -> extract -> structure -> summarize.
Turns an unstructured document into structured fields plus a summary.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class DocumentIntelligenceAgent(BaseAgent):
    def __init__(self, llm=None):
        super().__init__(
            name="DocumentIntelligenceAgent",
            system_prompt="Extract structured information from documents and summarize them.",
            llm=llm,
        )

    # stage 1
    def ingest(self, document: str) -> str:
        return document.strip()

    # stage 2
    def segment(self, text: str) -> List[str]:
        return [s.strip() for s in re.split(r"\n\s*\n", text) if s.strip()]

    # stage 3
    def extract(self, text: str) -> Dict[str, str]:
        fields = {}
        for key, pat in {
            "invoice_no": r"invoice\s*#?\s*([A-Z0-9-]+)",
            "date": r"date[:\s]+([0-9]{4}-[0-9]{2}-[0-9]{2})",
            "total": r"total[:\s]+\$?([0-9,]+\.?[0-9]*)",
        }.items():
            m = re.search(pat, text, re.I)
            if m:
                fields[key] = m.group(1)
        return fields

    # stage 4 + 5
    def run(self, document: str) -> AgentResult:
        self.trace = []
        text = self.ingest(document)
        segments = self.segment(text)
        self._log(f"segmented into {len(segments)} blocks")
        fields = self.extract(text)
        self._log(f"extracted fields: {fields}")
        summary = self.think(f"Summarize this document in one sentence:\n{text}")
        structured = {"fields": fields, "summary": summary, "n_segments": len(segments)}
        return AgentResult(output=structured, trace=list(self.trace))


if __name__ == "__main__":
    doc = """
    ACME Corp Invoice #INV-2045

    Date: 2026-03-14
    Services rendered: consulting

    Total: $4,250.00
    """
    llm = MockLLM().add_rule(r"Summarize", "Invoice INV-2045 from ACME Corp for $4,250 of consulting.")
    agent = DocumentIntelligenceAgent(llm=llm)
    result = agent.run(doc)
    print("Structured:", result.output)
