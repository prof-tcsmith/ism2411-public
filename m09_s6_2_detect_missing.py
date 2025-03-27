import pandas as pd
import numpy as np # Needed for np.nan

data = {
    'Product': ['A', 'B', None, 'B', 'A', 'C'], # Missing Product name
    'Sales': [100, 150, 120, np.nan, 110, 90], # Missing Sale value
    'Quantity': [10, 12, 11, 15, np.nan, 8]   # Missing Quantity
}
df_missing = pd.DataFrame(data)
print("DataFrame with Missing Values:")
print(df_missing)

# Check where values are null
print("\n.isnull() Check (Boolean DF):")
is_null_df = df_missing.isnull()
print(is_null_df)

# Count nulls per column
print("\n.isnull().sum() Count:")
missing_counts_series = df_missing.isnull().sum()
print(missing_counts_series)
