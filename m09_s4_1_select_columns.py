import pandas as pd

data = {
    'EmployeeID': ['E101', 'E102', 'E103'],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Salary': [70000, 80000, 75000]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# --- Select Single Column ('Salary') ---
salaries_series = df['Salary']
print("\nSelected 'Salary' (Series):")
print(salaries_series)
print(f"Type of selection: {type(salaries_series)}")


# --- Select Multiple Columns ('Name', 'Salary') ---
name_salary_df = df[['Name', 'Salary']] # Note the inner list!
print("\nSelected 'Name' and 'Salary' (DataFrame):")
print(name_salary_df)
print(f"Type of selection: {type(name_salary_df)}")


# --- Select using Dot Notation ('Name') ---
names_dot_series = df.Name
print("\nSelected 'Name' via dot (Series):")
print(names_dot_series)
print(f"Type of selection: {type(names_dot_series)}")
