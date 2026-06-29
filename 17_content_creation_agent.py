"""Agent 17 - Content Creation Agent (Chapter 10).

Pattern: structured content generation pipeline -- outline -> draft -> refine,
with multi-format (blog, social, email) adaptation from a single brief.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class ContentCreationAgent(BaseAgent):
    def __init__(self, llm=None):
        super().__init__(
            name="ContentCreationAgent",
            system_prompt="You are a versatile content creator producing clear, on-brand copy.",
            llm=llm,
        )

    def outline(self, brief: str) -> List[str]:
        raw = self.think(f"Create a 3-point outline for: {brief}\nOutline:")
        return [l.strip(" -.0123456789") for l in raw.splitlines() if l.strip()]

    def draft(self, outline: List[str]) -> str:
        return self.think("Write a draft from outline:\n" + "\n".join(outline) + "\nDraft:")

    def adapt(self, draft: str, fmt: str) -> str:
        return self.think(f"Rewrite for {fmt} format:\n{draft}\n{fmt}:")

    def run(self, brief: str, formats: List[str] = ("blog", "social")) -> AgentResult:
        self.trace = []
        outline = self.outline(brief)
        self._log(f"outline: {outline}")
        draft = self.draft(outline)
        variants: Dict[str, str] = {fmt: self.adapt(draft, fmt) for fmt in formats}
        return AgentResult(output=variants, trace=list(self.trace),
                           metadata={"outline": outline})


if __name__ == "__main__":
    llm = (
        MockLLM()
        .add_rule(r"Outline:", "1. Hook\n2. Benefits\n3. Call to action")
        .add_rule(r"Draft:", "Our new app saves you time. It's fast and simple. Try it today!")
        .add_rule(r"blog:", "Blog: Discover how our new app saves you hours every week...")
        .add_rule(r"social:", "Social: New app = more free time. Try it today! #productivity")
    )
    agent = ContentCreationAgent(llm=llm)
    result = agent.run("Announce our new productivity app", formats=["blog", "social"])
    for fmt, text in result.output.items():
        print(f"[{fmt}] {text}")
