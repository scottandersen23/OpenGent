
CREATE TABLE IF NOT EXISTS leads (

id SERIAL PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL,
role TEXT,
data_stack TEXT,
data_challenge TEXT,
answers JSONB,
referrer TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
