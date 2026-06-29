# Knowledge Retrieval Agent (advanced RAG) — Context & Usage

**Agent #4 · Chapter 6: Information Retrieval and Knowledge Agents · class `KnowledgeRetrievalAgent` · file `04_knowledge_retrieval_agent.py`**

## Chapter context

Agents that ground an LLM in external information via advanced RAG, document intelligence pipelines, and scientific literature review.

## This agent

- **Does:** Retrieves relevant chunks from a corpus, reranks, and generates a grounded, cited answer.
- **Use when:** You must answer questions from a known document corpus / knowledge base.
- **Not for:** open-ended creativity, or questions with no supporting corpus.
- **Inputs:** a corpus (list of texts), a question
- **Keywords:** rag, retrieval, search, knowledge base, grounding, citations, faq
- **Example task:** Answer 'what is the return window?' from the policy docs.

## Techniques (from the book)

LangChain + FAISS; hybrid semantic/keyword retrieval; cross-encoder reranking; provenance tracking

## Real-world use case (from the book)

Lexington Legal Partners - finds buried precedents across 14M pages.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 6 (Information Retrieval and Knowledge Agents) of the mirrored repo:

- README: [`../../book-repo/chapter06/README.md`](../../book-repo/chapter06/README.md)
- Use case: [`../../book-repo/chapter06/USECASE.md`](../../book-repo/chapter06/USECASE.md)
- Agents notes: [`../../book-repo/chapter06/AGENTS.md`](../../book-repo/chapter06/AGENTS.md)
- Notebook: [`../../book-repo/chapter06/ch06_knowledge_agents.ipynb`](../../book-repo/chapter06/ch06_knowledge_agents.ipynb)

## Run the built-in demo

```bash
python ../../04_knowledge_retrieval_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(4)   # KnowledgeRetrievalAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Answer 'what is the return window?' from the policy docs."
```
