# Audio Processing Agent — Context & Usage

**Agent #20 · Chapter 11: Multi-Modal Perception Agents · class `AudioProcessingAgent` · file `20_audio_processing_agent.py`**

## Chapter context

Agents that perceive non-text inputs: vision-language, audio/speech, and IoT physical-world sensing.

## This agent

- **Does:** Transcribes speech, analyzes sentiment, and responds empathetically.
- **Use when:** The input is voice/audio and you need transcription + sentiment-aware replies.
- **Not for:** image or pure text tasks.
- **Inputs:** an audio id (swap MockTranscriber for Whisper, etc.)
- **Keywords:** audio, speech, voice, transcription, sentiment, asr, call center
- **Example task:** Handle an angry voicemail with empathy.

## Techniques (from the book)

STFT/spectrograms; Whisper-style transcription; VAD prosody analysis; sentiment routing

## Real-world use case (from the book)

Meridian Facilities - routes tenant calls using voice sentiment.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 11 (Multi-Modal Perception Agents) of the mirrored repo:

- README: [`../../book-repo/chapter11/README.md`](../../book-repo/chapter11/README.md)
- Use case: [`../../book-repo/chapter11/USECASE.md`](../../book-repo/chapter11/USECASE.md)
- Agents notes: [`../../book-repo/chapter11/AGENTS.md`](../../book-repo/chapter11/AGENTS.md)
- Notebook: [`../../book-repo/chapter11/ch11_multimodal_agents.ipynb`](../../book-repo/chapter11/ch11_multimodal_agents.ipynb)

## Run the built-in demo

```bash
python ../../20_audio_processing_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(20)   # AudioProcessingAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Handle an angry voicemail with empathy."
```
