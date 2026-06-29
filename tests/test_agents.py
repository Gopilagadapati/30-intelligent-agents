"""Every agent's built-in demo must run to completion (exit code 0)."""
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
AGENTS = sorted(ROOT.glob("[0-9][0-9]_*.py"))


def test_all_31_agent_files_present():
    assert len(AGENTS) == 31, f"expected 31 agent modules, found {len(AGENTS)}"


@pytest.mark.parametrize("agent", AGENTS, ids=[a.name for a in AGENTS])
def test_agent_demo_runs(agent):
    proc = subprocess.run(
        [sys.executable, str(agent)],
        capture_output=True, text=True, timeout=120,
    )
    assert proc.returncode == 0, f"{agent.name} failed:\n{proc.stderr}"
