import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import permutation_importance

DATA_PATH = "data/synthetic_financial_applicants.csv"

df = pd.read_csv(DATA_PATH)

features = [
    "Age",
    "Annual_Income",
    "Credit_History",
    "Debt_To_Income",
    "Employment_Years"
]

X = df[features]
y = df["Actual_Eligible"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42))
])

model.fit(X_train, y_train)

importance = permutation_importance(
    model,
    X_test,
    y_test,
    scoring="f1",
    n_repeats=20,
    random_state=42
)

results = pd.DataFrame({
    "Feature": features,
    "Mean_Importance": importance.importances_mean,
    "Standard_Deviation": importance.importances_std
}).sort_values("Mean_Importance", ascending=False)

results.to_csv(
    "results/permutation_feature_importance.csv",
    index=False
)

print("\nPERMUTATION FEATURE IMPORTANCE")
print("=" * 55)
print(results.to_string(index=False))

plt.figure(figsize=(9, 5))
plt.barh(
    results["Feature"],
    results["Mean_Importance"],
    xerr=results["Standard_Deviation"]
)
plt.xlabel("Decrease in F1 score after feature permutation")
plt.title("Model Explainability - Permutation Feature Importance")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(
    "results/permutation_feature_importance.png",
    dpi=300
)
plt.close()

print("\nGenerated:")
print("- results/permutation_feature_importance.csv")
print("- results/permutation_feature_importance.png")
