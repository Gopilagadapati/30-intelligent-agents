"""Base agent implementing the cognitive loop from Chapter 1.

The cognitive loop is: perceive -> reason -> (optionally act) -> respond.
Concrete agents override the hooks they need.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .llm import LLM, get_llm


@dataclass
class Message:
    role: str
    content: str


@dataclass
class AgentResult:
    output: Any
    trace: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __str__(self) -> str:  # friendly printing in demos
        return str(self.output)


class BaseAgent:
    """Common skeleton: name, system prompt, llm, and a cognitive loop."""

    def __init__(self, name: str, system_prompt: str = "", llm: Optional[LLM] = None):
        self.name = name
        self.system_prompt = system_prompt
        self.llm = llm or get_llm(persona=name)
        self.trace: List[str] = []

    # --- cognitive loop hooks -------------------------------------------------
    def perceive(self, observation: Any) -> Any:
        """Normalize raw input into the agent's internal representation."""
        return observation

    def reason(self, perception: Any) -> Any:
        """Decide what to do. Default: a single LLM call."""
        return self.think(str(perception))

    def act(self, decision: Any) -> Any:
        """Carry out the decision. Default: passthrough."""
        return decision

    def run(self, observation: Any) -> AgentResult:
        self.trace = []
        perception = self.perceive(observation)
        self._log(f"perceive: {perception!r}")
        decision = self.reason(perception)
        self._log(f"reason: {decision!r}")
        output = self.act(decision)
        self._log(f"act: {output!r}")
        return AgentResult(output=output, trace=list(self.trace))

    # --- helpers --------------------------------------------------------------
    def think(self, prompt: str, **kwargs) -> str:
        return self.llm.complete(prompt, system=self.system_prompt, **kwargs)

    def _log(self, msg: str) -> None:
        self.trace.append(f"[{self.name}] {msg}")
