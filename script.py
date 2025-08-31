import pandas as pd
from io import BytesIO
import base64

# Creating sample sales data
sales_data = {
    'Date': ['2025-01-05', '2025-01-15', '2025-02-10', '2025-02-21', '2025-03-01', '2025-03-15', '2025-04-10', '2025-04-22'],
    'Product ID': ['P001', 'P002', 'P001', 'P003', 'P002', 'P004', 'P003', 'P005'],
    'Product Name': ['Headphones', 'T-Shirt', 'Headphones', 'Coffee Maker', 'T-Shirt', 'Blender', 'Coffee Maker', 'Smartwatch'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home Appliances', 'Clothing', 'Home Appliances', 'Home Appliances', 'Electronics'],
    'Units Sold': [10, 25, 15, 5, 10, 7, 8, 12],
    'Unit Price': [50, 20, 50, 80, 20, 60, 80, 150],
}

# Convert Date to datetime type
sales_df = pd.DataFrame(sales_data)
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

# Calculate Total Sales
sales_df['Total Sales'] = sales_df['Units Sold'] * sales_df['Unit Price']

# Save to Excel
filename = "sales_data_analysis.xlsx"
sales_df.to_excel(filename, index=False)

filename