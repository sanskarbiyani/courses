function [error_test] = testError(X_test, y_test, lambda)

m = size(X_test, 1);
error_test = zeros(m, 1);

for i=1:m,
    X_sub = X_test(1:i, :);
    y_sub = y_test(1:i);
    theta = trainLinearReg(X_sub, y_sub, lambda);
    error_test(i) = linearRegCostFunction(X_sub, y_sub, theta, lambda);
end
end