import pandas as pd
from io import StringIO

# --- Setup DataFrame ---
csv_content = """Date,Product,Revenue,Quantity
2025-01-05,WidgetA,150,10
2025-01-06,WidgetB,200,12
2025-01-06,WidgetA,160,11
2025-01-07,WidgetC,90,8"""
df = pd.read_csv(StringIO(csv_content))
# --- --- --- --- --- ---

print("--- Inspecting the DataFrame ---")

# 1. First 2 rows
print("\n.head(2):")
print(df.head(2))

# 2. Dimensions
shape_tuple = df.shape
print(f"\n.shape: {shape_tuple}")

# 3. Concise Summary
print("\n.info():")
df.info() # Prints directly

# 4. Data types
dtypes_series = df.dtypes
print(f"\n.dtypes:\n{dtypes_series}")

# 5. Column names
cols = df.columns
print(f"\n.columns: {cols}")

# 6. Index
idx = df.index
print(f"\n.index: {idx}")
