"""Agent 07 - Tool-Using Agent (Chapter 7).

Pattern: function-calling via a selection funnel -- the agent inspects the tool
catalog, selects a tool, fills arguments, invokes it, and incorporates the
result. Includes a simple recovery path for failed selections.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult, ToolRegistry
from common.llm import MockLLM


class ToolUsingAgent(BaseAgent):
    def __init__(self, registry: ToolRegistry, llm=None):
        super().__init__(
            name="ToolUsingAgent",
            system_prompt=(
                "You can call tools. Reply with JSON: {\"tool\": name, \"args\": {...}}. "
                "Choose the single best tool for the request."
            ),
            llm=llm,
        )
        self.registry = registry

    def select(self, request: str) -> dict:
        catalog = self.registry.catalog()
        raw = self.think(f"TOOLS:\n{catalog}\n\nREQUEST: {request}\nJSON:")
        m = re.search(r"\{.*\}", raw, re.S)
        if not m:
            raise ValueError("no tool selected")
        return json.loads(m.group(0))

    def run(self, request: str) -> AgentResult:
        self.trace = []
        try:
            call = self.select(request)
            self._log(f"selected {call}")
            result = self.registry.invoke(call["tool"], **call.get("args", {}))
        except Exception as exc:  # recovery strategy
            self._log(f"recovery after error: {exc}")
            result = f"Could not complete request ({exc})."
        return AgentResult(output=result, trace=list(self.trace))


def build_registry() -> ToolRegistry:
    reg = ToolRegistry()
    reg.add("add", lambda a, b: a + b, "add two numbers")
    reg.add("weather", lambda city: f"Sunny in {city}, 24C", "get weather for a city")
    return reg


if __name__ == "__main__":
    reg = build_registry()
    llm = MockLLM().add_rule(r"JSON:", '{"tool": "weather", "args": {"city": "Ottawa"}}')
    agent = ToolUsingAgent(reg, llm=llm)
    print(agent.run("What's the weather in Ottawa?").output)
