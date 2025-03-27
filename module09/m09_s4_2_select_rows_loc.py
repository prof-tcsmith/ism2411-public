import pandas as pd

data = {'Sales': [2500, 2800, 2650, 3100]}
months = ["Jan", "Feb", "Mar", "Apr"]
df = pd.DataFrame(data, index=months)
print("DataFrame:")
print(df)

# --- Select Single Row ('Mar')---
mar_data_series = df.loc["Mar"]
print("\nRow 'Mar' (Series):")
print(mar_data_series)
print(f"Type of selection: {type(mar_data_series)}")


# --- Select Multiple Rows ('Jan', 'Apr') ---
jan_apr_df = df.loc[["Jan", "Apr"]] # List of labels
print("\nRows 'Jan', 'Apr' (DataFrame):")
print(jan_apr_df)
print(f"Type of selection: {type(jan_apr_df)}")


# --- Slice Rows ('Feb' to 'Apr') ---
feb_apr_slice_df = df.loc["Feb":"Apr"] # Includes 'Apr'
print("\nSlice 'Feb':'Apr' (DataFrame):")
print(feb_apr_slice_df)
print(f"Type of selection: {type(feb_apr_slice_df)}")
