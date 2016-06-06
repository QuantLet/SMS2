```yaml

Example[r]: ' Model with constant and 1 regressor
 Call:
 lm(formula = Sales ~ Price, data = pullover)

 Residuals:
     Min      1Q  Median      3Q     Max 
 -70.095  -8.898   2.036   9.805  64.725 

 Coefficients:
             Estimate Std. Error t value Pr(>|t|)  
 (Intercept) 210.7736    79.9837   2.635   0.0299 *
 Price        -0.3640     0.7571  -0.481   0.6435  
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

 Residual standard error: 35.5 on 8 degrees of freedom
 Multiple R-squared:  0.02808,  Adjusted R-squared:  -0.09341 
 F-statistic: 0.2311 on 1 and 8 DF,  p-value: 0.6435
 
 R-squared: One explanatory variable:
     0.02808172
 
 Model with constant and 2 regressors
 Call:
 lm(formula = Sales ~ Price + Advertisement, data = pullover)

 Residuals:
     Min      1Q  Median      3Q     Max 
 -12.836  -9.023  -5.423   2.817  32.684 

 Coefficients:
                Estimate Std. Error t value Pr(>|t|)    
 (Intercept)   176.69193   36.50781   4.840 0.001878 ** 
 Price          -0.60125    0.34343  -1.751 0.123462    
 Advertisement   0.56634    0.09941   5.697 0.000737 ***
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

 Residual standard error: 15.98 on 7 degrees of freedom
 Multiple R-squared:  0.8276, Adjusted R-squared:  0.7783 
 F-statistic:  16.8 on 2 and 7 DF,  p-value: 0.002128
 
 R-squared: Two explanatory variables:
     0.8275805
 
 Model with constant and 3 regressors
 Call:
 lm(formula = Sales ~ Price + Advertisement + Hours, data = pullover)

 Residuals:
     Min      1Q  Median      3Q     Max 
 -13.369  -9.406   1.599   5.151  19.729 

 Coefficients:
               Estimate Std. Error t value Pr(>|t|)   
 (Intercept)   65.66956   57.12507   1.150  0.29407   
 Price         -0.21578    0.32194  -0.670  0.52764   
 Advertisement  0.48519    0.08678   5.591  0.00139 **
 Hours          0.84373    0.37400   2.256  0.06491 . 
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

 Residual standard error: 12.7 on 6 degrees of freedom
 Multiple R-squared:  0.9067, Adjusted R-squared:  0.8601 
 F-statistic: 19.44 on 3 and 6 DF,  p-value: 0.001713 

 R-squared: Three explanatory variables:
     0.9067102'


```
