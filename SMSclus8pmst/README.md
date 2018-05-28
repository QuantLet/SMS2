[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSclus8pmst** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet : SMSclus8pmst

Published in : 'Multivariate Statistics: Exercises and Solutions'

Description : Plots an 8 points example for minimum spanning trees (MST)

Keywords : cluster-analysis, plot, graphical representation, distance, euclidean
See also : 'MVAclususcrime, MVAdrugsim, SMSclus8p, SMSclus8pd, SMSclus8pd, 
SMSclus8pmst2, SMSclusbank, SMSclusbank2, SMSclusbank3, SMScluscomp, SMScluscrime, 
SMScluscrimechi2, SMSclushealth'

Author : Elisabeth Bommes, Awdesch Melzer

Submitted : Fri, August 22 2014 by Awdesch Melzer

Example : 8 points example for minimum spanning tree algorithm
```

![Picture1](SMSclus8pmst.png)

### R Code
```r

# clear cache and close windows
graphics.off()
rm(list=ls(all=TRUE))

# define eight points, compute distance matrix
eight        = cbind(c(-3,-2,-2,-2,1,1,2,4),c(0,4,-1,-2,4,2,-4,-3))
eight        = eight[c(8,7,3,1,4,2,6,5),]
dist_eight   = (as.matrix(dist(eight, method = "euclidian")))^2

dev.new()
# plot eight points using average linkage
par(mfrow = c(1, 1),cex=1)

plot(eight, pch=16, xlab="price conciousness",ylab="brand loyalty",main="8 points",
     xlim=c(-4.1,4.1),ylim=c(-4.1,4.1))

# Plot Lines
for (i in 1:8){
  for (j in 1:8){
    segments(eight[i,1],eight[i,2 ],eight[j,1 ],eight[j,2],lwd=2,"black")
  }
}

# Plot Distances
for (i in 1:8){
  for (j in 1:8){
    if (i!=j){
      points((eight[i,1]+eight[j,1])/2, (eight[i,2]+eight[j,2])/2, pch=22, cex=3, bg="white")
      text((eight[i,1]+eight[j,1])/2, (eight[i,2]+eight[j,2])/2 ,
           dist_eight[i,j],col="red3", cex = 0.8)     
    }
  }
}

# Plot Nodes
points(eight, pch=21, cex=3, bg="white")
text(eight[,1],eight[,2],as.character(1:8),col="blue3",cex=1)
```

automatically created on 2018-05-28