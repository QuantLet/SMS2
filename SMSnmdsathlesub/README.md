[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSnmdsathlesub** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMSnmdsathlesub

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'computes the nonmetric MDS for the athletic data set (athletic.rda) without four most outlying countries, e.g. Netherlands, West Samoa, Mauritius, and Cook Islands.'

Keywords: 'multidimensional scaling, mds, nonmetric, distance, Euclidean, correlation'

See also: 'SMSmdsbank, SMSnmdsathlesub, SMSnmdsathletic, SMSnmdscarm, SMSnmdsuscrime, SMSnmdsushealth'

Author[r]: Barbora Lebduskova, Zdenek Hlavka
Author[m]: Awdesch Melzer

Datafile[r]: athletic.rda
Datafile[m]: athletic.mat

Example: 'Nonmetric MDS for the athletic data set without four most outlying countries'
```

![Picture1](SMSnmdsathlesub_m.png)

![Picture2](SMSnmdsathlesub_r.png)

### R Code
```r

# clear variables and close windows
rm(list=ls(all=TRUE))
graphics.off()

# install and load packages
libraries = c("MASS")
lapply(libraries, function(x) if (!(x %in% installed.packages())) {
    install.packages(x)})
lapply(libraries, library, quietly = TRUE, character.only = TRUE)

# setwd("C:/...") # please set the working directory
# load data
load("athletic.rda")

x     = athletic[c(1:11,13:35,37,39:54),]       # subsample
x     = scale(x)                                # standardized
d     = dist(x)                                 # distance matrix
loc   = isoMDS(d,maxit=1000,tol = 1e-6)         # nonmetric MDS
xylim = range(loc$points[,1],-loc$points[,2])

# plot
plot(loc$points[,1],-loc$points[,2], main="athletic records", type = "n", ylab=expression(x[2]), xlab=expression(x[1]),xlim=xylim,ylim=xylim)
text(loc$points[,1],-loc$points[,2],labels=row.names(athletic)[c(1:11,13:35,37,39:54)])
```

automatically created on 2018-05-28

### MATLAB Code
```matlab

% clear variables and close windows
clear all
close all
clc

% load data
load('athletic.mat')

x = athletic.data([1:11,13:35,37,39:54]',:); % subsample
x = zscore(x);     % standardized
d = dist(x');      % distance matrix

% nonmetric MDS
[Y,stress,disparities] = mdscale(d,2,'criterion','stress');

% plot
rows = athletic.textdata(2:end,1);
rows = rows([1:11,13:35,37,39:54]);
plot(Y(:,1),Y(:,2),'wo')
title('athletic records','FontSize',16,'FontWeight','Bold')
ylabel('x_2','FontSize',16,'FontWeight','Bold')
xlabel('x_1','FontSize',16,'FontWeight','Bold')
text(Y(:,1),Y(:,2),rows,'FontSize',14)
set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold')
```

automatically created on 2018-05-28