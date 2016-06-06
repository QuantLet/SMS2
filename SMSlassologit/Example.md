```yaml

Example[r]: ' general linear model: logit
 summary(glm(y~.,data=data,family="binomial"))

 Call:
 glm(formula = y ~ ., family = "binomial", data = data)

 Deviance Residuals: 
        Min          1Q      Median          3Q         Max  
 -8.474e-05  -2.100e-08  -2.100e-08   2.100e-08   7.724e-05  

 Coefficients:
               Estimate Std. Error z value Pr(>|z|)
 (Intercept) -3.096e+03  6.945e+05  -0.004    0.996
 M            4.345e+00  2.672e+03   0.002    0.999
 R78         -4.130e+01  2.797e+04  -0.001    0.999
 R77         -6.459e+01  1.931e+04  -0.003    0.997
 H           -7.873e+01  3.137e+04  -0.003    0.998
 R            1.984e+01  6.233e+03   0.003    0.997
 Tr           3.189e+01  7.654e+03   0.004    0.997
 W            4.676e-01  1.032e+02   0.005    0.996
 L            5.869e+00  1.856e+03   0.003    0.997
 T           -7.746e+01  1.682e+04  -0.005    0.996
 D            4.247e+00  9.827e+02   0.004    0.997
 G            8.347e+02  1.820e+05   0.005    0.996
 C.US        -5.036e+02  1.673e+05  -0.003    0.998
 C.EU        -7.663e+01  1.147e+05  -0.001    0.999

 (Dispersion parameter for binomial family taken to be 1)

     Null deviance: 8.2565e+01  on 65  degrees of freedom
 Residual deviance: 4.5089e-08  on 52  degrees of freedom
 AIC: 28

 Number of Fisher Scoring iterations: 25

 Warning messages:
 1: glm.fit: algorithm did not converge 
 2: glm.fit: fitted probabilities numerically 0 or 1 occurred


 summary(glm(y~M+H+R+W+D+C.US+C.EU,family="binomial",data=data))

 Call:
 glm(formula = y ~ M + H + R + W + D + C.US + C.EU, family = "binomial", 
     data = data)

 Deviance Residuals: 
      Min        1Q    Median        3Q       Max  
 -2.11530  -0.30626  -0.05618   0.12592   2.02607  

 Coefficients:
               Estimate Std. Error z value Pr(>|z|)   
 (Intercept) -20.588580   8.986429  -2.291  0.02196 * 
 M            -0.037045   0.133031  -0.278  0.78065   
 H            -0.958662   0.913593  -1.049  0.29403   
 R             0.213218   0.239461   0.890  0.37325   
 W             0.006820   0.003194   2.135  0.03273 * 
 D             0.006069   0.015697   0.387  0.69902   
 C.US         -9.225817   3.143921  -2.934  0.00334 **
 C.EU          3.710133   2.067920   1.794  0.07279 . 
 ---
 Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

 (Dispersion parameter for binomial family taken to be 1)

     Null deviance: 82.565  on 65  degrees of freedom
 Residual deviance: 31.073  on 58  degrees of freedom
 AIC: 47.073

 Number of Fisher Scoring iterations: 7'
 
 ```
 
 ![Picture1](SMSlassologit.png)
