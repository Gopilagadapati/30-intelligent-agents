# Skills — one per agent (31 total)

Every agent in the library is packaged as its own **skill**. Each skill folder contains a `SKILL.md` (definition + when to use) and a `CONTEXT_AND_USAGE.md` (chapter context + usage details). Point your assistant at a skill's `SKILL.md` and state your task, or let `../meta_agent.py` route a task to the right skill automatically.


## Chapter 5 — Foundational Cognitive Architectures

| # | Skill | Use when |
|---|-------|----------|
| 1 | [`01-autonomous-decision-agent`](01-autonomous-decision-agent/SKILL.md) | You have a goal and a discrete set of possible actions, and want the agent to drive itself with minimal human steps. |
| 2 | [`02-planning-agent`](02-planning-agent/SKILL.md) | You need an explicit, ordered breakdown of a complex goal into sub-tasks before execution. |
| 3 | [`03-memory-augmented-agent`](03-memory-augmented-agent/SKILL.md) | The task needs recall of prior facts/interactions or personalization across turns. |

## Chapter 6 — Information Retrieval and Knowledge Agents

| # | Skill | Use when |
|---|-------|----------|
| 4 | [`04-knowledge-retrieval-agent`](04-knowledge-retrieval-agent/SKILL.md) | You must answer questions from a known document corpus / knowledge base. |
| 5 | [`05-document-intelligence-agent`](05-document-intelligence-agent/SKILL.md) | You have unstructured documents (invoices, forms, contracts) and need structured fields + a summary. |
| 6 | [`06-scientific-research-agent`](06-scientific-research-agent/SKILL.md) | You need to survey literature on a topic and propose research hypotheses. |

## Chapter 7 — Tool Manipulation and Orchestration Agents

| # | Skill | Use when |
|---|-------|----------|
| 7 | [`07-tool-using-agent`](07-tool-using-agent/SKILL.md) | The task needs external actions/APIs/functions (calculations, lookups, side effects). |
| 8 | [`08-chain-of-agents-orchestrator`](08-chain-of-agents-orchestrator/SKILL.md) | A task benefits from a pipeline of specialists (e.g., research->write->edit). |
| 9 | [`09-agentic-workflow-system`](09-agentic-workflow-system/SKILL.md) | A process has gated steps requiring human approval before continuing. |

## Chapter 8 — Data Analysis and Reasoning Agents

| # | Skill | Use when |
|---|-------|----------|
| 10 | [`10-data-analysis-agent`](10-data-analysis-agent/SKILL.md) | You have columnar/tabular data and want stats, a chart suggestion, and a plain-English insight. |
| 11 | [`11-verification-validation-agent`](11-verification-validation-agent/SKILL.md) | You need to verify factual consistency of a statement against trusted evidence. |
| 12 | [`12-general-problem-solver`](12-general-problem-solver/SKILL.md) | The problem can be framed as states + operators and you need a sequence of steps. |

## Chapter 9 — Software Development Agents

| # | Skill | Use when |
|---|-------|----------|
| 13 | [`13-code-generation-agent`](13-code-generation-agent/SKILL.md) | You need code written/fixed and have unit tests to validate it. |
| 14 | [`14-security-hardened-agent`](14-security-hardened-agent/SKILL.md) | You process untrusted user/content input and must resist prompt injection / jailbreaks. |
| 15 | [`15-self-improving-agent`](15-self-improving-agent/SKILL.md) | You want behavior to improve over time from ratings/feedback. |

## Chapter 10 — Conversational and Content Creation Agents

| # | Skill | Use when |
|---|-------|----------|
| 16 | [`16-conversational-agent`](16-conversational-agent/SKILL.md) | You are building a chatbot/assistant that must hold a persona and track conversation state. |
| 17 | [`17-content-creation-agent`](17-content-creation-agent/SKILL.md) | You need marketing/content copy generated and adapted to multiple formats. |
| 18 | [`18-recommendation-agent`](18-recommendation-agent/SKILL.md) | You need to recommend items from a catalog given a user profile/preferences. |

## Chapter 11 — Multi-Modal Perception Agents

| # | Skill | Use when |
|---|-------|----------|
| 19 | [`19-vision-language-agent`](19-vision-language-agent/SKILL.md) | The task involves images / visual question answering. |
| 20 | [`20-audio-processing-agent`](20-audio-processing-agent/SKILL.md) | The input is voice/audio and you need transcription + sentiment-aware replies. |
| 21 | [`21-physical-world-sensing-agent`](21-physical-world-sensing-agent/SKILL.md) | You monitor IoT/sensor streams and need anomaly detection + response. |

## Chapter 12 — Ethical and Explainable Agents

| # | Skill | Use when |
|---|-------|----------|
| 22 | [`22-ethical-reasoning-agent`](22-ethical-reasoning-agent/SKILL.md) | You must check whether an action is ethically acceptable (value alignment). |
| 23 | [`23-explainable-agent`](23-explainable-agent/SKILL.md) | A decision needs transparency: which factors drove it and what would flip it. |

## Chapter 13 — Healthcare and Scientific Agents

| # | Skill | Use when |
|---|-------|----------|
| 24 | [`24-healthcare-intelligence-agent`](24-healthcare-intelligence-agent/SKILL.md) | Clinical/medical screening framed as Bayesian probability over symptoms/findings. |
| 25 | [`25-scientific-discovery-agent`](25-scientific-discovery-agent/SKILL.md) | You search a candidate/parameter space using a (simulated) experiment objective. |

## Chapter 14 — Financial and Legal Domain Agents

| # | Skill | Use when |
|---|-------|----------|
| 26 | [`26-financial-advisory-agent`](26-financial-advisory-agent/SKILL.md) | Personalized financial planning framed with risk tolerance + suitability checks. |
| 27 | [`27-legal-intelligence-agent`](27-legal-intelligence-agent/SKILL.md) | Legal/contract questions that must be grounded in cited clauses/precedent. |

## Chapter 15 — Education and Knowledge Agents

| # | Skill | Use when |
|---|-------|----------|
| 28 | [`28-education-intelligence-agent`](28-education-intelligence-agent/SKILL.md) | You build a tutor that adapts difficulty to a learner's skill level. |
| 29 | [`29-collective-intelligence-agent`](29-collective-intelligence-agent/SKILL.md) | You want robustness via ensemble/consensus across several agents or models. |

## Chapter 16 — Embodied and Physical World Agents

| # | Skill | Use when |
|---|-------|----------|
| 30 | [`30-embodied-intelligence-agent`](30-embodied-intelligence-agent/SKILL.md) | The task is robotic/embodied control: sense, plan a move, actuate, repeat. |
| 31 | [`31-domain-transforming-integration-agent`](31-domain-transforming-integration-agent/SKILL.md) | You want novel solutions by borrowing patterns across domains (biomimicry, etc.). |

**Total:** 31 skills across 12 chapters.
