% SMSsvmspiral MATLAB Code
%
% translated from R by: Bey, Patrik (beypatri@gmail.com)
%
clear all

cd('./')    %adjust working directory

% generating spiral data

theta = linspace(0,3,100);

a = 1;
b = 0.5;    % b is near to zero, spiral approaches a circle

r =  a*exp(b*theta)

% X(+1) members of first group, centering in (c1p,c2p)

c1p = 0;
c2p = 0;

for i = 1:length(theta)
    X1p(i) = c1p + r(i)*cos(theta(i)*pi);
    X2p(i) = c2p + r(i)*sin(theta(i)*pi);
end

% X(-1) members of second group, centering in (c1n,c2n)

c1n = 1;
c2n = 0;
for i = 1:length(theta)
    X1n(i) = 1 - (c1n + r(i)*cos(theta(i)*pi));
    X2n(i) = - (c2n + r(i)*sin(theta(i)*pi));
end

% Agregating data from both classes

X1 = [X1p, X1n];
X2 = [X2p, X2n];

% generating indicator variable

yp = ones(100,1);
yn = -ones(100,1);

Y =  [yp;yn];

% Generating noise, N(0,0.01)
m = 0;
s = 0.1;
e = s.*randn(200,1)+m;

X1 =  X1' + e;
X2 = X2' + e;

Spiral_noise = [X2, X1]

%%%%%%%%%%%
%
% program for SVM classification plot with generated spiral data
%
%%%%%%%%%%%

%define kernel parameter for SVM
sgm = [0.2,8,0.2,8]'; %radial basis function kernel parameter sigma
C = [0.1,0.1,8,8]; %SVM cost function parameter C

for i = 1:length(sgm)
    %figure(i)
    subplot(2,2,i)
    svmStruct = svmtrain(Spiral_noise,Y,'ShowPlot',true,'kernel_function','rbf','rbf_sigma',sgm(i),'boxconstraint',C(i));
    title( ['SVM with sigma ' num2str(sgm(i)) ' and C ' num2str(C(i))])
end

