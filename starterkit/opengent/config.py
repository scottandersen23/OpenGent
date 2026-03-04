import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

def _f(name: str, default=None):
    v = os.getenv(name)
    return v if v not in (None, "") else default

@dataclass(frozen=True)
class Settings:
    database_url: str = _f("DATABASE_URL")
    slack_webhook_url: str | None = _f("SLACK_WEBHOOK_URL", None)

    openai_api_key: str | None = _f("OPENAI_API_KEY", None)
    openai_base_url: str = _f("OPENAI_BASE_URL", "https://api.openai.com/v1")
    openai_model: str = _f("OPENAI_MODEL", "gpt-4o-mini")
    openai_timeout_seconds: int = int(_f("OPENAI_TIMEOUT_SECONDS", "30"))

    tx_table: str = _f("TX_TABLE", "transactions")
    tx_id_col: str = _f("TX_ID_COL", "transaction_id")
    tx_date_col: str = _f("TX_DATE_COL", "transaction_date")
    tx_amount_col: str = _f("TX_AMOUNT_COL", "amount")

    revenue_table: str = _f("REVENUE_TABLE", "daily_revenue")
    rev_date_col: str = _f("REV_DATE_COL", "day")
    rev_amount_col: str = _f("REV_AMOUNT_COL", "revenue")

    freshness_max_hours: int = int(_f("FRESHNESS_MAX_HOURS", "36"))
    null_pct_warn: float = float(_f("NULL_PCT_WARN", "2.0"))
    dupes_warn: int = int(_f("DUPES_WARN", "0"))
    revenue_drop_pct_warn: float = float(_f("REVENUE_DROP_PCT_WARN", "15.0"))

def get_settings() -> Settings:
    s = Settings()
    if not s.database_url:
        raise ValueError("DATABASE_URL is required. Set it in .env or environment variables.")
    return s
