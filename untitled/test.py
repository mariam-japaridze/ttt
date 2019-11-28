import random

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

data = [
    [185, 72],
    [170, 56],
    [168, 60],
    [179, 68],
    [182, 72],
    [188, 77],
]

for i in range(200):
    data.append([random.randint(0, 200), random.randint(0, 200)])

X = np.array(data)

plt.scatter(X[:, 0], X[:, 1], label='True Position')

kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

print(kmeans.cluster_centers_)
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')
plt.show()
