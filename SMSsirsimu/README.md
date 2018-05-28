[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSsirsimu** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMSsirsimu

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'generates a data set and applies the sliced inverse regression algorithm (SIR) for dimension reduction.'

Keywords: 'sliced inverse regression, sir, EDR-directions, effective dimension reduction directions, eigenvalue'

See also: 'SMScartdiag, SMScartsq, SMSdisfbank2, SMSeppbank, SMSsimpdbank, SMSsimpdsimu, SMSsir2cars, SMSsir2simu, SMSsircars, SMSsirsimu, SMSsircars, SMSsirsimu, SMSsiruscomp, SMSsvmbankrupt, SMSsvmorange, SMSsvmspiral'

Author: Awdesch Melzer, Zdenek Hlavka, Alena Babiakova

Example: 'Effective dimension reduction directions (EDR-directions) for a simulated data set and plots for the response versus the estimated EDR-directions, a three-dimensional plot for the first two directions and the response and plot for the eigenvalues and the cumulative sum.'

```

![Picture1](SMSsirsimu.png)

### R Code
```r

rm(list=ls(all=TRUE))
graphics.off()


# install and load packages
libraries = c("dr","MASS")
lapply(libraries, function(x) if (!(x %in% installed.packages())) {
    install.packages(x)})
lapply(libraries, library, quietly = TRUE, character.only = TRUE)

# set seed for pseudo random numbers
set.seed(0)

n     = 400 #number of observations

# vectors of normal random numbers
x1 = rnorm(n) 
x2 = rnorm(n)
x3 = rnorm(n)
x4 = rnorm(n)
x = cbind(x1,x2,x3,x4)

# error term
e     = rnorm(n)

b1    = c(1,3,0,0)
b2    = c(0,0,1,-1)
i     = c(1,2,3,4)
y     = ((x%*%b1)^2)+((x%*%b2)^4)+e
 
 EDR   = dr(y~x,method="sir")
 f     = EDR$evectors
 g     = EDR$evalues

#f1    = ((x%*%b1)^2)+((x%*%b2)^4)
#m1    = cbind((x%*%b1),y)
#m2    = cbind((x%*%b2),y)
#m1    = m1[order(m1[,2],decreasing=T),]
#m2    = m2[order(m2[,2],decreasing=T),]

sg    = sum(g)
g     = g/sg
psi   = cumsum(g)

ig    = cbind(i,g)

p11   = cbind(as.matrix(x)%*%f[,1],y)

p12   = cbind(as.matrix(x)%*%f[,2],y)

p21   = cbind(as.matrix(x)%*%f[,3],y)

par(mfrow=c(2,2))
plot(p11, type="n", xlab="1st projection", ylab="response")
points(p11,pch=19,cex=0.7,col="blue3")

plot(p12, type="n", xlab="2nd projection", ylab="response")
points(p12,pch=19,cex=0.7,col="blue3")

plot(p21, type="n", xlab="3rd projection", ylab="response")
points(p21,pch=19,cex=0.7,col="blue3")

plot(ig, type="n", xlab="k",ylab="",ylim=c(0,1))
title("SIR scree plot")
points(ig, pch="*",col="black",cex=1)
points(cbind(i,psi),pch=1,col="black",cex=1)

```

automatically created on 2018-05-28