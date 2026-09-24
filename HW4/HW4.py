import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned five-city dataset
df = pd.read_csv("temperature_5cities.csv")

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()


# Months in chronological order
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]


# Convert data from wide format to long format
long_df = df.melt(
    id_vars=["State", "Station"],
    value_vars=months,
    var_name="Month",
    value_name="Record High"
)


# define the order of the months
long_df["Month"] = pd.Categorical(
    long_df["Month"],
    categories=months,
    ordered=True
)


# Abbreviated month labels
month_labels = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]




# Create Q1 line chart
plt.figure(figsize=(10, 6))

sns.lineplot(
    data=long_df,
    x="Month",
    y="Record High",
    hue="Station",
    marker="o"
)

plt.xlabel("Month")
plt.ylabel("Record High Temperature (°F)")
plt.title("Monthly Record High Temperatures for Five U.S. Cities")

plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.show()

# Check that the data loaded correctly
print(df)
print(df.columns)

