# Vision-Language Agent — Context & Usage

**Agent #19 · Chapter 11: Multi-Modal Perception Agents · class `VisionLanguageAgent` · file `19_vision_language_agent.py`**

## Chapter context

Agents that perceive non-text inputs: vision-language, audio/speech, and IoT physical-world sensing.

## This agent

- **Does:** Answers questions about images by fusing visual perception with language reasoning.
- **Use when:** The task involves images / visual question answering.
- **Not for:** text-only or audio tasks.
- **Inputs:** an image id (swap MockVisionEncoder for a real model), a question
- **Keywords:** vision, image, visual, vqa, multimodal, picture, perception
- **Example task:** Is there a pedestrian in this street image?

## Techniques (from the book)

ViT visual encoder; cross-modal attention; LLaVA 1.5; chain-of-thought prompting

## Real-world use case (from the book)

Meridian Facilities - occupancy analysis and after-hours intrusion detection.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 11 (Multi-Modal Perception Agents) of the mirrored repo:

- README: [`../../book-repo/chapter11/README.md`](../../book-repo/chapter11/README.md)
- Use case: [`../../book-repo/chapter11/USECASE.md`](../../book-repo/chapter11/USECASE.md)
- Agents notes: [`../../book-repo/chapter11/AGENTS.md`](../../book-repo/chapter11/AGENTS.md)
- Notebook: [`../../book-repo/chapter11/ch11_multimodal_agents.ipynb`](../../book-repo/chapter11/ch11_multimodal_agents.ipynb)

## Run the built-in demo

```bash
python ../../19_vision_language_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(19)   # VisionLanguageAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Is there a pedestrian in this street image?"
```
