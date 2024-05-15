#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:09:41 2024

@author: raulbag
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Seed for reproducibility
np.random.seed(1)

# Load data
ushealth = pd.read_csv("ushealth05.csv")

# K-means algorithm on selected columns
kmeans = KMeans(n_clusters=4, algorithm='full')  # 'full' corresponds to 'Lloyd' algorithm
clusters = kmeans.fit_predict(ushealth.iloc[:, 2:12])

# PCA
pr = PCA(n_components=2)
prx = pr.fit_transform(ushealth.iloc[:, 2:12])
prx *= np.sign(prx[0, :])  # Align signs for consistent orientation

# Plotting
plt.figure(figsize=(10, 8))
plt.title("US health data")
lab = ushealth.iloc[:, 21].astype(str)

# Adjusting colors based on cluster numbers
colors = np.choose(clusters, [1, 3, 2, 0])  # Reassign colors; matplotlib default colors are 0, 1, 2, 3

# Plotting each point
plt.figure(figsize=(10, 8))
plt.scatter(prx[:, 0], prx[:, 1], c=colors, cmap='viridis', s=50)
for i, txt in enumerate(lab):
    plt.text(prx[i, 0], prx[i, 1], txt, color='black')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('US health PCA Plot')
plt.savefig('SMSclushealth05_PCA_kmeans_py.png', dpi=600, transparent=True)
plt.show()