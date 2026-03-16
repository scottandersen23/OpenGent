
# OpenGent Lead Assessment

Lightweight lead capture app designed for Raspberry Pi deployment.

## Install

npm install

## Configure

cp .env.example .env

## Initialize database

npm run db:init

## Run server

npm start

Visit:

http://localhost:3000

## Verify database

psql -h localhost -p 5433 -U postgres -d postgres

SELECT * FROM leads;
