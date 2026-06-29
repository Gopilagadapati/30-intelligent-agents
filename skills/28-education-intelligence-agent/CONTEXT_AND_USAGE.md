# Education Intelligence Agent — Context & Usage

**Agent #28 · Chapter 15: Education and Knowledge Agents · class `EducationIntelligenceAgent` · file `28_education_intelligence_agent.py`**

## Chapter context

Agents for learning and collective reasoning: adaptive tutoring and multi-agent consensus.

## This agent

- **Does:** Adaptive tutor: tracks mastery and picks next item in the zone of proximal development.
- **Use when:** You build a tutor that adapts difficulty to a learner's skill level.
- **Not for:** content creation or generic Q&A.
- **Inputs:** skills, an item bank (id/skill/difficulty); optional last result
- **Keywords:** education, tutor, adaptive learning, curriculum, mastery, edtech, personalized
- **Example task:** Pick the next exercise after a correct 'loops' answer.

## Techniques (from the book)

POMDP tutor; Bayesian Knowledge Tracing; IRT 2PL placement; ZPD Gaussian curriculum; SM-2 spaced repetition; misconception detection

## Real-world use case (from the book)

LearnPath - adaptive placement raises course completion (52% -> 78%).

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 15 (Education and Knowledge Agents) of the mirrored repo:

- README: [`../../book-repo/chapter15/README.md`](../../book-repo/chapter15/README.md)
- Use case: [`../../book-repo/chapter15/USECASE.md`](../../book-repo/chapter15/USECASE.md)
- Agents notes: [`../../book-repo/chapter15/AGENTS.md`](../../book-repo/chapter15/AGENTS.md)
- Notebook: [`../../book-repo/chapter15/ch15_education_and_knowledge_agents.ipynb`](../../book-repo/chapter15/ch15_education_and_knowledge_agents.ipynb)

## Run the built-in demo

```bash
python ../../28_education_intelligence_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(28)   # EducationIntelligenceAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Pick the next exercise after a correct 'loops' answer."
```
