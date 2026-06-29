---
name: 21-physical-world-sensing-agent
description: Physical World Sensing Agent (Chapter 11, Multi-Modal Perception Agents). Ingests IoT sensor readings, detects threshold anomalies, recommends actions. Use when: You monitor IoT/sensor streams and need anomaly detection + response. Triggers: iot, sensors, monitoring, anomaly, telemetry, smart building, alerts.
---

# Skill 21 — Physical World Sensing Agent

*Chapter 11: Multi-Modal Perception Agents*

## What it does

Ingests IoT sensor readings, detects threshold anomalies, recommends actions.

## When to use this skill

You monitor IoT/sensor streams and need anomaly detection + response.

## When NOT to use

non-sensor data.

## Inputs required

threshold config, a reading dict of sensor->value

## Triggers / keywords

iot, sensors, monitoring, anomaly, telemetry, smart building, alerts

## Example task

Flag high CO2/temperature and recommend HVAC action.

## Techniques (from the book)

sensor fusion; temporal windowing; proportional control; deadband hysteresis

## Real-world use case (from the book)

Meridian Facilities - HVAC control, CO2 monitoring, and SLA protection.

## Book reference (official code)

- Chapter 11: Multi-Modal Perception Agents
- README: [`../../book-repo/chapter11/README.md`](../../book-repo/chapter11/README.md)
- Use case: [`../../book-repo/chapter11/USECASE.md`](../../book-repo/chapter11/USECASE.md)
- Agents notes: [`../../book-repo/chapter11/AGENTS.md`](../../book-repo/chapter11/AGENTS.md)
- Notebook: [`../../book-repo/chapter11/ch11_multimodal_agents.ipynb`](../../book-repo/chapter11/ch11_multimodal_agents.ipynb)

## How to run

```bash
# from the 30agents/ root
python 21_physical_world_sensing_agent.py                 # built-in demo
python meta_agent.py "<your task>"  # let the router pick this skill
```

```python
import sys; sys.path.append('../..')   # path to 30agents/ root
from meta_agent import MetaAgent
AgentClass = MetaAgent.load(21)   # PhysicalWorldSensingAgent
# construct with the inputs above, then call .run(...)
```

See `CONTEXT_AND_USAGE.md` in this folder for full chapter context and details.
