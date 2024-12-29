import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
print('oad the dataset')
file_path = "your_dataset.csv"  # Replace with your dataset path
df = pd.read_csv('Bitcoin_Historical_Data.csv')

# Display first 5 rows
print('Display first 5 rows')
print(df.head())

# Display dataset info
print('Display dataset info')
print(df.info())

# Display summary statistics
print('isplay summary statistics')
print(df.describe())

# Count rows and columns
print('Count rows and columns')
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Check for missing values
print('Check for missing values')
print(df.isnull().sum())

# Fill missing values with the median
print('Fill missing values with the median')
df['Close'] = df['Close'].fillna(df['Close'].median())

# Rename columns
print('Rename columns')
df.rename(columns={'Adj Close': 'Adj Close2'}, inplace=True)

# Display first 5 rows
print('Display first 5 rows')
print(df.head())

# Filter rows
print('Filter rows')
filtered_data = df[df['Close'] > 50]

# Sort data
print('Sort data')
sorted_data = df.sort_values('High', ascending=False)

# Group by and aggregate
print('Group by and aggregate')
grouped_data = df.groupby('High')['Low'].mean()
print(grouped_data)

# Plot a histogram
print('Plot a histogram')
df['High'].hist()
plt.title('Distribution of NumericColumn')
plt.show()

# Plot a histogram
print('Plot a histogram')
df['Low'].hist()
plt.title('Distribution of NumericColumn')
plt.show()