# Healthcare Intelligence Agent — Context & Usage

**Agent #24 · Chapter 13: Healthcare and Scientific Agents · class `HealthcareIntelligenceAgent` · file `24_healthcare_intelligence_agent.py`**

## Chapter context

Domain agents for biomedical research and care: Bayesian clinical decision support and hypothesis-driven scientific discovery (educational only).

## This agent

- **Does:** Bayesian clinical decision support: updates condition probability from findings (educational).
- **Use when:** Clinical/medical screening framed as Bayesian probability over symptoms/findings.
- **Not for:** general non-medical reasoning; this is a demo, not medical advice.
- **Inputs:** a prior, likelihood ratios, a findings dict
- **Keywords:** healthcare, medical, clinical, diagnosis, bayesian, sepsis, patient
- **Example task:** Estimate sepsis probability from vitals.

## Techniques (from the book)

FHIR normalization; Bayesian belief updating (posterior = likelihood x prior); 0.15 escalation threshold; immutable audit trail; differential privacy

## Real-world use case (from the book)

Pinnacle Health Network - catches missed sepsis earlier with auditable decisions.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 13 (Healthcare and Scientific Agents) of the mirrored repo:

- README: [`../../book-repo/chapter13/README.md`](../../book-repo/chapter13/README.md)
- Use case: [`../../book-repo/chapter13/USECASE.md`](../../book-repo/chapter13/USECASE.md)
- Agents notes: [`../../book-repo/chapter13/AGENTS.md`](../../book-repo/chapter13/AGENTS.md)
- Notebook: [`../../book-repo/chapter13/ch13_healthcare_scientific_agents.ipynb`](../../book-repo/chapter13/ch13_healthcare_scientific_agents.ipynb)

## Run the built-in demo

```bash
python ../../24_healthcare_intelligence_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(24)   # HealthcareIntelligenceAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Estimate sepsis probability from vitals."
```

> Educational demonstration only — not professional advice.
