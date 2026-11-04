cat > README.md <<'EOF'
# AICS-201: AI Ethics, Governance and Legal Compliance Assessment

## SecureFinance Africa — AI Governance Case Study

**Course:** AICS-201 – AI Ethics, Governance & Legal Frameworks  
**Assessment:** Assignment 01 – Individual Case-Based Practical  
**Project:** AI Governance Assessment for SecureFinance Africa  
**Data:** Synthetic data only

---

## 1. Project Overview

This project evaluates the ethical, legal, technical, and governance risks associated with a fictional AI-enabled financial platform called **SecureFinance Africa**.

The proposed platform uses Artificial Intelligence (AI) to support:

- Identity verification
- Financial fraud detection
- Automated financial risk assessment

The initial deployment scenario focuses on Nigeria, with consideration for possible international expansion.

The assessment examines how AI systems can be designed, evaluated, governed, and monitored responsibly while protecting individual rights, privacy, fairness, security, and institutional accountability.

**Important:** This is an academic case study. All experimental applicant records and outcomes are synthetic. No real customer or banking data is used.

---

## 2. Assessment Objectives

The project addresses five main assessment areas.

### Task 1 — Ethical Risk Identification

Identify ethical risks associated with AI-powered financial services, including:

- Algorithmic bias and discrimination
- Privacy and data protection
- Unfair financial decisions
- Lack of transparency and explainability
- Inadequate human oversight
- Cybersecurity and adversarial attacks
- Model drift and reliability
- Third-party and supply-chain risks
- Identity verification errors
- Accountability and auditability

### Task 2 — AI Governance and Risk Management

Apply the **NIST AI Risk Management Framework (AI RMF 1.0)** through its four core functions:

1. Govern
2. Map
3. Measure
4. Manage

A structured AI risk register evaluates likelihood, impact, inherent risk, proposed controls, residual risk, monitoring indicators, and escalation triggers.

### Task 3 — Legal and Ethical Compliance

Assess the relevance of the following frameworks:

| Framework | Nature |
|---|---|
| Nigeria Data Protection Act 2023 | Binding Nigerian legislation |
| EU Artificial Intelligence Act | Binding legislation where applicable |
| UNESCO Recommendation on the Ethics of AI (2021) | Non-binding ethical framework |
| OECD AI Principles | Non-binding international recommendation |

The assessment considers data protection, lawful processing, automated decision-making, high-risk AI classification, transparency, human oversight, security, and accountability.

### Task 4 — Fairness and Explainability Assessment

Develop a reproducible experiment using synthetic financial applicant data.

The experiment includes:

- Synthetic dataset generation
- Logistic regression classification
- Group-based fairness evaluation
- Demographic parity difference
- Equal opportunity difference
- Equalized odds difference
- Model performance evaluation
- Logistic regression coefficient analysis
- Permutation feature importance

### Task 5 — Integrated Assessment and Deployment Recommendation

Combine the ethical, governance, legal, fairness, and technical findings into an integrated assessment report.

The recommendation considers whether the proposed platform is ready for deployment and identifies the controls and validation activities required before production use.

---

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data generation and analysis |
| Pandas | Data manipulation |
| NumPy | Synthetic data generation |
| Scikit-learn | Machine learning and model evaluation |
| Fairlearn | Group fairness assessment |
| Matplotlib | Visualization |
| NIST AI RMF | AI governance framework |
| Git and GitHub | Version control and project management |

---

## 4. Repository Structure

```text
AICS-201-AI-Governance-Assessment/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── analysis/
│   ├── generate_synthetic_data.py
│   ├── fairness_analysis.py
│   ├── explainability_analysis.py
│   └── risk_analysis.py
│
├── data/
│   ├── README.md
│   └── synthetic_financial_applicants.csv
│
├── risk_register/
│   └── ai_risk_register.csv
│
├── evidence/
│   ├── analysis_notes.md
│   ├── ndpa_compliance_matrix.csv
│   └── legal_risk_traceability.csv
│
├── report/
│   ├── report_outline.md
│   └── legal_compliance_assessment.md
│
├── references/
│   └── references.md
│
└── results/
    ├── README.md
    ├── risk_analysis_summary.csv
    ├── residual_risk_matrix.png
    ├── fairness_metrics_by_group.csv
    ├── fairness_overall_summary.csv
    ├── fairness_test_predictions.csv
    ├── model_feature_coefficients.csv
    ├── permutation_feature_importance.csv
    └── permutation_feature_importance.png
