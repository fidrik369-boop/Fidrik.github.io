import pandas as pd
import matplotlib.pyplot as plt

data = {
    'A': [10, 15, 10, 20, 25, 30],
    'B': [5, 10, 15, 10, 20, 25]
}

df = pd.DataFrame(data)

df.iloc[:5].plot.bar(title="Bar Plot")
plt.show()

df['A'].plot.hist(title="Histogram of A")
plt.show()

df.plot.line(title="Line Plot")
plt.show()

df.plot.scatter(x='A', y='B', title="Scatter Plot: A vs B")
plt.show()
