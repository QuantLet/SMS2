
```yamlExample[m]: 'a =

   Columns 1 through 5

     Source     d.f.    Sum Sq    Mean Sq    F
     origin     [   2]    [0.1487]    [ 0.0744]    [  4.6597]
     X Value    [   1]    [2.9897]    [ 2.9897]    [187.3642]
     Error      [  70]    [1.1170]    [ 0.0160]            []

   Column 6

     Prob>F
     [    0.0126]
     [1.7939e-21]
               []


 c =

     Term         Estimate    Std. Err.    T           Prob>|T|
     Intercept    [ 10.4910]    [   0.5398]    [ 19.4338]    [6.4343e-30]
       1          [  0.0702]    [   0.0267]    [  2.6316]    [    0.0104]
       2          [  0.0043]    [   0.0305]    [  0.1408]    [    0.8885]
       3          [ -0.0745]    [   0.0297]    [ -2.5084]    [    0.0144]
     Slope        [ -0.9411]    [   0.0688]    [-13.6881]    [1.7939e-21]


 s =

         source: aoctool
         gnames: {3x1 cell}
              n: [3x1 double]
             df: 70
              s: 0.1263
          model: 4
     intercepts: [3x1 double]
       intercov: [3x3 double]
            pmm: [3x1 double]
         pmmcov: [3x3 double]'

```

