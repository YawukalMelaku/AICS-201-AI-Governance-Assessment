import numpy as np
import pandas as pd
from pathlib import Path

# Reproducibility
np.random.seed(42)

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

N = 1000

# Synthetic demographic groups
groups = np.random.choice(
    ["Group_A", "Group_B"],
    size=N,
    p=[0.5, 0.5]
)

# Generate applicant characteristics
age = np.random.randint(21, 61, N)

# Introduce a controlled income distribution difference
annual_income = np.where(
    groups == "Group_A",
    np.random.normal(65000, 15000, N),
    np.random.normal(52000, 15000, N)
)

annual_income = np.clip(annual_income, 15000, 150000)

credit_history = np.clip(
    np.random.normal(650, 75, N),
    300,
    850
)

debt_to_income = np.clip(
    np.random.normal(0.35, 0.15, N),
    0.05,
    0.85
)

employment_years = np.clip(
    np.random.normal(6, 4, N),
    0,
    35
)

# Generate a synthetic eligibility outcome.
# Group membership is deliberately excluded from this formula.
income_score = (annual_income - 50000) / 15000
credit_score = (credit_history - 600) / 75
debt_score = (0.40 - debt_to_income) / 0.15
employment_score = (employment_years - 5) / 4

eligibility_score = (
    0.30 * income_score
    + 0.35 * credit_score
    + 0.20 * debt_score
    + 0.15 * employment_score
)

# Convert score into a probability
probability = 1 / (1 + np.exp(-eligibility_score))

actual_eligible = np.random.binomial(1, probability)

# Build dataset
df = pd.DataFrame({
    "Age": age,
    "Annual_Income": annual_income.round(2),
    "Credit_History": credit_history.round(2),
    "Debt_To_Income": debt_to_income.round(3),
    "Employment_Years": employment_years.round(2),
    "Demographic_Group": groups,
    "Actual_Eligible": actual_eligible
})

output_file = DATA_DIR / "synthetic_financial_applicants.csv"
df.to_csv(output_file, index=False)

print("=" * 55)
print("SYNTHETIC FINANCIAL DATASET GENERATED")
print("=" * 55)
print(f"Total applicants: {len(df)}")
print(f"Features: {len(df.columns)}")
print("\nGroup distribution:")
print(df["Demographic_Group"].value_counts())

print("\nEligibility distribution:")
print(df["Actual_Eligible"].value_counts())

print("\nAverage annual income by group:")
print(df.groupby("Demographic_Group")["Annual_Income"].mean())

print(f"\nDataset saved to: {output_file}")
