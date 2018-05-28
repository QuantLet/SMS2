[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSclusbank** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMSclusbank

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'performs a PCA and a cluster analysis for 20 randomly chosen bank notes from the swiss bank notes dataset.
Centered principal components as well as cluster analysis employing
ward linkage to squared euclidean distance matrix perform
similarly quite well on seperating real from forged bank notes.'

Keywords: 'cluster analysis, distance, euclidean, euclidean norm,linkage, ward, ward algorithm, dendrogram, principal components, PCA, centering, pseudo random numbers, sampling'

See also: 'MVAQnetClusKmeans, MVAQnetClusKmeansB, MVAQnetClusKmeansT, MVAcarsim, MVAclus8p, MVAclusfood, MVAclususcrime, MVAdrugsim, MVAspecclust, SMScarsim, SMSclus8km, SMSclus8pa, SMSclus8pc, SMSclus8pd, SMSclus8pmst, SMSclus8pmst2, SMSclus8psc, SMSclusbank, SMSclusbank2, SMSclusbank3, SMScluscereal, SMScluscomp, SMScluscrime, SMScluscrimechi2, SMSclushealth, SMSclushealth05, SMScluskmcereal, SMScluskmhealth'

Author[r]: Kristyna Ivankova, Zdenek Hlavka, Awdesch Melzer
Author[m]: Awdesch Melzer

Datafile[r]: bank2.rda
Datafile[m]: bank2.dat

Example: 'PCA for the 20 randomly chosen bank notes and the Dendrogram of them after applying the Ward algorithm.'
```

![Picture1](SMSclusbank_m.png)

![Picture2](SMSclusbank_r.png)

### R Code
```r

# clear variables and close graphics
rm(list=ls(all=TRUE))
graphics.off()

load("bank2.rda") # load data

set.seed(100)     # set pseudo random numbers

bank = bank2[sample(1:200,20,replace=FALSE),] # 20 randomly selected Swiss bank notes

# plot
opar = par(mfrow = c(1, 2))
pcb=prcomp(bank, scale = TRUE)
plot(pcb$x[,1:2],type="n",main="20 Swiss bank notes")  # principal component analysis
text(pcb$x[,1:2],labels=row.names(bank))               # principal component analysis

# plot squared euclidean distance and ward algorithm.
par(mar=c(2, 4, 4, 2) +  0.1)
plot(hclust(dist(bank,method="euclidean")^2,method="ward.D"),ylab="squared Euclidean distance",xlab="",sub="",main="Ward dendrogram") #cluster analysis using Ward algorithm and squared Euclidean distance
par(opar)

```

automatically created on 2018-05-28

### MATLAB Code
```matlab

% clear variables and close graphics
clear all
close all
clc

%% load data and take sample
load('bank2.dat')

% set pseudo random numbers
RandStream.setGlobalStream(RandStream('mt19937ar','seed',100));

% sample n=20 out of the data set
bank2 = [(1:200)',bank2];    % set index variable
n     = 20;                  % sample size
bank  = datasample(bank2,n); % 20 randomly selected Swiss bank notes
lab   = strvcat(num2str(bank(:,1)));

%% principal component analysis
[coeff,score,latent]  = pca(bank(:,2:7));

% plot of scores
subplot(1,2,1)
plot(score(:,1),score(:,2),'w')
title('20 Swiss bank notes','FontSize',12,'FontWeight','Bold')
text(score(:,1),score(:,2),lab,'FontSize',14)
box on
set(gca,'LineWidth',1.6,'FontSize',12,'FontWeight','Bold')

%% ward method for squared Euclidean distance matrix
% Draw line segments between pairs of points 
d     = pdist(bank(:,2:7),'euclidean'); % euclidean distance matrix
dd    = d.^2;                     % squared euclidean distance matrix
ss    = linkage(dd,'ward');     % cluster analysis with ward algorithm 

% Dendrogram for the data points after ward linkage
subplot(1,2,2)
[H,T] = dendrogram(ss,'colorthreshold','default','Labels',lab);
set(H,'LineWidth',2)
title('Ward Dendrogram','FontSize',16,'FontWeight','Bold')
ylabel('Squared Euclidean Distance','FontSize',12,'FontWeight','Bold')
box on
set(gca,'LineWidth',1.6,'FontSize',12,'FontWeight','Bold')

```

automatically created on 2018-05-28