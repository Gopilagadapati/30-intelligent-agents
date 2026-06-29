# Conversational Agent — Context & Usage

**Agent #16 · Chapter 10: Conversational and Content Creation Agents · class `ConversationalAgent` · file `16_conversational_agent.py`**

## Chapter context

Agents that manage dialog and generate content: persona-driven conversation, multi-format content creation, and hybrid recommendation.

## This agent

- **Does:** Multi-turn dialog with persona and slot-filling state tracking.
- **Use when:** You are building a chatbot/assistant that must hold a persona and track conversation state.
- **Not for:** single API-style requests or content generation.
- **Inputs:** a persona, optional slot names; user turns
- **Keywords:** chatbot, conversation, dialog, persona, support, assistant, slots
- **Example task:** Run a friendly support chat that collects an order number.

## Techniques (from the book)

SafetyLayer sentinel; ConversationSummaryBufferMemory; FAISS semantic memory; PersonaEngine

## Real-world use case (from the book)

MindBridge Health - safe student-wellness chat with crisis escalation and memory.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 10 (Conversational and Content Creation Agents) of the mirrored repo:

- README: [`../../book-repo/chapter10/README.md`](../../book-repo/chapter10/README.md)
- Use case: [`../../book-repo/chapter10/USECASE.md`](../../book-repo/chapter10/USECASE.md)
- Agents notes: [`../../book-repo/chapter10/AGENTS.md`](../../book-repo/chapter10/AGENTS.md)
- Notebook: [`../../book-repo/chapter10/ch10_conversational_and_content_creation_agents.ipynb`](../../book-repo/chapter10/ch10_conversational_and_content_creation_agents.ipynb)

## Run the built-in demo

```bash
python ../../16_conversational_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(16)   # ConversationalAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Run a friendly support chat that collects an order number."
```
