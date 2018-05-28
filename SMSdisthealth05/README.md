[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSdisthealth05** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet : SMSdisthealth05

Published in : 'Multivariate Statistics: Exercises and Solutions'

Description : 'Calculates distance matrices for Maine, New Hampshire and New York 
from the US health 2005 data set. The distance measures are Euclidean, 
Manhattan and maximum distance.'

Keywords : 'cluster-analysis, distance, euclidean, euclidean-distance-matrix, 
manhattan metric' 

Author : Awdesch Melzer, Simon Trimborn

Submitted : Fri, August 22 2014 by Awdesch Melzer

Datafile : ushealth05.csv
```

### R Code
```r

# clear cache and close windows
rm(list=ls(all=TRUE))
graphics.off()

#setwd("C:/...")        # please change your working directory

ushealth05        = read.csv("ushealth05.csv",sep=",",header=T) # load ushealth data

ush               = ushealth05[order(ushealth05[,20]),] # order data
ushreg            = as.numeric(ush[,20])                # def. regrion
lab               = paste(ush[,22],ushreg)
row.names(ush)    = lab
ush        = ush[c(which(ush$ANSI==c("ME")),which(ush$ANSI==c("NH")),which(ush$ANSI==c("NY"))),]     # use only Maine, New Hampshire, New York
ush        = ush[,3:12] # for the disease related death causes

# Euclidean distance
dist.eu    = dist(ush,method="euclidean",p=2,diag=T)
dist.eu
# Manhattan distance
dist.ma    = dist(ush,method="manhattan",p=2,diag=T)
dist.ma
# Maximum distance
dist.mi    = dist(ush,method="maximum",p=2,diag=T)
dist.mi

```

automatically created on 2018-05-28