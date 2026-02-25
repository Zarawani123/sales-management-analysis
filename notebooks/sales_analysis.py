2️⃣ Python Notebook (sales_analysis.ipynb)
🔹 Install Requirements
pip install pandas matplotlib seaborn
🔹 Python Code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("../data/sales_data.csv")

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()

print("Total Sales:", round(total_sales,2))
print("Total Profit:", round(total_profit,2))
print("Total Orders:", total_orders)
🔹 Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().sort_values()

region_sales.plot(kind="barh")
plt.title("Sales by Region")
plt.show()
🔹 Monthly Sales Trend
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.show()
🔹 Profit by Category
category_profit = df.groupby("Category")["Profit"].sum()
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.show()