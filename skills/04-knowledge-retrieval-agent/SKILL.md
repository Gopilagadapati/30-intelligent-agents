---
name: 04-knowledge-retrieval-agent
description: Knowledge Retrieval Agent (advanced RAG) (Chapter 6, Information Retrieval and Knowledge Agents). Retrieves relevant chunks from a corpus, reranks, and generates a grounded, cited answer. Use when: You must answer questions from a known document corpus / knowledge base. Triggers: rag, retrieval, search, knowledge base, grounding, citations, faq.
---

# Skill 04 — Knowledge Retrieval Agent (advanced RAG)

*Chapter 6: Information Retrieval and Knowledge Agents*

## What it does

Retrieves relevant chunks from a corpus, reranks, and generates a grounded, cited answer.

## When to use this skill

You must answer questions from a known document corpus / knowledge base.

## When NOT to use

open-ended creativity, or questions with no supporting corpus.

## Inputs required

a corpus (list of texts), a question

## Triggers / keywords

rag, retrieval, search, knowledge base, grounding, citations, faq

## Example task

Answer 'what is the return window?' from the policy docs.

## Techniques (from the book)

LangChain + FAISS; hybrid semantic/keyword retrieval; cross-encoder reranking; provenance tracking

## Real-world use case (from the book)

Lexington Legal Partners - finds buried precedents across 14M pages.

## Book reference (official code)

- Chapter 6: Information Retrieval and Knowledge Agents
- README: [`../../book-repo/chapter06/README.md`](../../book-repo/chapter06/README.md)
- Use case: [`../../book-repo/chapter06/USECASE.md`](../../book-repo/chapter06/USECASE.md)
- Agents notes: [`../../book-repo/chapter06/AGENTS.md`](../../book-repo/chapter06/AGENTS.md)
- Notebook: [`../../book-repo/chapter06/ch06_knowledge_agents.ipynb`](../../book-repo/chapter06/ch06_knowledge_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 04_knowledge_retrieval_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(4)   # KnowledgeRetrievalAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
