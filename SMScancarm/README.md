[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMScancarm** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMScancarm

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'Estimates the canonical variables for a subset of variables of the car marks data set: X - price, Y - economy, handling. A scatterplot of the first 2 canonical variables are presented. The relationship between the two canonical variables is moderate.'

Keywords: 'canonical correlation, covariance, eigenvalue, eigenvector, singular value decomposition, canonical vector, canonical variable'

See also: 'SMScancarm, SMScancarm1, SMScancarm2'

Author[r]: Zdenek Hlavka
Author[m]: Awdesch Melzer

Datafile[r]: carmean2.rda
Datafile[m]: carmean2.dat

Example: 'Canonical correlation for car data'

```

![Picture1](SMScancarm_m.png)

![Picture2](SMScancarm_r.png)

### R Code
```r

# Clear workspace
graphics.off()
rm(list=ls(all=TRUE))

# setwd("C:/...") # change working directory
load("carmean2.rda")

x = as.matrix(carmean2[,c(4,1,8)]);  # reorder: price econ easy
xrows = c("audi","bmw","citroen","ferrari",
            "fiat","ford","hyundai","jaguar",
            "lada","mazda","mercedes","mitsubishi",
            "nissan","opel_corsa","opel_vectra",
            "peugeot","renault","rover","toyota",
            "trabant","vw_golf","vw_passat","wartburg"
            );
s    = cov(x);                  # covariance 
sa   = s[1,1];                  # variance of price
sb   = s[2:3,2:3];              # covariance of rest
temp = eigen(sa);               # spectral decomposition 
ea   = temp$values;
va   = temp$vectors;
temp = eigen(sb);               # spectral decomposition 
eb   = temp$values;
vb   = temp$vectors;
sa2  = as.matrix( va %*% (1/sqrt(ea)) %*% t(va));      # sa^(-1/2) - diag() doesn't work well for 1x1 "matrix"
sb2  = vb %*% diag(1/sqrt(eb)) %*% t(vb);  # sb^(-1/2)
k    = sa2 %*% s[1,2:3] %*% sb2;           # matrix k
temp = svd(t(k));                # singular value decomposition
l    = temp$d;
d    = -temp$u;
g    = -temp$v;
a    = sa2 %*% g;                # canonical vectors a
b    = sb2 %*% d;                # canonical vectors b
print("first pair of canonical vectors")
print(a[,1])
print(b[,1])
eta    = x[,1] %*% as.matrix(a[,1]);    # first canonical variable eta 
phi    = x[,2:3] %*% b[,1];             # first canonical variable phi 
etaphi = cbind(eta,phi);
plot(etaphi,type = "n", main = "subset of car marks", xlab = expression(eta), ylab = expression(varphi));
text(etaphi,xrows,xpd=NA);              # adding labels to points
```

automatically created on 2018-05-28

### MATLAB Code
```matlab

clear all
close all
clc

[type, economy, service, value, price, design, sporty, safety, handling] = textread('carmean2.dat','%s %f %f %f %f %f %f %f %f');
cars       = horzcat(economy, service, value, price, design, sporty, safety, handling); % Horizontal concatenation, creates data matrix
names      = strvcat('economy', 'service', 'value', 'price', 'design', 'sporty', 'safety', 'handling');
names      = cellstr(names);
names      = names([4, 1, 8]);  % reorder: price value econ serv design sport safe handling
x          = cars(:,[4, 1, 8]);
labels     = strvcat('audi','bmw','citroen','ferrari',...
            'fiat','ford','hyundai','jaguar',...
            'lada','mazda','mercedes','mitsubishi',...
            'nissan','opel corsa','opel vectra',...
            'peugeot','renault','rover','toyota',...
            'trabant','vw golf','vw passat','wartburg');
labels     = cellstr(labels);
s          = cov(x);             % covariance
s
sa         = s(1,1);         % covariance of price & value
sb         = s(2:3,2:3);         % covariance of rest
[va ea]    = eig(sa);            % spectral decomposition
ea         = diag(ea);
[ea, ind]  = sort(ea,'descend');
va         = va(:,ind);
[vb eb]    = eig(sb);% spectral decomposition
eb         = diag(eb);
[eb, ind]  = sort(eb,'descend');
vb         = vb(:,ind);
sa2        = va * diag(1./sqrt((ea))) * va';  % sa^(-1/2)
sb2        = vb * diag(1./sqrt((eb))) * vb';  % sb^(-1/2)
k          = sa2 * s(1,2:3) * sb2;           % matrix k
[g l d]    = svd(k,'econ');      % singular value decomposition
a          = sa2 * g;            % canonical vectors a
b          = sb2 * d;            % canonical vectors b
disp('first pair of canonical vectors')
disp(a(:,1))
disp(b(:,1))
eta        = x(:,1) * a(:,1);  % canonical variable eta 
phi        = x(:,2:3) * b(:,1);  % canonical variable phi 

plot(eta,phi, 'w')
title('subset of car marks','FontSize',16,'FontWeight','Bold')
xlabel('\eta','FontSize',16,'FontWeight','Bold')
ylabel('\phi','FontSize',16,'FontWeight','Bold')
text(eta,phi,labels,'FontSize',16,'FontWeight','Bold')
box on
set(gca,'LineWidth',1.6,'FontSize',16,'FontWeight','Bold')
xlim([min(eta)-0.25,max(eta)+0.5])
ylim([min(phi-0.25),max(phi)+0.25])
```

automatically created on 2018-05-28