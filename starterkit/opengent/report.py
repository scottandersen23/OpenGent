from __future__ import annotations
import json
from datetime import datetime, timezone
from jinja2 import Environment, FileSystemLoader
from .config import Settings
from .agent import summarize_findings

def build_next_actions(findings: list[dict]) -> list[str]:
    actions = []
    for f in findings:
        if f.get("severity") in ("warn", "critical") and f.get("recommended_action"):
            actions.append(f["recommended_action"])
    # de-dupe while preserving order
    seen = set()
    out = []
    for a in actions:
        if a not in seen:
            out.append(a)
            seen.add(a)
    return out[:8] if out else ["No immediate actions recommended."]

def render_weekly_report(settings: Settings, findings: list[dict], out_dir: str, client_name: str = "Client") -> dict:
    env = Environment(loader=FileSystemLoader(str(__import__("pathlib").Path(__file__).parent / "templates")))
    tmpl = env.get_template("weekly_report.md.j2")

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    ai_summary = summarize_findings(settings, findings)

    next_actions = build_next_actions(findings)
    md = tmpl.render(
        client_name=client_name,
        generated_at=generated_at,
        findings=findings,
        ai_summary=ai_summary,
        next_actions=next_actions,
    )

    out_path_md = __import__("pathlib").Path(out_dir) / "latest_report.md"
    out_path_json = __import__("pathlib").Path(out_dir) / "latest_findings.json"
    out_path_md.write_text(md, encoding="utf-8")
    out_path_json.write_text(json.dumps({"generated_at": generated_at, "findings": findings}, indent=2), encoding="utf-8")

    return {"report_md": str(out_path_md), "findings_json": str(out_path_json)}
