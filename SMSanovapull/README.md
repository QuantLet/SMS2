
![http://quantnet.wiwi.hu-berlin.de/style/banner.png](http://quantnet.wiwi.hu-berlin.de/style/banner.png)

## ![qlogo](http://quantnet.wiwi.hu-berlin.de/graphics/quantlogo.png) **SMSandcurpopu**


```yaml

Name of Quantlet: SMSanovapull

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'performes a linear regression and an analysis
of variance (ANOVA) for three marketing strategies.
A company decides to compare the effect of three marketing strategies:
1. advertisement in local newspaper
2. presence of sales assistant
3. special presentation in shop windows,
on the sales of their portfolio in 30 shops.
The 30 shops were divided into 3 groups of 10 shops.
The sales using the strategies 1, 2, and 3 were
y1 = (9, 11, 10, 12, 7, 11, 12, 10, 11, 13)'',
y2 = (10, 15, 11, 15, 15, 13, 7, 15, 13, 10)'', and
y3 = (18, 14, 17, 9, 14, 17, 16, 14, 17, 15)'', respectively.
A null hypothesis of equality of means of the three groups
is tested. The standard approach of using ANOVA leads to
an F-test. The alternative proposition is to use a
linear factor model using the strategies as regression
variables to build curve that corresponds to the alternative
hypothesis of the ANOVA with three horizontal lines,
each for one strategy. The F-test of testing equality of
the coefficients to zero corresponds to the null of testing
the marketing strategies having no effect.
The output shows rejection of the null hypothesis.
For more information see Exercise 3.20.'

Keywords: 'regression, linear model, analysis of variance, factor-model,
linear model, variance, F-test, F-statistic, F test, mean,
heteroskedasticity, test, Testing'

See also: 'SMScovbank, SMSdete2pull, SMSdeterpull, SMSlinregpull, SMSscabank45'

Author[r]: Dana Chromikova
Author[m]: Awdesch Melzer

Submitted:  

Output:     Summary statistics for linear regression and ANOVA and boxplot.

Example[m]: 'Regression:              
    b =

    8.2000
    2.2500


    bint =

    5.8417   10.5583
    1.1583    3.3417


    r =

   -1.4500
    0.5500
   -0.4500
    1.5500
   -3.4500
    0.5500
    1.5500
   -0.4500
    0.5500
    2.5500
   -2.7000
    2.3000
   -1.7000
    2.3000
    2.3000
    0.3000
   -5.7000
    2.3000
    0.3000
   -2.7000
    3.0500
   -0.9500
    2.0500
   -5.9500
   -0.9500
    2.0500
    1.0500
   -0.9500
    2.0500
    0.0500


    rint =

   -6.1756    3.2756
   -4.2051    5.3051
   -5.2067    4.3067
   -3.1706    6.2706
   -8.0116    1.1116
   -4.2051    5.3051
   -3.1706    6.2706
   -5.2067    4.3067
   -4.2051    5.3051
   -2.1026    7.2026
   -7.4708    2.0708
   -2.5033    7.1033
   -6.5419    3.1419
   -2.5033    7.1033
   -2.5033    7.1033
   -4.5867    5.1867
  -10.0410   -1.3590
   -2.5033    7.1033
   -4.5867    5.1867
   -7.4708    2.0708
   -1.5556    7.6556
   -5.6952    3.7952
   -2.6409    6.7409
  -10.0920   -1.8080
   -5.6952    3.7952
   -2.6409    6.7409
   -3.6920    5.7920
   -5.6952    3.7952
   -2.6409    6.7409
   -4.7100    4.8100


    stats =

    0.3890   17.8246    0.0002    5.6804


    p =

    0.0012


    table = 

    'Source'    'SS'          'df'    'MS'         'F'         'Prob>F'
    'Groups'    [102.6000]    [ 2]    [51.3000]    [8.7831]    [0.0012]
    'Error'     [157.7000]    [27]    [ 5.8407]          []          []
    'Total'     [260.3000]    [29]           []          []          []


    stats = 

    gnames: {3x1 cell}
         n: [10 10 10]
    source: 'anova1'
     means: [10.6000 12.4000 15.1000]
        df: 27
         s: 2.4168'

 Example[r]: 'Analysis of Variance Table

 anova(lm1)
 Analysis of Variance Table

 Response: y
           Df Sum Sq Mean Sq F value   Pr(>F)   
 x          2  102.6  51.300  8.7831 0.001153 **
 Residuals 27  157.7   5.841                    
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1


 summary(lm1)
 Call:
 lm(formula = y ~ x)

 Residuals:
    Min     1Q Median     3Q    Max 
   -6.1   -1.1    0.4    1.9    2.9 

 Coefficients:
           # Estimate Std. Error t value Pr(>|t|)    
 (Intercept)  10.6000     0.7642  13.870 8.44e-14 ***
 x2            1.8000     1.0808   1.665 0.107392    
 x3            4.5000     1.0808   4.164 0.000287 ***
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

 Residual standard error: 2.417 on 27 degrees of freedom
 Multiple R-squared:  0.3942, Adjusted R-squared:  0.3493 
 F-statistic: 8.783 on 2 and 27 DF,  p-value: 0.001153'
```

![Picture1](SMSanovapull.png)
![Picture2](SMSanovapull1.png)

```R
# clear variables and close windows
rm(list=ls(all=TRUE))
graphics.off()

y   = c(9,11,10,12,7,11,12,10,11,13,10,15,11,15,15,13,7,15,13,10,18,14,17,9,14,17,16,14,17,15)
x   = factor(rep(1:3,each=10))   # factor variable for 3 strategies and 30 observations
lm1 = lm(y~x)                    # linear model

anova(lm1)                       # anova table
summary(lm1)                     # regression summary

```

```Matlab

clear all
close all
clc

y   = [9,11,10,12,7,11,12,10,11,13,10,15,11,15,15,13,7,15,13,10,18,14,17,9,14,17,16,14,17,15]';
x   = [1*ones(10,1);2*ones(10,1);3*ones(10,1)]; % factor variable for the strategies
X   = [ones(30,1),x];                           % regression variable matrix
[b,bint,r,rint,stats] = regress(y,X)            % regression and summary
[p,table,stats]       = anova1(y,x)             % anova table

set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold');

```
