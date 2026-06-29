"""Memory subsystems used by the Memory-Augmented Agent (Ch.5) and reused widely.

Three memory types from the book:
* WorkingMemory  - short-term, bounded scratchpad for the current task.
* EpisodicMemory - time-ordered log of past interactions/events.
* SemanticMemory - durable facts with simple embedding-free vector recall.
"""
from __future__ import annotations

import math
import re
import time
from collections import Counter, deque
from dataclasses import dataclass, field
from typing import Any, Deque, Dict, List, Tuple


class WorkingMemory:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self._items: Deque[Any] = deque(maxlen=capacity)

    def add(self, item: Any) -> None:
        self._items.append(item)

    def all(self) -> List[Any]:
        return list(self._items)

    def clear(self) -> None:
        self._items.clear()


@dataclass
class Episode:
    content: str
    ts: float = field(default_factory=time.time)
    tags: Tuple[str, ...] = ()


class EpisodicMemory:
    def __init__(self):
        self._episodes: List[Episode] = []

    def record(self, content: str, tags: Tuple[str, ...] = ()) -> None:
        self._episodes.append(Episode(content=content, tags=tags))

    def recent(self, n: int = 5) -> List[Episode]:
        return self._episodes[-n:]

    def search(self, keyword: str) -> List[Episode]:
        k = keyword.lower()
        return [e for e in self._episodes if k in e.content.lower()]


def _tokens(text: str) -> Counter:
    return Counter(re.findall(r"[a-z0-9]+", text.lower()))


def _cosine(a: Counter, b: Counter) -> float:
    if not a or not b:
        return 0.0
    common = set(a) & set(b)
    dot = sum(a[t] * b[t] for t in common)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


class SemanticMemory:
    """Embedding-free semantic store using bag-of-words cosine similarity."""

    def __init__(self):
        self._facts: List[Tuple[str, Counter, Dict[str, Any]]] = []

    def store(self, fact: str, **meta: Any) -> None:
        self._facts.append((fact, _tokens(fact), meta))

    def retrieve(self, query: str, k: int = 3) -> List[Tuple[str, float]]:
        q = _tokens(query)
        scored = [(fact, _cosine(q, vec)) for fact, vec, _ in self._facts]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [(f, round(s, 3)) for f, s in scored[:k] if s > 0]
