# Scientific Research Agent — Context & Usage

**Agent #6 · Chapter 6: Information Retrieval and Knowledge Agents · class `ScientificResearchAgent` · file `06_scientific_research_agent.py`**

## Chapter context

Agents that ground an LLM in external information via advanced RAG, document intelligence pipelines, and scientific literature review.

## This agent

- **Does:** Literature review + synthesis + testable hypothesis generation over a paper corpus.
- **Use when:** You need to survey literature on a topic and propose research hypotheses.
- **Not for:** running experiments (use Scientific Discovery Agent).
- **Inputs:** a list of papers (title+abstract), a research topic
- **Keywords:** research, literature, papers, hypothesis, review, synthesis, science
- **Example task:** Review microbiome papers and propose a testable hypothesis.

## Techniques (from the book)

arXiv search; sentence-transformers; KMeans clustering; thematic synthesis

## Real-world use case (from the book)

Lexington Legal Partners - synthesizes expert reports and finds knowledge gaps.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 6 (Information Retrieval and Knowledge Agents) of the mirrored repo:

- README: [`../../book-repo/chapter06/README.md`](../../book-repo/chapter06/README.md)
- Use case: [`../../book-repo/chapter06/USECASE.md`](../../book-repo/chapter06/USECASE.md)
- Agents notes: [`../../book-repo/chapter06/AGENTS.md`](../../book-repo/chapter06/AGENTS.md)
- Notebook: [`../../book-repo/chapter06/ch06_knowledge_agents.ipynb`](../../book-repo/chapter06/ch06_knowledge_agents.ipynb)

## Run the built-in demo

```bash
python ../../06_scientific_research_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(6)   # ScientificResearchAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Review microbiome papers and propose a testable hypothesis."
```
