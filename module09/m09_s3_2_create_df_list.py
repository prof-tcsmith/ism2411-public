import pandas as pd
import numpy as np # Import numpy to use np.nan for missing values

# Data as a list of dicts (rows)
data_list = [
    {'EmployeeID': 'E101', 'Name': 'Alice', 'Department': 'HR', 'Salary': 70000},
    {'EmployeeID': 'E102', 'Name': 'Bob', 'Department': 'Sales', 'Salary': 80000},
    {'EmployeeID': 'E103', 'Name': 'Charlie', 'Department': 'Sales', 'Salary': np.nan}, # Missing Salary
    {'EmployeeID': 'E104', 'Name': 'David', 'Department': 'IT', 'Salary': 90000, 'Location': 'NY'} # Extra Location
]

# Create DataFrame
df_employees_from_list = pd.DataFrame(data_list)

print("--- DataFrame from List of Dicts ---")
print(df_employees_from_list)
