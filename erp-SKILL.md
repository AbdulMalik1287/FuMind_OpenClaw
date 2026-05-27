---
name: erp-skill
description: Fetches manufacturing orders from the ERP system. Source ID format M-XX (e.g. M-01, M-02).
---

# ERP Skill

This skill reads ERP orders data from erp_orders.json and returns a clean list of records.

## Usage

Fetch all ERP orders:
erp_skill.fetch()

## Source ID Format

Machine IDs in this source follow the format: M-XX (e.g. M-01, M-02)

## fetch()

Reads erp_orders.json and returns records with a normalized source_machine_id field.
