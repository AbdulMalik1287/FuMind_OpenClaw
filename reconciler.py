import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("reconciler")

MACHINE_REGISTRY = {
    "FM-01": ["M-01", "MACH001", "machine_1"],
    "FM-02": ["M-02", "MACH002", "machine_2"],
}

_reverse_map = {}
for canonical_id, aliases in MACHINE_REGISTRY.items():
    for alias in aliases:
        _reverse_map[alias] = canonical_id


def resolve(source_id: str):
    canonical = _reverse_map.get(source_id)
    if canonical is None:
        logger.warning(f"Unknown machine ID: '{source_id}' — skipping.")
    return canonical


def enrich(records: list, id_field: str = "source_machine_id") -> list:
    enriched = []
    for record in records:
        r = record.copy()
        r["canonical_machine_id"] = resolve(r.get(id_field))
        enriched.append(r)
    return enriched