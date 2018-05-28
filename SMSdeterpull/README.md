[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSdeterpull** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml


Name of Quantlet: SMSdeterpull

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'compares linear regression of  sales (X1) on 
price and advert (X2, X3) and price and ass. hours (x2,x4)
from the pullovers data set'

Keywords: 'linear, linear model, linear regression, least-squares, R-squared, regression, F test, F-statistic, F-test, test, summary, statistics'

See also: 'SMSanovapull, SMSdete2pull, SMSdeterpull, SMSlinregpull, SMSscabank45, SMScovbank'

Author[r]: Zdenek Hlavka
Author[m]: Awdesch Melzer

Submitted: 

Datafile[r]: pullover.rda
Datafile[m]: pullover.dat 

Output:     Tables of estimated coefficients, F-test and R-squared.

```

### MATLAB Code
```matlab

% -------------------------------------------------------------------------
% Book:        SMS
% -------------------------------------------------------------------------
% Quantlet:    SMSdeterpull
% -------------------------------------------------------------------------
% Description: SMSdeterpull compares linear regression of  sales (X1) on 
%              price and advert (X2, X3) and price and ass. hours (x2,x4)
%              from the pullovers data set ("pullover.dat")
% -------------------------------------------------------------------------
% Input:       None.
% -------------------------------------------------------------------------
% Output:      Tables of estimated coefficients, F-test and R-squared.
% -------------------------------------------------------------------------
% Results:     
% Model with constant and price and advert. as regressor
% coefficients
%   176.6919
%    -0.6013
%     0.5663
% 
%    F-test    p-value  error-variance
%    16.7993    0.0021  255.4789
% 
% R-squared: One explanatory variable:
%     0.8276
% 
% Model with constant and price and ass. hours as regressor
% coefficients
%   -24.1914
%     0.3485
%     1.7104
% 
%    F-test    p-value  error-variance
%     2.5421    0.1479  858.3230
% 
% R-squared: One explanatory variable:
%     0.4207
% -------------------------------------------------------------------------
% Keywords:    linear, linear model, linear regression, least-squares, R-squared
%              regression, F test, F-statistic, F-test, test, summary,
%              statistics
% -------------------------------------------------------------------------
% See also:    SMSanovapull, SMSdete2pull, SMSdeterpull, SMSlinregpull,
%              SMSscabank45, SMScovbank
% -------------------------------------------------------------------------
% Author:      Awdesch Melzer 20131105
% -------------------------------------------------------------------------

clear all
close all
clc


load pullover.dat

data   = pullover;
 y     = data(:,1);                 % sales (X1)
 x23   = data(:,[2,3]);             % price and advert. (X2 and X3)
 x24   = data(:,[2,4]);             % price and ass. hours. (X2 and X4)
 x1    = ones(10,1);                % constant

 [b23,bint23,r23,rint23,stats23] = regress(y,[x1,x23]);
 [b24,bint24,r24,rint24,stats24] = regress(y,[x1,x24]);
 
disp('Model with constant and price and advert. as regressor')
disp('coefficients')
disp(b23)
disp('   F-test    p-value  error-variance')
disp(stats23(2:4))

disp('R-squared: One explanatory variable:')
disp(stats23(1))

disp('Model with constant and price and ass. hours as regressor')
disp('coefficients')
disp(b24)
disp('   F-test    p-value  error-variance')
disp(stats24(2:4))

disp('R-squared: One explanatory variable:')
disp(stats24(1))

```

automatically created on 2018-05-28

### R Code
```r

# -------------------------------------------------------------------------
# Book:        SMS
# -------------------------------------------------------------------------
# Quantlet:    SMSdeterpull
# -------------------------------------------------------------------------
# Description: SMSdeterpull compares linear regression of  sales (X1) on 
#              price and advert (X2, X3) and price and ass. hours (x2,x4)
#              from the pullovers data set ("pullover.rda"). It produces the
#              summary statistics of each model and the corresponding ANOVA.
# -------------------------------------------------------------------------
# Keywords:    linear, linear model, linear regression, least-squares, R-squared
#              regression, F test, F-statistic, F-test, test, summary,
#              statistics
# -------------------------------------------------------------------------
# See also:    SMSanovapull, SMSdete2pull, SMSdeterpull, SMSlinregpull,
#              SMSscabank45, SMScovbank
# -------------------------------------------------------------------------
# Input:       None.
# -------------------------------------------------------------------------
# Output:      Tables of estimated coefficients, F-test and R-squared.
# -------------------------------------------------------------------------
# Results:     
# lm1    = lm(Sales~Price+Advertisement,data=pullover)
# anova(lm1)   #analysis of variance for lm1
# Analysis of Variance Table
#
# Response: Sales
#               Df Sum Sq Mean Sq F value    Pr(>F)    
# Price          1  291.3   291.3  1.1401 0.3210690    
# Advertisement  1 8292.5  8292.5 32.4586 0.0007374 ***
# Residuals      7 1788.4   255.5                      
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# summary(lm1) #summary statistics for lm1
#
# Call:
# lm(formula = Sales ~ Price + Advertisement, data = pullover)
#
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -12.836  -9.023  -5.423   2.817  32.684 
#
# Coefficients:
#                Estimate Std. Error t value Pr(>|t|)    
# (Intercept)   176.69193   36.50781   4.840 0.001878 ** 
# Price          -0.60125    0.34343  -1.751 0.123462    
# Advertisement   0.56634    0.09941   5.697 0.000737 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# Residual standard error: 15.98 on 7 degrees of freedom
# Multiple R-squared:  0.8276,	Adjusted R-squared:  0.7783 
# F-statistic:  16.8 on 2 and 7 DF,  p-value: 0.002128
#
#
# lm2    = lm(Sales~Price+Hours,data=pullover)
# anova(lm2)   #anova table for lm2
# Analysis of Variance Table
#
# Response: Sales
#           Df Sum Sq Mean Sq F value  Pr(>F)  
# Price      1  291.3   291.3  0.3393 0.57848  
# Hours      1 4072.6  4072.6  4.7448 0.06581 .
# Residuals  7 6008.3   858.3                  
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# summary(lm2) #summary stat for lm2
#
# Call:
# lm(formula = Sales ~ Price + Hours, data = pullover)
#
# Residuals:
#    Min     1Q Median     3Q    Max 
# -60.88 -12.30   8.92  16.91  24.19 
#
# Coefficients:
#             Estimate Std. Error t value Pr(>|t|)  
# (Intercept) -24.1914   126.4642  -0.191   0.8537  
# Price         0.3485     0.7053   0.494   0.6363  
# Hours         1.7104     0.7852   2.178   0.0658 .
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# Residual standard error: 29.3 on 7 degrees of freedom
# Multiple R-squared:  0.4207,	Adjusted R-squared:  0.2552 
# F-statistic: 2.542 on 2 and 7 DF,  p-value: 0.1479
#
# -------------------------------------------------------------------------
# Author:      Kristyna Ivankova
# -------------------------------------------------------------------------

# clear variables and close windows
rm(list=ls(all=TRUE))
graphics.off()

# setwd("/...")           # please change your working directory
load("pullover.rda")      # load data

lm1=lm(Sales~Price+Advertisement,data=pullover)
anova(lm1)                # analysis of variance for lm1
summary(lm1)              # summary statistics for lm1

lm2=lm(Sales~Price+Hours,data=pullover)
anova(lm2)                # anova table for lm2
summary(lm2)              # summary stat for lm2

```

automatically created on 2018-05-28