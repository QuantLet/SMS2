[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSdecobank** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml


Name of Quantlet: SMSdecobank

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'Performs the factorial analysis for Swiss bank notes data set by first, standardizing the data and then employing singular value decomposition.'

Keywords: analysis, dimension reduction, eigenvalues, eigenvectors, empirical, factorial, factorial decomposition, graphical representation, plot, scale, scaling, singular value, spectral decomposition, standardization, standardize, svd, transformation, visualization

See also: 'SMSdecotime, SMSdecobank, SMSdecofood'

Author[r]: Awdesch Melzer
Author[m]: Awdesch Melzer

Datafile[r]: bank2.rda
Datafile[m]: bank2.dat

Example: 'Visualization of variables and individuals after dimension reduction.'
```

![Picture1](SMSdecobank01_m.png)

![Picture2](SMSdecobank01_r.png)

![Picture3](SMSdecobank02_m.png)

![Picture4](SMSdecobank02_r.png)

![Picture5](SMSdecobank03_m.png)

![Picture6](SMSdecobank03_r.png)

### R Code
```r

rm(list=ls(all=TRUE))
graphics.off()

# install and load packages
libraries = c("scatterplot3d")
lapply(libraries, function(x) if (!(x %in% installed.packages())) {
  install.packages(x)
})
lapply(libraries, library, quietly = TRUE, character.only = TRUE)

# setwd("C:/...") # set working directory
# load data
load("bank2.rda")

x       = as.matrix(bank2)
x       = scale(x)
x       = x/sqrt(nrow(bank2))
deco    = svd(x)
w       = deco$v[,1:3]%*%diag(deco$d[1:3])
z       = deco$u[,1:3]%*%diag(deco$d[1:3])
counter = rep(c("G","F"),each=100)
xs      = expression(X[1],X[2],X[3],X[4],X[5],X[6])

opar=par(mfrow=c(2,2))
plot(w[,c(1,2)],type="n",xlab=expression(w[1]),ylab=expression(w[2]),xlim=c(-1.2,1.2),ylim=c(-1,1))
text(w[,c(1,2)],xs)
frame()
plot(w[,c(1,3)],type="n",xlab=expression(w[1]),ylab=expression(w[3]),xlim=c(-1.2,1.2),ylim=c(-1,1))
text(w[,c(1,3)],xs)
plot(w[,c(2,3)],type="n",xlab=expression(w[2]),ylab=expression(w[3]),xlim=c(-1.2,1.2),ylim=c(-1,1))
text(w[,c(2,3)],xs)
dev.new()
par(mfrow=c(2,2))
plot(z[,c(1,2)],type="n",xlab=expression(z[1]),ylab=expression(z[2]))
text(z[,c(1,2)],counter)
frame()
plot(z[,c(1,3)],type="n",xlab=expression(z[1]),ylab=expression(z[3]))
text(z[,c(1,3)],counter)
plot(z[,c(2,3)],type="n",xlab=expression(z[2]),ylab=expression(z[3]))
text(z[,c(2,3)],counter)
dev.new()
par(mfrow=c(1,1))
scatterplot3d(z,color=rep(1:2,each=100),xlab=expression(z[1]),ylab="",zlab=expression(z[3]))
par(opar)

```

automatically created on 2018-05-28

### MATLAB Code
```matlab


clear all
close all
clc

% load data
x        = load('bank2.dat');
[m,n]    = size(x);
xmeanm   = repmat((mean(x))',1,m);
stdvec   = sqrt((m-1)/m)*repmat(std(x)',1,m);

% transformation
x        = (x'-xmeanm)./stdvec;
x        = x'/sqrt(m);

% singular value decomposition
[U,S,V]  = svd(x);

% coordinates
w        = V(:,1:3)*S(1:3,1:3);
z        = U(:,1:3)*S(1:3,1:3);

% labels
a        = strvcat('Length','Height Left','Height Right','Inner Frame Lower','Inner Frame Upper','Diagonal');
lab      = cellstr(a);
b        = strvcat([repmat('G',100,1);repmat('F',100,1)]);
label    = cellstr(b);

%plot variables
figure(1)
subplot(2,2,1);
plot(w(:,1),w(:,2),'d', 'Color', 'white')
axis([-1.01 1.01  -1.01 1.01]);
xlabel('W_1','FontSize',16,'FontWeight','bold')
ylabel('W_2','FontSize',16,'FontWeight','bold')
title('Swiss bank variables','FontSize',16,'FontWeight','Bold')
for i=1:n
text(w(i,1)-0.2,w(i,2),lab(i),'FontSize',18, 'Color', 'blue')
end
set(gca,'FontSize',16,'LineWidth',2,'FontWeight','bold')

subplot(2,2,3);
plot(w(:,1),w(:,3),'d', 'Color', 'white')
axis([-1.01 1.01  -1.01 1.01]);
xlabel('W_1','FontSize',16,'FontWeight','bold')
ylabel('W_3','FontSize',16,'FontWeight','bold')
title('Swiss bank variables','FontSize',16,'FontWeight','Bold')
for i=1:n
text(w(i,1)-0.2,w(i,3),lab(i),'FontSize',18, 'Color', 'blue')
end
set(gca,'FontSize',16,'LineWidth',2,'FontWeight','bold')

subplot(2,2,4);
plot(w(:,2),w(:,3),'d', 'Color', 'white')
axis([-1.01 1.01  -1.01 1.01]);
xlabel('W_2','FontSize',16,'FontWeight','bold')
ylabel('W_3','FontSize',16,'FontWeight','bold')
title('Swiss bank variables','FontSize',16,'FontWeight','Bold')
for i=1:n
text(w(i,2)-0.2,w(i,3),lab(i),'FontSize',18, 'Color', 'blue')
end
set(gca,'FontSize',16,'LineWidth',2,'FontWeight','bold')

%plot bank notes
figure(2)
subplot(2,2,1);
plot(z(:,1),z(:,2),'d', 'Color', 'white')
axis([-0.25 0.25  -0.25 0.25]);
xlabel('Z_1','FontSize',16,'FontWeight','bold')
ylabel('Z_2','FontSize',16,'FontWeight','bold')
title('Swiss bank notes','FontSize',16,'FontWeight','Bold')
for i=1:m
text(z(i,1),z(i,2),label(i),'FontSize',18, 'Color', 'blue')
end
set(gca,'FontSize',16,'LineWidth',2,'FontWeight','bold')

subplot(2,2,3);
plot(z(:,1),z(:,3),'d', 'Color', 'white')
axis([-0.25 0.25  -0.25 0.25]);
xlabel('Z_1','FontSize',16,'FontWeight','bold')
ylabel('Z_3','FontSize',16,'FontWeight','bold')
title('Swiss bank notes','FontSize',16,'FontWeight','Bold')
for i=1:m
text(z(i,1),z(i,3),label(i),'FontSize',18, 'Color', 'blue')
end
set(gca,'FontSize',16,'LineWidth',2,'FontWeight','bold')

subplot(2,2,4);
plot(z(:,2),z(:,3),'d', 'Color', 'white')
axis([-0.25 0.25  -0.25 0.25]);
xlabel('Z_2','FontSize',16,'FontWeight','bold')
ylabel('Z_3','FontSize',16,'FontWeight','bold')
title('Swiss bank notes','FontSize',16,'FontWeight','Bold')
for i=1:m
text(z(i,2),z(i,3),label(i),'FontSize',18, 'Color', 'blue')
end
set(gca,'FontSize',16,'LineWidth',2,'FontWeight','bold')

% 3d scatter
figure(3)
plot3(z(:,1),z(:,2),z(:,3),'wo')
for i=1:100
text(z(i,1),z(i,2),z(i,3),label(i),'FontSize',18, 'Color', 'black')
end
for i=101:200
text(z(i,1),z(i,2),z(i,3),label(i),'FontSize',18, 'Color', 'red')
end
xlabel('Z_1','FontSize',16,'FontWeight','bold')
ylabel('Z_2','FontSize',16,'FontWeight','bold')
zlabel('Z_3','FontSize',16,'FontWeight','bold')
set(gca,'FontSize',16,'LineWidth',2,'FontWeight','bold')

```

automatically created on 2018-05-28