[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSboxunemp** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml


Name of Quantlet: SMSboxunemp

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'Produces a boxplot for unemployment data from Germany. Boxplots for East, West and the pooled data are presented. Within each group, East and West, we find rather homogeneously distributed data. By pooling over both groups the variability increases tremendously, and the mean and median diverge as the unrobust mean is directly affected by the high unemployment rates of East German federal states.'

Keywords: boxplot, data visualization, five number summary, graphical representation, mean, median, plot, robust estimation, visualization

See also: 'SMSandcurpopu, SMSboxbank6, SMSboxunemp, SMSboxunemp, SMSdenbank, SMSdenbank, SMSdrafcar, SMSdrafcar, SMSfacenorm, SMSfacenorm, SMShiscar, SMShiscar, SMShisheights, SMShisheights, SMSpcpcar, SMSpcpcar, SMSscanorm2, SMSscanorm3, SMSscanorm3, SMSscapopu, SMSscapopu'

Author[r]: Tomas Marada
Author[m]: Awdesch Melzer

Submitted:  Fri, August 07 2015 by Awdesch Melzer

Datafile[r]: unemploy.rda
Datafile[m]: unemploy.dat

Example: 'Produces a boxplot for unemployment data from Germany for the West, the East and the pooled data.'
```

![Picture1](SMSboxunemp_m.png)

![Picture2](SMSboxunemp_r.png)

### R Code
```r

rm(list=ls(all=TRUE))                                       # remove variables
graphics.off()                                              # close all windows
# setwd("C/...")                                            # set working direktory

load("unemploy.rda")                                        # load data

x = unemploy[,2]                                            # total unemployment
e = c( 15.1, 15.8, 16.8, 17.1, 17.3, 19.9);                 # unemployment East Germany
w = c( 5.8, 6.2, 7.7, 7.9, 8.7, 9.8, 9.8, 9.8, 10.4, 13.9); # unemployment West Germany

 # calculating means
means = c(mean(x), mean(e), mean(w));
 # producing boxplot without means
boxplot(x,e,w, names = c("All", "East", "West"), main = "Unemployment in Germany");
 # adding means into boxplot
lines(x=c(0.6,1.4),rep(means[1],2),lty=2)
lines(x=c(1.6,2.4),rep(means[2],2),lty=2)
lines(x=c(2.6,3.4),rep(means[3],2),lty=2)
```

automatically created on 2018-05-28

### MATLAB Code
```matlab

 % clear history
clear all
close all
clc

 % load data
load unemploy.dat

 % preparing data
all = unemploy;
we = [3 3 2 3 3 3 3 3 3 3 3 2 2 2 2 2]'; % 3=West, 2=East

j=1;
l=1;
for i=1:length(we)
    if (we(i)==3)
        w(j) = all(i); % west
        j = j+1;
    elseif (we(i)==2)
        e(l) = all(i); % east
        l = l+1;
    end
end

 % calculating means
means = [mean(all), mean(e), mean(w)];


 % resampling for plot
data = [all;all];
groups = [ones(length(all),1);we];

hold on
 % adding means into plot
line([0.775 1.225],[means(1) means(1)],'Color','k','LineStyle',':','LineWidth',1.2)
line([1.775 2.225],[means(2) means(2)],'Color','k','LineStyle',':','LineWidth',1.2)
line([2.775 3.225],[means(3) means(3)],'Color','k','LineStyle',':','LineWidth',1.2)
 % producing boxplots
boxplot(data,groups,'Symbol','o', 'labels',{'All', 'East', 'West'});
title('Unemployment in Germany','FontSize',16,'FontWeight','Bold');
set(findobj(gca,'Type','text'),'FontSize',16,'FontWeight','Bold');
box on
set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold')   % set frame
hold off


 % to save plot please uncomment following lines 
 % print -painters -dpng -r600 SMSboxunemp.png
 % print -painters -dpdf -r600 SMSboxunemp.pdf
```

automatically created on 2018-05-28