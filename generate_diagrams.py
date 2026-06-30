"""Generate a LinkedIn-ready architecture diagram (PNG) for each of the 31 agents.

Each diagram is a square 1200x1200 image with:
  - a branded header (DAY N / 30 + agent name + chapter)
  - the agent's core flow as a vertical pipeline of stages
  - an optional guardrail / human-in-the-loop callout
  - a footer (agent type, real-world use case, repo link)

Run:  python generate_diagrams.py
Output: diagrams/dayNN-<agent-slug>.png
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

from catalog import CATALOG, CHAPTER_TITLES, USE_CASES, by_number

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "diagrams"
REPO = "github.com/Gopilagadapati/30-intelligent-agents"

# palette
INK = "#0f1b2d"
ACCENT = "#1f6feb"
BOX = "#eaf1fb"
BOX_EDGE = "#1f6feb"
GATE = "#fff4e5"
GATE_EDGE = "#e8820c"
LOOP = "#137a4b"
MUTED = "#5b6b7f"
BG = "#ffffff"

MULTI_AGENT = {8, 26, 29}

# Core flow (3-6 stages) for each agent, grounded in catalog TECHNIQUES.
FLOWS = {
    1: ["Perceive state", "Reason: choose action", "Validate vs action set", "Act", "Goal met?"],
    2: ["Goal", "Decompose into sub-tasks", "Evaluate branches (ToT)", "Ordered plan", "Adaptive replan"],
    3: ["User input", "Retrieve memory\n(working/episodic/semantic)", "Reason with context", "Respond", "Store new memory"],
    4: ["Query", "Hybrid retrieve (FAISS)", "Cross-encoder rerank", "Generate grounded answer", "Attach citations"],
    5: ["Ingest document", "OCR + segment", "Extract fields", "Structure to schema", "Summarize"],
    6: ["Research topic", "Literature search (arXiv)", "Embed + cluster", "Synthesize themes", "Generate hypotheses"],
    7: ["Request", "Think / Plan", "Select tool (registry)", "Call tool (+ fallback)", "Observe result"],
    8: ["Task", "Manager decomposes", "Specialists run\n(shared memory)", "Resolve conflicts", "Aggregate output"],
    9: ["Start workflow", "Execute step", "Approval gate", "Advance / iterate", "Audit trail"],
    10: ["Tabular data", "Profile (pandas)", "Stats + regression", "Select chart", "Plain-English insight"],
    11: ["Statement", "Extract claims", "Retrieve evidence", "NLI check (BART-MNLI)", "Verdict + confidence"],
    12: ["Start state", "Apply operators", "Means-ends search", "Goal test", "Solution path"],
    13: ["Spec", "Generate code", "Run unit tests", "Refine on failure", "Tests pass"],
    14: ["Untrusted input", "Detect injection", "Sanitize", "Policy check", "Safe response"],
    15: ["Question", "Answer", "Collect feedback", "Learn / adapt", "Improved policy"],
    16: ["User turn", "Safety layer", "Memory (summary + FAISS)", "Persona reasoning", "Reply"],
    17: ["Content brief", "Sense-Model-Plan-Act", "Brand constraints (CSP)", "Draft + Editor", "CTR feedback"],
    18: ["User profile", "Generate candidates", "Hybrid score\n(content + collaborative)", "Rank", "Explain picks"],
    19: ["Image + question", "ViT visual encode", "Cross-modal attention", "Chain-of-thought", "Answer"],
    20: ["Audio", "STFT / spectrogram", "Transcribe (Whisper)", "Prosody + sentiment", "Route / respond"],
    21: ["Sensor streams", "Fuse + window", "Detect anomaly", "Proportional control", "Actuate (deadband)"],
    22: ["Proposed action", "Deontic check", "Bias test (4/5 rule)", "Frameworks (EU AI Act)", "Approve / reject"],
    23: ["Model decision", "Attribute (SHAP / LIME)", "Counterfactual", "Calibrate confidence", "Explanation"],
    24: ["Patient findings", "FHIR normalize", "Bayesian update", "Escalation threshold (0.15)", "Escalate + audit"],
    25: ["Literature scan", "Detect knowledge gap", "Abductive hypotheses", "Run experiment", "Closed-loop feedback"],
    26: ["Client profile", "Supervisor routes", "Specialist agents\n(market tools)", "Composite risk score", "Compliance gate"],
    27: ["Legal question", "Hybrid retrieve", "Authority-weighted rank", "Draft answer", "Citation-verify gate"],
    28: ["Learner state", "Assess (BKT / IRT)", "Select item (ZPD)", "Teach", "Spaced repetition (SM-2)"],
    29: ["Question", "Agents propose", "Adversarial critique", "Synthesize", "Weighted consensus"],
    30: ["Sense environment", "Plan move", "Constraint envelope", "Safety fusion (all())", "Actuate"],
    31: ["Problem", "Build knowledge graph", "BFS influence propagation", "Cross-domain mapping", "Transferred solution"],
}

# Which stage index is a guardrail / human-in-the-loop / safety gate (0-based), if any.
GATE_STAGE = {
    1: 2, 8: 3, 9: 2, 11: 3, 13: 2, 14: 3, 22: 4, 23: 3,
    24: 3, 26: 4, 27: 4, 29: 2, 30: 3,
}
# Which agents loop back to the top (cyclic cognitive loop).
LOOPING = {1, 3, 13, 15, 21, 25, 30}


def slug(spec) -> str:
    stem = spec.file[:-3].split("_", 1)[1]
    return stem.replace("_", "-")


def wrap(text: str, width: int) -> str:
    if "\n" in text:
        return text
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return "\n".join(lines)


def draw(spec) -> Path:
    num = spec.num
    flow = FLOWS[num]
    gate_idx = GATE_STAGE.get(num)

    fig, ax = plt.subplots(figsize=(8, 8), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # --- header band ---
    ax.add_patch(FancyBboxPatch((0, 88), 100, 12, boxstyle="square,pad=0",
                                facecolor=INK, edgecolor="none"))
    ax.text(4, 95.6, f"DAY {num:02d} / 30", color="#7fb1ff",
            fontsize=13, fontweight="bold", va="center")
    atype = "MULTI-AGENT SYSTEM" if num in MULTI_AGENT else "SINGLE AGENT"
    ax.text(96, 95.6, atype, color="#9fb3cc", fontsize=10.5,
            fontweight="bold", va="center", ha="right")
    ax.text(4, 90.6, spec.name, color="white", fontsize=16.5,
            fontweight="bold", va="center")

    # --- chapter subtitle ---
    ax.text(50, 84.5, f"Chapter {spec.chapter} - {CHAPTER_TITLES[spec.chapter]}",
            color=MUTED, fontsize=11, ha="center", va="center", style="italic")

    # --- vertical pipeline ---
    n = len(flow)
    top, bottom = 80.0, 20.0
    box_h = (top - bottom) / n - 2.2
    box_w = 56
    cx = 38
    centers = []
    for i, label in enumerate(flow):
        y = top - i * ((top - bottom) / n) - box_h
        cy = y + box_h / 2
        centers.append(cy)
        is_gate = (gate_idx is not None and i == gate_idx)
        fc, ec = (GATE, GATE_EDGE) if is_gate else (BOX, BOX_EDGE)
        ax.add_patch(FancyBboxPatch((cx - box_w / 2, y), box_w, box_h,
                                    boxstyle="round,pad=0.6,rounding_size=2.5",
                                    facecolor=fc, edgecolor=ec, linewidth=2))
        ax.text(cx, cy, wrap(label, 26), color=INK, fontsize=12,
                fontweight="bold", ha="center", va="center")
        # step number bubble
        ax.add_patch(plt.Circle((cx - box_w / 2 + 1.5, y + box_h - 1.5), 1.7,
                                color=ACCENT, zorder=5))
        ax.text(cx - box_w / 2 + 1.5, y + box_h - 1.5, str(i + 1), color="white",
                fontsize=9, fontweight="bold", ha="center", va="center", zorder=6)
        if is_gate:
            ax.text(cx + box_w / 2 + 2, cy, "HUMAN /\nGUARDRAIL", color=GATE_EDGE,
                    fontsize=9.5, fontweight="bold", ha="left", va="center")

        # arrow to next
        if i < n - 1:
            ny = top - (i + 1) * ((top - bottom) / n) - box_h
            ax.add_patch(FancyArrowPatch((cx, y - 0.3), (cx, ny + box_h + 0.3),
                                         arrowstyle="-|>", mutation_scale=18,
                                         color=ACCENT, linewidth=2))

    # --- loop-back arrow (cyclic agents): routed down a left channel ---
    if num in LOOPING:
        ch = 5.0  # left channel x
        left_edge = cx - box_w / 2
        ax.plot([left_edge, ch], [centers[-1], centers[-1]], color=LOOP,
                linewidth=2, linestyle=(0, (4, 2)))
        ax.plot([ch, ch], [centers[-1], centers[0]], color=LOOP,
                linewidth=2, linestyle=(0, (4, 2)))
        ax.add_patch(FancyArrowPatch((ch, centers[0]), (left_edge, centers[0]),
                                     arrowstyle="-|>", mutation_scale=16,
                                     color=LOOP, linewidth=2, linestyle=(0, (4, 2))))
        ax.text(2.6, (centers[0] + centers[-1]) / 2, "loop", color=LOOP,
                fontsize=10, fontweight="bold", rotation=90, ha="center", va="center")

    # --- footer band ---
    ax.add_patch(FancyBboxPatch((0, 0), 100, 14, boxstyle="square,pad=0",
                                facecolor="#f3f6fb", edgecolor="none"))
    ax.plot([0, 100], [14, 14], color="#d7e0ee", linewidth=1)
    ax.text(4, 9.6, "Use case:", color=ACCENT, fontsize=10, fontweight="bold", va="center")
    ax.text(19, 9.6, wrap(USE_CASES[num], 60), color=INK, fontsize=10, va="center")
    ax.text(4, 3.2, REPO, color=MUTED, fontsize=9.5, va="center", fontweight="bold")
    ax.text(96, 3.2, "30 AI Agents in 30 Days", color=MUTED, fontsize=9.5,
            va="center", ha="right", style="italic")

    OUT.mkdir(exist_ok=True)
    path = OUT / f"day{num:02d}-{slug(spec)}.png"
    fig.savefig(path, facecolor=BG, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    return path


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for spec in CATALOG:
        p = draw(spec)
        print(f"wrote {p.name}")
    print(f"\nGenerated {len(CATALOG)} diagrams in {OUT}")


if __name__ == "__main__":
    main()
