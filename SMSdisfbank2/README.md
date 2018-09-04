[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSdisfbank2** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMSdisfbank2

Published in: 'Multivariate Statistics: Exercises and Solutions'

Description: "Reads the Swiss bank notes data and spheres it to run Fisher's LDA and PC projection on it."

Keywords: "sphere, Fisher's LDA, PC projection"

See also: 'SMScartdiag, SMScartsq, SMSdisfbank2, SMSeppbank, SMSsimpdbank, SMSsimpdsimu, SMSsir2cars, SMSsir2simu, SMSsircars, SMSsirsimu, SMSsircars, SMSsirsimu, SMSsiruscomp, SMSsvmbankrupt, SMSsvmorange, SMSsvmspiral'

Author: Zdenek Hlavka, Awdesch Melzer

Example: "Fisher's LDA and PC projection plot"
```

![Picture1](SMSdisfbank2_r.png)

### R Code
```r

# clear variables and close windows
rm(list=ls(all=TRUE))
graphics.off()

# install and load packages
libraries = c("stats","MASS","KernSmooth")
lapply(libraries, function(x) if (!(x %in% installed.packages())) {
    install.packages(x)})
lapply(libraries, library, quietly = TRUE, character.only = TRUE)

# setwd("C:/...") # set working directory
load("bank2.rda")
truth     = factor(rep(c("Genuine","Forged"),each=100))

# centering
x         = t(t(as.matrix(bank2))-sapply(bank2,mean))
# sphering
t         = eigen(var(x))
v12       = t$vectors%*%diag(1/sqrt(t$values))%*%t(t$vectors)
x         = x%*%v12
fisher    = as.matrix(x)%*%(lda(truth~x)$scaling)
fisher    = (fisher-mean(fisher))/sd(fisher)
principal = prcomp(x,scale.=TRUE)$x[,1]
est.p     = bkde(principal, bandwidth=0.25)
est.f     = bkde(fisher, bandwidth=0.25)
dum       = rbind(c(min(c(est.p$x,est.f$x)),-0.2),c(max(c(est.p$x,est.f$x)),max(c(est.p$y,est.f$y))))

plot(dum,type="n",main="Fisher's LDA and PC projection",xlab="",ylab="")
lines(est.f,col="red", lwd=2)
lines(est.p,col="blue", lty=2, lwd=2)
t         = (runif(200)*0.09)-0.095
points(t~fisher,col="red",pch=c(rep(1,100),rep(2,100)),cex=1)
t         = (runif(200)*0.09)-0.195
points(t~principal,col="blue",pch=c(rep(1,100),rep(2,100)),cex=1)

```

automatically created on 2018-09-04