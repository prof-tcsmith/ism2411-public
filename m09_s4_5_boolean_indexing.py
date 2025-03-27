import pandas as pd

data = {
    'EmployeeID': ['E101', 'E102', 'E103', 'E104'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'Sales', 'Sales', 'IT'],
    'Salary': [70000, 80000, 75000, 90000]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# --- Condition 1: Salary > 75000 ---
condition1 = df['Salary'] > 75000
print("\nCondition 1 (Salary > 75k Boolean Series):\n", condition1)
# Use the boolean Series to filter
high_earners_df = df[condition1]
print("\nHigh Earners (Salary > 75k DataFrame):")
print(high_earners_df)

# --- Condition 2: Department is 'Sales' (Directly) ---
# Put the condition directly inside the brackets
sales_team_df = df[df['Department'] == 'Sales']
print("\nSales Team:")
print(sales_team_df)

# --- Combined Condition: Sales AND Salary > 75000 ---
# Note the parentheses around each individual condition!
high_earning_sales_df = df[(df['Department'] == 'Sales') & (df['Salary'] > 75000)]
print("\nHigh Earning Sales Team:")
print(high_earning_sales_df)
