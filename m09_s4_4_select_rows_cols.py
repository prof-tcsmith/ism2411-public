import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'Sales', 'Sales', 'IT'],
    'Salary': [70000, 80000, 75000, 90000]
}
index_labels = ['E101', 'E102', 'E103', 'E104']
df = pd.DataFrame(data, index=index_labels)
print("DataFrame:")
print(df)

# --- Using .loc[row_labels, column_labels] ---
# Get Name and Salary for E102 and E103
subset_loc_df = df.loc[['E102', 'E103'], ['Name', 'Salary']]
print("\nUsing .loc (Labels):")
print(subset_loc_df)
print(f"Type of selection: {type(subset_loc_df)}")


# --- Using .iloc[row_positions, column_positions] ---
# Get data in rows 0 and 2, columns 1 and 2
# (Department and Salary for Alice and Charlie)
subset_iloc_df = df.iloc[[0, 2], [1, 2]]
print("\nUsing .iloc (Positions):")
print(subset_iloc_df)
print(f"Type of selection: {type(subset_iloc_df)}")


# Get a single value: Bob's Salary (Row label 'E102', Column label 'Salary')
bob_salary_loc = df.loc['E102', 'Salary']
print(f"\nBob's Salary (loc): {bob_salary_loc}")
print(f"Type of selection: {type(bob_salary_loc)}")


# Get a single value: Bob's Salary (Row position 1, Column position 2)
bob_salary_iloc = df.iloc[1, 2]
print(f"Bob's Salary (iloc): {bob_salary_iloc}")
print(f"Type of selection: {type(bob_salary_iloc)}")
