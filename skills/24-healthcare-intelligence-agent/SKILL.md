---
name: 24-healthcare-intelligence-agent
description: Healthcare Intelligence Agent (Chapter 13, Healthcare and Scientific Agents). Bayesian clinical decision support: updates condition probability from findings (educational). Use when: Clinical/medical screening framed as Bayesian probability over symptoms/findings. Triggers: healthcare, medical, clinical, diagnosis, bayesian, sepsis, patient.
---

# Skill 24 — Healthcare Intelligence Agent

*Chapter 13: Healthcare and Scientific Agents*

## What it does

Bayesian clinical decision support: updates condition probability from findings (educational).

## When to use this skill

Clinical/medical screening framed as Bayesian probability over symptoms/findings.

## When NOT to use

general non-medical reasoning; this is a demo, not medical advice.

## Inputs required

a prior, likelihood ratios, a findings dict

## Triggers / keywords

healthcare, medical, clinical, diagnosis, bayesian, sepsis, patient

## Example task

Estimate sepsis probability from vitals.

## Techniques (from the book)

FHIR normalization; Bayesian belief updating (posterior = likelihood x prior); 0.15 escalation threshold; immutable audit trail; differential privacy

## Real-world use case (from the book)

Pinnacle Health Network - catches missed sepsis earlier with auditable decisions.

## Book reference (official code)

- Chapter 13: Healthcare and Scientific Agents
- README: [`../../book-repo/chapter13/README.md`](../../book-repo/chapter13/README.md)
- Use case: [`../../book-repo/chapter13/USECASE.md`](../../book-repo/chapter13/USECASE.md)
- Agents notes: [`../../book-repo/chapter13/AGENTS.md`](../../book-repo/chapter13/AGENTS.md)
- Notebook: [`../../book-repo/chapter13/ch13_healthcare_scientific_agents.ipynb`](../../book-repo/chapter13/ch13_healthcare_scientific_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 24_healthcare_intelligence_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(24)   # HealthcareIntelligenceAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.

> Educational demonstration only — not professional advice.
