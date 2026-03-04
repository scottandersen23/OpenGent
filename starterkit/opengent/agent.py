from __future__ import annotations
import json
import requests
from .config import Settings

SYSTEM_PROMPT = """You are OpenGent's Data Intelligence Agent.
Write concise, executive-ready summaries based only on the provided findings.
Do not speculate beyond the evidence. Avoid jargon. Provide action-oriented recommendations."""

def summarize_findings(settings: Settings, findings: list[dict], max_chars: int = 1200) -> str | None:
    if not settings.openai_api_key:
        return None

    # Use OpenAI Responses API compatible payload (works for OpenAI; some gateways may differ).
    url = settings.openai_base_url.rstrip("/") + "/responses"
    headers = {"Authorization": f"Bearer {settings.openai_api_key}", "Content-Type": "application/json"}

    user_payload = {
        "findings": findings,
        "instructions": {
            "format": "Return 5 bullets max. Each bullet: impact + recommended next action.",
            "max_length_chars": max_chars
        }
    }

    body = {
        "model": settings.openai_model,
        "input": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(user_payload)}
        ]
    }

    try:
        r = requests.post(url, headers=headers, json=body, timeout=settings.openai_timeout_seconds)
        r.raise_for_status()
        data = r.json()
        # Responses API typically returns output_text in a convenience field
        # but fall back to parsing common shapes.
        if "output_text" in data and data["output_text"]:
            return data["output_text"].strip()
        # fallback parsing
        out = []
        for item in data.get("output", []):
            for c in item.get("content", []):
                if c.get("type") == "output_text":
                    out.append(c.get("text", ""))
        text = "\n".join(out).strip()
        return text or None
    except Exception as e:
        return f"(AI summary unavailable: {e})"
