from __future__ import annotations
from sqlalchemy.engine import Engine
from .base import Finding
from ..config import Settings
from ..db import fetch_all

def run(engine: Engine, s: Settings) -> list[Finding]:
    # Pull last 14 days and compute WoW for last 7 vs prior 7.
    sql = f"""
    SELECT {s.rev_date_col}::date AS day, SUM({s.rev_amount_col}) AS revenue
    FROM {s.revenue_table}
    WHERE {s.rev_date_col} >= (CURRENT_DATE - INTERVAL '14 days')
    GROUP BY 1
    ORDER BY 1
    """
    rows = fetch_all(engine, sql)
    if not rows:
        return [Finding(
            check_name="revenue",
            severity="warn",
            title="Revenue anomaly check skipped",
            details=f"No rows found in {s.revenue_table} for last 14 days. Configure REVENUE_TABLE or derive from transactions.",
            recommended_action="Point REVENUE_TABLE to a daily revenue model or implement a derived revenue query."
        )]

    # aggregate
    from datetime import date, timedelta
    today = date.today()
    start = today - timedelta(days=13)
    rev_by_day = {r["day"]: float(r["revenue"] or 0.0) for r in rows}
    last7 = 0.0
    prev7 = 0.0
    for i in range(7):
        d = today - timedelta(days=i)
        last7 += rev_by_day.get(d, 0.0)
    for i in range(7, 14):
        d = today - timedelta(days=i)
        prev7 += rev_by_day.get(d, 0.0)

    if prev7 <= 0:
        return [Finding(
            check_name="revenue",
            severity="info",
            title="Revenue anomaly check",
            details="Prior week revenue is zero or unavailable; cannot compute week-over-week change.",
            metric={"last_7d_revenue": round(last7, 2), "prev_7d_revenue": round(prev7, 2)},
            recommended_action="No action required."
        )]

    change_pct = ((last7 - prev7) / prev7) * 100.0
    severity = "info"
    if change_pct <= -abs(s.revenue_drop_pct_warn):
        severity = "warn" if change_pct > -(abs(s.revenue_drop_pct_warn) * 2) else "critical"

    details = f"Last 7 days revenue = {last7:,.2f}; prior 7 days = {prev7:,.2f}; WoW change = {change_pct:.1f}%."
    rec = "Investigate drivers: failed payments, refunds, churn, pricing, outages, attribution changes." if severity != "info" else "No action required."
    title = "Revenue drop detected" if severity != "info" else "Revenue trend stable"

    return [Finding(
        check_name="revenue",
        severity=severity,
        title=title,
        details=details,
        metric={"wow_change_pct": round(change_pct, 2), "last_7d_revenue": round(last7, 2), "prev_7d_revenue": round(prev7, 2)},
        recommended_action=rec
    )]
