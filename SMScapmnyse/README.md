[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMScapmnyse** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMScapmnyse

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'Produces plot of regression lines for 3 NYSE traded stocks according to CAPM'

Keywords: 'CAPM, linear model'

See also: 'SMScapmnyse, SMSportfol'

Author[r]: Kristyna Sionova
Author[m]: Awdesch Melzer

Datafile[r]: nyse.rda
Datafile[m]: nyse.dat

Example: 'plot of regression lines for 3 NYSE traded stocks according to CAPM'
```

![Picture1](SMScapmnyse_m.png)

![Picture2](SMScapmnyse_r.png)

### R Code
```r

# Clear variables and close windows
graphics.off()
rm(list=ls(all=TRUE))
#setwd("C:/...")         #set your working directory, create there a subdirectory 'data' for the datasets

load("nyse.rda")
attach(nyse)

pi = lm(PanAm~IBM)				    #linear models
di = lm(DEC~IBM)

par(mfrow=c(1,2)) #plot of the results
plot(PanAm~IBM,col="blue",main="PanAm vs. IBM",xlim=c(-0.19,0.19),ylim=c(-0.41,0.41))
abline(pi)
plot(DEC~IBM,col="blue",main="DEC vs. IBM",xlim=c(-0.19,0.19),ylim=c(-0.41,0.41))
abline(di)

detach(nyse)
```

automatically created on 2018-05-28

### MATLAB Code
```matlab

% Clear variables and close windows
clear all
close all
clc

load('nyse.dat')
% IBM PanAm Delta Edison Gerber Texaco DEC
pi = LinearModel.fit(nyse(:,1),nyse(:,2));				    %linear models
bp = pi.Coefficients.Estimate;
t  = -0.2:0.05:0.2;

di = LinearModel.fit(nyse(:,7),nyse(:,2));
bd = di.Coefficients.Estimate;


subplot(1,2,1) %plot of the results
plot(nyse(:,1),nyse(:,2),'bo')
title('PanAm vs. IBM','FontSize',16,'FontWeight','Bold')
box on
set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold')
xlim([-0.19,0.19])
ylim([-0.41,0.41])
line(t,bp(1)+bp(2)*t,'Color','k', 'LineWidth',1.5)
subplot(1,2,2)
plot(nyse(:,1),nyse(:,7),'bo')
title('DEC vs. IBM','FontSize',16,'FontWeight','Bold')
box on
set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold')
xlim([-0.19,0.19])
ylim([-0.41,0.41])
line(t,bd(1)+bd(2)*t,'Color','k', 'LineWidth',1.5)
```

automatically created on 2018-05-28