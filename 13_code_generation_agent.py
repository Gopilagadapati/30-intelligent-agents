"""Agent 13 - Code-Generation Agent (Chapter 9).

Pattern: program synthesis with a generate-test-repair loop. The agent writes a
function from a spec, runs the provided unit tests in a sandboxed namespace, and
retries with the failure feedback until tests pass or attempts run out.
"""
from __future__ import annotations

import sys
import traceback
from pathlib import Path
from typing import Callable, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class CodeGenerationAgent(BaseAgent):
    def __init__(self, max_attempts: int = 3, llm=None):
        super().__init__(
            name="CodeGenerationAgent",
            system_prompt="You write correct Python functions from a specification and tests.",
            llm=llm,
        )
        self.max_attempts = max_attempts

    def generate(self, spec: str, feedback: str = "") -> str:
        prompt = f"SPEC: {spec}\n{('PREVIOUS ERROR: ' + feedback) if feedback else ''}\nPython code:"
        return self.think(prompt)

    def _run_tests(self, code: str, tests: Callable[[dict], None]) -> str:
        ns: dict = {}
        exec(code, ns)
        tests(ns)
        return "ok"

    def run(self, spec: str, tests: Callable[[dict], None]) -> AgentResult:
        self.trace = []
        feedback = ""
        for attempt in range(1, self.max_attempts + 1):
            code = self.generate(spec, feedback)
            try:
                self._run_tests(code, tests)
                self._log(f"attempt {attempt}: tests passed")
                return AgentResult(output=code, trace=list(self.trace),
                                   metadata={"attempts": attempt, "passed": True})
            except Exception:
                feedback = traceback.format_exc().splitlines()[-1]
                self._log(f"attempt {attempt} failed: {feedback}")
        return AgentResult(output=code, trace=list(self.trace),
                           metadata={"attempts": self.max_attempts, "passed": False})


if __name__ == "__main__":
    attempts = iter([
        "def add(a, b):\n    return a - b",      # buggy first attempt
        "def add(a, b):\n    return a + b",      # fixed
    ])
    llm = MockLLM().add_rule(r"Python code:", lambda p: next(attempts, "def add(a,b):\n    return a+b"))

    def tests(ns):
        assert ns["add"](2, 3) == 5
        assert ns["add"](-1, 1) == 0

    agent = CodeGenerationAgent(llm=llm)
    result = agent.run("Write add(a, b) returning the sum.", tests)
    print("Passed:", result.metadata["passed"], "in", result.metadata["attempts"], "attempts")
    print(result.output)
