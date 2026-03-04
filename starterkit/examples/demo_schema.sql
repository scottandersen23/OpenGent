-- Minimal demo schema for local testing
CREATE TABLE IF NOT EXISTS transactions (
  transaction_id TEXT NOT NULL,
  transaction_date TIMESTAMP NOT NULL,
  amount NUMERIC(12,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS daily_revenue (
  day DATE NOT NULL,
  revenue NUMERIC(12,2) NOT NULL
);
