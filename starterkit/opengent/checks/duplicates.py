from __future__ import annotations
from sqlalchemy.engine import Engine
from .base import Finding
from ..config import Settings
from ..db import fetch_one

def run(engine: Engine, s: Settings) -> list[Finding]:
    sql = f"""
    SELECT COALESCE(SUM(CASE WHEN cnt > 1 THEN 1 ELSE 0 END),0) AS duplicate_keys
    FROM (
      SELECT {s.tx_id_col} AS k, COUNT(*) AS cnt
      FROM {s.tx_table}
      GROUP BY {s.tx_id_col}
    ) t
    """
    row = fetch_one(engine, sql) or {"duplicate_keys": 0}
    dupes = int(row.get("duplicate_keys") or 0)
    severity = "info"
    if dupes > s.dupes_warn:
        severity = "warn" if dupes <= max(10, s.dupes_warn) else "critical"
    return [Finding(
        check_name="duplicates",
        severity=severity,
        title="Duplicate transaction key check",
        details=f"Found {dupes} duplicated {s.tx_id_col} keys in {s.tx_table}.",
        metric={"duplicate_keys": dupes},
        recommended_action="Add de-duplication in ingestion/transform layer; enforce unique keys; check source replays."
            if severity != "info" else "No action required."
    )]
