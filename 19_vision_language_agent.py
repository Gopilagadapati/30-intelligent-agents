"""Agent 19 - Vision-Language Agent (Chapter 11).

Pattern: image understanding by fusing a (simulated) vision encoder's structured
perception with language reasoning. Real deployments swap the MockVisionEncoder
for a model like CLIP/GPT-4o-vision; the agent logic is unchanged.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class MockVisionEncoder:
    """Stand-in for a vision model. Returns structured perception for an image id."""

    _scenes = {
        "img_street.jpg": {"objects": ["car", "pedestrian", "traffic_light"], "scene": "urban street", "colors": ["red", "gray"]},
        "img_xray.png": {"objects": ["ribcage", "opacity_lower_left"], "scene": "chest x-ray", "colors": ["gray"]},
    }

    def perceive(self, image_id: str) -> Dict[str, object]:
        return self._scenes.get(image_id, {"objects": [], "scene": "unknown", "colors": []})


class VisionLanguageAgent(BaseAgent):
    def __init__(self, encoder: MockVisionEncoder = None, llm=None):
        super().__init__(
            name="VisionLanguageAgent",
            system_prompt="You answer questions about images using structured visual perception.",
            llm=llm,
        )
        self.encoder = encoder or MockVisionEncoder()

    def run(self, image_id: str, question: str) -> AgentResult:
        self.trace = []
        perception = self.encoder.perceive(image_id)
        self._log(f"perception: {perception}")
        answer = self.think(
            f"VISUAL FACTS: {perception}\nQUESTION: {question}\nAnswer:"
        )
        return AgentResult(output=answer, trace=list(self.trace), metadata={"perception": perception})


if __name__ == "__main__":
    llm = MockLLM().add_rule(
        r"Answer:",
        lambda p: "Yes, there is a pedestrian near a traffic light." if "pedestrian" in p else "I don't see that.",
    )
    agent = VisionLanguageAgent(llm=llm)
    result = agent.run("img_street.jpg", "Is there a pedestrian in the image?")
    print("Answer:", result.output)
    print("Detected:", result.metadata["perception"]["objects"])
