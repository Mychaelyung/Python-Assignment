# Data Loading, Analysis & Visualization
# ==========================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================
# Task 1: Load and Explore the Dataset
# ==========================
try:
    # Load dataset from sklearn (Iris dataset)
    from sklearn.datasets import load_iris
    iris = load_iris(as_frame=True)
    df = iris.frame

    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ File not found. Please check the file path.")
except Exception as e:
    print("⚠️ An error occurred:", e)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nDataset info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Clean dataset (if missing values existed, fill them with mean)
df = df.fillna(df.mean(numeric_only=True))

# ==========================
# Task 2: Basic Data Analysis
# ==========================
print("\nBasic Statistics:")
print(df.describe())

# Group by species and calculate mean of numerical columns
grouped = df.groupby("target").mean()
print("\nAverage values by Species (target):")
print(grouped)

# Interesting finding (example)
print("\nObservation: Iris-virginica generally has the largest petal length and width.")

# ==========================
# Task 3: Data Visualization
# ==========================
sns.set(style="whitegrid")  # better style

# 1. Line chart (trend of sepal length for first 30 samples)
plt.figure(figsize=(8,5))
plt.plot(df.index[:30], df['sepal length (cm)'][:30], marker="o")
plt.title("Sepal Length Trend (first 30 samples)")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(8,5))
sns.barplot(x="target", y="petal length (cm)", data=df, estimator="mean")
plt.title("Average Petal Length per Species")
plt.xlabel("Species (0=setosa, 1=versicolor, 2=virginica)")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", palette="Set1", data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
