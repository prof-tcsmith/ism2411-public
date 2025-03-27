import pandas as pd
from io import StringIO # Used to simulate a file in memory

# CSV content as a multi-line string
csv_content = """Date,Product,Revenue
2025-01-05,WidgetA,150
2025-01-06,WidgetB,200
2025-01-06,WidgetA,160"""

# Use StringIO to make the string behave like a file object
csv_file_simulator = StringIO(csv_content)

# Read from the simulated file using pandas read_csv function
# In practice, you'd use: df_sales = pd.read_csv("your_file.csv")
df_sales = pd.read_csv(csv_file_simulator)

print("--- DataFrame loaded from simulated CSV ---")
print(df_sales)
# Pandas infers column names from the first row and data types.
