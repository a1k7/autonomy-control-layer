from introspection.api import IntrospectionEngine
import csv

engine = IntrospectionEngine()

rows = []

print("step | decision | confidence | uncertainty | trust | autonomy")
print("-" * 60)

for step in range(1, 20):

    # Phase design
    if step <= 8:          # stable behavior
        pred, obs = "approve", "approve"
    elif step <= 14:       # silent failure
        pred, obs = "approve", "reject"
    else:                  # recovery
        pred, obs = "approve", "approve"

    out = engine.step(
        signature="finance:approve",
        predicted=pred,
        observed=obs
    )

    out["step"] = step
    rows.append(out)

    print(
        f"{step:>4} | "
        f"{out['decision']:<8} | "
        f"{out['confidence']:.2f}      | "
        f"{out['uncertainty']:.2f}       | "
        f"{out['trust_score']:.1f}  | "
        f"{out['autonomy_allowed']}"
    )

# Write CSV
with open("introspection_run.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "step",
            "decision",
            "confidence",
            "uncertainty",
            "trust_score",
            "autonomy_allowed",
        ],
    )
    writer.writeheader()

    filtered_rows = []
    for r in rows:
        filtered_rows.append({
            "step": r["step"],
            "decision": r["decision"],
            "confidence": r["confidence"],
            "uncertainty": r["uncertainty"],
            "trust_score": r["trust_score"],
            "autonomy_allowed": r["autonomy_allowed"],
        })

    writer.writerows(filtered_rows)
