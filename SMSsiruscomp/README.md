[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSsiruscomp** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SMSsiruscomp

Published in: Multivariate Statistics: Exercises and Solutions

Description: 'Applies the sliced inverse regression algorithm (SIR) to US company data for dimension reduction.'

Keywords: 'sliced inverse regression, sir, EDR-directions, effective dimension reduction directions, eigenvalue'

See also: 'SMScartdiag, SMScartsq, SMSdisfbank2, SMSeppbank, SMSsimpdbank, SMSsimpdsimu, SMSsir2cars, SMSsir2simu, SMSsircars, SMSsirsimu, SMSsircars, SMSsirsimu, SMSsiruscomp, SMSsvmbankrupt, SMSsvmorange, SMSsvmspiral'

Author: Awdesch Melzer

Datafile: uscomp.rda

Example: 'Effective dimension reduction directions (EDR-directions) for the US company data and plots for the response versus the estimated EDR-directions, a three-dimensional plot for the first two directions and the response and plot for the eigenvalues and the cumulative sum.'
```

![Picture1](SMSsiruscomp_r.png)

### R Code
```r

rm(list=ls(all=TRUE))
graphics.off()

## subroutine SIR

sir = function(x, y, h){            
# -----------------------------------------------------------------
#   Quantlet:    sir
# -----------------------------------------------------------------
#   Keywords:    sliced inverse regression, dimension reduction 
# -----------------------------------------------------------------
#   Description: Calculates the effective dimension-reduction (edr)  
#                directions by Sliced Inverse Regression (Li, 1991)
# -----------------------------------------------------------------
#   Reference:   Li (1991), "Sliced inverse regression, 
#                Journal of the American Statistical Association, 86, 316-342
# -----------------------------------------------------------------
#   Usage        sir (x, y, h)
#   Input
#     Parameter  x
#     Definition n x p matrix, the explonatory variable
#     Parameter  y
#     Definition n vector, the dependent variable
#     Parameter  h
#     Definition scalar, number of slices (h>=2)
#                        width of slice (0 < h < 1)
#                        elements in a slice (-h)
#   Output
#     Parameter  edr
#     Definition p x p matrix containing estimates of the edr
#     Parameter  eigsv
#     Definition p vector of the eigsvvalues
# -----------------------------------------------------------------
#   Author:     R: Awdesch Melzer 20130205
# -----------------------------------------------------------------

  n    = nrow(x)              # number of observations                 
  ndim = ncol(x)              # number of dimension
  if(-h > n){
    stop ("Number of slice elements can't exceed number of data")
  }
  x    = as.matrix(x)
# calculate the covariance matrix and its inverse root to standardize X
# step 1 in original article

  xb   = apply(x,2,mean)                 # mean of x                       
  s    = (t(x)%*%x - n*xb%*%t(xb))/(n-1) # cov of x                        
  E    = eigen(s)                        # eigsvdecomposititon of cov   
  eval = E$values
  evec = E$vectors
  #Adjust second Eigenvector
  if (any(evec[,1]<0)){
    evec=evec*(-1);
  }
  
  si2  = evec%*%diag(sqrt(1/eval))%*%t(evec)  # compute cov(x)^(-1/2)        
  xt   = (x-xb)%*%si2                         # stand. x to mean=0, cov=I    

# construct slices in Y space
#  step 2 in original article
 data  = cbind(y,xt)
 data  = data[order(data[,1]),]                     # sort data with respect to y   

# build slices 
#  ns     = number of slices 
#  condit = n values controlling which x-data fall
#           in a slice depending on choic
#  choice = vector of ns choices to build the slice subset of x 
# case 1: h<=-2  -> each slice with <= abs(h) elements                   
# if n div h != 0 then the first and last slice get the remainder        

  hold   = h
if (hold <= -2){ 
  h      = abs(hold)
  ns     = floor(n / h)
  condit = seq(1, n, 1)              # enumber the x values             
  choice = seq(1, ns, 1)*h           # take h values in each slice      
  if (h*ns != n){                    # if there are remaining values    
      hk = floor((n-h*ns)/2)
    if (hk>=0){
      choice = c(hk,choice+hk)       # generate a new first ...         
    }
      choice = c(choice,n)             # ... and last slice               
  }
  ns = length(choice)                # number of slices                 


# case 2: h>=2  -> take h slices with equal width                        
}else if(hold >= 2){
  ns        = hold
  slwidth   = (data[n,1] - data[1,1]) / ns    # width of slices          
              # compute higher value of all ns slices                    
  slend     = seq ((data[1,1]+slwidth), length=ns,by=slwidth)
  slend[ns] = data[n,1]             # avoids numerical problems        
  condit    = data[,1]              # choose on original y values      
  choice    = slend                 # choice to end of slice           


# case 3: 0<h<1  -> take slices with range in percent. of the y-range    

}else if((0<hold) &&(hold<=1)) {
  h  = hold
  ns = floor(1/h)                   # number of slices        

#   compute width of slices and vector of upper limit of slice intervals  

  slwidth = (data[n,1] - data[1,1]) * h
  slend   = seq(data[1,1]+slwidth, length=ns, by=slwidth)
  if (slend[ns] > data[n-1,1]){      # does only the last value            
    slend[ns] = data[n,1]           # lay behind the last slice ?         
  }else{
    slend = c(slend,data[n,1])         # if not, build another slice         
  }
  condit = data[,1]                 # choose on original y values  
  choice = slend                    # choice to end of slice              
  ns     = length(choice)             # compute the number of slices        
  if(h>0||h<=-2){
  stop("Error: h must not lay in (-2,0] !!")            
  }
}
if(ns==1){
  message("Warning: Only one slice is generated !")
}

#  run over all slices, compute estimate for V = Cov(E(x|y))            
#  step 3            
  hk   = 0
  v    = matrix(0,ndim, ndim)  # initialise V matrix                        
  ind  = matrix(1,n,1)         # index vector of length n# 0 means,         
                               #  this values was already choosen             
                               #  in a previous slice                         
  d    = ndim            
  ndim = ndim+1                # sorted x values are in data[,2:ndim]       
  j    = 1
  while (j <= ns){            
    sborder  = as.numeric(condit <= choice[j] & ind)   # sborder is index            
    p        = sum(sborder)                         # if jth obs. belongs         
    if (p != 0){                             # current slice               
      ind    = ind - sborder                 # don't take this values        
                                             # in further slices           
      xslice = data[which(sborder==1),2:ndim]   # get sliced x-values         
      xmean  = apply(xslice,2,mean)
      v      = v + xmean%*%t(xmean)*nrow(xslice)      # compute V                   
      hk     = hk+1
    }
    j = j+1
  }

if(sum(ind)!=0){
  message("Error: sum(ind) elements unused !!")
  }
  v          = (v+t(v))/2/n              # for numerical errors 
  ES         = eigen (v)                 # step 5, eigsvvectors of V 
  eigsv      = ES$values
  b          = ES$vectors
    #Adjust second Eigenvector
  #if (any(b[,1]<0)){
  #  b=b*(-1);
  #}
  b          = si2 %*% b                 # calculate e.d.r. direction 
  data       = sqrt(sum(b^2))            # ... and standardize them   
  edr        = b/data
  h          = cbind(eigsv,t(edr))
  h          = h[order(h[,1],decreasing=T),]  # sort eigsvvalues
  eigsv      = h[,1]                          # and e.d.r. directions
  edr        = t(h[,2:ncol(h)])

return(list(edr=edr, eigsv=eigsv) )
}

## main calculation

load("uscomp.rda")

x     = matrix(0,nrow(uscomp),ncol(uscomp))
for(i in 1:(ncol(uscomp)-1)){
x[,i] = as.numeric(as.character(uscomp[,i]))
}
x[65,2]=1601
x[,7] = as.numeric(uscomp[,7])
m     = x
# get rid of the outliers
keep = c(c(1:37),39,c(41:79))
#keep=1:79
x    = m[keep,c(1,2,4,5,6)]
y    = m[keep,3]
t    = rownames(uscomp)
n    = nrow(x)
x    = log(x-matrix(apply(x,2,min),nrow(x),ncol(x),byrow=T)+(matrix(apply(x,2,max),nrow(x),ncol(x),byrow=T)-matrix(apply(x,2,min),nrow(x),ncol(x),byrow=T))/200)
x    = (x-matrix(apply(x,2,mean),nrow(x),ncol(x),byrow=T))/sqrt(matrix(apply(x,2,var),nrow(x),ncol(x),byrow=T))


EDR   = sir(x,y,h=-11) #{f,g}
f     = EDR$edr
f[,1:3]     = t(t(f[,1:3])*sign(f[1,1]))
g     = EDR$eigsv
sg    = sum(g)
g     = g/sg
psi   = cumsum(g) # % explained by eigenvalue


i     = 1:length(g)
ig    = cbind(i,g)

p11   = cbind(as.matrix(x)%*%(f[,1]),y)

p12   = cbind(as.matrix(x)%*%(f[,2]),y)

p21   = cbind(as.matrix(x)%*%(f[,3]),y)

par(mfrow=c(2,2))
plot(p11, type="n", xlab="1st projection", ylab="market value")
points(p11,pch=19,cex=0.7,col="blue3")

plot(p12, type="n", xlab="2nd projection", ylab="market value")
points(p12,pch=19,cex=0.7,col="blue3")

plot(p21, type="n", xlab="3rd projection", ylab="market value")
points(p21,pch=19,cex=0.7,col="blue3")

plot(ig, type="n", xlab="k",ylab="",ylim=c(0,1))
title("SIR scree plot")
points(ig, pch="*",col="black",cex=1)
points(cbind(i,psi),pch=1,col="black",cex=1)

print("eigenvectors")
f
print("eigenvalues and proportions")
cbind(g,cumsum(g))

```

automatically created on 2018-05-28