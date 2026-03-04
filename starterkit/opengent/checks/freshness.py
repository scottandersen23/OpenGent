from __future__ import annotations
from sqlalchemy.engine import Engine
from .base import Finding
from ..config import Settings
from ..db import fetch_one

def run(engine: Engine, s: Settings) -> list[Finding]:
    # Computes max timestamp in TX table and compares to now (DB side).
    sql = f"""
    SELECT
      MAX({s.tx_date_col}) AS max_ts,
      EXTRACT(EPOCH FROM (NOW() - MAX({s.tx_date_col}))) / 3600.0 AS hours_since_max
    FROM {s.tx_table}
    """
    row = fetch_one(engine, sql) or {}
    hours = row.get("hours_since_max")
    if hours is None:
        return [Finding(
            check_name="freshness",
            severity="critical",
            title="No transaction timestamps found",
            details=f"Could not compute freshness. Table {s.tx_table} may be empty or {s.tx_date_col} invalid.",
            recommended_action="Verify ingestion into the transaction table and confirm date column mapping."
        )]
    severity = "info"
    if hours > s.freshness_max_hours:
        severity = "warn" if hours <= s.freshness_max_hours * 2 else "critical"
    return [Finding(
        check_name="freshness",
        severity=severity,
        title="Data freshness check",
        details=f"Latest {s.tx_date_col} is {row.get('max_ts')}; approximately {hours:.1f} hours since latest record.",
        metric={"hours_since_latest": round(hours, 2), "max_ts": str(row.get("max_ts"))},
        recommended_action="Investigate ingestion lag, upstream source availability, and scheduler failures."
            if severity != "info" else "No action required."
    )]
