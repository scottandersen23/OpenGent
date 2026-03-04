from __future__ import annotations
import requests
from .config import Settings

def send_slack(settings: Settings, title: str, message: str) -> None:
    if not settings.slack_webhook_url:
        return
    payload = {
        "text": f"*{title}*\n{message}"
    }
    r = requests.post(settings.slack_webhook_url, json=payload, timeout=15)
    r.raise_for_status()
