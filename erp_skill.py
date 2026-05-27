import json

class ERPSkill:
    name = "erp_skill"
    source_id_format = "M-XX"
    description = "Fetches manufacturing orders from the ERP system."

    def fetch(self):
        with open("erp_orders.json") as f:
            records = json.load(f)
        for r in records:
            r["source_machine_id"] = r.pop("machine")
        return records