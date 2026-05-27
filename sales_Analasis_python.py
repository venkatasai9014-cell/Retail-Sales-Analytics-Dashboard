import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load Dataset
df = pd.read_csv('Superstore.csv', encoding='latin1')

# -----------------------------
# Basic Information
# -----------------------------

print(df.head())

print(df.info())

print(df.describe())

#-----------------------------
#Missing Values
# -----------------------------

print(df.isnull().sum())

# -----------------------------
# Remove Duplicates
# -----------------------------

df.drop_duplicates(inplace=True)

# -----------------------------
# Convert Date Columns
# -----------------------------

df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# -----------------------------
# Create New Columns
# -----------------------------

df['Month'] = df['Order Date'].dt.month

df['Year'] = df['Order Date'].dt.year

df['Shipping Days'] = (
    df['Ship Date'] - df['Order Date']
).dt.days

# -----------------------------
# KPI Metrics
# -----------------------------

total_sales = df['Sales'].sum()

total_profit = df['Profit'].sum()

total_orders = df['Order ID'].nunique()

total_customers = df['Customer ID'].nunique()

print("Total Sales:", total_sales)

print("Total Profit:", total_profit)

print("Total Orders:", total_orders)

print("Total Customers:", total_customers)

# -----------------------------
# Monthly Sales Trend
# -----------------------------

monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10,5))

monthly_sales.plot(marker='o')

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.show()

# -----------------------------
# Top 10 Products
# -----------------------------

top_products = df.groupby(
    'Product Name'
)['Sales'].sum().sort_values(
    ascending=False
).head(10)

print(top_products)

plt.figure(figsize=(12,6))

top_products.plot(kind='bar')

plt.title("Top 10 Products by Sales")

plt.ylabel("Sales")

plt.show()

# -----------------------------
# Sales by Region
# -----------------------------

region_sales = df.groupby(
    'Region'
)['Sales'].sum()

plt.figure(figsize=(7,7))

region_sales.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Sales by Region")

plt.ylabel("")

plt.show()

# -----------------------------
# Profit by Category
# -----------------------------

category_profit = df.groupby(
    'Category'
)['Profit'].sum()

plt.figure(figsize=(8,5))

sns.barplot(
    x=category_profit.index,
    y=category_profit.values
)

plt.title("Profit by Category")

plt.ylabel("Profit")

plt.show()

# -----------------------------
# Customer Segment Analysis
# -----------------------------

segment_sales = df.groupby(
    'Segment'
)['Sales'].sum()

print(segment_sales)

# -----------------------------
# Average Shipping Days
# -----------------------------

avg_shipping = df['Shipping Days'].mean()

print("Average Shipping Days:", avg_shipping)

# -----------------------------
# Top 10 Customers
# -----------------------------

top_customers = df.groupby(
    'Customer Name'
)['Sales'].sum().sort_values(
    ascending=False
).head(10)

print(top_customers)

# -----------------------------
# Save Cleaned Dataset
# -----------------------------

df.to_csv(
    'data/cleaned_superstore.csv',
    index=False
)

print("Cleaned Dataset Saved")