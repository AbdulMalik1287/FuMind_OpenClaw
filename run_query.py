from skill_registry import SkillRegistry
from reconciler import enrich
from collections import defaultdict
from tabulate import tabulate
import csv

# --- 1. Load skills ---
registry = SkillRegistry()
mes_skill = registry.get("mes_skill")
scada_skill = registry.get("scada_skill")
erp_skill = registry.get("erp_skill")

# --- 2. Fetch and reconcile data from each source ---
mes_records = enrich(mes_skill.fetch())
scada_records = enrich(scada_skill.fetch())
erp_records = enrich(erp_skill.fetch())

# --- 3. Aggregate MES: total produced, total rejected per machine ---
mes_agg = defaultdict(lambda: {"produced": 0, "rejected": 0})
for r in mes_records:
    cid = r["canonical_machine_id"]
    if cid:
        mes_agg[cid]["produced"] += r["produced"]
        mes_agg[cid]["rejected"] += r["rejected"]

# --- 4. Detect SCADA faults per machine ---
scada_faults = defaultdict(bool)
for r in scada_records:
    cid = r["canonical_machine_id"]
    if cid and r["status"] == "FAULT":
        scada_faults[cid] = True

# --- 5. ERP status mapping ---
erp_status_map = defaultdict(list)
for r in erp_records:
    cid = r["canonical_machine_id"]
    if cid:
        erp_status_map[cid].append(r["status"])

# --- 6. Build the final summary table ---
all_machines = set(mes_agg.keys()) | set(scada_faults.keys())

rows = []
for machine in sorted(all_machines):
    produced = mes_agg[machine]["produced"]
    rejected = mes_agg[machine]["rejected"]
    had_fault = "YES" if scada_faults[machine] else "NO"
    erp_statuses = erp_status_map.get(machine, [])
    erp_status_str = ", ".join(erp_statuses) if erp_statuses else "N/A"
    alert = "ALERT" if scada_faults[machine] and "DELAYED" in erp_statuses else ""
    rows.append([machine, produced, rejected, had_fault, erp_status_str, alert])

headers = ["Canonical Machine", "Total Produced", "Total Rejected", "SCADA Fault?", "ERP Status(es)", "Delayed+Fault Alert"]

print("\n=== Cross-Silo Manufacturing Query Result ===\n")
print(tabulate(rows, headers=headers, tablefmt="grid"))

# --- 7. Save as CSV ---
with open("query_output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print("\nOutput also saved to query_output.csv")