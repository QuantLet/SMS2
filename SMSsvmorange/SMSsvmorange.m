% SMSsvmorange MATLAB Code
%
% translated from R by: Bey, Patrik (beypatri@gmail.com)
%

clear all

cd('./')                              %adjust working directory

%%
% generation of ideal data set: Xp with covariance (4,0,0,4) and Xn with covariance (0.25,0,0,0.25) for groups x(1) and x(-1)
%%

n = 200;                              % number of observations

%%
% generating 2-variate data, member of group x(1)
%%  
sigma_p = [4 0;0 4];
  
Mp      = chol(sigma_p);               % Cholesky square root
Zp      = randn(2,n/2);                % 2 row, 100 columns /in orig R-code 50 columns
Xp      = (Mp*Zp)';
Xp1     = Xp(:,1);
Xp2     = Xp(:,2);

%%
% generating 2-variate data, member of group x(-1)
%%
  
sigma_n = [0.25 0; 0 0.25];
  
Mn      = chol(sigma_n);               % Cholesky square root
Zn      = randn(2,n/2);                % 2 row, 100 columns /in orig R-code 50 columns
Xn      = (Mn*Zn)';
Xn1     = Xn(:,1);
Xn2     = Xn(:,2);

%%  
% Aggregating data
%%  

X1      = [Xp1;Xn1];
X2      = [Xp2;Xn2];
  
%%
%generating indicator variable
%%

yp      = ones(n/2,1);
yn      = -ones(n/2,1);
  
Y       = [yp;yn];                     % group labels used in SVM
OP      = [X2, X1]                     % training data used in SVM

%%%%%%
%% Main program of SVM classification plot
%%%%%%

%%
%define kernel parameter for SVM
%%
sgm = [0.2,5,0.2,5]'; %radial basis function kernel parameter sigma
C = [0.1,0.1,8,8]; %SVM cost function parameter C
  
for i = 1:length(sgm)
    figure(i)
    svmStruct = svmtrain(OP,Y,'ShowPlot',true,'kernel_function','rbf','rbf_sigma',sgm(i),'boxconstraint',C(i));
    title( ['SVM with sigma ' num2str(sgm(i)) ' and C ' num2str(C(i))])
end


