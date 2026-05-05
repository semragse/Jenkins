# Jenkins CI/CD for Data Engineering Pipeline

## 🎯 Project Overview
Automated ETL pipeline with Jenkins CI/CD integration. Demonstrates continuous integration practices for data engineering workflows.

## 📁 Project Structure
```
.
├── etl.py              # Main ETL pipeline (Extract, Transform, Load)
├── test_data.py        # Data quality validation tests
├── requirements.txt    # Python dependencies
├── Jenkinsfile        # Jenkins pipeline configuration (Declarative)
└── output/            # Generated output files (gitignored)
```

## 🚀 What This Pipeline Does

1. **Extract**: Generates sample sales data
2. **Transform**: Applies business logic (tax calculation, categorization)
3. **Load**: Saves to CSV with metadata
4. **Test**: Validates data quality and business rules
5. **Archive**: Stores results as Jenkins artifacts

## 🔧 Local Testing (Without Jenkins)

```bash
# Install dependencies
pip install -r requirements.txt

# Run ETL
python etl.py

# Run tests
python test_data.py
```

## 🏗️ Jenkins Pipeline Stages

| Stage | Purpose | What It Does |
|-------|---------|--------------|
| **Setup** | Dependency installation | Installs pandas and other requirements |
| **Run ETL** | Execute pipeline | Runs etl.py to process data |
| **Run Tests** | Data validation | Runs test_data.py to ensure quality |
| **Archive Results** | Store outputs | Saves CSV and JSON to Jenkins artifacts |

## 📊 Output Files

- `output/sales_report.csv` - Transformed sales data
- `output/metadata.json` - Pipeline execution metadata

## ✅ Interview Talking Points

**Why Jenkins for Data Engineering?**
- Automate daily ETL jobs
- Validate data quality automatically
- Track pipeline execution history
- Integrate with Git for version control
- Schedule jobs (nightly data loads, etc.)

**This Pipeline Demonstrates:**
- Declarative pipeline syntax
- Environment variables
- Multi-stage workflow
- Artifact archiving
- Post-build actions (success/failure handling)
