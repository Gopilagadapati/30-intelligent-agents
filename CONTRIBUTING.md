# Contributing

Thanks for your interest in improving the 30-agents toolkit! This project is an
educational re-implementation of the agent patterns from *30 Intelligent Agents
Every AI Engineer Should Know* (Imran Ahmad, Packt). Contributions that make the
patterns clearer, more correct, or better documented are very welcome.

## Project layout (what to edit)

- **`catalog.py`** — the single source of truth for every agent's metadata
  (capability, *use-when*, inputs, keywords, techniques, real-world use case, and
  book references). `agents/AGENT.md` and everything under `skills/` are
  **generated** from it — never edit those by hand.
- **`NN_*.py`** — the 31 self-contained agent modules. Each ships a `MockLLM`
  demo so it runs offline.
- **`common/`** — shared scaffolding (`llm.py`, `base.py`, `memory.py`, `tools.py`).
- **`meta_agent.py`** — the routing MetaAgent.
- **`tests/`** — the pytest suite.
- **`book-repo/`** — a read-only mirror of the official Packt repo. Do not edit.

## Development setup

```bash
python --version           # 3.10+
pip install ".[dev]"       # installs pytest (everything else is stdlib)
```

The agents run **fully offline** via the built-in `MockLLM`. Set `OPENAI_API_KEY`
or `ANTHROPIC_API_KEY` (and `pip install ".[openai]"` / `".[anthropic]"`) only if
you want to exercise a live model.

## Before opening a pull request

1. **Run the suite** and make sure everything is green:
   ```bash
   python run_all.py        # expect "31/31 agents passed"
   pytest                   # expect all tests passing
   ```
2. **If you changed `catalog.py`, regenerate the derived docs:**
   ```bash
   python generate_agent_md.py
   python generate_skills.py
   ```
   Commit the regenerated `agents/AGENT.md` and `skills/` alongside your change.
3. Keep changes focused; one logical change per PR.
4. Match the existing style: standard-library-only core, no new runtime
   dependencies, ASCII in code (`->` instead of `→`), and concise comments.

## Reporting issues

Use the issue templates (bug report / feature request) and include the Python
version, the command you ran, and the full error output where relevant.

## License & scope

By contributing you agree your work is released under the project's
[MIT License](LICENSE). Note the Healthcare, Financial, and Legal agents are
**educational demonstrations only** — please keep that framing intact and do not
present them as professional advice.
