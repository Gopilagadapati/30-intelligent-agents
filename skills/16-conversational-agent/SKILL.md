---
name: 16-conversational-agent
description: Conversational Agent (Chapter 10, Conversational and Content Creation Agents). Multi-turn dialog with persona and slot-filling state tracking. Use when: You are building a chatbot/assistant that must hold a persona and track conversation state. Triggers: chatbot, conversation, dialog, persona, support, assistant, slots.
---

# Skill 16 — Conversational Agent

*Chapter 10: Conversational and Content Creation Agents*

## What it does

Multi-turn dialog with persona and slot-filling state tracking.

## When to use this skill

You are building a chatbot/assistant that must hold a persona and track conversation state.

## When NOT to use

single API-style requests or content generation.

## Inputs required

a persona, optional slot names; user turns

## Triggers / keywords

chatbot, conversation, dialog, persona, support, assistant, slots

## Example task

Run a friendly support chat that collects an order number.

## Techniques (from the book)

SafetyLayer sentinel; ConversationSummaryBufferMemory; FAISS semantic memory; PersonaEngine

## Real-world use case (from the book)

MindBridge Health - safe student-wellness chat with crisis escalation and memory.

## Book reference (official code)

- Chapter 10: Conversational and Content Creation Agents
- README: [`../../book-repo/chapter10/README.md`](../../book-repo/chapter10/README.md)
- Use case: [`../../book-repo/chapter10/USECASE.md`](../../book-repo/chapter10/USECASE.md)
- Agents notes: [`../../book-repo/chapter10/AGENTS.md`](../../book-repo/chapter10/AGENTS.md)
- Notebook: [`../../book-repo/chapter10/ch10_conversational_and_content_creation_agents.ipynb`](../../book-repo/chapter10/ch10_conversational_and_content_creation_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 16_conversational_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(16)   # ConversationalAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
