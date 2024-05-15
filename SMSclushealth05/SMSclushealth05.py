import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.decomposition import PCA

# Read data
ushealth05 = pd.read_csv("ushealth05.csv")  # Adjust the path as necessary
# Order data based on the 20th column
ush = ushealth05.sort_values(by=ushealth05.columns[19])

# Define region
ushreg = ush.iloc[:, 19].values
ushreg[ushreg == 'Northeaast'] = 1
ushreg[ushreg == 'Midwest'] = 2
ushreg[ushreg == 'South'] = 3
ushreg[ushreg == 'West'] = 4

# Create labels
lab = ush.iloc[:, 21].astype(str)
ush.index = lab

# Calculate Euclidean distance matrix
D = pdist(ush.iloc[:, 2:12], metric='euclidean')

# Perform hierarchical clustering using Ward's method
hc = linkage(D, method='ward')

# Create clusters
cl = fcluster(hc, 4, criterion='maxclust')

# Plot dendrogram
plt.figure(figsize=(10, 8))
dendrogram(hc, labels=lab.values, orientation='left')
plt.title("Ward dendrogram for US health")
plt.xlabel("Euclidean distance")
plt.savefig('SMSclushealth05_ward_py.png', dpi=600, transparent=True)
plt.show()

# Perform PCA
pr = PCA(n_components=2)
prx = pr.fit_transform(ush.iloc[:, 2:12])
prx *= np.sign(prx[0, :])  # Align signs for consistent orientation

# Update cluster colors based on cluster ids
cl2 = cl.copy()
cl2[cl == 1] = 2
cl2[cl == 4] = 1
cl2[cl == 2] = 3
cl2[cl == 3] = 4

# Plot PCA results
plt.figure(figsize=(10, 8))
plt.scatter(prx[:, 0], prx[:, 1], c=cl2, cmap='viridis', s=50)
for i, txt in enumerate(lab):
    plt.text(prx[i, 0], prx[i, 1], txt, color='black')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('US health PCA Plot')
plt.savefig('SMSclushealth05_PCA_py.png', dpi=600, transparent=True)
plt.show()

# Calculate mean for each cluster in the principal components
mu_table = pd.DataFrame({
    'Cluster 1': ush[cl == 1].iloc[:, 2:12].mean(),
    'Cluster 2': ush[cl == 2].iloc[:, 2:12].mean(),
    'Cluster 3': ush[cl == 3].iloc[:, 2:12].mean(),
    'Cluster 4': ush[cl == 4].iloc[:, 2:12].mean()
})

print(mu_table)
