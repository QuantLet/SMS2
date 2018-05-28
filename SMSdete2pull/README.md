[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSdete2pull** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml


Name of Quantlet: SMSdete2pull

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'estimates coefficients, F-statistics and coefficients of
determination of three linear models for pullover sales,
first with one regressor, second with two regressors, and
third with three regressors.  R-squared is a measure for 
model comparison of nested models. The model with three explanatory
variables has highest value of the coefficient of determination. The
model with only one explanatory variables performes worst.'

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
% Quantlet:    SMSdete2pull
% -------------------------------------------------------------------------
% Description: It estimates coefficients, F-statistics and coefficients of
%              determination of three linear models for pullover sales,
%              first with one regressor, second with two regressors, and
%              third with three regressors.  R-squared is a measure for 
%              model comparison of nested models. The model with three explanatory
%              variables has highest value of the coefficient of determination. The
%              model with only one explanatory variables performes worst.
% -------------------------------------------------------------------------
% Input:       None.
% -------------------------------------------------------------------------
% Output:      Tables of estimated coefficients, F-test and R-squared.
% -------------------------------------------------------------------------
% Results:     
% Model with constant and 1 regressor
% coefficients
%   210.7736
%    -0.3640
% 
%    F-test    p-value  error-variance
%    1.0e+03 *
% 
%     0.0002    0.0006    1.2601
% 
% R-squared: One explanatory variable:
%     0.0281
% 
% Model with constant and 2 regressors
% coefficients
%   176.6919
%    -0.6013
%     0.5663
% 
%    F-test    p-value  error-variance
%    16.7993    0.0021  255.4789
% 
% R-squared: Two explanatory variables:
%     0.8276
% 
% Model with constant and 3 regressors
% coefficients
%    65.6696
%    -0.2158
%     0.4852
%     0.8437
% 
%    F-test    p-value  error-variance
%    19.4386    0.0017  161.2685
% 
% R-squared: Three explanatory variables:
%     0.9067
%  
% -------------------------------------------------------------------------
% Keywords:    linear, linear model, linear regression, least-squares, R-squared
%              regression, F test, F-statistic, F-test, test, summary,
%              statistics
% -------------------------------------------------------------------------
% See also:    SMSanovapull, SMSdete2pull, SMSdeterpull, SMSlinregpull,
%              SMSscabank45, SMScovbank
% -------------------------------------------------------------------------
% Author:      Awdesch Melzer 20131023
% -------------------------------------------------------------------------

clear all
close all
clc


load pullover.dat        % load data

data = pullover;
y    = data(:,1);        % sales
x1   = ones(10,1);       % constant
x2   = [x1,data(:,2)];   % price
x23  = [x1,data(:,2:3)]; % price and advertisement
x234 = [x1,data(:,2:4)]; % price, advertisement, ass. hours

[b2,bint2,r2,rint2,stats2]           = regress(y,x2);

disp('Model with constant and 1 regressor')
disp('coefficients')
disp(b2)
disp('   F-test    p-value  error-variance')
disp(stats2(2:4))

disp('R-squared: One explanatory variable:')
disp(stats2(1))

[b23,bint23,r23,rint23,stats23]      = regress(y,x23);

disp('Model with constant and 2 regressors')
disp('coefficients')
disp(b23)

disp('   F-test    p-value  error-variance')
disp(stats23(2:4))

disp('R-squared: Two explanatory variables:')
disp(stats23(1))


[b234,bint234,r234,rint234,stats234] = regress(y,x234);
disp('Model with constant and 3 regressors')
disp('coefficients')
disp(b234)

disp('   F-test    p-value  error-variance')
disp(stats234(2:4))

disp('R-squared: Three explanatory variables:')
disp(stats234(1))

```

automatically created on 2018-05-28

### R Code
```r

# -------------------------------------------------------------------------
# Book:        SMS
# -------------------------------------------------------------------------
# Quantlet:    SMSdete2pull
# -------------------------------------------------------------------------
# Description: Computes coefficients, F-statistics, as well as R-squared values of three linear models for
#              pullover sales, first with one regressor, second with two regressors, and third with three regressors.
#              R-squared is a measure for model comparison of nested models. The model with three explanatory variables
#              has highest value of the coefficient of determination.
#              The model with only one explanatory variables performes worst.
# -------------------------------------------------------------------------
# Output:      Tables of estimated coefficients, F-test and R-squared.
# -------------------------------------------------------------------------
# Results:     
# Model with constant and 1 regressor
# Call:
# lm(formula = Sales ~ Price, data = pullover)
#
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -70.095  -8.898   2.036   9.805  64.725 
#
# Coefficients:
#             Estimate Std. Error t value Pr(>|t|)  
# (Intercept) 210.7736    79.9837   2.635   0.0299 *
# Price        -0.3640     0.7571  -0.481   0.6435  
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# Residual standard error: 35.5 on 8 degrees of freedom
# Multiple R-squared:  0.02808,	Adjusted R-squared:  -0.09341 
# F-statistic: 0.2311 on 1 and 8 DF,  p-value: 0.6435
# 
# R-squared: One explanatory variable:
#     0.02808172
# 
# Model with constant and 2 regressors
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
# R-squared: Two explanatory variables:
#     0.8275805
# 
# Model with constant and 3 regressors
# Call:
# lm(formula = Sales ~ Price + Advertisement + Hours, data = pullover)
#
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -13.369  -9.406   1.599   5.151  19.729 
#
# Coefficients:
#               Estimate Std. Error t value Pr(>|t|)   
# (Intercept)   65.66956   57.12507   1.150  0.29407   
# Price         -0.21578    0.32194  -0.670  0.52764   
# Advertisement  0.48519    0.08678   5.591  0.00139 **
# Hours          0.84373    0.37400   2.256  0.06491 . 
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# Residual standard error: 12.7 on 6 degrees of freedom
# Multiple R-squared:  0.9067,	Adjusted R-squared:  0.8601 
# F-statistic: 19.44 on 3 and 6 DF,  p-value: 0.001713# 
#
# R-squared: Three explanatory variables:
#     0.9067102
#  
# -------------------------------------------------------------------------
# Keywords:    linear, linear model, linear regression, least-squares, R-squared
#              regression, F test, F-statistic, F-test, test, summary,
#              statistics
# -------------------------------------------------------------------------
# See also:    SMSanovapull, SMSdete2pull, SMSdeterpull, SMSlinregpull,
#              SMSscabank45, SMScovbank
# -------------------------------------------------------------------------
# Author:      Zdenek Hlavka
# -------------------------------------------------------------------------

# clear variable list and close windows
rm(list=ls(all=TRUE))
graphics.off()

load("pullover.rda")                                      # load data

lm2   = lm(Sales~Price,data=pullover)                     # "One explanatory variable:"
print(summary(lm2)$r.squared)

lm23  = lm(Sales~Price+Advertisement,data=pullover)       # "Two explanatory variables:"
print(summary(lm23)$r.squared)

lm234 = lm(Sales~Price+Advertisement+Hours,data=pullover) # "Three explanatory variables:"
print(summary(lm234)$r.squared)

```

automatically created on 2018-05-28