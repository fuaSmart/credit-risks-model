# Enterprise-Grade Credit Risk Model for the BNPL Sector

[![CI/CD Pipeline](https://github.com/fuaSmart/credit-risk-model/actions/workflows/ci_cd.yaml/badge.svg)](https://github.com/[your-username]/credit-risk-model/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 1. Project Overview

This project provides a robust, enterprise-grade machine learning solution for assessing credit risk in the Buy-Now-Pay-Later (BNPL) and financial services industry. The primary objective is to move beyond a simple proof-of-concept model and build a reliable, auditable, and maintainable system that can be trusted by financial stakeholders.

The solution automates the prediction of transaction fraud and customer default probability, enabling businesses to minimize credit losses while safely maximizing customer approvals. It is built with a focus on professional software engineering practices, including comprehensive testing, CI/CD automation, and model explainability.

---

## 2. The Business Problem

In the fast-paced BNPL market, accurately assessing a customer's creditworthiness is critical. Inaccurate models lead to two major business costs:

- **Credit Loss:** Approving loans for high-risk individuals who are likely to default.
- **Missed Opportunity:** Denying loans to creditworthy individuals, resulting in lost revenue and poor customer experience.

This project addresses this challenge by providing a consistent, data-driven, and transparent scoring system.

---

## 3. Key Features

This project is designed to showcase a production-ready approach to machine learning:

- **📈 Hybrid ML Model:** A planned hybrid model combining the strengths of Graph Neural Networks (GNNs) for relational data and LightGBM for high-performance classification.
- **⚙️ Automated ETL:** A modular PySpark data pipeline for processing raw transaction data into a clean, structured format.
- **🚀 FastAPI Endpoint:** A production-ready API built with FastAPI and Pydantic for real-time, schema-validated risk scoring.
- **✅ Comprehensive Testing:** Unit and integration tests written with `pytest` to ensure the reliability of data pipelines, features, and the API.
- **🤖 CI/CD Automation:** A GitHub Actions workflow automates code quality checks (linting, formatting) and testing on every commit.
- **🔍 Model Explainability:** Integration with SHAP to provide clear, visual explanations for model predictions, building trust with non-technical stakeholders.
- **🏦 Financial Compliance:** Includes documentation templates for model governance, validation, and compliance mapping (e.g., Basel II/III), demonstrating an understanding of the regulatory environment.

---

## 4. Tech Stack

- **Backend:** Python 3.9+, FastAPI, Uvicorn
- **Data Science & ML:** Pandas, PySpark, Scikit-learn, LightGBM, MLflow, SHAP, EvidentlyAI
- **Databases:** Delta Lake (for data pipeline)
- **DevOps & Testing:** Docker, Pytest, GitHub Actions, Makefile
- **Infrastructure (Planned):** Kubernetes (k8s), Seldon Core

---

## 5. Getting Started

### Prerequisites

- Python 3.9 or higher
- `venv` for virtual environment management

### Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/fuaSmart/credit-risk-model.git
    cd credit-risk-model
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r models/deployment/requirements.txt
    pip install pytest flake8 black jupyterlab
    ```

---

## 6. How to Use the Project

The `Makefile` provides convenient shortcuts for common tasks.

- **Run all tests:**

  ```bash
  make test
  ```

- **Check code for style issues (linting):**

  ```bash
  make lint
  ```

- **Automatically format the code:**

  ```bash
  make format
  ```

- **Data Analysis & Model Training:**
  All analysis and model development is done in the Jupyter Notebooks located in the `/notebooks` directory. Start the environment with:
  ```bash
  jupyter lab
  ```
