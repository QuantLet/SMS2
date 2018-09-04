[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSdisfwais** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMSdisfwais

Published in: 'Multivariate Statistics: Exercises and Solutions'

Description: "computes Fisher's linear discrimination function for the wais data set. The apparent error rate (APER) and the actual error rate (AER) are computed. APER = 0.2449, AER = 0.3061."

Keywords: 'Fisher LDA, discriminant analysis, aper, discrimination, Fisher, LDA, aer'

See also: 'SMSdiscbaycar, SMSdisccar, SMSdisfbank, SMSdisfwais'

Author[r]: Zdenek Hlavka
Author[m]: Awdesch Melzer

Datafile[r]: wais.rda
Datafile[m]: wais.dat

Example: 'Calculates Fisher LDA for WAIS data.'
```

### R Code
```r

# Clear workspace
rm(list=ls(all=TRUE))
graphics.off()

# install and load packages
libraries = c("stats","MASS")
lapply(libraries, function(x) if (!(x %in% installed.packages())) {
    install.packages(x)})
lapply(libraries, library, quietly = TRUE, character.only = TRUE)

# setwd("C:/...") # please change the working directory
load("wais.rda")

fisher.w=lda(group~.-subject,prior=c(0.5,0.5),data=wais)
prediction=predict(fisher.w, wais)$class

t=table(wais$group,prediction)

print(t)
aper=(sum(t)-sum(diag(t)))/sum(t)
print(aper)

correct=0

for (i in 1:nrow(wais)) {
  fisher.t=lda(group~.-subject,prior=c(0.5,0.5),subset=-i,data=wais)
  predict=predict(fisher.t, wais[i,])$class
  if (predict==wais[i,"group"]) correct=correct+1
}

aer=1-correct/nrow(wais)
print(aer)

```

automatically created on 2018-09-04

### MATLAB Code
```matlab

clear all
close all
clc

%% Fisher's LDA for WAIS data

load('wais.dat')

mdl        = ClassificationDiscriminant.fit(wais(:,3:end),wais(:,1),'Prior','uniform');
% LDA model prediction
pred       = predict(mdl,wais(:,3:end));
% truth-prediction 
label      = wais(:,1);
[C,order]  = confusionmat(label,pred);

cols       = cellstr(strvcat('         ','         ','Prediction','         '));
rows       = cellstr(strvcat('         ','Truth     ','         '));
rows1      = cellstr(strvcat('         ',order));
cols1      = cellstr(strvcat(order(1,:), num2str(C(:,1))));
cols2      = cellstr(strvcat(order(2,:), num2str(C(:,2))));
table      = [rows, rows1, cols1, cols2];
table      = [cols'; table];
disp(table)

%% compute apparent error rate (APER)
aper       = (sum(sum(C))-sum(diag(C)))/sum(sum(C));
disp(aper)

%% compute actual error rate (AER)
correct=0;
for i = 1:size(wais,1)
    subset      = wais;
    subset(i,:) = [];
    mdl         = ClassificationDiscriminant.fit(subset(:,3:end),subset(:,1),'Prior','uniform');
    pred        = predict(mdl,wais(i,3:end));
    if (pred==wais(i,1))
        correct=correct+1;
    end
end


aer  = 1-correct/size(wais,1);
disp(aer)

```

automatically created on 2018-09-04