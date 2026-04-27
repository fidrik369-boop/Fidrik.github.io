from sklearn.cluster import KMeans

from sklearn. datasets import load iris

import matplotlib.pyplot as plt

data = load iris()

X = data.data

inertia = []

K range = range (1, 11)

for k in K range:

kmeans = KMeans (n clusters=k, random_state=42) kmeans.fit (X) inertia.append(kmeans.inertia_)

#. Plotting the Elbow Graph

plt.plot (K_range, inertia, marker='o') plt.title('Elbow Method for Optimal K') plt.xlabel('Number of Clusters (K)') plt.ylabel('Inertia (Sum of Euclidean Distances)') plt.show()

Output: (A line graph appears showing a curve decreasing. The "Elbow" is u K=3 for Iris data).
