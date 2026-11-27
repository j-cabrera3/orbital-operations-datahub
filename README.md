# Orbital Operations Data Hub

An end-to-end ETL pipeline that extracts launch and space-related data from NASA and SpaceX APIs, transforms the data using Python, and loads it into PostgreSQL for analysis and reporting.

---

## Project Overview

The goal of this project is to demonstrate modern data engineering concepts including:

- API data extraction
- Python-based ETL workflows
- Data transformation and validation
- PostgreSQL integration
- Automated testing
- CI/CD pipeline automation

The project retrieves data from publicly available NASA and SpaceX APIs, standardizes the information, and stores it in PostgreSQL for downstream analytics and reporting.

---

## Architecture

```text
NASA API
    ↓
Python ETL
    ↓
Data Transformation
    ↓
PostgreSQL

SpaceX API
    ↓
Python ETL
    ↓
Data Transformation
    ↓
PostgreSQL
```

---

## Technologies Used

### Languages & Libraries

- Python 3.15
- Pandas
- Requests
- Psycopg2
- PyYAML
- Python-Dotenv

### Database

- PostgreSQL

### Development & Automation

- Git
- GitLab CI/CD
- Pytest
- VS Code

---

## Project Structure

```text
orbital-operations-datahub/
│
├── config/
│   └── Database configuration
│
├── etl/
│   ├── nasa_etl.py
│   └── spacex_etl.py
│
├── sql/
│   └── schema/
│
├── tests/
│   └── Unit tests
│
├── utils/
│   ├── db.py
│   └── logger.py
│
├── requirements.txt
├── requirements-dev.txt
└── .gitlab-ci.yml
```

---

## Features

### NASA ETL Pipeline

- Retrieves data from NASA APIs
- Transforms API responses into structured datasets
- Loads data into PostgreSQL

### SpaceX ETL Pipeline

- Retrieves launch and mission data from SpaceX APIs
- Performs data cleaning and transformation
- Loads processed data into PostgreSQL

### Automated Testing

- Unit tests using Pytest
- Validation of ETL functionality

### CI/CD Automation

- Automated linting
- Automated testing
- Automated ETL execution through GitLab pipelines

---

## Installation

### Clone Repository

```bash
git clone https://github.com/j-cabrera3/orbital-operations-datahub.git
```

### Navigate to Project

```bash
cd orbital-operations-datahub
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the ETL Pipelines

Run NASA pipeline:

```bash
python -m etl.nasa_etl
```

Run SpaceX pipeline:

```bash
python -m etl.spacex_etl
```

---

## Example Skills Demonstrated

- REST API Integration
- ETL Design Patterns
- Data Transformation
- Relational Databases
- PostgreSQL Development
- Logging and Error Handling
- Git Version Control
- CI/CD Automation
- Python Project Structure

---

## Future Enhancements

Potential improvements include:

- Docker containerization
- Scheduling with Apache Airflow
- Data warehouse implementation
- Power BI dashboard integration
- Historical launch analytics
- Expanded test coverage
- Cloud deployment

---

## Author

Johnny Cabrera

Data professional with interests in Data Engineering, ETL Development, Business Systems Analysis, and Analytics Engineering.

GitHub: https://github.com/j-cabrera3
