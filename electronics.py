import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Explore the dataset
print(df.head())
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Fill missing discounts with the mean discount
df["Discount (%)"] = df["Discount (%)"].fillna(df["Discount (%)"].mean())

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate Net Revenue
df["Net Revenue"] = df["Revenue"] * (1 - df["Discount (%)"] / 100)

# Total revenue by region
revenue_by_region = df.groupby("Region")["Net Revenue"].sum()
print("Revenue by Region:\n", revenue_by_region)

# Product with the highest sales
top_product = df.groupby("Product")["Net Revenue"].sum().idxmax()
print("Top Product by Revenue:", top_product)

# Monthly revenue trends
df["Month"] = df["Date"].dt.to_period("M")
monthly_revenue = df.groupby("Month")["Net Revenue"].sum()
print("Monthly Revenue:\n", monthly_revenue)


# Bar chart: Revenue by region
revenue_by_region.plot(kind="bar", title="Revenue by Region", color="skyblue")
plt.ylabel("Net Revenue")
plt.show()

# Line chart: Monthly revenue
monthly_revenue.plot(title="Monthly Revenue Trend")
plt.ylabel("Net Revenue")
plt.show()

# Pie chart: Revenue share by product
product_revenue = df.groupby("Product")["Net Revenue"].sum()
product_revenue.plot(kind="pie", autopct="%1.1f%%", title="Revenue Share by Product")
plt.ylabel("")  # Remove y-axis label
plt.show()

sns.boxplot(data=df, x="Region", y="Net Revenue")
plt.title("Revenue Distribution by Region")
plt.show()

category_sales = df.groupby("Category")["Net Revenue"].sum()
category_sales.plot(kind="bar", title="Sales by Category", color="lightgreen")
plt.show()
