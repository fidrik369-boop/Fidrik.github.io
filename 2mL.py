import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    'A': [10, 15, 10, 20, 25, 30, 25],
    'B': [5, 10, 15, 10, 20, 25, 30]
}

# Create DataFrame
df = pd.DataFrame(data)

# i. Bar Plot
df.iloc[:5].plot.bar(title="Bar Plot")
plt.show()

# ii. Histogram
df['A'].plot.hist(title="Histogram of A")
plt.show()

# iii. Line Plot
df.plot.line(title="Line Plot")
plt.show()

# iv. Scatter Plot
df.plot.scatter(x='A', y='B', title="Scatter Plot: A vs B")
plt.show()
