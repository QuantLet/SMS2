<div style="margin: 0; padding: 0; text-align: center; border: none;">
<a href="https://quantlet.com" target="_blank" style="text-decoration: none; border: none;">
<img src="https://github.com/StefanGam/test-repo/blob/main/quantlet_design.png?raw=true" alt="Header Image" width="100%" style="margin: 0; padding: 0; display: block; border: none;" />
</a>
</div>

```
Name of Quantlet: SMSellipse

Published in: Multivariate Statistics: Exercises and Solutions

Description: computes ellipsoids for varying rho and d. rho is the direction and correlation parameter lying between -1 and 1. d is the radius of the ellipsoids. Given a covariance structure Sigma, depending on rho, the ellipse function calculates the cholesky decomposition of Sigma = Q''*Q, resulting in a upper triangular matrix Q, which in turn is used for the transformation of the unit circle with respect to the direction. The shape of the ellipsoids is in accordance with the correlation parameter rho.

Keywords: ellipse, correlation, plot, covariance matrix, Cholesky decomposition

See also: SMSellipse, SMSjordandec

Author: Monika Jakubcova, Awdesch Melzer, Dedy Dwi Prastyo

Submitted: 27.02.2015

Example: Ellipsoids for rho = (0.5, -0.75, 0, 0.25) and radius = (4, 4, 4, 1) are plotted.

```
<div align="center">
<img src="https://raw.githubusercontent.com/QuantLet/SMS2/master/SMSellipse/SMSellipse_m.png" alt="Image" />
</div>

<div align="center">
<img src="https://raw.githubusercontent.com/QuantLet/SMS2/master/SMSellipse/SMSellipse_r.png" alt="Image" />
</div>

