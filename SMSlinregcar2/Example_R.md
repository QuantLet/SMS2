```yaml

Example[r]: 'linear model with origin
 summary(lm3<-lm(log(Mileage)~log(Weight)+Origin))

  Call:
 lm(formula = log(Mileage) ~ log(Weight) + Origin)

 Residuals:
      Min       1Q   Median       3Q      Max 
 -0.27642 -0.08388 -0.01317  0.04856  0.46870 

 Coefficients:
              Estimate Std. Error t value Pr(>|t|)    
 (Intercept)  10.56123    0.55568  19.006  < 2e-16 ***
 log(Weight)  -0.94108    0.06875 -13.688  < 2e-16 ***
 OriginJapan  -0.06591    0.04898  -1.346  0.18278    
 OriginEurope -0.14469    0.04752  -3.045  0.00328 ** 
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

 Residual standard error: 0.1263 on 70 degrees of freedom
 Multiple R-squared:  0.774,    Adjusted R-squared:  0.7643 
 F-statistic: 79.89 on 3 and 70 DF,  p-value: < 2.2e-16
 

 summary(lm3.int<-lm(log(Mileage)~(log(Weight)+Origin)^2))

 Call:
 lm(formula = log(Mileage) ~ (log(Weight) + Origin)^2)

 Residuals:
      Min       1Q   Median       3Q      Max 
 -0.24228 -0.08267 -0.01660  0.05127  0.45775 

 Coefficients:
                          Estimate Std. Error t value Pr(>|t|)    
 (Intercept)              10.21992    0.61465  16.627   <2e-16 ***
 log(Weight)              -0.89883    0.07606 -11.818   <2e-16 ***
 OriginJapan               3.67677    2.40542   1.529    0.131    
 OriginEurope              0.83818    1.55118   0.540    0.591    
 log(Weight):OriginJapan  -0.48341    0.31103  -1.554    0.125    
 log(Weight):OriginEurope -0.12500    0.19876  -0.629    0.532    
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

 Residual standard error: 0.1257 on 68 degrees of freedom
 Multiple R-squared:  0.7824,   Adjusted R-squared:  0.7664 
 F-statistic: 48.91 on 5 and 68 DF,  p-value: < 2.2e-16


 anova(lm3,lm3.int)

 Analysis of Variance Table

 Model 1: log(Mileage) ~ log(Weight) + Origin
 Model 2: log(Mileage) ~ (log(Weight) + Origin)^2
   Res.Df   RSS Df Sum of Sq      F Pr(>F)
 1     70 1.117                           
 2     68 1.075  2  0.041917 1.3257 0.2724'
 
 ```
 ![Picture1](SMSlinregcar2_r.png)
 
