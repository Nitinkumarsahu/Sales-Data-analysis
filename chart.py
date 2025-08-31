import pandas as pd
import matplotlib.pyplot as plt

# Load data
sales_df = pd.read_excel('sales_data_analysis.xlsx')
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

# Extract month period
sales_df['Month'] = sales_df['Date'].dt.to_period('M')

# Aggregate monthly sales
monthly_sales = sales_df.groupby('Month')['Total Sales'].sum()

# Aggregate sales by category
category_sales = sales_df.groupby('Category')['Total Sales'].sum()

# Plot monthly sales trend
plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o')
plt.title('Monthly Total Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot sales by category bar chart
plt.figure(figsize=(8,5))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot sales revenue share by category (pie chart)
plt.figure(figsize=(7,7))
category_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Sales Revenue Share by Category')
plt.ylabel('')  # Hide y-label
plt.tight_layout()
plt.show()
