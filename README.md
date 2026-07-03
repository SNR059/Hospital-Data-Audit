
# Metropolis General Hospital: Surgical Suite Operational Audit Pipeline

## Project Overview
This repository contains a production-grade Python data processing pipeline designed to ingest, clean, and analyze complex clinical operational data from a high-volume surgical center. The pipeline simulates the rigorous triage and data administration required to manage surgical flows, optimize patient throughput, and track key clinical outcomes.

## Core Capabilities
* **Data Cleaning & Regex Standardization:** Automatically handles data-entry anomalies, structural inconsistencies, and malformed strings within clinical logs.
* **Statistical Modeling:** Leverages SciPy and NumPy to run descriptive and inferential statistical operations on surgical performance metrics.
* **Clinical Architecture Insight:** Formulated through the lens of a clinical practitioner to isolate high-acuity administrative friction points.

## Technologies Used
* **Language:** Python 3
* **Libraries:** Pandas (Dataframe manipulation), NumPy (Numerical frameworks), SciPy (Statistical calculation), Re (Regular Expressions parsing)

## How It Works
The primary script `audit_pipeline.py` executes a structured multi-layer processing sequence:
1. **Ingestion:** Loads the raw, unformatted clinical logs.
2. **Triage & Audit:** Detects missing entries and uses customized regular expressions to standardize clinical strings.
3. **Analysis:** Generates core performance metrics, calculating baseline throughput efficiencies and operational variances.
