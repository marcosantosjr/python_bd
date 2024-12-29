import pandas as pd
import numpy as np

# Generate fake sales data
np.random.seed(42)
data = {
    "Date": pd.date_range(start="2022-01-01", periods=1000),
    "Product": np.random.choice(["Laptop", "Smartphone", "Tablet", "Accessories"], 1000),
    "Category": np.random.choice(["Electronics", "Mobile", "Accessories"], 1000),
    "Revenue": np.random.uniform(50, 5000, 1000).round(2),
    "Region": np.random.choice(["North", "South", "East", "West"], 1000),
    "Units Sold": np.random.randint(1, 50, 1000),
    "Discount (%)": np.random.choice([5, 10, 15, 20, 25, None], 1000),
}

sales_df = pd.DataFrame(data)
sales_df.to_csv("sales_data.csv", index=False)