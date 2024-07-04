import pandas as pd

df = pd.read_csv('supermarket_sales.csv')
df = df.dropna()
df['Date'] = pd.to_datetime(df['Date'])

numericalSummary = df.describe()
print(numericalSummary)

totalSales = df['Total'].sum()
print('Total Sales', totalSales)

df['MonthOfYear'] = df['Date'].dt.to_period('M')
averagePerMonth = df.groupby('MonthOfYear')['Total'].mean()
print('Average amount per month \n', averagePerMonth)

maxSales = df['Total'].max()
print('Max Sales', maxSales)

minSales = df['Total'].min()
print('Min Sales', minSales)

categoricalCount = df['Product line'].value_counts()
print('Categorical count \n', categoricalCount)

cityCount = df['City'].value_counts()
print('City count \n', cityCount)

df['Profit Margin'] = (df['gross income'] / df['Total']) * 100
print('Profit Margin \n', df['Profit Margin'])

monthSumSales = df.groupby('MonthOfYear')['Total'].sum()
salesGrowthRate = monthSumSales.pct_change().fillna(0) * 100
print('Sales growth rate \n', salesGrowthRate)

salesContributionCategory = df.groupby('Product line')['Total'].sum()
print('Sales Contribution Category \n ', salesContributionCategory)

salesContributionCity = df.groupby('City')['Total'].sum()
print('Sales Contribution City \n ', salesContributionCity)

topPerformingCategory = salesContributionCategory.sort_values(ascending=False)
print('Top Performing Category \n', topPerformingCategory)

topPerformingCity = salesContributionCity.sort_values(ascending=False)
print('Top Performing City \n', topPerformingCity)
