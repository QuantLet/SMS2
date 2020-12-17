rm(list=ls())
graphics.off()
# install.packages("mvtnorm")
library(mvtnorm)
n      = 100
rho    = 0.9
mean_x = c(0,0)
mean_y = c(4,0)

sigma  = matrix(c(1,rho,rho,1), nrow = 2, ncol = 2)
x      = rmvnorm(n=n, mean = mean_x, sigma = sigma)
y      = rmvnorm(n=n, mean = mean_y, sigma = sigma)
xy     = rbind(x,y) # defined for computing xlim and ylim

plot(x, col='blue', pch = 19, ylim = c(round(min(xy[,2]))-1,round(max(xy[,2]))+1),
     xlim = c(round(min(xy[,1]))-1,round(max(xy[,1]))+1),
     xlab = 'x1, y1', ylab = 'x2, y2')
points(y,col = 'red', pch = 19)
