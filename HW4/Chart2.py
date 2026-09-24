import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset containing all cities
df = pd.read_csv("temperature_ogsheet.csv")

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()


# Months in chronological order
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]


# Create a count for each month
month_counts = {month: 0 for month in months}


# Find the highest recorded temperature for each city
for _, row in df.iterrows():

    highest_temp = row[months].max()

    # Count each month that is tied for the city's highest temperature
    for month in months:
        if row[month] == highest_temp:
            month_counts[month] += 1


# Print counts to check the results
print(month_counts)


# Convert month counts to a DataFrame for the chart
count_df = pd.DataFrame({
    "Month": months,
    "Count": [month_counts[month] for month in months]
})


# Define the order of the months
count_df["Month"] = pd.Categorical(
    count_df["Month"],
    categories=months,
    ordered=True
)


# Create Q2 bar chart
plt.figure(figsize=(10, 6))

sns.barplot(
    data=count_df,
    x="Month",
    y="Count"
)

plt.xlabel("Month")
plt.ylabel("Number of Cities")
plt.title("Months with the Highest Recorded Temperature by City")

plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.show()