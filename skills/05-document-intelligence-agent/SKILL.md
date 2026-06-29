---
name: 05-document-intelligence-agent
description: Document Intelligence Agent (Chapter 6, Information Retrieval and Knowledge Agents). Five-stage pipeline: ingest->segment->extract->structure->summarize a document. Use when: You have unstructured documents (invoices, forms, contracts) and need structured fields + a summary. Triggers: document, extraction, ocr, invoice, form, parse, structure, summarize.
---

# Skill 05 — Document Intelligence Agent

*Chapter 6: Information Retrieval and Knowledge Agents*

## What it does

Five-stage pipeline: ingest->segment->extract->structure->summarize a document.

## When to use this skill

You have unstructured documents (invoices, forms, contracts) and need structured fields + a summary.

## When NOT to use

answering questions across many docs (use Knowledge Retrieval).

## Inputs required

raw document text

## Triggers / keywords

document, extraction, ocr, invoice, form, parse, structure, summarize

## Example task

Extract invoice number, date and total from an invoice.

## Techniques (from the book)

five-stage pipeline; Tesseract OCR; confidence scoring; schema-driven extraction; rapidfuzz matching

## Real-world use case (from the book)

Lexington Legal Partners - extracts contract clauses for due diligence.

## Book reference (official code)

- Chapter 6: Information Retrieval and Knowledge Agents
- README: [`../../book-repo/chapter06/README.md`](../../book-repo/chapter06/README.md)
- Use case: [`../../book-repo/chapter06/USECASE.md`](../../book-repo/chapter06/USECASE.md)
- Agents notes: [`../../book-repo/chapter06/AGENTS.md`](../../book-repo/chapter06/AGENTS.md)
- Notebook: [`../../book-repo/chapter06/ch06_knowledge_agents.ipynb`](../../book-repo/chapter06/ch06_knowledge_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 05_document_intelligence_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(5)   # DocumentIntelligenceAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
