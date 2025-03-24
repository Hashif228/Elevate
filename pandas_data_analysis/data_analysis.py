import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv" 
df = pd.read_csv(file_path)  
print(df.describe())
print(df.head(3))

df = df.dropna() 
df = df.select_dtypes(include=['number']) 

print("\nDescriptive Statistics:")
print(df.describe()) 

plt.figure(figsize=(12, 6))

sns.histplot(df, kde=True)
plt.title("Histogram of Numeric Data")
plt.show()

if 'category_column' in df.columns:  
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x='category_column')
    plt.title("Category Distribution")
    plt.xticks(rotation=45)
    plt.show()
with open("summary_report.txt", "w") as f:
    f.write("Summary Report\n\n")

    mean = df.mean().rename("Mean")
    median = df.median().rename("Median")
    std = df.std().rename("Std")

    f.write("Mean:\n")
    f.write(mean.to_string() + "\n\n")

    f.write("Median:\n")
    f.write(median.to_string() + "\n\n")

    f.write("Standard Deviation:\n")
    f.write(std.to_string() + "\n\n")

print("\nSummary report saved as 'summary_report.txt'.")
