"""Agent 09 - Agentic Workflow System (Chapter 7).

Pattern: a multi-step workflow engine with human-in-the-loop checkpoints. Steps
run automatically until a step is flagged for human approval, which gates
continuation. Supports approve/reject.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable, Dict, List, Optional

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class WorkflowStep:
    def __init__(self, name: str, run: Callable[[dict], str], requires_approval: bool = False):
        self.name = name
        self.run = run
        self.requires_approval = requires_approval


class AgenticWorkflowSystem(BaseAgent):
    def __init__(self, steps: List[WorkflowStep], approver: Optional[Callable[[str, str], bool]] = None, llm=None):
        super().__init__(name="WorkflowSystem", system_prompt="Execute multi-step workflows.", llm=llm)
        self.steps = steps
        # default approver auto-approves; pass a callable for real HITL
        self.approver = approver or (lambda step, output: True)

    def run(self, initial: dict) -> AgentResult:
        self.trace = []
        ctx = dict(initial)
        for step in self.steps:
            output = step.run(ctx)
            ctx[step.name] = output
            self._log(f"{step.name}: {output!r}")
            if step.requires_approval:
                approved = self.approver(step.name, output)
                self._log(f"approval for {step.name}: {approved}")
                if not approved:
                    return AgentResult(output=ctx, trace=list(self.trace),
                                       metadata={"halted_at": step.name})
        return AgentResult(output=ctx, trace=list(self.trace), metadata={"completed": True})


if __name__ == "__main__":
    steps = [
        WorkflowStep("draft", lambda c: f"draft for {c['topic']}"),
        WorkflowStep("review", lambda c: f"reviewed: {c['draft']}", requires_approval=True),
        WorkflowStep("publish", lambda c: f"published: {c['review']}"),
    ]
    system = AgenticWorkflowSystem(steps, approver=lambda s, o: "draft" in o)
    result = system.run({"topic": "Q3 report"})
    print("Final context:", result.output)
    print("Meta:", result.metadata)
