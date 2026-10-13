
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# Load Statcast dataset
# -------------------------

df = pd.read_csv("stats.csv")

# Limit to the same age range used in Milestone 2
df = df[df["player_age"].between(21, 37)].copy()

df["age_group"] = pd.cut(
    df["player_age"],
    bins=[20, 24, 28, 32, 37],
    labels=["21-24", "25-28", "29-32", "33-37"]
)

# -------------------------
# Calculate age-group averages
# -------------------------

summary = (
    df.groupby("age_group", observed=True)
    .agg(
        wOBA=("woba", "mean"),
        SLG=("slg_percent", "mean"),
        **{
            "Strikeout Rate": ("k_percent", "mean"),
            "Walk Rate": ("bb_percent", "mean")
        }
    )
    .reset_index()
)

print("Original averages:")
print(summary.to_string(index=False))

# -------------------------
# Normalize each metric
# Baseline: ages 21-24 = 100
# -------------------------

metrics = ["wOBA", "SLG", "Strikeout Rate", "Walk Rate"]

for metric in metrics:
    baseline = summary[metric].iloc[0]
    summary[metric] = summary[metric] / baseline * 100

print("\nNormalized averages:")
print(summary.to_string(index=False))

# Convert to long format for Seaborn
plot_data = summary.melt(
    id_vars="age_group",
    value_vars=metrics,
    var_name="Metric",
    value_name="Indexed Value"
)

# -------------------------
# Create final visualization
# -------------------------

sns.set_theme(style="whitegrid")

colors = {
    "wOBA": "#6C757D",
    "SLG": "#0072B2",
    "Strikeout Rate": "#D55E00",
    "Walk Rate": "#009E73"
}

fig, ax = plt.subplots(figsize=(12, 7))

sns.lineplot(
    data=plot_data,
    x="age_group",
    y="Indexed Value",
    hue="Metric",
    hue_order=metrics,
    palette=colors,
    marker="o",
    markersize=10,
    linewidth=3,
    ax=ax
)

# Baseline reference
ax.axhline(
    100,
    color="gray",
    linestyle="--",
    linewidth=1,
    alpha=0.6
)

# Finding-focused headline
ax.set_title(
    "MLB Hitters' Overall Production Stays Stable,\n"
    "But the Numbers Behind It Change with Age",
    fontsize=18,
    fontweight="bold",
    pad=22
)

ax.set_xlabel("Player Age Group", fontsize=12)

ax.set_ylabel(
    "Indexed Average (Ages 21-24 = 100)",
    fontsize=12
)

ax.set_ylim(85, 115)

# -------------------------
# Annotate final percentage changes
# -------------------------

label_offsets = {
    "wOBA": 0.5,
    "SLG": -0.5,
    "Strikeout Rate": 0,
    "Walk Rate": 0
}

for metric in metrics:
    final_value = summary[metric].iloc[-1]
    change = final_value - 100

    ax.annotate(
        f"{change:+.1f}%",
        xy=(3, final_value),
        xytext=(12, label_offsets[metric]),
        textcoords="offset points",
        color=colors[metric],
        fontsize=12,
        fontweight="bold",
        va="center",
        annotation_clip=False
    )

# Leave room on the right for annotations
ax.set_xlim(-0.15, 3.35)

# Legend
ax.legend(
    title="Batting Metric",
    loc="upper left",
    frameon=False
)

# Context beneath chart
fig.text(
    0.5, 0.01,
    "Source: Baseball Savant Statcast (2015-2025) | "
    "Qualifying hitter-seasons (250+ PA) | "
    "Values indexed to youngest age group",
    ha="center",
    fontsize=9,
    color="dimgray"
)

sns.despine()
plt.tight_layout(rect=[0, 0.04, 1, 1])

# Save chart
plt.savefig(
    "final_statcast_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
