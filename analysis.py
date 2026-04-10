# analysis.py
# Sales and Profit Analysis Project
# Nur's first Python project for GitHub

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Excel file
df = pd.read_excel("sale and profit.xlsx")

# 2. Clean and export to CSV
df.to_csv("sales_profit_clean.csv", index=False)

# 3. Summary statistics
print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Average Profit per Order:", df["Profit"].mean())

# 4. Visualization: Profit trend over time
df.groupby("Order Date")["Profit"].sum().plot(kind="line")
plt.title("Profit Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Profit")
plt.savefig("profit_trend.png")

# 5. Visualization: Sales vs Profit by Category
df = pd.read_excel("sale and profit.xlsx")
df.groupby("Category")[["Sales","Profit"]].sum().plot(kind="bar")
plt.title("Sales vs Profit by Category")
plt.savefig("sales_profit_category.png")

# 6. Visualization: Top 10 product by profit
df.groupby("Product Name")["Profit"].sum().nlargest(10).plot(kind="bar")
plt.title("Top 10 Products by Profit")
plt.savefig("top10_products_profit.png")
