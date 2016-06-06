% SVMbankruptcy MATLAB Code
%
% translated from R by: Bey, Patrik (beypatri@gmail.com)
%
clear all

cd('./')    %adjust working directory

%load bankruptcy data
data = readtable('bankruptcy.csv', 'Delimiter', ';','ReadVariableNames',true);

%define kernel parameter for SVM
sgm = [0.2,0.2,1,1,2,2]'; %radial basis function kernel parameter sigma
C = [1,8,1,8,1,8]; %SVM cost function parameter C


group = data.Bankruptcy;   %group labels 
train_data = [data.Profitability,data.Leverage]%,data.Bankruptcy];    %training data

for i = 1:length(sgm)
    figure(i)
    svmStruct = svmtrain(train_data,group,'ShowPlot',true,'kernel_function','rbf','rbf_sigma',sgm(i),'boxconstraint',C(i));
     title( ['SVM with sigma ' num2str(sgm(i)) ' and C ' num2str(C(i))])
end
