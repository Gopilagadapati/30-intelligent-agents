"""Agent 20 - Audio Processing Agent (Chapter 11).

Pattern: speech pipeline -- (simulated) transcription -> intent + sentiment
analysis -> response. Swap MockTranscriber for Whisper/Deepgram in production;
the downstream reasoning is unchanged.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict

sys.path.append(str(Path(__file__).resolve().parent))

from common import BaseAgent, AgentResult
from common.llm import MockLLM


class MockTranscriber:
    _clips = {
        "clip_complaint.wav": "I am really frustrated, my order is three weeks late!",
        "clip_praise.wav": "Thank you so much, the service was excellent.",
    }

    def transcribe(self, audio_id: str) -> str:
        return self._clips.get(audio_id, "")


class AudioProcessingAgent(BaseAgent):
    POSITIVE = {"thank", "excellent", "great", "love", "good"}
    NEGATIVE = {"frustrated", "late", "angry", "bad", "terrible"}

    def __init__(self, transcriber: MockTranscriber = None, llm=None):
        super().__init__(
            name="AudioProcessingAgent",
            system_prompt="You handle transcribed voice messages with empathy.",
            llm=llm,
        )
        self.transcriber = transcriber or MockTranscriber()

    def sentiment(self, text: str) -> str:
        t = text.lower()
        pos = sum(w in t for w in self.POSITIVE)
        neg = sum(w in t for w in self.NEGATIVE)
        if neg > pos:
            return "negative"
        if pos > neg:
            return "positive"
        return "neutral"

    def run(self, audio_id: str) -> AgentResult:
        self.trace = []
        transcript = self.transcriber.transcribe(audio_id)
        sentiment = self.sentiment(transcript)
        self._log(f"transcript={transcript!r} sentiment={sentiment}")
        reply = self.think(f"TRANSCRIPT: {transcript}\nSENTIMENT: {sentiment}\nReply:")
        return AgentResult(output=reply, trace=list(self.trace),
                           metadata={"transcript": transcript, "sentiment": sentiment})


if __name__ == "__main__":
    llm = MockLLM().add_rule(
        r"Reply:",
        lambda p: "I'm sorry for the delay — let me escalate this right away." if "negative" in p else "Thanks for the kind words!",
    )
    agent = AudioProcessingAgent(llm=llm)
    result = agent.run("clip_complaint.wav")
    print("Sentiment:", result.metadata["sentiment"])
    print("Reply:", result.output)
