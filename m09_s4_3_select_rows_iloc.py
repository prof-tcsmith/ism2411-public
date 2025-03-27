import pandas as pd

data = {'Sales': [2500, 2800, 2650, 3100, 2900]}
months = ["Jan", "Feb", "Mar", "Apr", "May"] # Index labels don't matter for iloc
df = pd.DataFrame(data, index=months)
print("DataFrame:")
print(df)
# Positions: 0    1     2     3     4

# --- Select Row at Position 1 ('Feb' data) ---
row_pos_1_series = df.iloc[1]
print("\nRow at position 1 (Series):")
print(row_pos_1_series)
print(f"Type of selection: {type(row_pos_1_series)}")


# --- Select Rows at Positions 0 and 3 ('Jan', 'Apr' data) ---
rows_pos_0_3_df = df.iloc[[0, 3]] # List of positions
print("\nRows at positions 0, 3 (DataFrame):")
print(rows_pos_0_3_df)
print(f"Type of selection: {type(rows_pos_0_3_df)}")


# --- Slice Rows from Position 1 up to 4 ('Feb', 'Mar', 'Apr' data) ---
rows_pos_1_to_4_df = df.iloc[1:4] # Excludes position 4
print("\nSlice positions 1:4 (DataFrame):")
print(rows_pos_1_to_4_df)
print(f"Type of selection: {type(rows_pos_1_to_4_df)}")
