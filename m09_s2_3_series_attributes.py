import pandas as pd

months = ["Jan", "Feb", "Mar"]
sales_data = [2500, 2800, 2650]
monthly_sales = pd.Series(sales_data, index=months, name="Monthly Sales")

print(f"Series:\n{monthly_sales}")

# Accessing attributes
vals = monthly_sales.values
idx = monthly_sales.index
dtype = monthly_sales.dtype
name = monthly_sales.name
shape = monthly_sales.shape

print(f"\nValues: {vals}")
print(f"Index: {idx}")
print(f"Data type: {dtype}")
print(f"Name: {name}")
print(f"Shape: {shape}")

# You can interact with the index object too
first_label = idx[0]
print(f"First index label: {first_label}")
