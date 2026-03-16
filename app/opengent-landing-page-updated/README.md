
# OpenGent Landing Page (Production MVP)

This repository contains a production‑ready landing page for collecting early access leads.

## Stack

Frontend
- React
- TypeScript
- Vite

Backend
- Node.js
- Express
- Prisma ORM

Database
- PostgreSQL

## Core Features

• Dark navy UI with purple/blue gradient styling  
• Early access signup form  
• Lead storage in Postgres  
• Hidden referrer tracking field  
• Smooth CTA scroll to form  
• Progressive form fields to increase conversion  
• API validation

## Conversion Optimizations Implemented

1. **Clear Hero Value Proposition**
2. **Problem → Solution section**
3. **Reduced friction form with optional details**
4. **Immediate confirmation message**
5. **Referrer tracking** via query parameter `?ref=`

Example:

```
https://opengent.ai/?ref=linkedin
```

## Database Schema

```
CREATE TABLE leads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  company TEXT,
  role TEXT,
  data_challenge TEXT,
  data_stack TEXT,
  referrer TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

## Running the Project

### Backend

```
cd backend
npm install
npx prisma generate
npm run dev
```

### Frontend

```
cd frontend
npm install
npm run dev
```

## Production Best Practices Included

• API validation  
• Type safety with TypeScript  
• Environment variables  
• Database ORM (Prisma)  
• Clean project structure

## Out of Scope (Future)

• Email automation
• CRM integration
• Lead scoring
• Analytics dashboards
• A/B testing
