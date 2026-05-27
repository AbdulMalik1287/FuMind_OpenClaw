---
name: scada-skill
description: Fetches real-time telemetry from SCADA sensors. Source ID format machine_N (e.g. machine_1, machine_2).
---

# SCADA Skill

This skill reads SCADA telemetry data from scada_telemetry.json and returns a clean list of records.

## Usage

Fetch all SCADA telemetry:
scada_skill.fetch()

## Source ID Format

Machine IDs in this source follow the format: machine_N (e.g. machine_1, machine_2)

## fetch()

Reads scada_telemetry.json and returns records with a normalized source_machine_id field.
