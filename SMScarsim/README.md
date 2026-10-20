<div style="margin: 0; padding: 0; text-align: center; border: none;">
<a href="https://quantlet.com" target="_blank" style="text-decoration: none; border: none;">
<img src="https://github.com/StefanGam/test-repo/blob/main/quantlet_design.png?raw=true" alt="Header Image" width="100%" style="margin: 0; padding: 0; display: block; border: none;" />
</a>
</div>

```
Name of Quantlet: SMScarsim

Published in: Multivariate Statistics: Exercises and Solutions

Description: computes the Jaccard, simple matching and Tanimoto proximity coefficients for binary car data

Keywords: cluster-analysis, distance, proximity

Keywords[new]: Jaccard proximity coefficient, Tanimoto proximity coefficient, simple matching coefficient

See also: MVAclus8p, MVAclusbank, MVAclusbh, MVAclusfood, MVAclususcrime, MVAdrugsim, SMSclus8p, SMSclus8pd, SMSclus8pmst2, SMSclusbank, SMSclusbank2, SMSclusbank3, SMScluscomp, SMScluscrime, SMScluscrimechi2, SMSclushealth

Author: Awdesch Melzer

Submitted: Sun, September 07 2014 by Awdesch Melzer

Usage: please install "simba" package

Datafile: carmean2.dat

Input: Matrix enclosing car marks: Economy, Service, Non depreciation of value, Price, Mark 1 for very cheap cars, Design, Sporty car, Safety, Easy handling

Output: Jaccard, simple matching and Tanimoto proximity coefficients

Example: Result: y [,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8] [1,] 0 1 1 0 1 1 0 0 [2,] 1 0 0 1 0 0 1 1 [3,] 0 0 1 0 1 0 1 0 sim(y,method="jaccard") # jaccard 1 2 2 0.0000000 3 0.4000000 0.1666667 sim(y,method="simplematching") # simple matching 1 2 2 0.000 3 0.625 0.375 sim(y,method="roger") # tanimoto 1 2 2 0.0000000 3 0.4545455 0.2307692

```
