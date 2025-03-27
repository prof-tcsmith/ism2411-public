import pandas as pd
import numpy as np

data = {
    'Product': ['A', 'B', None, 'B', 'A', 'C'],
    'Sales': [100, 150, 120, np.nan, 110, 90],
    'Quantity': [10, 12, 11, 15, np.nan, 8]
}
df_missing = pd.DataFrame(data)
print("Original DataFrame with Missing Values:")
print(df_missing)

# Quick preview - dropping rows with any NaN
print("\nPreview: After dropping rows with any NaN:")
df_dropped = df_missing.dropna()
print(df_dropped)
