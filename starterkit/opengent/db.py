from __future__ import annotations
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from .config import Settings

def get_engine(settings: Settings) -> Engine:
    # Pooling settings are conservative for MVP. Adjust for production.
    return create_engine(settings.database_url, pool_pre_ping=True)

def fetch_one(engine: Engine, sql: str, params: dict | None = None):
    with engine.connect() as conn:
        res = conn.execute(text(sql), params or {})
        row = res.fetchone()
        return None if row is None else dict(row._mapping)

def fetch_all(engine: Engine, sql: str, params: dict | None = None):
    with engine.connect() as conn:
        res = conn.execute(text(sql), params or {})
        return [dict(r._mapping) for r in res.fetchall()]
