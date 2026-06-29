# Physical World Sensing Agent — Context & Usage

**Agent #21 · Chapter 11: Multi-Modal Perception Agents · class `PhysicalWorldSensingAgent` · file `21_physical_world_sensing_agent.py`**

## Chapter context

Agents that perceive non-text inputs: vision-language, audio/speech, and IoT physical-world sensing.

## This agent

- **Does:** Ingests IoT sensor readings, detects threshold anomalies, recommends actions.
- **Use when:** You monitor IoT/sensor streams and need anomaly detection + response.
- **Not for:** non-sensor data.
- **Inputs:** threshold config, a reading dict of sensor->value
- **Keywords:** iot, sensors, monitoring, anomaly, telemetry, smart building, alerts
- **Example task:** Flag high CO2/temperature and recommend HVAC action.

## Techniques (from the book)

sensor fusion; temporal windowing; proportional control; deadband hysteresis

## Real-world use case (from the book)

Meridian Facilities - HVAC control, CO2 monitoring, and SLA protection.

## Book reference (official code)

The authoritative implementation and narrative for this agent live in Chapter 11 (Multi-Modal Perception Agents) of the mirrored repo:

- README: [`../../book-repo/chapter11/README.md`](../../book-repo/chapter11/README.md)
- Use case: [`../../book-repo/chapter11/USECASE.md`](../../book-repo/chapter11/USECASE.md)
- Agents notes: [`../../book-repo/chapter11/AGENTS.md`](../../book-repo/chapter11/AGENTS.md)
- Notebook: [`../../book-repo/chapter11/ch11_multimodal_agents.ipynb`](../../book-repo/chapter11/ch11_multimodal_agents.ipynb)

## Run the built-in demo

```bash
python ../../21_physical_world_sensing_agent.py
```

## Use in code

```python
import sys; sys.path.append('../..')
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(21)   # PhysicalWorldSensingAgent
# Provide the Inputs listed above, then:
# result = AgentClass(...).run(...)
# print(result.output)
```

## Route to this skill automatically

```bash
python ../../meta_agent.py "Flag high CO2/temperature and recommend HVAC action."
```
