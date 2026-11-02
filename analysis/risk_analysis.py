import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = ROOT / "risk_register" / "ai_risk_register.csv"
RESULTS_DIR = ROOT / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# Load the risk register
df = pd.read_csv(INPUT_FILE)

required_columns = [
    "Risk_ID", "Category", "Likelihood", "Impact",
    "Residual_Likelihood", "Residual_Impact"
]

missing = [column for column in required_columns if column not in df.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

# Convert rating fields to numeric values
rating_columns = [
    "Likelihood", "Impact",
    "Residual_Likelihood", "Residual_Impact"
]

for column in rating_columns:
    df[column] = pd.to_numeric(df[column], errors="raise")

# Validate the 1-5 rating scale
for column in rating_columns:
    if not df[column].between(1, 5).all():
        raise ValueError(f"{column} must contain values from 1 to 5.")

# Recalculate risk scores
df["Inherent_Risk_Score"] = df["Likelihood"] * df["Impact"]
df["Residual_Risk_Score"] = (
    df["Residual_Likelihood"] * df["Residual_Impact"]
)

def classify_risk(score):
    if score <= 4:
        return "Low"
    elif score <= 9:
        return "Moderate"
    elif score <= 15:
        return "High"
    return "Critical"

df["Inherent_Risk_Level"] = df["Inherent_Risk_Score"].apply(classify_risk)
df["Residual_Risk_Level"] = df["Residual_Risk_Score"].apply(classify_risk)

# Calculate score reduction
df["Risk_Score_Reduction"] = (
    df["Inherent_Risk_Score"] - df["Residual_Risk_Score"]
)

# Export detailed analysis
output_file = RESULTS_DIR / "risk_analysis_summary.csv"
df.to_csv(output_file, index=False)

# Print a concise summary
print("\nAI GOVERNANCE RISK ANALYSIS")
print("=" * 55)
print(f"Total risks assessed: {len(df)}")
print("\nInherent risk levels:")
print(df["Inherent_Risk_Level"].value_counts().to_string())
print("\nResidual risk levels:")
print(df["Residual_Risk_Level"].value_counts().to_string())

print("\nRisk score comparison:")
print(
    df[[
        "Risk_ID", "Category",
        "Inherent_Risk_Score", "Inherent_Risk_Level",
        "Residual_Risk_Score", "Residual_Risk_Level"
    ]].to_string(index=False)
)

print(f"\nDetailed results saved to: {output_file}")

# Create a residual-risk matrix
matrix = (
    df.pivot_table(
        index="Residual_Impact",
        columns="Residual_Likelihood",
        values="Risk_ID",
        aggfunc="count",
        fill_value=0
    )
    .reindex(index=range(5, 0, -1), columns=range(1, 6), fill_value=0)
)

fig, ax = plt.subplots(figsize=(8, 6))
image = ax.imshow(matrix.values, cmap="YlOrRd", vmin=0, vmax=5)

ax.set_xticks(range(5))
ax.set_xticklabels(range(1, 6))
ax.set_yticks(range(5))
ax.set_yticklabels(range(5, 0, -1))
ax.set_xlabel("Residual Likelihood (1 = Rare, 5 = Almost Certain)")
ax.set_ylabel("Residual Impact (1 = Negligible, 5 = Severe)")
ax.set_title("SecureFinance Africa — Residual AI Risk Matrix")

for row in range(5):
    for col in range(5):
        ax.text(
            col, row, str(matrix.values[row, col]),
            ha="center", va="center"
        )

fig.colorbar(image, ax=ax, label="Number of Risks")
fig.tight_layout()

chart_file = RESULTS_DIR / "residual_risk_matrix.png"
fig.savefig(chart_file, dpi=300)
plt.close(fig)

print(f"Residual risk matrix saved to: {chart_file}")
