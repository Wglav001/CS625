import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Q2
# -------------------------

# Read data containing all cities
all_df = pd.read_csv("temperature_ogsheet.csv")

# Remove whitespace from column names
all_df.columns = all_df.columns.str.strip()

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# Create a count for each month
month_counts = {month: 0 for month in months}

# Find the highest monthly temperature for each city
# and count every month tied for that city's highest value
for _, row in all_df.iterrows():
    highest_temp = row[months].max()

    for month in months:
        if row[month] == highest_temp:
            month_counts[month] += 1

print(month_counts)


# Abbreviated month names for the chart
month_labels = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

counts = list(month_counts.values())

plt.figure(figsize=(10, 6))

plt.bar(month_labels, counts)

plt.xlabel("Month")
plt.ylabel("Number of Cities")
plt.title("Months with the Highest Recorded Temperature by City")

plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig("q2_highest_month_counts.png", dpi=300, bbox_inches="tight")
plt.show()