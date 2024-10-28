import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = "D:\\smoking_data_500.csv"
df_smoking = pd.read_csv(file_path)

# Dataset Overview
print("Dataset Overview:")
print(df_smoking.head())

# Using NumPy for data manipulation
smoker_status = df_smoking['currentSmoker'].values
cigs_per_day = df_smoking['cigsPerDay'].values
totChol = df_smoking['totChol'].values
sysBP = df_smoking['sysBP'].values
diabetes = df_smoking['diabetes'].values

# Calculate statistics
mean_cigs = np.mean(cigs_per_day)
median_cigs = np.median(cigs_per_day)
std_cigs = np.std(cigs_per_day)

mean_chol = np.mean(totChol)
median_chol = np.median(totChol)
std_chol = np.std(totChol)

print(f"Mean Cigarettes Per Day: {mean_cigs}, Median: {median_cigs}, Standard Deviation: {std_cigs}")
print(f"Mean Cholesterol: {mean_chol}, Median: {median_chol}, Standard Deviation: {std_chol}")

#--------HISTOGRAM-------------
plt.figure(figsize=(10, 5))

# Smoking Status Distribution
plt.subplot(1, 2, 1)
plt.bar(
    ['Non-Smoker', 'Smoker'],
    df_smoking['currentSmoker'].value_counts().values,
    color=['blue', 'orange'],
    edgecolor='black'
)
plt.xlabel('Smoking Status')
plt.ylabel('Frequency')
plt.title('Smoking Status Distribution')

# Cigarettes Per Day Distribution for Smokers
plt.subplot(1, 2, 2)
plt.hist(
    df_smoking[df_smoking['currentSmoker'] == 1]['cigsPerDay'],
    bins=10,
    color='brown',
    alpha=0.7,
    edgecolor='black'
)
plt.xlabel('Cigarettes per Day')
plt.ylabel('Frequency')
plt.title('Cigarettes per Day (Smokers Only)')
plt.tight_layout()
plt.show()

#------SCATTER PLOT---------
plt.figure(figsize=(10, 5))

# Smoking Status vs. Systolic Blood Pressure
plt.subplot(1, 3, 1)
plt.scatter(
    df_smoking['currentSmoker'],
    df_smoking['sysBP'],
    color='purple',
    alpha=0.7,
    edgecolors='black'
)
plt.xlabel('Smoking Status (0=Non-Smoker, 1=Smoker)')
plt.ylabel('Systolic Blood Pressure')
plt.title('Smoking Status vs Systolic BP')

# Cigarettes per Day vs. Cholesterol
plt.subplot(1, 3, 2)
plt.scatter(
    df_smoking['cigsPerDay'],
    df_smoking['totChol'],
    color='green',
    alpha=0.7,
    edgecolors='black'
)
plt.xlabel('Cigarettes per Day')
plt.ylabel('Total Cholesterol')
plt.title('Cigarettes per Day vs Cholesterol')

# Cigarettes per Day vs. Diabetes Presence
plt.subplot(1, 3, 3)
plt.scatter(
    df_smoking['cigsPerDay'],
    df_smoking['diabetes'],
    color='red',
    alpha=0.7,
    edgecolors='black'
)
plt.xlabel('Cigarettes per Day')
plt.ylabel('Diabetes (0=No, 1=Yes)')
plt.title('Cigarettes per Day vs Diabetes')

plt.tight_layout()
plt.show()