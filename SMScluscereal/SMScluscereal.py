#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:31:57 2024

@author: raulbag
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

colnames = ['Name','Manufacturer','Type' ,'Calories','Protein','Fat','Sodium','Dietary Fiber','Complex Carbohydrates','Sugars','Disaply Shelf','Potassium','Vitamin and Minerals','Weight','Cups']
UScereal = pd.read_csv('us_cereal_data.csv', sep="\s+", names=colnames, header=None)

cereal = UScereal[['Calories', 'Protein', 'Fat', 'Sugars']].values

cereal_names = ['C' + str(i) for i in range(len(UScereal))]

scaler = StandardScaler()
sc_cereal = scaler.fit_transform(cereal)

D = pdist(sc_cereal, 'euclidean')
hc = linkage(D, method='ward')

plt.figure(figsize=(10, 7))
dendrogram(hc, labels=cereal_names)
plt.xlabel('')
plt.ylabel('Euclidean distance')
plt.title('Ward dendrogram for US cereal data')
plt.savefig('SMScluscereal_ward_py.png', dpi=600, transparent=True)
plt.show()

pr = PCA(n_components=2)
prx = pr.fit_transform(sc_cereal)
prx *= np.sign(prx[0, :])

cut = fcluster(hc, t=15, criterion='distance')
merg = np.column_stack((prx, cut))
merg = merg[np.argsort(merg[:, 2]), :]

merg1 = merg[:17, :2]
merg2 = merg[17:41, :2]
merg3 = merg[41:, :2]

plt.figure()
plt.scatter(prx[:, 0], prx[:, 1], c=cut, cmap='viridis', edgecolor='k')
plt.xlabel('First PC')
plt.ylabel('Second PC')
plt.title('65 US cereals, cut height 15')
for i, txt in enumerate(cereal_names):
    if i < 17:
        plt.text(merg1[i, 0], merg1[i, 1], txt, color='red', fontsize=12)
    elif i < 41:
        plt.text(merg2[i - 17, 0], merg2[i - 17, 1], txt, color='blue', fontsize=12)
    else:
        plt.text(merg3[i - 41, 0], merg3[i - 41, 1], txt, color='black', fontsize=12)
plt.savefig('SMScluscereal_PCA_py.png', dpi=600, transparent=True)
plt.show()
