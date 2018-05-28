[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMSclus8psc** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet : SMSclus8psc

Published in : 'Multivariate Statistics: Exercises and Solutions'

Description : 'Employs the spectral clustering algorithm on 
an 8 points example'

Keywords : 'cluster-analysis, spectral, plot, graphical representation, 
eigenvalues, eigenvectors'

See also : 'SMSclus8p, SMSclus8pd, SMSclus8pd, SMSclusbank, SMSclusbank2, 
SMSclusbank3, SMScluscomp, SMScluscrime, SMScluscrimechi2, SMSclushealth'

Author : Awdesch Melzer, Simon Trimborn

Submitted : Thu, October 02 2014 by Awdesch Melzer

Example : 'The 8 points example; second smallest eigenvalue: 0.9 and 
corresponding eigenvector' 

```

![Picture1](SMSclus8psc.png)

### R Code
```r

# close windows, clear variables
rm(list = ls(all = TRUE))
graphics.off()

install.packages("kernlab")
library(kernlab)
install.packages("ellipse")
library(ellipse)


################################################################################
########################## manipulate subroutine specc #########################
#################### to return eigenvalues and eigenvectors ####################
################################################################################

setGeneric("specc",function(x, ...) standardGeneric("specc"))
setMethod("specc", signature(x = "formula"),
function(x, data = NULL, na.action = na.omit, ...)
{
    mt <- terms(x, data = data)
    if(attr(mt, "response") > 0) stop("response not allowed in formula")
    attr(mt, "intercept") <- 0
    cl <- match.call()
    mf <- match.call(expand.dots = FALSE)
    mf$formula <- mf$x
    mf$... <- NULL
    mf[[1]] <- as.name("model.frame")
    mf <- eval(mf, parent.frame())
    na.act <- attr(mf, "na.action")
    x <- model.matrix(mt, mf)
    res <- specc(x, ...)
   
    cl[[1]] <- as.name("specc")
     if(!is.null(na.act)) 
        n.action(res) <- na.action
    
   
    return(res)
  })


setMethod("specc",signature(x="matrix"),function(x, centers, kernel = "rbfdot", kpar = "automatic", nystrom.red = FALSE, nystrom.sample = dim(x)[1]/6, iterations = 200, mod.sample =  0.75, na.action = na.omit, ...)
{
  x <- na.action(x)
  rown <- rownames(x)
  x <- as.matrix(x)
  m <- nrow(x)
  if (missing(centers))
    stop("centers must be a number or a matrix")
  if (length(centers) == 1) {
    nc <-  centers
    if (m < centers)
      stop("more cluster centers than data points.")
  }
  else
    nc <- dim(centers)[2]

  
  if(is.character(kpar)) {
    kpar <- match.arg(kpar,c("automatic","local"))
   
    if(kpar == "automatic")
      {
        if (nystrom.red == TRUE)
          sam <- sample(1:m, floor(mod.sample*nystrom.sample))
        else
          sam <- sample(1:m, floor(mod.sample*m))

        sx <- unique(x[sam,])
        ns <- dim(sx)[1]
        dota <- rowSums(sx*sx)/2
        ktmp <- crossprod(t(sx))
        for (i in 1:ns)
          ktmp[i,]<- 2*(-ktmp[i,] + dota + rep(dota[i], ns))

  
        ## fix numerical prob.
        ktmp[ktmp<0] <- 0
        ktmp <- sqrt(ktmp)
        
        kmax <- max(ktmp)
        kmin <- min(ktmp + diag(rep(Inf,dim(ktmp)[1])))
        kmea <- mean(ktmp)
        lsmin <- log2(kmin)
        lsmax <- log2(kmax)
        midmax <- min(c(2*kmea, kmax))
        midmin <- max(c(kmea/2,kmin))
        rtmp <- c(seq(midmin,0.9*kmea,0.05*kmea), seq(kmea,midmax,0.08*kmea))
        if ((lsmax - (Re(log2(midmax))+0.5)) < 0.5) step <- (lsmax - (Re(log2(midmax))+0.5))
        else step <- 0.5
        if (((Re(log2(midmin))-0.5)-lsmin) < 0.5 ) stepm <-  ((Re(log2(midmin))-0.5) - lsmin)
        else stepm <- 0.5
        
        tmpsig <- c(2^(seq(lsmin,(Re(log2(midmin))-0.5), stepm)), rtmp, 2^(seq(Re(log2(midmax))+0.5, lsmax,step)))
        diss <- matrix(rep(Inf,length(tmpsig)*nc),ncol=nc)

        for (i in 1:length(tmpsig)){
          ka <- exp((-(ktmp^2))/(2*(tmpsig[i]^2)))
          diag(ka) <- 0
          
          d <- 1/sqrt(rowSums(ka))
     
          if(!any(d==Inf) && !any(is.na(d))&& (max(d)[1]-min(d)[1] < 10^4))
            {
              l <- d * ka %*% diag(d)
              xi <- eigen(l,symmetric=TRUE)$vectors[,1:nc]
              yi <- xi/sqrt(rowSums(xi^2))
              res <- kmeans(yi, centers, iterations)
              diss[i,] <- res$withinss
            }
        }

        ms <- which.min(rowSums(diss))
        kernel <- rbfdot((tmpsig[ms]^(-2))/2)

        ## Compute Affinity Matrix
        if (nystrom.red == FALSE)
          km <- kernelMatrix(kernel, x)
      }
    if (kpar=="local")
      {
        if (nystrom.red == TRUE)
          stop ("Local Scaling not supported for nystrom reduction.")
        s <- rep(0,m)
        dota <- rowSums(x*x)/2
        dis <- crossprod(t(x))
        for (i in 1:m)
          dis[i,]<- 2*(-dis[i,] + dota + rep(dota[i],m))
        
        ## fix numerical prob.
        dis[dis < 0] <- 0
        
        for (i in 1:m)
          s[i] <- median(sort(sqrt(dis[i,]))[1:5])
        
        ## Compute Affinity Matrix
        km <- exp(-dis / s%*%t(s))
        kernel <- "Localy scaled RBF kernel"


      }
  }
    else 
      {
        if(!is(kernel,"kernel"))
          {
            if(is(kernel,"function")) kernel <- deparse(substitute(kernel))
            kernel <- do.call(kernel, kpar)
          }
        if(!is(kernel,"kernel")) stop("kernel must inherit from class `kernel'")

        ## Compute Affinity Matrix
        if (nystrom.red == FALSE)
          km <- kernelMatrix(kernel, x)
      }

   
     
  if (nystrom.red == TRUE){

    n <- floor(nystrom.sample)
    ind <- sample(1:m, m)
    x <- x[ind,]

    tmps <- sort(ind, index.return = TRUE)
    reind <- tmps$ix
    A <- kernelMatrix(kernel, x[1:n,])
    B <- kernelMatrix(kernel, x[-(1:n),], x[1:n,])
    d1 <- colSums(rbind(A,B))
    d2 <- rowSums(B) + drop(matrix(colSums(B),1) %*% .ginv(A)%*%t(B))
    dhat <- sqrt(1/c(d1,d2))
 
    A <- A * (dhat[1:n] %*% t(dhat[1:n]))
    B <- B * (dhat[(n+1):m] %*% t(dhat[1:n]))

    Asi <- .sqrtm(.ginv(A))
    Q <- A + Asi %*% crossprod(B) %*% Asi
    tmpres <- svd(Q)
    U <- tmpres$u
    L <- tmpres$d
    V <- rbind(A,B) %*% Asi %*% U %*% .ginv(sqrt(diag(L)))
    yi <- matrix(0,m,nc)

   ## for(i in 2:(nc +1))
   ##   yi[,i-1] <- V[,i]/V[,1]

    for(i in 1:nc) ## specc
      yi[,i] <- V[,i]/sqrt(sum(V[,i]^2))
    
    res <- kmeans(yi[reind,], centers, iterations)
    
  }
  else{
    if(is(kernel)[1] == "rbfkernel")
      diag(km) <- 0
    
    d <- 1/sqrt(rowSums(km))
    l <- d * km %*% diag(d)
    xu <- eigen(l)$values[1:nc]
    xi <- eigen(l)$vectors[,1:nc]
    xxu <- eigen(l)$values
    xxi <- eigen(l)$vectors
    yi <- xi/sqrt(rowSums(xi^2))
    res <- kmeans(yi, centers, iterations)
  }
  
  cent <- matrix(unlist(lapply(1:nc,ll<- function(l){colMeans(x[which(res$cluster==l),])})),ncol=dim(x)[2], byrow=TRUE)
  
  withss <- unlist(lapply(1:nc,ll<- function(l){sum((x[which(res$cluster==l),] - cent[l,])^2)}))
  names(res$cluster) <- rown
  return(new("specc", .Data=list(data=res$cluster,evalues=xxu, evectors=xxi), size = res$size, centers=cent, withinss=withss, kernelf= kernel))
 
})


###########################################################################
############################## main computation ###########################
###########################################################################
set.seed(1)

# define eight points
eight  = cbind(c(-3,-2,-2,-2,1,1,2,4),c(0,4,-1,-2,4,2,-4,-3))
eight  = eight[c(8,7,3,1,4,2,6,5),]

sc      = specc(eight, centers=2)

centers = attr(sc, "centers") # center coordinates
size    = attr(sc, "size")    # size of clusters
datacl  = sc$data             # clusters
evalues = sc$evalues          # eigenvalues
evectors= sc$evectors         # eigenvectors

xtable(as.matrix(evalues))
xtable(evectors)


plot(eight,type="n",xlab="price conciousness",ylab="brand loyalty",xlim=c(-4,4),main="8 points")
points(eight, pch=21, cex=2.7, bg="white")
text(eight,as.character(1:8),col="red3",xlab="first coordinate", ylab="second coordinate", main="8 points",cex=1)
lines(ellipse(0.6,centre=centers[2,],scale=c(1.2,2)),col="red3",lwd=2)
lines(ellipse(0.6,centre=centers[1,],scale=c(.7,.4)),col="blue3",lwd=2)


```

automatically created on 2018-05-28