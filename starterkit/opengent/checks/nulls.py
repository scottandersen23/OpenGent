from __future__ import annotations
from sqlalchemy.engine import Engine
from .base import Finding
from ..config import Settings
from ..db import fetch_one

def _null_pct(engine: Engine, table: str, col: str) -> float | None:
    sql = f"""
    SELECT
      CASE WHEN COUNT(*) = 0 THEN NULL
           ELSE (SUM(CASE WHEN {col} IS NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*))
      END AS null_pct
    FROM {table}
    """
    row = fetch_one(engine, sql)
    if not row or row.get("null_pct") is None:
        return None
    return float(row["null_pct"])

def run(engine: Engine, s: Settings) -> list[Finding]:
    cols = [s.tx_id_col, s.tx_date_col, s.tx_amount_col]
    findings: list[Finding] = []
    for col in cols:
        pct = _null_pct(engine, s.tx_table, col)
        if pct is None:
            findings.append(Finding(
                check_name="nulls",
                severity="warn",
                title=f"Null rate unavailable for {col}",
                details=f"Could not compute null rate for {s.tx_table}.{col}. Table may be empty or permissions limited.",
                recommended_action="Verify table permissions and column mapping."
            ))
            continue
        severity = "info"
        if pct >= s.null_pct_warn:
            severity = "warn" if pct < (s.null_pct_warn * 3) else "critical"
        findings.append(Finding(
            check_name="nulls",
            severity=severity,
            title=f"Null rate for {col}",
            details=f"{pct:.2f}% of rows have NULL {col} in {s.tx_table}.",
            metric={"column": col, "null_pct": round(pct, 2)},
            recommended_action="Backfill missing values; enforce source requirements; add validation at ingestion."
                if severity != "info" else "No action required."
        ))
    return findings
