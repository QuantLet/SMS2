[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSdenbank** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml


Name of Quantlet: SMSdenbank

Published in: 'Multivariate Statistics: Exercises and Solutions'

Description: "Computes kernel density estimates of the diagonal of the genuine and forged swiss bank notes. The bandwidth parameter are chosen by Silverman's rule of thumb."

Keywords: Silverman, bandwidth, data visualization, density, estimation, gaussian, graphical representation, kde, kernel, plot

See also: 'SMSandcurpopu, SMSboxbank6, SMSboxunemp, SMSboxunemp, SMSdenbank, SMSdenbank, SMSdrafcar, SMSdrafcar, SMSfacenorm, SMSfacenorm, SMShiscar, SMShiscar, SMShisheights, SMShisheights, SMSpcpcar, SMSpcpcar, SMSscanorm2, SMSscanorm3, SMSscanorm3, SMSscapopu, SMSscapopu'

Author[r]: Kristyna Ivankova, Dedy D. Prastyo
Author[m]: Awdesch Melzer

Submitted:  Fri, August 07 2015 by Awdesch Melzer

Datafile[r]: bank2.rda
Datafile[m]: bank2.dat

Example: 'Kernel density estimates of the diagonal of the genuine and forged swiss bank notes.'
```

![Picture1](SMSdenbank_m.png)

![Picture2](SMSdenbank_r.png)

### R Code
```r

# remove variables and close windows
 rm(list=ls(all=TRUE))
 graphics.off()

# setwd("C:/...")                                 # set working directory
load("bank2.rda")                                 # load data
bank  = bank2[,6]                                 # sixth column (X6)
x1    = bank[1:100]                               # genuine bank notes
x2    = bank[101:200]                             # counterfeit bank notes
h.opt = c(sd(x1),sd(x2))*length(x1)^(-1/5)*1.06   # Silverman's rule of thumb
fh1   = density(x1,kernel="gaussian",bw=h.opt[1]) # kernel density estimation for the diagonal of genuine bank notes
fh2   = density(x2,kernel="gaussian",bw=h.opt[2]) # kernel density estimation for the diagonal of counterfeit bank notes
plot(fh1,xlim=c(137.5,143),ylim=c(0.0,0.9),xlab="Counterfeit    /    Genuine",ylab="density estimates for diagonals",main="Swiss bank notes")
lines(fh2,lty=2)
```

automatically created on 2018-09-04

### MATLAB Code
```matlab

% remove variables and close windows
clear all
close all
clc

% load data
load bank2.dat

bank     = bank2(:,6);                                    % sixth column (X6)
x1       = bank(1:100);                                   % genuine bank notes
x2       = bank(101:200);                                 % counterfeit bank notes
h_opt    = [std(x1),std(x2)].*size(x1,1).^(-1/5).*1.06;   % Silverman's rule of thumb

% density estimates
[x1 fh1] = ksdensity(x1,'width',h_opt(1)); % kernel density estimation for the diagonal of 
% genuine bank notes
[x2 fh2] = ksdensity(x2,'width',h_opt(2)); % kernel density estimation for the diagonal of
% counterfeit bank notes

% plot
hold on
plot(fh1,x1,'LineWidth',2,'Color','k')
xlabel('counterfeit/genuine','FontSize',16,'FontWeight','Bold')
ylabel('density estimates for diagonals','FontSize',16,'FontWeight','Bold')
title('Swiss bank notes','FontSize',16,'FontWeight','Bold')
box on
set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold')
plot(fh2,x2,'LineWidth',2,'Color','r','LineStyle','-.')
hold off

% to save plot please uncomment following lines 
% print -painters -dpng -r600 SMSdenbank.png
% print -painters -dpdf -r600 SMSdenbank.pdf
```

automatically created on 2018-09-04