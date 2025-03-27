import pandas as pd

months = ["Jan", "Feb", "Mar", "Apr"]
sales_data = [2500, 2800, 2650, 3100]
s = pd.Series(sales_data, index=months)
print(f"Sales Series:\n{s}")

# --- Access by Label ---
feb_sales = s["Feb"] # Preferred way for labeled index
print(f"\nSales in Feb (label 'Feb'): {feb_sales}")

# --- Access by Integer Position (.iloc) ---
# Get the first item (position 0)
jan_sales_iloc = s.iloc[0]
print(f"Sales in first month (iloc[0]): {jan_sales_iloc}")

# Get the last item (position -1)
apr_sales_iloc = s.iloc[-1]
print(f"Sales in last month (iloc[-1]): {apr_sales_iloc}")

# --- Slicing ---
# Slice by label - often includes endpoint for .loc or direct [] slicing
jan_to_mar_sales_loc = s.loc["Jan":"Mar"] # Using .loc explicitly
print(f"\nSales Jan to Mar (loc['Jan':'Mar']):\n{jan_to_mar_sales_loc}")

# Slice by position (stop index is exclusive)
feb_mar_sales_iloc = s.iloc[1:3] # Positions 1 and 2 (up to, not including, 3)
print(f"\nSales Feb to Mar (iloc[1:3]):\n{feb_mar_sales_iloc}")
