

# **Data Quality & Governance Analytics Platform**

## **Overview**

The Data Quality & Governance Analytics Platform is an end-to-end solution designed to improve the accuracy, consistency, and reliability of financial transaction data. It combines a Python-based data validation engine with Tableau dashboards to provide transparent data-quality insights, operational controls monitoring, and governance reporting.

The platform mimics data-quality and governance processes commonly used in financial institutions. It automates rule execution, generates structured audit artefacts, and supports investigative analysis through dashboards. This ensures that stakeholders across data, operations, MI reporting, and risk functions can monitor data integrity with clarity and confidence.

---

## **Key Capabilities**

### **Automated Data-Quality Validation**

The Python pipeline runs a series of rule-based checks on raw financial transactions, identifying issues such as:

* Missing values
* Duplicate transaction IDs
* Invalid or incorrectly formatted dates
* Future-dated transactions
* Negative or anomalous amounts
* Missing or invalid country codes

### **Four Structured Output Datasets**

Each execution produces four datasets, each optimised for a specific governance purpose (detailed below).

### **KPI and Audit Dashboards**

Tableau dashboards present a high-level view of:

* Run status
* Total errors
* Pass rate
* Run history
* Time-series performance

These visuals support daily monitoring and management reviews.

### **Failed-Control Analytics**

Aggregated results show:

* Which controls failed
* How frequently they fail
* Severity and recurrence patterns

This helps teams prioritise remediation.

### **Record-Level Investigation**

Analysts can drill down into individual rows to see:

* Which rules failed
* Error type
* Patterns by customer, country, or time

### **Governance-Oriented Approval Workflow**

A parameter-driven approval interface simulates:

* Operational sign-off
* Risk manager approval
* Governance checkpoints

This mirrors real-world control testing and validation workflows.

---

## **Architecture**

The platform follows a modular and extensible architecture:

1. **Raw Transaction Ingestion**
   The system reads transaction data from a CSV input file and loads it into the validation engine.

2. **Python Validation Pipeline**
   The core script, **data_quality.py**, executes all rules, logs results, and generates the required artefacts.

3. **Structured Output Tables**
   Four datasets are produced to support auditability, analytics, and governance reporting.

4. **Tableau Dashboards for MI and Governance**
   Dashboards consume the output datasets, offering:

   * KPIs
   * Trend analysis
   * Row-level traceability
   * Control summaries

This architecture is similar to the data-quality and risk reporting frameworks used in banking environments.

---

## **Output Tables**

| File Name                  | Purpose                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------- |
| **clean_transactions.csv** | Contains only those records that passed all validation rules; analysis-ready dataset.   |
| **row_level_results.csv**  | Provides pass/fail outcomes for every rule per record; used for detailed investigation. |
| **control_results.csv**    | Summaries of control execution: failures, total tested, and overall control status.     |
| **audit_log.csv**          | A timestamped audit trail of each pipeline run, including run status and error counts.  |

Each table has been structured to support distinct governance needs:
operational monitoring, rule-level diagnostics, MI reporting, and audit readiness.

---

## **Technical Stack**

### **Python**

Used for automated validation logic, data cleaning, and audit log generation.
Libraries:

* Pandas
* Datetime
* OS / file handling

### **Tableau Desktop**

Used to build interactive dashboards enabling oversight, control testing analytics, and historic run summaries.

### **CSV Files / Local Storage**

Used as lightweight, transparent storage for intermediate and final datasets.

### **GitHub**

Used for version control and project documentation.

---

## **Dashboards**

### **Audit Monitoring Dashboard**

Displays:

* Run history
* Pass/fail status
* KPI cards
* Error counts
* Execution timestamps

### **Control Results Dashboard**

Shows:

* Controls that failed
* Number of records affected
* Severity patterns
* Trend of control performance over time

### **Row-Level Investigation Dashboard**

Enables identification of specific faulty records and rule breaches.

### **Clean Transactions View**

Presents the validated, trustworthy dataset ready for downstream consumption.

Screenshots are located in:
`/tableau/screenshots/`

---

## **Project Case Study**

The full documentation explaining business context, architecture, and design decisions is available at:
`/docs/case_study.md`

---

## **How to Run the Validation Pipeline**

### **1. Ensure dependencies are installed**

```
pip install -r python/requirements.txt
```

### **2. Run the script**

```
python python/data_quality.py
```

### **3. Outputs generated**

After execution, the four output tables will appear under the `/data/` directory:

* clean_transactions.csv
* row_level_results.csv
* control_results.csv
* audit_log.csv

These are automatically read by Tableau dashboards.

---

## **Future Enhancements**

* **Scheduler Automation**
  Integrate with cron (Mac/Linux), Task Scheduler (Windows), or cloud-based schedulers.

* **Cloud Deployment**
  Deploy pipeline to AWS Lambda, Azure Function Apps, or GCP Cloud Run.

* **Extended Rule Library**
  Add additional data quality checks: outliers, regex validations, cross-field checks, referential integrity rules.


