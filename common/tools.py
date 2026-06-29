"""Tool registry + function-calling support for the Tool-Using Agent (Ch.7)."""
from __future__ import annotations

import inspect
from dataclasses import dataclass
from typing import Any, Callable, Dict, List


@dataclass
class Tool:
    name: str
    description: str
    func: Callable[..., Any]

    def signature(self) -> str:
        return f"{self.name}{inspect.signature(self.func)} - {self.description}"

    def __call__(self, *args, **kwargs) -> Any:
        return self.func(*args, **kwargs)


class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Tool] = {}

    def register(self, name: str, description: str = ""):
        def deco(func: Callable[..., Any]) -> Callable[..., Any]:
            self._tools[name] = Tool(name=name, description=description or func.__doc__ or "", func=func)
            return func
        return deco

    def add(self, name: str, func: Callable[..., Any], description: str = "") -> None:
        self._tools[name] = Tool(name=name, description=description or func.__doc__ or "", func=func)

    def get(self, name: str) -> Tool:
        return self._tools[name]

    def names(self) -> List[str]:
        return list(self._tools)

    def catalog(self) -> str:
        return "\n".join(t.signature() for t in self._tools.values())

    def invoke(self, name: str, **kwargs) -> Any:
        if name not in self._tools:
            raise KeyError(f"unknown tool: {name}")
        return self._tools[name](**kwargs)
