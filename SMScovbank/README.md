
![http://quantnet.wiwi.hu-berlin.de/style/banner.png](http://quantnet.wiwi.hu-berlin.de/style/banner.png)

## ![qlogo](http://quantnet.wiwi.hu-berlin.de/graphics/quantlogo.png) **SMSandcurpopu**


```yaml

Name of Quantlet: SMScovbank

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'calculates the covariance matrix (and eigevalues)
of the Swiss Bank (bank2.dat) dataset and the variance of
the counterfeit bank notes (observations 101-200) after they 
were lineary transformed by a vector a = (1, 1, 1, 1, 1, 1)''.'

Keywords: 'covariance, eigenvalues, spectral decomposition,
multivariate, multi dimensional, variance, transformation,
decomposition, eigenvalue decomposition, Covariance'

See also: 'SMSanovapull, SMScovbank, SMSdete2pull, SMSdeterpull,
SMSlinregpull, SMSscabank45'

Author[r]: Dana Chromikova
Author[m]: Awdesch Melzer

Submitted:  

Output: 'covariance matrix (and eigevalues) of the transformed counterfeit bank notes from bank2 dataset'

Example[r]: 'Covariance matrix:
 round(cov(bank2),4)
                    Length Height Left Height Right Inner Frame Lower Inner Frame Upper Diagonal
 Length             0.1418      0.0314       0.0231           -0.1032           -0.0185   0.0843
 Height Left        0.0314      0.1303       0.1084            0.2158            0.1050  -0.2093
 Height Right       0.0231      0.1084       0.1633            0.2841            0.1300  -0.2405
 Inner Frame Lower -0.1032      0.2158       0.2841            2.0869            0.1645  -1.0370
 Inner Frame Upper -0.0185      0.1050       0.1300            0.1645            0.6447  -0.5496
 Diagonal           0.0843     -0.2093      -0.2405           -1.0370           -0.5496   1.3277

 Eigenvalues:
 e
 3.00030487 0.93562052 0.24341371 0.19465874 0.08521185 0.03551468

 Variance of the transformed (summed over rows) counterfeit bank notes
 v
 1.742282'

 Example[m]: 'Covariance matrix:
   V =

    0.1418    0.0314    0.0231   -0.1032   -0.0185    0.0843
    0.0314    0.1303    0.1084    0.2158    0.1050   -0.2093
    0.0231    0.1084    0.1633    0.2841    0.1300   -0.2405
   -0.1032    0.2158    0.2841    2.0869    0.1645   -1.0370
   -0.0185    0.1050    0.1300    0.1645    0.6447   -0.5496
    0.0843   -0.2093   -0.2405   -1.0370   -0.5496    1.3277

   Eigenvalues:
   e =

    3.0003         0         0         0         0         0
         0    0.9356         0         0         0         0
         0         0    0.2434         0         0         0
         0         0         0    0.1947         0         0
         0         0         0         0    0.0852         0
         0         0         0         0         0    0.0355%

   Variance of the transformed counterfeit bank notes:
   v =

    1.7423'
```



```R
# clear variables and close windows
 rm(list=ls(all=TRUE))
 graphics.off()

# setwd("C:/...")                         # set working directory

load("bank2.rda")                         # load data

V = var(bank2)                            # variance matrix
V
e = eigen(V)$val                          # eigenvalues of V
e
a = rep(1,times=6)
v = var(as.matrix(bank2[101:200,])%*%a)   # the variance of the row sums
v

```

```Matlab

clear all
close all
clc

load bank2.dat;

V      = cov(bank2);                  % variance matrix
V
[v, e] = eigs(V);                     % eigenvalues of V
e
a      = ones(6,1);
v      = var((bank2(101:200,:))*a);   % the variance of the row sum
v

```
