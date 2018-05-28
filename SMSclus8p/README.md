[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSclus8p** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMSclus8p

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'Employs the Ward method and complete linkage using squared Euclidean distance matrices to perform a cluster analysis on an 8 points example.'

Keywords: 'Ward algorithm, cluster-analysis, complete linkage, dendrogram, distance, euclidean, euclidean distance matrix, euclidean-norm, linkage'

See also: 'MVAQnetClusKmeans, MVAQnetClusKmeansB, MVAQnetClusKmeansT, MVAcarsim, MVAclus8p, MVAclusfood, MVAclususcrime, MVAdrugsim, MVAspecclust, SMScarsim, SMSclus8km, SMSclus8pa, SMSclus8pc, SMSclus8pd, SMSclus8pmst, SMSclus8pmst2, SMSclus8psc, SMSclusbank, SMSclusbank2, SMSclusbank3, SMScluscereal, SMScluscomp, SMScluscrime, SMScluscrimechi2, SMSclushealth, SMSclushealth05, SMScluskmcereal, SMScluskmhealth'

Author[r]: Zdenek Hlavka, Awdesch Melzer
Author[m]: Awdesch Melzer

Example: 'ward algorithm and dendrogram and complete linkage algorithm and dendrogram'
```

![Picture1](SMSclus8p01_m.png)

![Picture2](SMSclus8p01_r.png)

![Picture3](SMSclus8p02_m.png)

![Picture4](SMSclus8p02_r.png)

### R Code
```r

# clear cache and close windows
graphics.off()
rm(list=ls(all=TRUE))

# define eight points
eight=cbind(c(-3,-2,-2,-2,1,1,2,4),c(0,4,-1,-2,4,2,-4,-3))
eight=eight[c(8,7,3,1,4,2,6,5),]

# plot eight points using ward algorithm
par(mfrow = c(1, 2))
plot(eight,type="n",xlab="price conciousness",ylab="brand loyalty",xlim=c(-4,4),main="8 points")
segments(eight[1,1],eight[1,2 ],eight[2,1 ],eight[2,2],lwd=2)
segments(eight[2,1],eight[2,2 ],eight[5,1 ],eight[5,2],lwd=2)
segments(eight[5,1],eight[5,2 ],eight[3,1 ],eight[3,2],lwd=2)
segments(eight[3,1],eight[3,2 ],eight[4,1 ],eight[4,2],lwd=2)
segments(eight[3,1],eight[3,2 ],eight[7,1 ],eight[7,2],lwd=2)
segments(eight[7,1],eight[7,2 ],eight[8,1 ],eight[8,2],lwd=2)
segments(eight[8,1],eight[8,2 ],eight[6,1 ],eight[6,2],lwd=2)
points(eight, pch=21, cex=2.7, bg="white")
text(eight,as.character(1:8),col="red3",xlab="first coordinate", ylab="second coordinate", main="8 points",cex=1)

plot(hclust(dist(eight,method="euclidean")^2,method="ward.D"),ylab="squared Euclidean distance", xlab="",sub="",main="Ward dendrogram") 

dev.new()
# plot eight points using complete linkage
par(mfrow = c(1, 2))
plot(eight,type="n",xlab="price conciousness",ylab="brand loyalty",xlim=c(-4,4), main="8 points")
segments(eight[1,1],eight[1,2 ],eight[2,1 ],eight[2,2],lwd=2)
segments(eight[1,1],eight[1,2 ],eight[6,1 ],eight[6,2],lwd=2)
segments(eight[6,1],eight[6,2 ],eight[7,1 ],eight[7,2],lwd=2)
segments(eight[7,1],eight[7,2 ],eight[8,1 ],eight[8,2],lwd=2)
segments(eight[8,1],eight[8,2 ],eight[5,1 ],eight[5,2],lwd=2)
segments(eight[5,1],eight[5,2 ],eight[4,1 ],eight[4,2],lwd=2)
segments(eight[5,1],eight[5,2 ],eight[3,1 ],eight[3,2],lwd=2)
points(eight, pch=21, cex=2.7, bg="white")
text(eight,as.character(1:8),col="red3",xlab="first coordinate", ylab="second coordinate", main="8 points",cex=1)
plot(hclust(dist(eight,method="euclidean")^2,method="complete"),ylab="squared Euclidean distance",xlab="",sub="",main="complete linkage dendrogram") 
```

automatically created on 2018-05-28

### MATLAB Code
```matlab

% clear cache and close windows
clear all
close all
clc

%% example data set containing 8 points
eight  = [-3,-2,-2,-2,1,1,2,4;
          0,4,-1,-2,4,2,-4,-3]';
eight  = eight([8,7,3,1,4,2,6,5]',:);

%% cluster analysis employing ward algorithm
figure(1)
subplot(1,2,1)
plot(eight,'w')
hold on
plot(eight(1:2,1),eight(1:2,2),'k','LineWidth',2)
plot(eight([2 5],1),eight([2 5],2),'k','LineWidth',2)
plot(eight([5 3],1),eight([5 3],2),'k','LineWidth',2)
plot(eight([3 4],1),eight([3 4],2),'k','LineWidth',2)
plot(eight([3 7],1),eight([3 7],2),'k','LineWidth',2)
plot(eight([7 8],1),eight([7 8],2),'k','LineWidth',2)
plot(eight([8 6],1),eight([8 6],2),'k','LineWidth',2)
lab = strvcat(num2str((1:8)'));
ylim([-4.2,4.2])
xlim([-4.4,4.4])
text(eight(:,1),eight(:,2),lab,'Color','r','FontSize',14)
xlabel('first coordinate','FontSize',16,'FontWeight','Bold')
ylabel('second coordinate','FontSize',16,'FontWeight','Bold')
title('8 points','FontSize',16,'FontWeight','Bold')
set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold')


% Draw line segments between pairs of points 
% euclidean distance matrix
d      = pdist(eight,'euclidean');

% squared euclidean distance matrix
dd     = d.^2;

% cluster analysis with ward algorithm                                                  
ss     = linkage(dd,'ward');

% Dendrogram for the 8 data points after ward
subplot(1,2,2)
[H,T]  = dendrogram(ss,'colorthreshold','default');
set(H,'LineWidth',2)
title('Ward Dendrogram - 8 points','FontSize',16,'FontWeight','Bold')
ylabel('Squared Euclidean Distance','FontSize',16,'FontWeight','Bold')
box on
set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold')

%% cluster analysis employing complete linkage algorithm
figure(2)
subplot(1,2,1)
plot(eight,'w')
hold on
plot(eight(1:2,1),eight(1:2,2),'k','LineWidth',2)
plot(eight([1 6],1),eight([1 6],2),'k','LineWidth',2)
plot(eight([6 7],1),eight([6 7],2),'k','LineWidth',2)
plot(eight([7 8],1),eight([7 8],2),'k','LineWidth',2)
plot(eight([8 5],1),eight([8 5],2),'k','LineWidth',2)
plot(eight([5 4],1),eight([5 4],2),'k','LineWidth',2)
plot(eight([5 3],1),eight([5 3],2),'k','LineWidth',2)
lab = strvcat(num2str((1:8)'));
ylim([-4.2,4.2])
xlim([-4.4,4.4])
text(eight(:,1),eight(:,2),lab,'Color','r','FontSize',14)
xlabel('first coordinate','FontSize',16,'FontWeight','Bold')
ylabel('second coordinate','FontSize',16,'FontWeight','Bold')
title('8 points','FontSize',16,'FontWeight','Bold')
set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold')


% Draw line segments between pairs of points 
% euclidean distance matrix
d      = pdist(eight,'euclidean');

% squared euclidean distance matrix
dd     = d.^2;

% cluster analysis with complete linkage algorithm                                                  
ss     = linkage(dd,'complete');

% Dendrogram for the 8 data points after complete linkage
subplot(1,2,2)
[H,T]  = dendrogram(ss,'colorthreshold','default');
set(H,'LineWidth',2)
title('Complete Linkage Dendrogram - 8 points','FontSize',16,'FontWeight','Bold')
ylabel('Squared Euclidean Distance','FontSize',16,'FontWeight','Bold')
box on
set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold')



```

automatically created on 2018-05-28