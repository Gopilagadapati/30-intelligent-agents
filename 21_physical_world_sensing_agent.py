"""Agent 21 - Physical World Sensing Agent (Chapter 11).

Pattern: integrate streaming IoT sensor data, detect anomalies against thresholds,
and reason about the physical situation to recommend an action.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class PhysicalWorldSensingAgent(BaseAgent):
    def __init__(self, thresholds: Dict[str, tuple], llm=None):
        super().__init__(
            name="PhysicalWorldSensingAgent",
            system_prompt="You monitor IoT sensors and recommend actions for anomalies.",
            llm=llm,
        )
        self.thresholds = thresholds  # name -> (low, high)

    def detect(self, reading: Dict[str, float]) -> List[str]:
        anomalies = []
        for sensor, value in reading.items():
            if sensor in self.thresholds:
                low, high = self.thresholds[sensor]
                if value < low or value > high:
                    anomalies.append(f"{sensor}={value} out of [{low},{high}]")
        return anomalies

    def run(self, reading: Dict[str, float]) -> AgentResult:
        self.trace = []
        anomalies = self.detect(reading)
        self._log(f"reading={reading} anomalies={anomalies}")
        if not anomalies:
            return AgentResult(output="All systems nominal.", trace=list(self.trace),
                               metadata={"anomalies": []})
        action = self.think(f"ANOMALIES: {anomalies}\nRecommended action:")
        return AgentResult(output=action, trace=list(self.trace), metadata={"anomalies": anomalies})


if __name__ == "__main__":
    thresholds = {"temp_c": (18, 27), "co2_ppm": (300, 1000), "humidity": (30, 60)}
    llm = MockLLM().add_rule(r"Recommended action:", "Activate HVAC cooling and increase ventilation.")
    agent = PhysicalWorldSensingAgent(thresholds, llm=llm)
    result = agent.run({"temp_c": 31.2, "co2_ppm": 1450, "humidity": 45})
    print("Anomalies:", result.metadata["anomalies"])
    print("Action:", result.output)
