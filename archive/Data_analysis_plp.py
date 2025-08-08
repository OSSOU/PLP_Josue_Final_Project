# Import libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 1. Load the CSV file
#file_path = "airlines_flights_data.csv"  # <-- change this to your file name
df = pd.read_csv("airlines_flights_data.csv")

# 2. Basic exploration
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())

# 3. Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# 4. Check column names
print("\nColumn names:")
print(df.columns)


sns.set(style="whitegrid")

# 1️⃣ Line Chart – Average price vs. days left (trend-like view)
avg_price_by_days = df.groupby("days_left")["price"].mean().reset_index()
plt.figure(figsize=(8, 5))
plt.plot(avg_price_by_days["days_left"], avg_price_by_days["price"], marker='o', color='b', label='Avg Price')
plt.title("Average Ticket Price vs Days Left")
plt.xlabel("Days Left Before Departure")
plt.ylabel("Average Price")
plt.legend()
plt.tight_layout()
plt.show()

# 2️⃣ Bar Chart – Average price per airline
avg_price_per_airline = df.groupby("airline")["price"].mean().sort_values()
plt.figure(figsize=(8, 5))
sns.barplot(x=avg_price_per_airline.index, y=avg_price_per_airline.values, palette="viridis")
plt.title("Average Ticket Price per Airline")
plt.xlabel("Airline")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3️⃣ Histogram – Distribution of flight prices
plt.figure(figsize=(8, 5))
plt.hist(df['price'], bins=20, color='orange', edgecolor='black')
plt.title("Distribution of Ticket Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4️⃣ Scatter Plot – Duration vs. Price (colored by class)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="duration", y="price", hue="class", palette="Set2")
plt.title("Flight Duration vs Price")
plt.xlabel("Duration (hours)")
plt.ylabel("Price")
plt.legend(title="Class")
plt.tight_layout()
plt.show()

# 5. Example: Value counts for a categorical column
# Replace 'column_name' with your column
# print(df['column_name'].value_counts())

# 6. Visualization (Optional)
# Replace 'numeric_column' with your column name
# Histogram
# df['numeric_column'].hist()
# plt.title('Distribution of numeric_column')
# plt.show()

# Scatter plot example
# Replace with relevant numeric columns
# df.plot(kind='scatter', x='column_x', y='column_y')
# plt.show()
