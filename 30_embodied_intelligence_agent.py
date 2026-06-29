"""Agent 30 - Embodied Intelligence Agent (Chapter 16).

Pattern: the perception-action loop for a physical/robotic agent. The agent reads
sensors, updates a world model, plans toward a goal pose, and emits motor
commands -- iterating until the goal is reached. Uses a simple grid world.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Tuple

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class EmbodiedIntelligenceAgent(BaseAgent):
    MOVES = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}

    def __init__(self, obstacles: set = None, max_steps: int = 20, llm=None):
        super().__init__(
            name="EmbodiedIntelligenceAgent",
            system_prompt="You control a robot navigating a grid via a perception-action loop.",
            llm=llm,
        )
        self.obstacles = obstacles or set()
        self.max_steps = max_steps

    def plan_move(self, pos: Tuple[int, int], goal: Tuple[int, int]) -> str:
        # greedy action selection reducing Manhattan distance, avoiding obstacles
        best, best_d = None, None
        for name, (dx, dy) in self.MOVES.items():
            nxt = (pos[0] + dx, pos[1] + dy)
            if nxt in self.obstacles:
                continue
            d = abs(nxt[0] - goal[0]) + abs(nxt[1] - goal[1])
            if best_d is None or d < best_d:
                best, best_d = name, d
        return best or "wait"

    def run(self, start: Tuple[int, int], goal: Tuple[int, int]) -> AgentResult:
        self.trace = []
        pos = start
        actions: List[str] = []
        for step in range(self.max_steps):
            if pos == goal:
                break
            move = self.plan_move(pos, goal)  # action
            dx, dy = self.MOVES.get(move, (0, 0))
            pos = (pos[0] + dx, pos[1] + dy)   # actuate + perceive new state
            actions.append(move)
            self._log(f"step {step}: move {move} -> {pos}")
        return AgentResult(output=actions, trace=list(self.trace),
                           metadata={"reached": pos == goal, "final": pos})


if __name__ == "__main__":
    agent = EmbodiedIntelligenceAgent(obstacles={(1, 0), (1, 1)})
    result = agent.run(start=(0, 0), goal=(2, 2))
    print("Actions:", result.output)
    print("Reached goal:", result.metadata["reached"])
