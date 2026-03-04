# OpenGent Data Intelligence Agent Starter Kit (Prototype)

A working prototype for OpenGent AI Corp: **data health + anomaly detection + AI insight summarization + Slack alerts + weekly executive report**.

This kit is intentionally **simple, deployable, and client-stack agnostic**:
- Connect to any SQL database via `DATABASE_URL` (Postgres, Snowflake*, BigQuery*, etc.)
- Run standardized checks (freshness, nulls, duplicates, revenue anomalies)
- Generate a weekly executive report (Markdown)
- Optionally summarize findings with an LLM
- Optionally send alerts to Slack via webhook

> **Note:** Snowflake/BigQuery connectors are optional. Start with Postgres for the MVP.

## What You Get
- `opengent/checks/` – reusable data health checks
- `opengent/agent.py` – LLM summarizer (OpenAI-compatible)
- `opengent/slack.py` – Slack webhook notifier
- `opengent/report.py` – weekly executive report generator
- `opengent/cli.py` – run checks + generate report (one command)

## Quick Start

### 1) Setup
```bash
cd opengent-data-intelligence-agent-starter-kit
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

### 2) Configure
Edit `.env`:

- `DATABASE_URL` (required) e.g. `postgresql+psycopg2://user:pass@host:5432/dbname`
- `SLACK_WEBHOOK_URL` (optional)
- `OPENAI_API_KEY` (optional, enables AI summaries)
- `OPENAI_MODEL` (optional; defaults provided)

### 3) Run a Weekly Report
```bash
python -m opengent.cli weekly
```

Outputs:
- `reports/latest_report.md`
- `reports/latest_findings.json`

### 4) Run Once + Send Slack Alert (if configured)
```bash
python -m opengent.cli weekly --notify-slack
```

## Data Model Assumptions (MVP)
This prototype expects you to map your client to these logical tables:

- `transactions` (or equivalent)
  - `transaction_id` (unique-ish id)
  - `transaction_date` (date or timestamp)
  - `amount` (numeric)
  - `status` (optional)
- `daily_revenue` (or derived from transactions)
  - `day` (date)
  - `revenue` (numeric)

If your client schema differs, update `opengent/config.py` table names and column mappings.

## Typical Delivery Flow (Client Engagement)
1. Set up read-only DB credentials and verify access
2. Configure table/column mappings
3. Run checks + generate baseline report
4. Add 1–2 custom checks (client-specific KPIs)
5. Deploy as scheduled job (cron/GitHub Actions/Cloud Run/etc.)

## Safety / Compliance Notes
- Do **not** send raw PII to LLMs.
- Use sampling/redaction for any sensitive fields.
- Keep the LLM summary focused on aggregate metrics and anomalies.

## Roadmap Ideas (Next)
- dbt metadata ingestion + lineage-aware checks
- Metric definition registry + drift detection
- Self-healing playbooks (Jira ticket creation, runbooks, auto rollback)

---
© OpenGent AI Corp – Prototype starter kit.
