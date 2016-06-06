```yaml


Example[r]: '  reasonable model...
  summary(lm1<-lm(log(Mileage)~log(Weight)+log(Displacement)+Origin))

 Call:
 lm(formula = log(Mileage) ~ log(Weight) + log(Displacement) + 
     Origin)

 Residuals:
      Min       1Q   Median       3Q      Max 
 -0.27077 -0.08380 -0.00444  0.04649  0.46751 

 Coefficients:
                   Estimate Std. Error t value Pr(>|t|)    
 (Intercept)       10.21060    0.74575  13.692  < 2e-16 ***
 log(Weight)       -0.85981    0.13390  -6.421 1.46e-08 ***
 log(Displacement) -0.05688    0.08032  -0.708   0.4812    
 OriginJapan       -0.07518    0.05087  -1.478   0.1440    
 OriginEurope      -0.15620    0.05038  -3.100   0.0028 ** 
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

 Residual standard error: 0.1268 on 69 degrees of freedom
 Multiple R-squared:  0.7756,	Adjusted R-squared:  0.7626 
 F-statistic: 59.62 on 4 and 69 DF,  p-value: < 2.2e-16


 Analysis of Variance Table

 Model 1: log(Mileage) ~ log(Weight) + log(Displacement) + Origin
 Model 2: log(Mileage) ~ log(Weight) + log(Displacement)
   Res.Df    RSS Df Sum of Sq      F  Pr(>F)  
 1     69 1.1089                              
 2     71 1.2638 -2  -0.15494 4.8207 0.01097 *
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1


  the outlier:
 carc[71,]
                  Mileage Weight Displacement Origin Price
 VW_Rabbit_Diesel      41   2040           90 Europe  5397


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
 Multiple R-squared:  0.774,	Adjusted R-squared:  0.7643 
 F-statistic: 79.89 on 3 and 70 DF,  p-value: < 2.2e-16'

```

![Picture1](SMSlinregcar01_r.png)
![Picture1](SMSlinregcar02_r.png)
![Picture1](SMSlinregcar03_r.png)
![Picture1](SMSlinregcar04_r.png)
![Picture1](SMSlinregcar05_r.png)
