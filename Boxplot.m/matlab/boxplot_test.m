x1 = rand(10,1); x2 = 2*rand(15,1); x3 = randn(30,1);
x = [x1;x2;x3];
g = [ones(size(x1)); 2*ones(size(x2)); 3*ones(size(x3))];
boxplot(x,g)