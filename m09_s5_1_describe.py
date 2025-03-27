import pandas as pd

data = {
    'Product': ['A', 'B', 'A', 'B', 'A', 'C'],
    'Sales': [100, 150, 120, 160, 110, 90],
    'Quantity': [10, 12, 11, 15, 10, 8]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Get descriptive statistics
print("\nDescriptive Statistics (.describe()):")
desc_stats_df = df.describe() # The result is a DataFrame
print(desc_stats_df)
