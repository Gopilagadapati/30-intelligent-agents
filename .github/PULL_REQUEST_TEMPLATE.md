<!-- Thanks for contributing! Please fill in the sections below. -->

## What does this PR do?

<!-- A short summary of the change and the motivation. -->

## Related issue

<!-- e.g. Closes #12 -->

## Type of change

- [ ] Bug fix
- [ ] New agent / skill
- [ ] Existing agent or router improvement
- [ ] Docs / tooling / CI
- [ ] Other

## Checklist

- [ ] `python run_all.py` passes (31/31 agents)
- [ ] `pytest` passes
- [ ] If I changed `catalog.py`, I regenerated `agents/AGENT.md`
      (`python generate_agent_md.py`) and the skills
      (`python generate_skills.py`) and committed the results
- [ ] No new runtime dependencies (core stays standard-library only)
- [ ] I did not edit generated files (`agents/AGENT.md`, `skills/`) or the
      `book-repo/` mirror by hand
