import matplotlib
matplotlib.use("Agg")  # force non-GUI backend (macOS safe)

import pandas as pd
import matplotlib.pyplot as plt
import os

print("Running in:", os.getcwd())

# Load CSV
df = pd.read_csv("introspection_run.csv")

# Create plot
plt.figure(figsize=(10, 5))
plt.plot(df["step"], df["confidence"], label="Confidence", linewidth=2)
plt.plot(df["step"], df["uncertainty"], label="Uncertainty", linewidth=2)
plt.plot(df["trust_score"] / 100, label="Trust (scaled)", linestyle="--")

# Shade regions where autonomy is False
for i, allowed in enumerate(df["autonomy_allowed"]):
    if not allowed:
        plt.axvspan(i - 0.5, i + 0.5, color="red", alpha=0.08)

plt.xlabel("Step")
plt.ylabel("Normalized Value")
plt.title("Runtime Governance: Autonomy Grant, Revocation, Escalation")
plt.legend()
plt.tight_layout()

# Save file (absolute path to avoid ambiguity)
output_path = "/Users/akhileshwarik/project_root/runtime_governance_plot.png"
plt.savefig(output_path, dpi=150)

print("Plot saved to:", output_path)

