[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSdisfbank** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMSdisfbank

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'Computes Fisher''s linear discrimination
               function (LDA) either for the 20 bank notes from Exercise 12.6 or
               for a random set of banknotes. The discrimination function
               is then applied to the the entire bank data set. With the 
               linear discrimination function based on the 20 bank notes 
               from Ex. 12.6 only 6 bank notes out of the entire 200 
               are misclassified, which leads to an error rate of 3 percent.'

Keywords: 'Fisher LDA, discriminant analysis, aper, discrimination, Fisher, LDA'

See also: 'SMSdiscbaycar, SMSdisccar, SMSdisfbank, SMSdisfwais'

Author[r]: Zdenek Hlavka
Author[m]: Awdesch Melzer

Datafile[r]: bank2.rda
Datafile[m]: bank2.dat

Example: 'Calculates Fisher LDA Swiss bank notes data.'

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
load("bank2.rda")

keep       = sample(1:200,20,replace=FALSE)
                                        # 20 randomly selected Swiss bank notes
#keep=c(7,8,16,39,71,73,89,94,94,100,110,121,129,131,149,150,154,161,163,174)
                                        # uncomment for 20 banknotes in the book
bank       = bank2[keep,]                   
truth      = factor(rep(c("Genuine","Forged"),each=100))
group      = truth[keep]

fisher     = lda(bank,grouping=group)
prediction = predict(fisher, bank2)$class

table(truth,prediction)
```

automatically created on 2018-05-28

### MATLAB Code
```matlab

clear all
close all
clc

%% load data and take sample
load('bank2.dat')

% set pseudo random numbers
RandStream.setGlobalStream(RandStream('mt19937ar','seed',9));

% sample n=20 out of the data set
bank2      = [(1:200)',bank2];    % set index variable
n          = 20;                  % sample size
keep       = datasample(bank2,n); % 20 randomly selected Swiss bank notes

label      = [];
for k = 1:200
    if k<=100
        label = [label; 'Genuine  '];
    else
        label = [label; 'Forged   '];
    end
end

% uncomment for 20 banknotes as in the book
 % keep  = [7,8,16,39,71,73,89,94,94,100,110,121,129,131,149,150,154,161,163,174]';

%% compute Fisher's LDA with training sample
test_ind   = keep(:,1);
truth      = [ones(100,1);zeros(100,1)];
group      = truth(keep(:,1));

% LDA classifier
mdl        = ClassificationDiscriminant.fit(bank2(test_ind,2:end),label(test_ind,:));
% LDA model prediction
pred       = predict(mdl,bank2(:,2:end));
% truth-prediction 
[C,order]  = confusionmat(label,pred);

%% create table of true vs predicted observations
cols       = cellstr(strvcat('         ','         ','Prediction','         '));
rows       = cellstr(strvcat('         ','Truth     ','         '));
rows1      = cellstr(strvcat('         ',order));
cols1      = cellstr(strvcat(order(1,:), num2str(C(:,1))));
cols2      = cellstr(strvcat(order(2,:), num2str(C(:,2))));
table      = [rows, rows1, cols1, cols2];
table      = [cols'; table];
disp(table)
```

automatically created on 2018-05-28