```yaml

Example[m]: ' lm3 = 
 
 
 Linear regression model:
     y ~ 1 + x1 + x2
 
 Estimated Coefficients:
                    Estimate    SE          tStat      pValue    
     (Intercept)      10.658     0.53695     19.849     1.085e-30
     x1             -0.94407    0.064924    -14.541    5.5883e-23
     x2             -0.07195    0.023431    -3.0708     0.0030248
 
 
 Number of observations: 74, Error degrees of freedom: 71
 Root Mean Squared Error: 0.125
 R-squared: 0.774,  Adjusted R-Squared 0.768
 F-statistic vs. constant model: 122, p-value = 1.2e-23


 
 lm3int = 
 
 
 Generalized Linear regression model:
     y ~ 1 + x1*x2
     Distribution = Normal
 
 Estimated Coefficients:
                    Estimate    SE          tStat      pValue    
     (Intercept)       10.22     0.61465     16.627    1.1828e-25
     x1             -0.89883    0.076055    -11.818    3.8193e-18
     x1:x2_2        -0.48341     0.31103    -1.5542       0.12477
     x1:x2_3          -0.125     0.19876    -0.6289       0.53152
     x2_2             3.6768      2.4054     1.5285       0.13102
     x2_3            0.83818      1.5512    0.54035       0.59072
 
 
 74 observations, 68 error degrees of freedom
 Estimated Dispersion: 0.0158
 F-statistic vs. constant model: 48.9, p-value = 3.31e-21'

```
