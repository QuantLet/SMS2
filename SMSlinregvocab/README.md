

[<img src="https://github.com/QuantLet/Styleguide-and-Validation-procedure/blob/master/pictures/banner.png" alt="Visit QuantNet">](http://quantlet.de/index.php?p=info)

## [<img src="https://github.com/QuantLet/Styleguide-and-Validation-procedure/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSlinregvocab** [<img src="https://github.com/QuantLet/Styleguide-and-Validation-procedure/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/d3/ia)


```yaml
Name of Quantlet: SMSlinregvocab

Published in: Multivariate Statistics: Exercises and Solutions Series 

Description: 'computes a linear regression of vocab. score in grade 11 on vocabulary grades in previous years for the vocabulary data.
Linear Regressions:
grade11 = const + grade8 + grade9 + grade10 + epsilon
grade11 = const + grade9 + grade10 + epsilon'

Keywords: 'linear model, linear regression, least squares, R-squared, gls'

See also: 'SMSlinregbank2, SMSlinregvocab, SMSprofil, SMSprofplasma, SMStestcov, SMStestcov4i, SMStestcovwais, SMStestsim, SMStestuscomp'

Author[r]:   Jakub Pecanka
Author[m]:   Philipp Jackmuth

Submitted:  

Datafile[r]: vocabulary.rda
Datafile[m]: vocabulary.dat

Output: 'Coefficients, Standard Errors, p-values, t-stats and other statistics of the two linear regressions'

Example[r]: ' print(summary(res1))

 Call:
 lm(formula = grade11 ~ grade8 + grade9 + grade10, data = vocabulary)

 Residuals:
     Min      1Q  Median      3Q     Max 
 -2.8741 -0.6186 -0.0501  0.6743  3.1859 

 Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
 (Intercept)   1.4782     0.2999   4.929 6.86e-06 ***
 grade8        0.2015     0.1582   1.273   0.2078    
 grade9        0.2278     0.1152   1.977   0.0526 .  
 grade10       0.3965     0.1304   3.041   0.0035 ** 
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

 Residual standard error: 1.073 on 60 degrees of freedom
 Multiple R-squared:  0.7042,	Adjusted R-squared:  0.6894 
 F-statistic: 47.61 on 3 and 60 DF,  p-value: 7.144e-16

  print(summary(res2))

 Call:
 lm(formula = grade11 ~ grade9 + grade10, data = vocabulary)

 Residuals:
     Min      1Q  Median      3Q     Max 
 -2.7450 -0.7227 -0.0853  0.6816  3.4194 

 Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
 (Intercept)   1.2355     0.2327   5.309 1.63e-06 ***
 grade9        0.2893     0.1051   2.752  0.00779 ** 
 grade10       0.5022     0.1011   4.969 5.75e-06 ***
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

 Residual standard error: 1.079 on 61 degrees of freedom
 Multiple R-squared:  0.6962,	Adjusted R-squared:  0.6862 
 F-statistic: 69.89 on 2 and 61 DF,  p-value: < 2.2e-16'

Example[m]: 'Regression results: regress "grade11" on "grade8", "grade9" and "grade10"

 Linear regression model:
     y ~ 1 + x1 + x2 + x3

 Estimated Coefficients:
                    Estimate    SE         tStat     pValue
     (Intercept)     1.4782     0.29993    4.9286    6.8605e-06
     x1             0.20149     0.15824    1.2733       0.20781
     x2             0.22782     0.11521    1.9775      0.052587
     x3             0.39651      0.1304    3.0408     0.0034955


 Number of observations: 64, Error degrees of freedom: 60
 Root Mean Squared Error: 1.07
 R-squared: 0.704,  Adjusted R-Squared 0.689
 F-statistic vs. constant model: 47.6, p-value = 7.14e-16
 Regression results: regress "grade11" on "grade9" and "grade10"

 Linear regression model:
     y ~ 1 + x1 + x2

 Estimated Coefficients:
                    Estimate    SE         tStat     pValue
     (Intercept)     1.2355      0.2327    5.3092    1.6292e-06
     x1             0.28931     0.10513    2.7518     0.0077927
     x2             0.50222     0.10107    4.9692    5.7517e-06


 Number of observations: 64, Error degrees of freedom: 61
 Root Mean Squared Error: 1.08
 R-squared: 0.696,  Adjusted R-Squared 0.686
 F-statistic vs. constant model: 69.9, p-value = 1.66e-16'

```

```R
# -------------------------------------------------------------------------
# Book:         SMS
# -------------------------------------------------------------------------
# Quantlet:     SMSlinregvocab
# -------------------------------------------------------------------------
# Description:  computes a linear regression of vocab. score in
#               grade 11 on vocabulary grades in previous years for the
#               vocabulary data ('vocabulary.dat')
#               Linear Regressions:
#               grade11 = cons + grade8 + grade9 + grade10 + epsilon
#               grade11 = cons + grade9 + grade10 + epsilon
# -------------------------------------------------------------------------
# Usage:		-
# -------------------------------------------------------------------------
# See also:     -
# -------------------------------------------------------------------------
# Inputs:       none
# -------------------------------------------------------------------------
# Output:       Coefficients, Standard Errors, p-values, t-stats and other 
#               statistics of the two linear regressions
# -------------------------------------------------------------------------
# Example:      -
# -------------------------------------------------------------------------
# Results:
# print(summary(res1))
#
# Call:
# lm(formula = grade11 ~ grade8 + grade9 + grade10, data = vocabulary)
#
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -2.8741 -0.6186 -0.0501  0.6743  3.1859 
#
# Coefficients:
#             Estimate Std. Error t value Pr(>|t|)    
# (Intercept)   1.4782     0.2999   4.929 6.86e-06 ***
# grade8        0.2015     0.1582   1.273   0.2078    
# grade9        0.2278     0.1152   1.977   0.0526 .  
# grade10       0.3965     0.1304   3.041   0.0035 ** 
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# Residual standard error: 1.073 on 60 degrees of freedom
# Multiple R-squared:  0.7042,	Adjusted R-squared:  0.6894 
# F-statistic: 47.61 on 3 and 60 DF,  p-value: 7.144e-16
#
#  print(summary(res2))
#
# Call:
# lm(formula = grade11 ~ grade9 + grade10, data = vocabulary)
#
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -2.7450 -0.7227 -0.0853  0.6816  3.4194 
#
# Coefficients:
#             Estimate Std. Error t value Pr(>|t|)    
# (Intercept)   1.2355     0.2327   5.309 1.63e-06 ***
# grade9        0.2893     0.1051   2.752  0.00779 ** 
# grade10       0.5022     0.1011   4.969 5.75e-06 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# Residual standard error: 1.079 on 61 degrees of freedom
# Multiple R-squared:  0.6962,	Adjusted R-squared:  0.6862 
# F-statistic: 69.89 on 2 and 61 DF,  p-value: < 2.2e-16
# -------------------------------------------------------------------------
# Keywords:    linear model, linear regression, least squares, R-squared,
#              gls
# -------------------------------------------------------------------------
# See also:    SMSlinregbank2, SMSlinregvocab, SMSprofil, SMSprofplasma,
#              SMStestcov, SMStestcov4i, SMStestcovwais, SMStestsim,
#              SMStestuscomp
# -------------------------------------------------------------------------
# Author:       Jakub Pecanka
# -------------------------------------------------------------------------

# clear variables and close windows
rm(list=ls(all=TRUE))
graphics.off()

# setwd("C:/...") # set working directory
load("vocabulary.rda")

names(vocabulary)=c("grade8","grade9","grade10","grade11","mean")

res1=lm(grade11~grade8+grade9+grade10,data=vocabulary)
res2=lm(grade11~grade9+grade10,data=vocabulary)

print(summary(res1))
print(summary(res2))

```
