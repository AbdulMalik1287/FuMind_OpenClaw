---
name: mes-skill
description: Fetches production batch records from the MES system. Source ID format MACHXXX (e.g. MACH001, MACH002).
---

# MES Skill

This skill reads MES batch data from mes_batches.json and returns a clean list of records.

## Usage

Fetch all MES batches:
mes_skill.fetch()

## Source ID Format

Machine IDs in this source follow the format: MACHXXX (e.g. MACH001, MACH002)

## fetch()

Reads mes_batches.json and returns records with a normalized source_machine_id field.