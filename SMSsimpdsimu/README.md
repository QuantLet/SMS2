[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSsimpdsimu** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMSsimpdsimu

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'Calculates simplicial depth of simulated data set with n=10. The red star represents the deepest point, the blue triangle the coordinatewise median. The numbers represent the depth of each observation.'

Keywords: 'simplicial depth, convex hull, median'

See also: 'SMScartdiag, SMScartsq, SMSdisfbank2, SMSeppbank, SMSsimpdbank, SMSsimpdsimu, SMSsir2cars, SMSsir2simu, SMSsircars, SMSsirsimu, SMSsircars, SMSsirsimu, SMSsiruscomp, SMSsvmbankrupt, SMSsvmorange, SMSsvmspiral'

Author: Awdesch Melzer, Zdenek Hlavka

Example: 'Simplicial depth for a sample of the Swiss bank notes data'
```

![Picture1](SMSsimpdsimu_r.png)

### R Code
```r

rm(list=ls(all=TRUE))
graphics.off()

# install and load packages
libraries = c("depth","MASS")
lapply(libraries, function(x) if (!(x %in% installed.packages())) {
    install.packages(x)})
lapply(libraries, library, quietly = TRUE, character.only = TRUE)

# simulate data
set.seed(2007)
n     = 10
a     = runif(n)*2*pi
x     = cbind(cos(a),sin(a))
x     = x + 0.1*mvrnorm(n,c(0,0),Sigma=matrix(c(1,0,0,1),2,2))
x     = rbind(x,c(0.4,0.5))

# estimate the location by simdep
m     = med(x,method="Liu")
mm    = m$median #the two-dimensional median

med12 = apply(x,2,median)

dep   = 165*apply(x,1,depth,x,"Liu")
par(c(1,1),cex=1)

plot(x, type="n",xlab=expression(x[1]),ylab=expression(x[2]),main="simplicial depth",xlim=c(-1.2,1.2),ylim=c(-1.2,1.2),lwd=3)
#median is the big red star
points(mm[1],mm[2],col="red",pch=8,cex=4,lwd=2)
points(med12[1],med12[2],col="blue",pch=2,cex=3,lwd=2)
text(x[,1],x[,2],round(dep,0),col="blue3",cex=1.2)
```

automatically created on 2018-05-28