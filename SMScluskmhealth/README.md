[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMScluskmhealth** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet : SMScluskmhealth

Published in : 'Multivariate Statistics: Exercises and Solutions'

Description : 'Performs a k-means cluster analysis with the standard algorithm (Lloyds) 
on the 2005 US health data set. Four clusters are extracted and plotted with different 
colours for the first two principal components.'

Keywords : 'cluster-analysis, principal-components, plot, graphical representation,
partitioning'

See also : 'MVAclususcrime, MVAdrugsim, SMSclus8p, SMSclus8pd, SMSclus8pmst2, SMSclusbank, 
SMSclusbank2, SMSclusbank3, SMScluscomp, SMScluscrime, SMScluscrimechi2, SMSclushealth'

Author : Simon Trimborn, Awdesch Melzer

Submitted : Fri, August 22 2014 by Awdesch Melzer

Datafiles : ushealth05.csv

Example :
- 'principal components of US health data 2005 with 4 coloured clusters'


```

![Picture1](SMScluskmhealth.png)

### R Code
```r

graphics.off()
rm(list=ls(all=T))


# setwd("C:/...")
# install required packages
# install.packages("MASS")
library(MASS)
# set pseudo random numbers for algorithm starting value
set.seed(99)

ushealth = read.csv("ushealth05.csv",sep=",",header=T) # load data

results  = kmeans(ushealth[,3:12],4, algorithm="Lloyd") # k-means algorithm

PC       = prcomp(ushealth[3:12])$x[,1:2] # PCA

# first 2 PCs with clusters in 4 colours
plot(PC,type="n",main="US health data") 
cl         = as.numeric(results$cluster)
col        = cl
col[cl==3] = 2
col[cl==2] = 3
text(PC[,1],PC[,2],ushealth$ANSI,col=col)

```

automatically created on 2018-05-28