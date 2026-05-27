import json

class MESSkill:
    name = "mes_skill"
    source_id_format = "MACHXXX"
    description = "Fetches production batch records from the MES system."

    def fetch(self):
        with open("mes_batches.json") as f:
            records = json.load(f)
        for r in records:
            r["source_machine_id"] = r.pop("machine_id")
        return records