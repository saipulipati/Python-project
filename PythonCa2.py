import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv(r"/Users/ayyappa/Downloads/pythonCA.csv")

print(df.head())
print("Missing values:\n",df.isnull().sum())

correlation_matrix = df.corr(numeric_only = True)
sns.heatmap(correlation_matrix, annot=True, cmap="Blues", fmt=".3f", linewidths=0.8)
plt.title("HeatMap")
plt.show()



#grouped = df.groupby(['District', 'Commodity'])['Max_x0020_Price'].mean().reset_index()
top_districts = df['District'].value_counts().head(15).index.tolist()
filtered_df = df[df['District'].isin(top_districts)]

plt.figure(figsize=(8,8))
sns.boxplot(x=filtered_df['District'], y=filtered_df['Max_x0020_Price'], palette='viridis')
plt.title('Max Price Distribution of Commodities in Top 15 Districts')
plt.xlabel('District')
plt.ylabel('Max Price')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.show()

sns.histplot(df["Modal_x0020_Price"].dropna(), bins=30, kde=True, color ="coral", edgecolor="green")
plt.title("Modal Price (seaborn)")
plt.xlabel("Modal_x0020_Price")
plt.ylabel("Commodity")
plt.xscale("log")
plt.yscale("log")
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(df['Modal_x0020_Price'].head(20), marker='*', linestyle='-', color='blue')
plt.title('Line Chart')
plt.xlabel('Commodity')
plt.ylabel('Modal_x0020_Price')
plt.show()

#Pie chart for commodity and districts
top_districts = df['District'].value_counts().head(5).index
filtered_df = df[df['District'].isin(top_districts)]
district_name = top_districts[0] 
district_data = filtered_df[filtered_df['District'] == district_name]
commodity_counts = district_data['Commodity'].value_counts()
top_commodities = commodity_counts.head(20)

plt.figure(figsize=(7, 7))
plt.pie(top_commodities, labels=top_commodities.index, autopct='%1.1f%%', startangle=140)
plt.title(f'Commodity Proportion in {district_name}')
plt.axis('equal')
plt.show()


# Plot using seaborn (barplot )
avg_prices = df.groupby(['District', 'Commodity'])['Modal_x0020_Price'].mean().reset_index()
top_districts = avg_prices['District'].unique()[:5]  # for example, first 5
filtered_prices = avg_prices[avg_prices['District'].isin(top_districts)]
top_commodities = filtered_prices.groupby('Commodity')['Modal_x0020_Price'].mean().nlargest(18).index
filtered_prices_top_commodities = filtered_prices[filtered_prices['Commodity'].isin(top_commodities)]

sns.barplot(data=filtered_prices_top_commodities,x="Commodity",y="Modal_x0020_Price",
            hue='District',legend=False)
plt.title('Average Commodity Prices Across Districts')
plt.ylabel('Average Modal Price')
plt.xlabel('Commodity')
plt.xticks(rotation=30)
plt.show()

#########
price_comparison = df.groupby(['District', 'Commodity'])[['Min_x0020_Price', 'Max_x0020_Price', 'Modal_x0020_Price']].mean().reset_index()

top_commodities = price_comparison['Commodity'].value_counts().head(15).index.tolist()

filtered_price_comparison = price_comparison[price_comparison['Commodity'].isin(top_commodities)]

price_comparison_melted = filtered_price_comparison.melt(id_vars=['District', 'Commodity'], 
                                                         value_vars=['Min_x0020_Price', 'Max_x0020_Price', 'Modal_x0020_Price'], 
                                                         var_name='Price_Type', 
                                                         value_name='Price')

sns.scatterplot(data=price_comparison_melted, x='Commodity', y='Price', hue='Price_Type', style='Price_Type', s=100)
plt.title('Price Comparison for Top 15 Commodities')
plt.xlabel('Commodity')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.legend(title='Price Type')
plt.tight_layout()
plt.show()
