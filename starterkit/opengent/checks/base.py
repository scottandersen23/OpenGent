from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Literal

Severity = Literal["info", "warn", "critical"]

@dataclass
class Finding:
    check_name: str
    severity: Severity
    title: str
    details: str
    metric: dict[str, Any] | None = None
    recommended_action: str | None = None
