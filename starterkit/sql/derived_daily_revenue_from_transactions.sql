-- Derive daily revenue from a transactions table (edit for your schema)
-- Assumes:
--  - transaction_date (timestamp/date)
--  - amount (numeric)
--  - status indicates successful payments (optional)
SELECT
  DATE(transaction_date) AS day,
  SUM(amount) AS revenue
FROM transactions
WHERE 1=1
  -- AND status = 'succeeded'
GROUP BY 1
ORDER BY 1;
