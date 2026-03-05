Below is a **clear requirements summary for each deliverable** in the **OpenGent Data Intelligence Audit**. This structure helps you standardize engagements and ensures you can deliver the audit in **1–2 weeks with repeatable output**.

---

# OpenGent Data Intelligence Audit

## Deliverable Requirements

## 1. Data Stack Architecture Review

### Objective

Understand how data moves through the company’s systems and identify structural weaknesses.

### Inputs Required

From the client:

* Data sources list

  * Product database
  * Payment systems
  * CRM
  * Marketing tools
* Data pipeline tools
* Data warehouse
* BI tools
* Infrastructure documentation (if available)

Example stack information:

* Application DB (Postgres / MySQL)
* ETL tools
* Data warehouse
* BI platform
* Reverse ETL

### Data You Need

* pipeline architecture diagram (if available)
* ingestion schedules
* transformation frameworks
* schema structure
* access to warehouse metadata

### Analysis Performed

Evaluate:

* ingestion latency
* schema design
* pipeline dependencies
* transformation layer
* warehouse performance
* reporting architecture

### Deliverable Output

Architecture document including:

* data flow diagram
* system inventory
* pipeline reliability assessment
* architecture risks

---

# 2. KPI Definition Audit

### Objective

Ensure business metrics are **consistent, traceable, and reliable**.

### Inputs Required

From leadership or analytics team:

* KPI definitions
* executive dashboards
* finance metrics
* product metrics
* revenue calculations

Examples:

* ARR
* MRR
* churn
* CAC
* LTV
* activation
* conversion

### Data You Need

* metric SQL queries
* dashboard definitions
* data model tables
* business definitions

### Analysis Performed

Check for:

* conflicting definitions
* metric drift
* data source mismatches
* calculation inconsistencies
* transformation errors

### Deliverable Output

KPI governance report including:

* standardized metric definitions
* source-of-truth tables
* metric lineage
* recommended metric governance structure

---

# 3. Data Quality Report

### Objective

Evaluate reliability and integrity of the data environment.

### Inputs Required

* warehouse access (read-only)
* key tables
* transformation models
* historical data samples

### Data You Analyze

Key operational tables:

* transactions
* users
* events
* subscriptions
* invoices

### Tests Performed

Typical data checks:

* null values
* duplicate records
* schema inconsistencies
* timestamp anomalies
* missing ingestion cycles
* invalid foreign keys

### Deliverable Output

Data quality assessment including:

* quality score by dataset
* integrity issues
* missing data patterns
* pipeline reliability analysis

---

# 4. Anomaly Detection Analysis

### Objective

Detect hidden problems and business signals inside historical data.

### Inputs Required

* revenue data
* user activity
* product usage metrics
* financial reporting tables

### Analysis Performed

Look for:

* revenue fluctuations
* churn spikes
* customer behavior shifts
* pipeline breaks
* missing events
* abnormal data growth

### Methods Used

* statistical outlier detection
* time-series comparison
* trend deviation analysis
* cohort analysis

### Deliverable Output

Anomaly report including:

* detected anomalies
* probable root causes
* business risk impact
* recommended remediation

---

# 5. AI Automation Roadmap

### Objective

Identify where AI agents can automate monitoring, analysis, and reporting.

### Inputs Required

Insights from the previous four deliverables.

### Analysis Performed

Evaluate opportunities for:

* pipeline monitoring agents
* data validation agents
* anomaly detection agents
* executive reporting agents
* metric governance agents

### Deliverable Output

Automation roadmap including:

* prioritized automation opportunities
* recommended agent architecture
* estimated engineering effort
* potential ROI

---

# Final Deliverable Package

At the end of the engagement, the client receives:

1. **Data Architecture Review**
2. **KPI Governance Audit**
3. **Data Quality Assessment**
4. **Anomaly Detection Report**
5. **AI Automation Roadmap**

Plus an **Executive Intelligence Summary** explaining the key findings.

---

# Internal Tools to Deliver

Minimal tools required to run the audit:

* SQL
* Python
* warehouse access
* anomaly scripts
* visualization tool
* reporting template