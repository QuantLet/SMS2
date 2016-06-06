```yaml


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


```
