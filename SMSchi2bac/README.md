[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSchi2bac** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMSchi2bac

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'Performs a test of independence for French baccalaurent data'

Keywords: 'testing, chisquare, asymptotic chisquare test, independence, test'

See also: 'SMScorrcarm, SMSchi2bac, SMScorrcrime, SMScorrhealth, SMScorrfood'

Author[r]: Zdenek Hlavka
Author[m]: Awdesch Melzer

Datafile[r]: bac.rda
Datafile[m]: bac.dat

Example: 'Test of independence for French baccalaurent data.'
```

### R Code
```r

# clear memory and close windows
rm(list=ls(all=TRUE))
graphics.off()

load("bac.rda")
chisq.test(bac)
```

automatically created on 2018-05-28

### MATLAB Code
```matlab

% clear memory and close windows
clear all
close all
clc

% SMSchi2bac
% test of independence for french baccalaureat data
[type, A, B, C, D, E, F, G, H] = textread('bac.dat','%s %f %f %f %f %f %f %f %f');
bac                            = [A, B, C, D, E, F, G, H];
[hNull pValue X2]              = chi2test(bac,0.05)
```

automatically created on 2018-05-28