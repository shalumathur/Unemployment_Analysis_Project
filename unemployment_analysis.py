# Task 2: Unemployment Analysis using Python
# Created by: Shalu Mathur

# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
data = pd.read_csv("unemployment_sample.csv")
print("✅ Dataset Loaded Successfully!")
print(data.head())

# Step 3: Rename long column names (optional but clean)
data.rename(columns={
    'Region': 'State',
    'Date': 'Month',
    'Estimated Unemployment Rate (%)': 'Unemployment Rate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Labour Participation Rate'
}, inplace=True)

# Step 4: Bar plot - State-wise Unemployment Rate
plt.figure(figsize=(8, 5))
sns.barplot(x='Unemployment Rate', y='State', data=data, palette='Blues_r')
plt.title('Unemployment Rate by State')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('State')
plt.tight_layout()
plt.show()

# Step 5: Line plot - Unemployment Trend Over Time
plt.figure(figsize=(8, 5))
sns.lineplot(x='Month', y='Unemployment Rate', data=data, marker='o')
plt.title('Unemployment Trend Over Time')
plt.xlabel('Month')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
