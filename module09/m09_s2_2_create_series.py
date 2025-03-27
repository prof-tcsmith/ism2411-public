import pandas as pd

# --- Create Series from a Python list ---
sales_data_list = [2500, 2800, 2650] # e.g., sales for Q1, Q2, Q3
# Default integer index (0, 1, 2, ...) is created automatically
series_from_list = pd.Series(sales_data_list)
print("--- Series from List (Default Index) ---")
print(series_from_list)

# --- Create Series from a list with a custom index ---
months = ["Jan", "Feb", "Mar"]
# Index labels must match the number of data items
series_custom_index = pd.Series(sales_data_list, index=months)
print("\n--- Series from List (Custom Index) ---")
print(series_custom_index)

# --- Create Series from a Python dictionary ---
product_stock_dict = {"Laptop": 50, "Mouse": 250, "Keyboard": 175}
# Dictionary keys automatically become the Series index
series_from_dict = pd.Series(product_stock_dict)
print("\n--- Series from Dictionary ---")
print(series_from_dict)

# --- Giving a Series a Name ---
series_from_dict.name = 'Stock Quantity' # Assign a name attribute
print("\n--- Series with a Name ---")
print(series_from_dict)
