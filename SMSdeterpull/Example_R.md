```yaml


 Example[r]: ' lm1    = lm(Sales~Price+Advertisement,data=pullover)
 anova(lm1)   analysis of variance for lm1
 Analysis of Variance Table

 Response: Sales
               Df Sum Sq Mean Sq F value    Pr(>F)    
 Price          1  291.3   291.3  1.1401 0.3210690    
 Advertisement  1 8292.5  8292.5 32.4586 0.0007374 ***
 Residuals      7 1788.4   255.5                      
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
 summary(lm1) summary statistics for lm1

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
 Multiple R-squared:  0.8276,   Adjusted R-squared:  0.7783 
 F-statistic:  16.8 on 2 and 7 DF,  p-value: 0.002128


 lm2    = lm(Sales~Price+Hours,data=pullover)
 anova(lm2)   anova table for lm2
 Analysis of Variance Table

 Response: Sales
           Df Sum Sq Mean Sq F value  Pr(>F)  
 Price      1  291.3   291.3  0.3393 0.57848  
 Hours      1 4072.6  4072.6  4.7448 0.06581 .
 Residuals  7 6008.3   858.3                  
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
 summary(lm2) summary stat for lm2

 Call:
 lm(formula = Sales ~ Price + Hours, data = pullover)

 Residuals:
    Min     1Q Median     3Q    Max 
 -60.88 -12.30   8.92  16.91  24.19 

 Coefficients:
             Estimate Std. Error t value Pr(>|t|)  
 (Intercept) -24.1914   126.4642  -0.191   0.8537  
 Price         0.3485     0.7053   0.494   0.6363  
 Hours         1.7104     0.7852   2.178   0.0658 .
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

 Residual standard error: 29.3 on 7 degrees of freedom
 Multiple R-squared:  0.4207,   Adjusted R-squared:  0.2552 
 F-statistic: 2.542 on 2 and 7 DF,  p-value: 0.1479'


```
