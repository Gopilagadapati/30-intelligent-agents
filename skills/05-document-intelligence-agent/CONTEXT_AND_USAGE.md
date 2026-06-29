# Document Intelligence Agent — Context & Usage

**Agent #5 · Chapter 6: Information Retrieval and Knowledge Agents · class `DocumentIntelligenceAgent` · file `05_document_intelligence_agent.py`**

## Chapter context

Agents that ground an LLM in external information via advanced RAG, document intelligence pipelines, and scientific literature review.

## This agent

- **Does:** Five-stage pipeline: ingest->segment->extract->structure->summarize a document.
- **Use when:** You have unstructured documents (invoices, forms, contracts) and need structured fields + a summary.
- **Not for:** answering questions across many docs (use Knowledge Retrieval).
- **Inputs:** raw document text
- **Keywords:** document, extraction, ocr, invoice, form, parse, structure, summarize
- **Example task:** Extract invoice number, date and total from an invoice.

## Techniques (from the book)

five-stage pipeline; Tesseract OCR; confidence scoring; schema-driven extraction; rapidfuzz matching

## Real-world use case (from the book)

Lexington Legal Partners - extracts contract clauses for due diligence.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 6 (Information Retrieval and Knowledge Agents) of the mirrored repo:

- README: [`../../book-repo/chapter06/README.md`](../../book-repo/chapter06/README.md)
- Use case: [`../../book-repo/chapter06/USECASE.md`](../../book-repo/chapter06/USECASE.md)
- Agents notes: [`../../book-repo/chapter06/AGENTS.md`](../../book-repo/chapter06/AGENTS.md)
- Notebook: [`../../book-repo/chapter06/ch06_knowledge_agents.ipynb`](../../book-repo/chapter06/ch06_knowledge_agents.ipynb)

## Run the built-in demo

```bash
python ../../05_document_intelligence_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(5)   # DocumentIntelligenceAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Extract invoice number, date and total from an invoice."
```
