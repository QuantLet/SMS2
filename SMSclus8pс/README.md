[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSclus8pc** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet : SMSclus8pc

Published in : 'Multivariate Statistics: Exercises and Solutions'

Description : 'Employs the centroid linkage using squared Euclidean distance 
matrices to perform a cluster analysis on an 8 points example'

Keywords : cluster-analysis, dendrogram, euclidean, distance, linkage

See also : 'MVAclususcrime, MVAdrugsim, SMSclus8p, SMSclus8pd, SMSclus8pd, 
SMSclus8pmst2, SMSclusbank, SMSclusbank2, SMSclusbank3, SMScluscomp, SMScluscrime,
SMScluscrimechi2, SMSclushealth'

Author : Awdesch Melzer
Author[Python]: 'Matthias Fengler, Liudmila Gorkun-Voevoda'

Submitted : Fri, August 22 2014 by Awdesch Melzer
Submitted[Python]: 'Wed, September 9 2020 by Liudmila Gorkun-Voevoda'
 
Example : 8 points example for centroid algorithm

```

![Picture1](SMSclus8pc.png)

![Picture2](SMSclus8pc_python.png)

### R Code
```r

# clear cache and close windows
graphics.off()
rm(list=ls(all=TRUE))

# install.packages("car")
library(car)

# define eight points
eight  = cbind(c(-3,-2,-2,-2,1,1,2,4),c(0,4,-1,-2,4,2,-4,-3))
eight  = eight[c(8,7,3,1,4,2,6,5),]
w      = hclust(dist(eight,method="euclidean")^2,method="centroid")
groups = cutree(w, k=2)
merg   = cbind(eight, as.matrix(groups))
merg   = merg[sort.list(merg[,3]),]
merg1  = merg[which(merg[,3]==1),1:2]
merg2  = merg[which(merg[,3]==2),1:2]
m1     = apply(merg1,2,mean)
m2     = apply(merg2,2,mean)


dev.new()
# plot eight points using centroid linkage
par(mfrow = c(1, 2))
plot(eight,type="n", xlab="price conciousness",ylab="brand loyalty",main="8 points - centroid linkage", xlim=c(-4,4))

dataEllipse(x = c(merg1[,1]), y = c(merg1[,2]), center.pch = 1, col = "red", 
            plot.points = F, add = T,levels = 0.7)
dataEllipse(x = merg2[,1], y = merg2[,2], center.pch = 1, col = "blue", 
            plot.points = F, add = T,levels = 0.7)

segments(m2[1],m2[2],eight[3,1],eight[3,2],lwd=2)
segments(m2[1],m2[2],eight[4,1],eight[4,2],lwd=2)
segments(m2[1],m2[2],eight[5,1],eight[5,2],lwd=2)
segments(m2[1],m2[2],eight[6,1],eight[6,2],lwd=2)
segments(m2[1],m2[2],eight[7,1],eight[7,2],lwd=2)
segments(m2[1],m2[2],eight[8,1],eight[8,2],lwd=2)

segments(m1[1],m1[2],eight[1,1],eight[1,2],lwd=2)
segments(m1[1],m1[2],eight[2,1],eight[2,2],lwd=2)

segments(m1[1],m1[2],m2[1],m2[2],lwd=2)
points(eight, pch=21, cex=2.6, bg="white")
text(eight,as.character(1:8),col="red3",cex=1)

plot(hclust(dist(eight,method="euclidean")^2,method="centroid"),ylab="squared Euclidean distance",sub="",xlab="",main="centroid linkage dendrogram") 


```

automatically created on 2020-09-11

### PYTHON Code
```python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from scipy.cluster import hierarchy


eight = np.array(([-3, -2, -2, -2, 1, 1, 2, 4], [0, 4, -1, -2, 4, 2, -4, -3])).T
eight = eight[[7,6,2,0,3,1,5,4], :]

d = np.zeros([8,8])

for i in range(0, 8):
    for j in range(0, 8):
        d[i, j] = np.linalg.norm(eight[i, :] - eight[j, :])

dd = (d**2)

ddd  = dd[1:, :-1][:, 0]
for i in range(1, 7):
    ddd = np.concatenate((ddd, dd[1:, :-1][i:, i]))

w = hierarchy.linkage(ddd, 'centroid')

groups = hierarchy.cut_tree(w, n_clusters = 2)

merg = pd.DataFrame(data = {"0": eight[:,0], "1": eight[:,1]})
merg["2"] = groups
merg1 = merg[merg["2"] == 0].iloc[:, :2]
merg2 = merg[merg["2"] == 1].iloc[:, :2]
m1 = np.mean(merg1)
m2 = np.mean(merg2)

covm = np.cov(merg1.iloc[:, 0], merg1.iloc[:, 1])
covm1 = np.cov(merg2.iloc[:, 0], merg2.iloc[:, 1])

eigva = np.sqrt(np.linalg.eig(covm)[0])
eigve = np.linalg.eig(covm)[1]
eigva1 = np.sqrt(np.linalg.eig(covm1)[0])
eigve1 = np.linalg.eig(covm1)[1]


fig = plt.figure(figsize = (15, 10))

ax = fig.add_subplot(1, 2, 1)
plt.xlim(-4.2, 4.2)
plt.ylim(-4.2, 4.2)
plt.title("8 points - centroid linkage", fontsize = 16)
plt.ylabel("brand loyalty")
plt.xlabel("price conciousness")

ax.scatter(np.mean(merg1.iloc[:, 0]), np.mean(merg1.iloc[:, 1]), facecolor = "w", edgecolor = "r", zorder = 0, s = 250)
ax.add_patch(Ellipse(xy = (np.mean(merg1.iloc[:, 0]), np.mean(merg1.iloc[:, 1])),
                     width = eigva[0]*3*1.15, height = eigva[1]*3*1.15,
                     angle = np.rad2deg(np.arccos(eigve[0, 0])), facecolor = "w", edgecolor = "r", zorder = 0))

ax.add_patch(Ellipse(xy = (np.mean(merg2.iloc[:, 0]), np.mean(merg2.iloc[:, 1])),
                     width = eigva1[0]*3*1.15, height = eigva1[1]*3*1.15,
                     angle = np.rad2deg(np.arccos(eigve1[0, 0])), facecolor = "w", edgecolor = "b", zorder = 0))
ax.scatter(np.mean(merg2.iloc[:, 0]), np.mean(merg2.iloc[:, 1]), facecolor = "w", edgecolor = "b", s = 250, zorder = 5)

for i in range(2, 8):
    plt.plot([m2[0], eight[i, 0]], [m2[1], eight[i, 1]], c = "black", zorder = 10)

plt.plot([m1[0], eight[0, 0]], [m1[1], eight[0, 1]], c = "black", zorder = 10)
plt.plot([m1[0], eight[1, 0]], [m1[1], eight[1, 1]], c = "black", zorder = 10)

plt.plot([m1[0], m2[0]], [m1[1], m2[1]], c = "black", zorder = 10)

plt.scatter(eight[:, 0], eight[:, 1], c = "w", edgecolors = "black", s = 500, zorder = 15)
for i in range(0, 8):
    plt.text(eight[i, 0]-0.1, eight[i, 1]-0.1, str(i), fontsize = 20, color = "r", zorder = 20)

fig.add_subplot(1, 2, 2)
h = hierarchy.dendrogram(w)
plt.title("Centroid linkage dendrogram", fontsize = 16)
plt.ylabel("Squared Euclidean Distance")

plt.show()


```

automatically created on 2020-09-11