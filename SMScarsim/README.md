[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMScarsim** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet : SMScarsim

Published in : 'Multivariate Statistics: Exercises and Solutions'

Description : 'computes the Jaccard, simple matching and Tanimoto proximity coefficients 
for binary car data'

Keywords : cluster-analysis, distance, proximity 

Keywords[new] : Jaccard proximity coefficient, Tanimoto proximity coefficient, simple matching coefficient

See also : 'MVAclus8p, MVAclusbank, MVAclusbh, MVAclusfood, MVAclususcrime, MVAdrugsim,
SMSclus8p, SMSclus8pd, SMSclus8pmst2, SMSclusbank, SMSclusbank2, SMSclusbank3, 
SMScluscomp, SMScluscrime, SMScluscrimechi2, SMSclushealth'

Author : Awdesch Melzer

Submitted : Sun, September 07 2014 by Awdesch Melzer

Usage : please install "simba" package

Datafile : carmean2.dat

Input : 'Matrix enclosing car marks: Economy, Service, Non depreciation of value, Price, Mark 1 for very cheap cars, Design, Sporty car, Safety, Easy handling'

Output : 'Jaccard, simple matching and Tanimoto proximity coefficients'

Example : 'Result: y 

[,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8] 
[1,] 0 1 1 0 1 1 0 0 
[2,] 1 0 0 1 0 0 1 1 
[3,] 0 0 1 0 1 0 1 0 

sim(y,method="jaccard") # jaccard 
1 2 
2 0.0000000 
3 0.4000000 0.1666667 

sim(y,method="simplematching") # simple matching 
1 2 
2 0.000 
3 0.625 0.375 

sim(y,method="roger") # tanimoto 
1 2 
2 0.0000000 
3 0.4545455 0.2307692'
```

### R Code
```r

# clear variables and close windows
rm(list=ls(all=TRUE))
graphics.off()

# install packages
# install.packages("simba")
library(simba)

# setwd("C:/...")                          # please change working directory
x     = read.table("carmean2.dat") # load data
x     = as.matrix(x[,2:9])         # retrieve Renault, Rover, Toyota
x1719 = x[c(17:19),]

x.mu  = apply(x1719,2,mean)           # column means
y     = matrix(0,nrow(x1719),ncol(x1719)) # empty matrix

# fill binary matrix
for (i in 1:nrow(x1719)){             # if x(i,k)>x_bar(k): 1, else 0
	for(k in 1:ncol(x1719)){
	    if(x1719[i,k]>x.mu[k]){
	    	y[i,k]=1
	    }else{
	    	y[i,k]=0
	    }
	}
}

# similarity coefficients for binary data

sim(y,method="jaccard")         # jaccard

sim(y,method="simplematching")  # simple matching

sim(y,method="roger")           # tanimoto
```

automatically created on 2018-05-28