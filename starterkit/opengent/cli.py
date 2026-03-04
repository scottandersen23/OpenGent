from __future__ import annotations
import argparse
import os
from .config import get_settings
from .db import get_engine
from .checks import DEFAULT_CHECKS
from .report import render_weekly_report
from .slack import send_slack

def run_checks():
    s = get_settings()
    engine = get_engine(s)
    findings = []
    for fn in DEFAULT_CHECKS:
        try:
            findings.extend([f.__dict__ for f in fn(engine, s)])
        except Exception as e:
            findings.append({
                "check_name": getattr(fn, "__module__", "check"),
                "severity": "critical",
                "title": "Check execution failed",
                "details": str(e),
                "metric": None,
                "recommended_action": "Review database connectivity, permissions, and SQL compatibility."
            })
    return s, findings

def main():
    parser = argparse.ArgumentParser(prog="opengent", description="OpenGent Data Intelligence Agent Prototype")
    sub = parser.add_subparsers(dest="cmd", required=True)

    weekly = sub.add_parser("weekly", help="Run checks and generate a weekly executive report")
    weekly.add_argument("--notify-slack", action="store_true", help="Send summary to Slack if configured")
    weekly.add_argument("--client-name", default=os.getenv("CLIENT_NAME", "Client"), help="Client name for report header")

    args = parser.parse_args()
    if args.cmd == "weekly":
        s, findings = run_checks()
        out_dir = os.path.join(os.path.dirname(__file__), "..", "reports")
        out = render_weekly_report(s, findings, out_dir=out_dir, client_name=args.client_name)

        if args.notify_slack:
            # Send only warn/critical titles in Slack for signal clarity
            hot = [f for f in findings if f.get("severity") in ("warn","critical")]
            if hot:
                lines = []
                for f in hot[:6]:
                    lines.append(f"• {f.get('title')} ({f.get('severity')})")
                msg = "\n".join(lines)
            else:
                msg = "No warn/critical findings detected."

            send_slack(s, "OpenGent Weekly Data Intelligence", msg + f"\n\nReport: {out['report_md']}")

        print("Generated:")
        print(f" - {out['report_md']}")
        print(f" - {out['findings_json']}")

if __name__ == "__main__":
    main()
