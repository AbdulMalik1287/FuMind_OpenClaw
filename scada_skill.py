import json

class SCADASkill:
    name = "scada_skill"
    source_id_format = "machine_N"
    description = "Fetches real-time telemetry from SCADA sensors."

    def fetch(self):
        with open("scada_telemetry.json") as f:
            records = json.load(f)
        for r in records:
            r["source_machine_id"] = r.pop("machine")
        return records