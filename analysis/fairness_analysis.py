import pandas as pd
import numpy as np

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
from fairlearn.metrics import (
    MetricFrame,
    selection_rate,
    true_positive_rate,
    false_positive_rate,
    demographic_parity_difference,
    equalized_odds_difference
)

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "synthetic_financial_applicants.csv"
RESULTS_DIR = ROOT / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# Load synthetic data
df = pd.read_csv(DATA_FILE)

# Sensitive attribute is used for evaluation only.
sensitive_features = df["Demographic_Group"]

# Exclude group membership and target from model features.
feature_columns = [
    "Age",
    "Annual_Income",
    "Credit_History",
    "Debt_To_Income",
    "Employment_Years"
]

X = df[feature_columns]
y = df["Actual_Eligible"]

# Split data while preserving eligibility proportions.
X_train, X_test, y_train, y_test, group_train, group_test = (
    train_test_split(
        X,
        y,
        sensitive_features,
        test_size=0.30,
        random_state=42,
        stratify=y
    )
)

# Train a reproducible baseline model.
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(
        max_iter=1000,
        random_state=42
    ))
])

model.fit(X_train, y_train)

# Predictions on held-out test data.
y_pred = model.predict(X_test)

# Define metrics for group-level evaluation.
metrics = {
    "Selection_Rate": selection_rate,
    "True_Positive_Rate": true_positive_rate,
    "False_Positive_Rate": false_positive_rate,
    "Accuracy": accuracy_score,
    "Precision": precision_score,
    "Recall": recall_score,
    "F1_Score": f1_score
}

# Evaluate outcomes by demographic group.
metric_frame = MetricFrame(
    metrics=metrics,
    y_true=y_test,
    y_pred=y_pred,
    sensitive_features=group_test
)

group_results = metric_frame.by_group
group_results.index.name = "Demographic_Group"
group_results.to_csv(RESULTS_DIR / "fairness_metrics_by_group.csv")

# Calculate overall fairness differences.
dp_difference = demographic_parity_difference(
    y_test,
    y_pred,
    sensitive_features=group_test
)

eo_difference = metric_frame.difference(
    method="between_groups"
)["True_Positive_Rate"]

eod_difference = equalized_odds_difference(
    y_test,
    y_pred,
    sensitive_features=group_test
)

# Overall model performance.
performance = {
    "Accuracy": accuracy_score(y_test, y_pred),
    "Precision": precision_score(y_test, y_pred, zero_division=0),
    "Recall": recall_score(y_test, y_pred, zero_division=0),
    "F1_Score": f1_score(y_test, y_pred, zero_division=0),
    "Demographic_Parity_Difference": dp_difference,
    "Equal_Opportunity_Difference": eo_difference,
    "Equalized_Odds_Difference": eod_difference
}

pd.DataFrame([performance]).to_csv(
    RESULTS_DIR / "fairness_overall_summary.csv",
    index=False
)

# Save predictions with group membership for auditability.
prediction_results = X_test.copy()
prediction_results["Demographic_Group"] = group_test.values
prediction_results["Actual_Eligible"] = y_test.values
prediction_results["Predicted_Eligible"] = y_pred

prediction_results.to_csv(
    RESULTS_DIR / "fairness_test_predictions.csv",
    index=False
)

# Save model coefficients for a basic explainability analysis.
classifier = model.named_steps["classifier"]

coefficients = pd.DataFrame({
    "Feature": feature_columns,
    "Standardized_Coefficient": classifier.coef_[0]
})

coefficients["Absolute_Importance"] = (
    coefficients["Standardized_Coefficient"].abs()
)

coefficients = coefficients.sort_values(
    "Absolute_Importance",
    ascending=False
)

coefficients.to_csv(
    RESULTS_DIR / "model_feature_coefficients.csv",
    index=False
)

# Print results.
print("=" * 65)
print("SECUREFINANCE AFRICA - SYNTHETIC AI FAIRNESS ASSESSMENT")
print("=" * 65)

print(f"\nTraining records: {len(X_train)}")
print(f"Testing records: {len(X_test)}")

print("\nOverall model performance:")
for name, value in performance.items():
    print(f"{name}: {value:.4f}")

print("\nFairness metrics by demographic group:")
print(group_results.round(4).to_string())

print("\nFairness differences:")
print(f"Demographic parity difference: {dp_difference:.4f}")
print(f"Equal opportunity difference: {eo_difference:.4f}")
print(f"Equalized odds difference: {eod_difference:.4f}")

print("\nModel feature coefficients:")
print(coefficients.round(4).to_string(index=False))

print("\nGenerated evidence:")
for filename in [
    "fairness_metrics_by_group.csv",
    "fairness_overall_summary.csv",
    "fairness_test_predictions.csv",
    "model_feature_coefficients.csv"
]:
    print(f"- results/{filename}")

print("\nNote: All data and outcomes are synthetic.")
print("Fairness metrics describe this experiment, not real customers.")
