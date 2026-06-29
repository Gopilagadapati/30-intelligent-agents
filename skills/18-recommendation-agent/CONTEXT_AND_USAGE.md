# Recommendation Agent — Context & Usage

**Agent #18 · Chapter 10: Conversational and Content Creation Agents · class `RecommendationAgent` · file `18_recommendation_agent.py`**

## Chapter context

Agents that manage dialog and generate content: persona-driven conversation, multi-format content creation, and hybrid recommendation.

## This agent

- **Does:** Hybrid recommender (content + popularity) with LLM-explained suggestions.
- **Use when:** You need to recommend items from a catalog given a user profile/preferences.
- **Not for:** open-ended generation; it ranks existing items.
- **Inputs:** a catalog (item->description), optional popularity, a user profile
- **Keywords:** recommendation, recommender, personalization, ranking, suggest, catalog
- **Example task:** Recommend books to a sci-fi fan and explain why.

## Techniques (from the book)

hybrid recommender (content-based + collaborative/popularity); preference modeling; explanation generation

## Real-world use case (from the book)

MindBridge Health - personalized content/resource recommendations.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 10 (Conversational and Content Creation Agents) of the mirrored repo:

- README: [`../../book-repo/chapter10/README.md`](../../book-repo/chapter10/README.md)
- Use case: [`../../book-repo/chapter10/USECASE.md`](../../book-repo/chapter10/USECASE.md)
- Agents notes: [`../../book-repo/chapter10/AGENTS.md`](../../book-repo/chapter10/AGENTS.md)
- Notebook: [`../../book-repo/chapter10/ch10_conversational_and_content_creation_agents.ipynb`](../../book-repo/chapter10/ch10_conversational_and_content_creation_agents.ipynb)

## Run the built-in demo

```bash
python ../../18_recommendation_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(18)   # RecommendationAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Recommend books to a sci-fi fan and explain why."
```
