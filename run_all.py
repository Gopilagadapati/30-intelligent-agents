"""Run every agent's demo and report pass/fail. Usage: python run_all.py"""
import subprocess
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
agents = sorted(p for p in here.glob("[0-9][0-9]_*.py"))
failures = []
for agent in agents:
    proc = subprocess.run([sys.executable, str(agent)], capture_output=True, text=True)
    status = "PASS" if proc.returncode == 0 else "FAIL"
    print(f"{status}: {agent.name}")
    if proc.returncode != 0:
        failures.append((agent.name, proc.stderr.strip()))

print(f"\n{len(agents) - len(failures)}/{len(agents)} agents passed.")
for name, err in failures:
    print(f"\n--- {name} ---\n{err}")
sys.exit(1 if failures else 0)
