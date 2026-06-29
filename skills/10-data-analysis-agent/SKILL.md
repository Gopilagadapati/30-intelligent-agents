---
name: 10-data-analysis-agent
description: Data Analysis Agent (Chapter 8, Data Analysis and Reasoning Agents). Profiles tabular data, recommends a chart, and narrates the key insight. Use when: You have columnar/tabular data and want stats, a chart suggestion, and a plain-English insight. Triggers: data, analysis, statistics, visualization, chart, tabular, eda, insights.
---

# Skill 10 — Data Analysis Agent

*Chapter 8: Data Analysis and Reasoning Agents*

## What it does

Profiles tabular data, recommends a chart, and narrates the key insight.

## When to use this skill

You have columnar/tabular data and want stats, a chart suggestion, and a plain-English insight.

## When NOT to use

unstructured text or fact-checking.

## Inputs required

a dict of column_name -> list of values

## Triggers / keywords

data, analysis, statistics, visualization, chart, tabular, eda, insights

## Example task

Profile ad_spend vs revenue and recommend a chart.

## Techniques (from the book)

cognitive loop; Pandas code generation; chart selection; OLS regression; z-score anomaly detection

## Real-world use case (from the book)

CanadaFirst News - analyzes infrastructure spending vs. construction activity.

## Book reference (official code)

- Chapter 8: Data Analysis and Reasoning Agents
- README: [`../../book-repo/chapter08/README.md`](../../book-repo/chapter08/README.md)
- Use case: [`../../book-repo/chapter08/USECASE.md`](../../book-repo/chapter08/USECASE.md)
- Agents notes: [`../../book-repo/chapter08/AGENTS.md`](../../book-repo/chapter08/AGENTS.md)
- Notebook: [`../../book-repo/chapter08/ch08_data_analysis_reasoning_agents.ipynb`](../../book-repo/chapter08/ch08_data_analysis_reasoning_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 10_data_analysis_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(10)   # DataAnalysisAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
