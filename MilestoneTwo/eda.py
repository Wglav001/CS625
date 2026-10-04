import pandas as pd
import matplotlib.pyplot as plt


# -------------------------
# Load data
# -------------------------

df = pd.read_csv("stats.csv")

print("Dataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())


# -------------------------
# Summarize metrics by age
# -------------------------

age_summary = (
    df.groupby("player_age")
      .agg(
          avg_woba=("woba", "mean"),
          avg_xwoba=("xwoba", "mean"),
          avg_avg=("batting_avg", "mean"),
          avg_slg=("slg_percent", "mean"),
          avg_iso=("isolated_power", "mean"),
          avg_k=("k_percent", "mean"),
          avg_bb=("bb_percent", "mean"),
          player_seasons=("woba", "count")
      )
      .reset_index()
)

print("\nOffensive performance by age:")
print(age_summary.to_string(index=False))


# -------------------------
# Limit individual-age charts
# to reasonable sample sizes
# -------------------------

chart_data = age_summary[
    age_summary["player_seasons"] >= 20
]


# -------------------------
# wOBA by age
# -------------------------

plt.figure(figsize=(10, 6))
plt.plot(
    chart_data["player_age"],
    chart_data["avg_woba"],
    marker="o"
)

plt.xlabel("Age")
plt.ylabel("Average wOBA")
plt.title("Average MLB Hitter wOBA by Age")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("woba_by_age.png", dpi=300)
plt.show()


# -------------------------
# SLG by age
# -------------------------

plt.figure(figsize=(10, 6))
plt.plot(
    chart_data["player_age"],
    chart_data["avg_slg"],
    marker="o"
)

plt.xlabel("Age")
plt.ylabel("Average SLG")
plt.title("Average MLB Hitter Slugging Percentage by Age")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("slg_by_age.png", dpi=300)
plt.show()


# -------------------------
# ISO by age
# -------------------------

plt.figure(figsize=(10, 6))
plt.plot(
    chart_data["player_age"],
    chart_data["avg_iso"],
    marker="o"
)

plt.xlabel("Age")
plt.ylabel("Average ISO")
plt.title("Average MLB Hitter Isolated Power by Age")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("iso_by_age.png", dpi=300)
plt.show()


# -------------------------
# Batting average by age
# -------------------------

plt.figure(figsize=(10, 6))
plt.plot(
    chart_data["player_age"],
    chart_data["avg_avg"],
    marker="o"
)

plt.xlabel("Age")
plt.ylabel("Batting Average")
plt.title("Average MLB Batting Average by Age")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("avg_by_age.png", dpi=300)
plt.show()


# -------------------------
# Strikeout rate by age
# -------------------------

plt.figure(figsize=(10, 6))
plt.plot(
    chart_data["player_age"],
    chart_data["avg_k"],
    marker="o"
)

plt.xlabel("Age")
plt.ylabel("Strikeout Rate (%)")
plt.title("Average MLB Hitter Strikeout Rate by Age")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("strikeout_rate_by_age.png", dpi=300)
plt.show()


# -------------------------
# Walk rate by age
# -------------------------

plt.figure(figsize=(10, 6))
plt.plot(
    chart_data["player_age"],
    chart_data["avg_bb"],
    marker="o"
)

plt.xlabel("Age")
plt.ylabel("Walk Rate (%)")
plt.title("Average MLB Hitter Walk Rate by Age")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("walk_rate_by_age.png", dpi=300)
plt.show()


# -------------------------
# xwOBA by age
# -------------------------

plt.figure(figsize=(10, 6))
plt.plot(
    chart_data["player_age"],
    chart_data["avg_xwoba"],
    marker="o"
)

plt.xlabel("Age")
plt.ylabel("Average xwOBA")
plt.title("Average MLB Hitter xwOBA by Age")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("xwoba_by_age.png", dpi=300)
plt.show()


# =========================================================
# AGE GROUP ANALYSIS
# =========================================================

# Create broader age groups to reduce year-to-year noise.
# Ages outside 21-37 are excluded from this grouped analysis
# because there are relatively few qualifying hitter-seasons.

age_group_data = df[
    df["player_age"].between(21, 37)
].copy()

age_group_data["age_group"] = pd.cut(
    age_group_data["player_age"],
    bins=[20, 24, 28, 32, 37],
    labels=["21-24", "25-28", "29-32", "33-37"]
)


# -------------------------
# Summarize by age group
# -------------------------

age_group_summary = (
    age_group_data.groupby(
        "age_group",
        observed=True
    )
    .agg(
        avg_woba=("woba", "mean"),
        avg_slg=("slg_percent", "mean"),
        avg_iso=("isolated_power", "mean"),
        avg_k=("k_percent", "mean"),
        avg_bb=("bb_percent", "mean"),
        player_seasons=("woba", "count")
    )
    .reset_index()
)

print("\nOffensive performance by age group:")
print(age_group_summary.to_string(index=False))


# -------------------------
# wOBA by age group
# -------------------------

plt.figure(figsize=(9, 6))

plt.plot(
    age_group_summary["age_group"],
    age_group_summary["avg_woba"],
    marker="o"
)

plt.xlabel("Age Group")
plt.ylabel("Average wOBA")
plt.title("Average MLB Hitter wOBA by Age Group")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("woba_by_age_group.png", dpi=300)
plt.show()


# -------------------------
# ISO by age group
# -------------------------

plt.figure(figsize=(9, 6))

plt.plot(
    age_group_summary["age_group"],
    age_group_summary["avg_iso"],
    marker="o"
)

plt.xlabel("Age Group")
plt.ylabel("Average ISO")
plt.title("Average MLB Hitter Isolated Power by Age Group")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("iso_by_age_group.png", dpi=300)
plt.show()


# -------------------------
# Strikeout rate by age group
# -------------------------

plt.figure(figsize=(9, 6))

plt.plot(
    age_group_summary["age_group"],
    age_group_summary["avg_k"],
    marker="o"
)

plt.xlabel("Age Group")
plt.ylabel("Strikeout Rate (%)")
plt.title("Average MLB Hitter Strikeout Rate by Age Group")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("strikeout_rate_by_age_group.png", dpi=300)
plt.show()


# -------------------------
# Walk rate by age group
# -------------------------

plt.figure(figsize=(9, 6))

plt.plot(
    age_group_summary["age_group"],
    age_group_summary["avg_bb"],
    marker="o"
)

plt.xlabel("Age Group")
plt.ylabel("Walk Rate (%)")
plt.title("Average MLB Hitter Walk Rate by Age Group")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("walk_rate_by_age_group.png", dpi=300)
plt.show()