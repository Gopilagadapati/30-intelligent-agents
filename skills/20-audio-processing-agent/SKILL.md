---
name: 20-audio-processing-agent
description: Audio Processing Agent (Chapter 11, Multi-Modal Perception Agents). Transcribes speech, analyzes sentiment, and responds empathetically. Use when: The input is voice/audio and you need transcription + sentiment-aware replies. Triggers: audio, speech, voice, transcription, sentiment, asr, call center.
---

# Skill 20 — Audio Processing Agent

*Chapter 11: Multi-Modal Perception Agents*

## What it does

Transcribes speech, analyzes sentiment, and responds empathetically.

## When to use this skill

The input is voice/audio and you need transcription + sentiment-aware replies.

## When NOT to use

image or pure text tasks.

## Inputs required

an audio id (swap MockTranscriber for Whisper, etc.)

## Triggers / keywords

audio, speech, voice, transcription, sentiment, asr, call center

## Example task

Handle an angry voicemail with empathy.

## Techniques (from the book)

STFT/spectrograms; Whisper-style transcription; VAD prosody analysis; sentiment routing

## Real-world use case (from the book)

Meridian Facilities - routes tenant calls using voice sentiment.

## Book reference (official code)

- Chapter 11: Multi-Modal Perception Agents
- README: [`../../book-repo/chapter11/README.md`](../../book-repo/chapter11/README.md)
- Use case: [`../../book-repo/chapter11/USECASE.md`](../../book-repo/chapter11/USECASE.md)
- Agents notes: [`../../book-repo/chapter11/AGENTS.md`](../../book-repo/chapter11/AGENTS.md)
- Notebook: [`../../book-repo/chapter11/ch11_multimodal_agents.ipynb`](../../book-repo/chapter11/ch11_multimodal_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 20_audio_processing_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(20)   # AudioProcessingAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
