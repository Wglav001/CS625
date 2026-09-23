import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned five-city dataset
df = pd.read_csv("temperature_5cities.csv")

# Check that the data loaded correctly
print(df)
print(df.columns)