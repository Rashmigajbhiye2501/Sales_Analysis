import pandas as pd
import random
import calendar

# Simulated market data for three companies over 6 months
companies = ['Company ABC', 'Company XYZ', 'Company Rect']
months = [calendar.month_name[i] for i in range(1, 7)]

data = {
    'Company': [random.choice(companies) for _ in range(54)],
    'Month': [random.choice(months) for _ in range(54)],
    'Sales': [random.randint(1000, 5000) for _ in range(54)],
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Calculate overall sales
overall_sales = df['Sales'].sum()

# Calculate sales for each company
company_sales = df.groupby('Company')['Sales'].sum().reset_index()

# Calculate the number of months each company had sales
company_months = df.groupby('Company')['Month'].nunique().reset_index()

# Calculate the rate of sales (sales per month) for each company
company_sales['Sales_Per_Month'] = company_sales['Sales'] / company_months['Month']

# Find the company with the highest rate of sales
highest_sales_rate_company = company_sales.loc[company_sales['Sales_Per_Month'].idxmax()]

# Display analysis results
print("Simulated Market Data:")
print(df)
print("\nOverall Sales for All Companies: ", overall_sales)
print("\nSales for Each Company:")
print(company_sales)
print("\nCompany with Highest Rate of Sales:")
print(highest_sales_rate_company)
