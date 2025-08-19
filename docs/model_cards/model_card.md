# Model Card: BNPL Customer Credit Risk Assessment

## 1. Model Details

- **Model Name:** Hybrid GNN+LightGBM Credit Scoring Model
- **Model Version:** 1.0.0
- **Developed By:** Fuad Kedir
- **Development Date:** 2025-08-19

## 2. Business Objective

- **Purpose:** To provide an automated and reliable credit risk assessment for new and existing customers of a Buy-Now-Pay-Later (BNPL) service, modeled after Xente.
- **Business Problem:** The core business challenge is to minimize credit losses from customer defaults while maximizing loan approvals for creditworthy applicants. An inaccurate or unreliable risk model can lead to significant financial losses or missed revenue opportunities.
- **Target Audience:** This model and its outputs are intended for use by the credit and risk management departments.

## 3. Technical Overview

- **Model Type:** A hybrid ensemble model combining a Graph Neural Network (GNN) for relational feature extraction and a LightGBM model for final probability of default (PD) prediction.
- **Inputs:**
    -   Customer transaction history (frequency, amounts, merchants).
    -   Recency, Frequency, Monetary (RFM) aggregated features.
    -   (Future) Graph-based features derived from user-merchant interaction networks.
- **Outputs:**
    -   **Default Probability (0-1):** The likelihood that a customer will default on a payment.
    -   **Credit Score (300-850):** A standardized score translated from the default probability for easier interpretation.
    -   **Recommended Credit Limit:** A suggested maximum credit line based on the customer's risk profile.

## 4. Business Impact

- **Reduces Default Rate:** By more accurately identifying high-risk applicants, the model aims to lower the percentage of non-performing loans.
- **Increases Approval Rate:** By confidently identifying low-risk applicants, the model can help safely increase the customer base and transaction volume.
- **Ensures Consistency:** Provides an objective and consistent framework for credit decisions, reducing manual bias and improving auditability.