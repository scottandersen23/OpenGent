
require("dotenv").config();

const express = require("express");
const helmet = require("helmet");
const path = require("path");
const { Pool } = require("pg");

const app = express();
const PORT = process.env.PORT || 3000;

const pool = new Pool({
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  database: process.env.DB_NAME,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD
});

app.use(helmet());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, "public")));

app.post("/api/submit", async (req, res) => {
  try {
    const { name, email, role, data_stack, data_challenge, answers, referrer } = req.body;

    const query = `
      INSERT INTO leads
      (name,email,role,data_stack,data_challenge,answers,referrer)
      VALUES ($1,$2,$3,$4,$5,$6,$7)
      RETURNING id;
    `;

    const values = [
      name,
      email,
      role,
      data_stack,
      data_challenge,
      JSON.stringify(answers),
      referrer
    ];

    const result = await pool.query(query, values);

    res.json({
      success: true,
      lead_id: result.rows[0].id
    });

  } catch (error) {
    console.error(error);

    res.status(500).json({
      success: false,
      message: "Database write failed"
    });
  }
});

app.listen(PORT, () => {
  console.log(`OpenGent Lead App running on port ${PORT}`);
});
