import pandas as pd

# Data for employees
data_dict = {
    'EmployeeID': ['E101', 'E102', 'E103', 'E104'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'Sales', 'Sales', 'IT'],
    'Salary': [70000, 80000, 75000, 90000]
}

# Create DataFrame
df_employees = pd.DataFrame(data_dict)

print("--- DataFrame from Dict of Lists ---")
print(df_employees)
