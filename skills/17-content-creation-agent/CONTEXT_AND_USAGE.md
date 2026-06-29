# Content Creation Agent — Context & Usage

**Agent #17 · Chapter 10: Conversational and Content Creation Agents · class `ContentCreationAgent` · file `17_content_creation_agent.py`**

## Chapter context

Agents that manage dialog and generate content: persona-driven conversation, multi-format content creation, and hybrid recommendation.

## This agent

- **Does:** Outline->draft->multi-format adaptation (blog, social, email) from one brief.
- **Use when:** You need marketing/content copy generated and adapted to multiple formats.
- **Not for:** factual retrieval or data analysis.
- **Inputs:** a content brief, target formats
- **Keywords:** content, writing, copywriting, marketing, blog, social, creative
- **Example task:** Announce a new app as a blog post and a social post.

## Techniques (from the book)

SMPA (Sense-Model-Plan-Act); CSP brand constraints; EditorAgent; CTR/analytics feedback

## Real-world use case (from the book)

MindBridge Health - brand/compliance-safe campus marketing content.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 10 (Conversational and Content Creation Agents) of the mirrored repo:

- README: [`../../book-repo/chapter10/README.md`](../../book-repo/chapter10/README.md)
- Use case: [`../../book-repo/chapter10/USECASE.md`](../../book-repo/chapter10/USECASE.md)
- Agents notes: [`../../book-repo/chapter10/AGENTS.md`](../../book-repo/chapter10/AGENTS.md)
- Notebook: [`../../book-repo/chapter10/ch10_conversational_and_content_creation_agents.ipynb`](../../book-repo/chapter10/ch10_conversational_and_content_creation_agents.ipynb)

## Run the built-in demo

```bash
python ../../17_content_creation_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(17)   # ContentCreationAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Announce a new app as a blog post and a social post."
```
