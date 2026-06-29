# Data Analysis Agent — Context & Usage

**Agent #10 · Chapter 8: Data Analysis and Reasoning Agents · class `DataAnalysisAgent` · file `10_data_analysis_agent.py`**

## Chapter context

Agents specialized in analyzing data and reasoning: data exploration, fact verification, and a domain-agnostic problem solver.

## This agent

- **Does:** Profiles tabular data, recommends a chart, and narrates the key insight.
- **Use when:** You have columnar/tabular data and want stats, a chart suggestion, and a plain-English insight.
- **Not for:** unstructured text or fact-checking.
- **Inputs:** a dict of column_name -> list of values
- **Keywords:** data, analysis, statistics, visualization, chart, tabular, eda, insights
- **Example task:** Profile ad_spend vs revenue and recommend a chart.

## Techniques (from the book)

cognitive loop; Pandas code generation; chart selection; OLS regression; z-score anomaly detection

## Real-world use case (from the book)

CanadaFirst News - analyzes infrastructure spending vs. construction activity.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 8 (Data Analysis and Reasoning Agents) of the mirrored repo:

- README: [`../../book-repo/chapter08/README.md`](../../book-repo/chapter08/README.md)
- Use case: [`../../book-repo/chapter08/USECASE.md`](../../book-repo/chapter08/USECASE.md)
- Agents notes: [`../../book-repo/chapter08/AGENTS.md`](../../book-repo/chapter08/AGENTS.md)
- Notebook: [`../../book-repo/chapter08/ch08_data_analysis_reasoning_agents.ipynb`](../../book-repo/chapter08/ch08_data_analysis_reasoning_agents.ipynb)

## Run the built-in demo

```bash
python ../../10_data_analysis_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(10)   # DataAnalysisAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Profile ad_spend vs revenue and recommend a chart."
```
