import pandas as pd
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

# Abbreviated month labels
month_labels = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]




# Create a line for each city
for city in long_df["Station"].unique():
    city_data = long_df[long_df["Station"] == city]

    plt.plot(
        month_labels,
        city_data["Record High"],
        marker="o",
        label=city
    )


# Chart labels and formatting
plt.xlabel("Month")
plt.ylabel("Record High Temperature (°F)")
plt.title("Monthly Record High Temperatures for Five U.S. Cities")

plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.show()

# Check that the data loaded correctly
print(df)
print(df.columns)

