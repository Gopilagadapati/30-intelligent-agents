"""Agent 10 - Data Analysis Agent (Chapter 8).

Pattern: explore a dataset, compute descriptive statistics, and recommend an
appropriate visualization based on the data shape -- then narrate insights.
Uses only the standard library so it runs anywhere.
"""
from __future__ import annotations

import statistics
import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class DataAnalysisAgent(BaseAgent):
    def __init__(self, llm=None):
        super().__init__(
            name="DataAnalysisAgent",
            system_prompt="Analyze tabular data and explain insights for a non-technical audience.",
            llm=llm,
        )

    def profile(self, columns: Dict[str, List[float]]) -> Dict[str, dict]:
        prof = {}
        for name, values in columns.items():
            nums = [v for v in values if isinstance(v, (int, float))]
            if nums:
                prof[name] = {
                    "type": "numeric",
                    "mean": round(statistics.mean(nums), 3),
                    "stdev": round(statistics.pstdev(nums), 3),
                    "min": min(nums),
                    "max": max(nums),
                }
            else:
                prof[name] = {"type": "categorical", "unique": len(set(values))}
        return prof

    def recommend_chart(self, prof: Dict[str, dict]) -> str:
        numeric = [n for n, p in prof.items() if p["type"] == "numeric"]
        categorical = [n for n, p in prof.items() if p["type"] == "categorical"]
        if len(numeric) >= 2:
            return f"scatter plot of {numeric[0]} vs {numeric[1]}"
        if numeric and categorical:
            return f"bar chart of {numeric[0]} by {categorical[0]}"
        return "histogram"

    def run(self, columns: Dict[str, List[float]]) -> AgentResult:
        self.trace = []
        prof = self.profile(columns)
        self._log(f"profile: {prof}")
        chart = self.recommend_chart(prof)
        insight = self.think(f"PROFILE: {prof}\nRecommended chart: {chart}\nKey insight:")
        return AgentResult(
            output={"profile": prof, "chart": chart, "insight": insight},
            trace=list(self.trace),
        )


if __name__ == "__main__":
    data = {
        "ad_spend": [100, 200, 300, 400, 500],
        "revenue": [120, 240, 360, 480, 600],
        "region": ["N", "S", "N", "E", "W"],
    }
    llm = MockLLM().add_rule(r"Key insight:", "Revenue scales linearly with ad spend (~1.2x).")
    agent = DataAnalysisAgent(llm=llm)
    result = agent.run(data)
    print("Chart:", result.output["chart"])
    print("Insight:", result.output["insight"])
