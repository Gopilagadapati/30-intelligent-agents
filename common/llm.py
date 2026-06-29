"""LLM abstraction layer.

Every agent talks to an ``LLM`` instance. By default a deterministic
``MockLLM`` is used so the agents run with **no API key and no network access**
(this mirrors the book's "Simulation Mode"). If an API key is present in the
environment and the relevant SDK is installed, ``get_llm`` returns a live
provider-backed client instead.
"""
from __future__ import annotations

import os
import re
import textwrap
from typing import Callable, Dict, List, Optional


class LLM:
    """Minimal chat interface shared by all providers."""

    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:  # pragma: no cover
        raise NotImplementedError

    def complete(self, prompt: str, system: Optional[str] = None, **kwargs) -> str:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        return self.chat(messages, **kwargs)


class MockLLM(LLM):
    """Deterministic, offline stand-in for a real LLM.

    Responses are derived from the prompt so output is reproducible and the
    agents remain fully runnable without external services. Custom rules can be
    registered to make a given agent's simulated reasoning more realistic.
    """

    def __init__(self, rules: Optional[List[tuple]] = None, persona: str = "assistant"):
        # rules: list of (compiled_regex, response_or_callable)
        self.rules = rules or []
        self.persona = persona

    def add_rule(self, pattern: str, response) -> "MockLLM":
        self.rules.append((re.compile(pattern, re.I | re.S), response))
        return self

    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        prompt = messages[-1]["content"] if messages else ""
        for pattern, response in self.rules:
            if pattern.search(prompt):
                return response(prompt) if callable(response) else response
        return self._default(prompt)

    def _default(self, prompt: str) -> str:
        snippet = textwrap.shorten(prompt.strip().replace("\n", " "), width=160)
        return f"[{self.persona}] Considering: {snippet}"


def get_llm(persona: str = "assistant", rules: Optional[List[tuple]] = None) -> LLM:
    """Return a live LLM if credentials/SDKs exist, otherwise a MockLLM."""
    provider = os.getenv("AGENT_LLM_PROVIDER", "").lower()
    try:
        if (provider == "openai" or os.getenv("OPENAI_API_KEY")) and provider != "mock":
            import openai  # type: ignore  # noqa: F401
            return _OpenAILLM()
        if (provider == "anthropic" or os.getenv("ANTHROPIC_API_KEY")) and provider != "mock":
            import anthropic  # type: ignore  # noqa: F401
            return _AnthropicLLM()
    except Exception:
        pass
    return MockLLM(rules=rules, persona=persona)


class _OpenAILLM(LLM):  # pragma: no cover - exercised only with a real key
    def __init__(self, model: str = "gpt-4o-mini"):
        import openai
        self.client = openai.OpenAI()
        self.model = model

    def chat(self, messages, **kwargs):
        resp = self.client.chat.completions.create(
            model=self.model, messages=messages, **kwargs
        )
        return resp.choices[0].message.content


class _AnthropicLLM(LLM):  # pragma: no cover - exercised only with a real key
    def __init__(self, model: str = "claude-3-5-sonnet-latest"):
        import anthropic
        self.client = anthropic.Anthropic()
        self.model = model

    def chat(self, messages, **kwargs):
        system = "\n".join(m["content"] for m in messages if m["role"] == "system")
        chat = [m for m in messages if m["role"] != "system"]
        resp = self.client.messages.create(
            model=self.model, system=system or None,
            messages=chat, max_tokens=kwargs.get("max_tokens", 1024),
        )
        return resp.content[0].text
