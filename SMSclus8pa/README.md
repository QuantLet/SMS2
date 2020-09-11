[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSclus8pa** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet : SMSclus8pa
Published in : 'Multivariate Statistics: Exercises and Solutions'

Description : 'Employs the average linkage using squared Euclidean distance matrices 
to perform a cluster analysis on an 8 points example'

Keywords : cluster-analysis, dendrogram, linkage, euclidean, distance, plot 

See also : 'MVAclususcrime, MVAdrugsim, SMSclus8p, SMSclus8pd, SMSclus8pd, SMSclus8pmst2,
SMSclusbank, SMSclusbank2, SMSclusbank3, SMScluscomp, SMScluscrime, SMScluscrimechi2, SMSclushealth'

Author : Awdesch Melzer
Author[Python]: 'Matthias Fengler, Liudmila Gorkun-Voevoda'

Submitted : Fri, August 22 2014 by Awdesch Melzer
Submitted[Python]: 'Wed, September 9 2020 by Liudmila Gorkun-Voevoda'

Example : 8 points example for average linkage algorithm

```

![Picture1](SMSclus8pa.png)

![Picture2](SMSclus8pa_python.png)

### R Code
```r

# clear cache and close windows
graphics.off()
rm(list=ls(all=TRUE))

# define eight points
eight = cbind(c(-3,-2,-2,-2,1,1,2,4),c(0,4,-1,-2,4,2,-4,-3))
eight = eight[c(8,7,3,1,4,2,6,5),]
dev.new()
# plot eight points using average linkage
par(mfrow = c(1, 2))
plot(eight,type="n", xlab="price conciousness",ylab="brand loyalty",main="8 points", xlim=c(-4,4))

# agglomarate first two nearest points
segments(eight[5,1],eight[5,2 ],eight[3,1 ],eight[3,2],lwd=2,"black")
# add third point via average
segments(eight[3,1],eight[3,2 ],eight[4,1 ],eight[4,2],lwd=2,lty=2,col="darkgrey")
segments(eight[5,1],eight[5,2 ],eight[4,1 ],eight[4,2],lwd=2,lty=2,col="darkgrey")
# agglomerate second two nearest points
segments(eight[7,1],eight[7,2 ],eight[8,1 ],eight[8,2],lwd=2,"black")
# agglomarate third two nearest points
segments(eight[1,1],eight[1,2 ],eight[2,1 ],eight[2,2],lwd=2,"black")
# add point six to second subcluster via average
segments(eight[8,1],eight[8,2 ],eight[6,1 ],eight[6,2],lwd=2,lty=2,col="darkgrey")
segments(eight[7,1],eight[7,2 ],eight[6,1 ],eight[6,2],lwd=2,lty=2,col="darkgrey")

# compute subcluster between 345 and 678 via average
segments(eight[4,1],eight[4,2],eight[6,1],eight[6,2],lwd=2,lty=3,col="skyblue")
segments(eight[4,1],eight[4,2],eight[8,1],eight[8,2],lwd=2,lty=3,col="skyblue")
segments(eight[4,1],eight[4,2],eight[7,1],eight[7,2],lwd=2,lty=3,col="skyblue")
segments(eight[3,1],eight[3,2],eight[6,1],eight[6,2],lwd=2,lty=3,col="skyblue")
segments(eight[3,1],eight[3,2],eight[7,1],eight[7,2],lwd=2,lty=3,col="skyblue")
segments(eight[3,1],eight[3,2],eight[8,1],eight[8,2],lwd=2,lty=3,col="skyblue")
segments(eight[5,1],eight[5,2],eight[6,1],eight[6,2],lwd=2,lty=3,col="skyblue")
segments(eight[5,1],eight[5,2],eight[7,1],eight[7,2],lwd=2,lty=3,col="skyblue")
segments(eight[5,1],eight[5,2],eight[8,1],eight[8,2],lwd=2,lty=3,col="skyblue")

# compute in case of merging of two last clusters:
segments(eight[2,1],eight[2,2 ],eight[6,1 ],eight[6,2],lwd=2,lty=3,col="lightgreen")
segments(eight[2,1],eight[2,2 ],eight[4,1 ],eight[4,2],lwd=2,lty=3,col="lightgreen")
segments(eight[2,1],eight[2,2 ],eight[5,1 ],eight[5,2],lwd=2,lty=3,col="lightgreen")
segments(eight[2,1],eight[2,2 ],eight[7,1 ],eight[7,2],lwd=2,lty=3,col="lightgreen")
segments(eight[2,1],eight[2,2 ],eight[8,1 ],eight[8,2],lwd=2,lty=3,col="lightgreen")
segments(eight[2,1],eight[2,2 ],eight[3,1 ],eight[3,2],lwd=2,lty=3,col="lightgreen")
segments(eight[1,1],eight[1,2 ],eight[6,1 ],eight[6,2],lwd=2,lty=3,col="lightgreen")
segments(eight[1,1],eight[1,2 ],eight[4,1 ],eight[4,2],lwd=2,lty=3,col="lightgreen")
segments(eight[1,1],eight[1,2 ],eight[5,1 ],eight[5,2],lwd=2,lty=3,col="lightgreen")
segments(eight[1,1],eight[1,2 ],eight[7,1 ],eight[7,2],lwd=2,lty=3,col="lightgreen")
segments(eight[1,1],eight[1,2 ],eight[8,1 ],eight[8,2],lwd=2,lty=3,col="lightgreen")
segments(eight[1,1],eight[1,2 ],eight[3,1 ],eight[3,2],lwd=2,lty=3,col="lightgreen")

points(eight, pch=21, cex=2.6, bg="white")
text(eight,as.character(1:8),col="red3", cex=1)

plot(hclust(dist(eight,method="euclidean")^2,method="average"),ylab="squared Euclidean distance",sub="",xlab="",main="average linkage dendrogram") 


```

automatically created on 2020-09-11

### PYTHON Code
```python

import numpy as np
import matplotlib.pyplot as plt
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

Z = hierarchy.linkage(ddd, 'average')


fig = plt.figure(figsize = (15, 10))

fig.add_subplot(1, 2, 1)
plt.xlim(-4.2, 4.2)
plt.ylim(-4.2, 4.2)
plt.title("8 points", fontsize = 16)
plt.ylabel("brand loyalty")
plt.xlabel("price conciousness")

# agglomarate first two nearest points
plt.plot([eight[4, 0], eight[2, 0]], [eight[4, 1], eight[2, 1]], c = "black", zorder = 0)
# add third point via average
plt.plot([eight[2, 0], eight[3, 0]], [eight[2, 1], eight[3, 1]], c = "grey", zorder = 0, linestyle = "--")
plt.plot([eight[4, 0], eight[3, 0]], [eight[4, 1], eight[3, 1]], c = "grey", zorder = 0, linestyle = "--")
# agglomerate second two nearest points
plt.plot([eight[6, 0], eight[7, 0]], [eight[6, 1], eight[7, 1]], c = "black", zorder = 0)
# agglomarate third two nearest points
plt.plot([eight[0, 0], eight[1, 0]], [eight[0, 1], eight[1, 1]], c = "black", zorder = 0)
# add point six to second subcluster via average
plt.plot([eight[7, 0], eight[5, 0]], [eight[7, 1], eight[5, 1]], c = "grey", zorder = 0, linestyle = "--")
plt.plot([eight[6, 0], eight[5, 0]], [eight[6, 1], eight[5, 1]], c = "grey", zorder = 0, linestyle = "--")

# compute subcluster between 345 and 678 via average
for i in range(2, 5):
    for j in range(5, 8):
        plt.plot([eight[i, 0], eight[j, 0]], [eight[i, 1], eight[j, 1]], 
                 c = "lightskyblue", zorder = 0, linestyle = "dotted")


# compute in case of merging of two last clusters:
for i in [0, 1]:
    for j in range(2, 8):
        plt.plot([eight[i, 0], eight[j, 0]], [eight[i, 1], eight[j, 1]], 
                 c = "lightgreen", zorder = 0, linestyle = "dotted")

plt.scatter(eight[:, 0], eight[:, 1], c = "w", edgecolors = "black", s = 500)
for i in range(0, 8):
    plt.text(eight[i, 0]-0.1, eight[i, 1]-0.1, str(i), fontsize = 20, color = "r")

fig.add_subplot(1, 2, 2)
h = hierarchy.dendrogram(Z)
plt.title("Average linkage dendrogram", fontsize = 16)
plt.ylabel("Squared Euclidean Distance")

plt.show()


```

automatically created on 2020-09-11