import pandas as pd

data = {
    'Sales': [100, 150, 120, 160, 110, 90],
    'Quantity': [10, 12, 11, 15, 10, 8]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# --- Stats on 'Sales' Series ---
mean_sales = df['Sales'].mean()
max_sales = df['Sales'].max()
total_sales = df['Sales'].sum()
count_sales = df['Sales'].count() # Counts non-missing values

print(f"\nMean Sales: {mean_sales:.2f}")
print(f"Max Sales: {max_sales:.2f}")
print(f"Total Sales: {total_sales:.2f}")
print(f"Count of Sales: {count_sales}")

# --- Stats on entire DataFrame ---
mean_all = df.mean() # Calculates mean for each column
print(f"\nMean per column:\n{mean_all}")

max_all = df.max() # Calculates max for each column
print(f"\nMax per column:\n{max_all}")
