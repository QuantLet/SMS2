[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSconjexmp** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMSconjexmp

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'Computes conjoint measurement analysis of an example'

Keywords: 'conjoint analysis, analysis of variance, ANOVA, linear model'

See also: 'SMSconjcars, SMSconjexmp'

Author[r]: Jakub Pecanka
Author[m]: Awdesch Melzer

Example: 'summary of the regression model and ANOVA table'
```

### R Code
```r

# clear variables and close windows
rm(list=ls(all=TRUE))
graphics.off()

y1  = c(1,2,4,3,6,5)
y2  = c(1,3,4,2,5,6)
y3  = c(3,1,5,2,6,4)
y   = c(y1,y2,y3)

x1  = cbind(1,c(0,0,1,1,0,0),c(0,0,0,0,1,1),c(0,1,0,1,0,1))
x   = rbind(x1,x1,x1)

cat("n SUMMARY lm(y~x-1)n")
print(summary(lm(y~x-1)))
z1  = as.vector(cbind(y1[1:2],y2[1:2],y3[1:2]))
z2  = as.vector(cbind(y1[3:4],y2[3:4],y3[3:4]))
z3  = as.vector(cbind(y1[5:6],y2[5:6],y3[5:6]))
z   = cbind(z1,z2,z3)
lmz = lm(z3~z1+z2)
cat("n ANOVA lm(z3~z1+z2) nn")
print(anova(lmz))
```

automatically created on 2018-05-28

### MATLAB Code
```matlab

% clear variables and close windows
clear all
close all
clc

y1  = [1,2,4,3,6,5]';
y2  = [1,3,4,2,5,6]';
y3  = [3,1,5,2,6,4]';
y   = [y1;y2;y3];

x1  = [ones(6,1),[0;0;1;1;0;0],[0;0;0;0;1;1],[0;1;0;1;0;1]];
x   = [x1;x1;x1];

disp('     SUMMARY lm(y~x-1)n     ')
lmd = LinearModel.fit(x,y,'Intercept',false)

z1  = [y1(1:2)',y2(1:2)',y3(1:2)'];
z2  = [y1(3:4)',y2(3:4)',y3(3:4)'];
z3  = [y1(5:6)',y2(5:6)',y3(5:6)'];
z   = [z1,z2,z3];

lmz = LinearModel.fit([z1',z2'],z3)
disp('      ANOVA lm(z3~z1+z2)    ')
anova(lmz)
```

automatically created on 2018-05-28