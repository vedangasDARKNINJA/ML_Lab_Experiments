clc
clear all

n = input('Enter number of samples: ');
d = input('Enter d: ');
coeffs = input('Enter Coeffs of Line for generating data: ');
v = input('range in which noise should vary (-a,a): ');
x = 1:d:n*d;
l = polyval(coeffs,x);
y = l -v + (2*v)*rand(1,n);

figure(1);
scatter(x,y,'filled'); hold on;
plot(x,l);
xlabel('x');
ylabel('y');
title('Original Data set');
legend('distributed data','original line');
hold off;

p=polyfit(x,y,1);
fitLine = polyval(p,x);
figure(2);
scatter(x,y,'filled'); hold on;
plot(x,fitLine);
xlabel('x');
ylabel('y');
title('Fitted Line');
legend('Data Set','Fitted Line');
hold off;

figure(3);
plot(x,fitLine);hold on;
plot(x,l);
xlabel('x');
ylabel('y');
title('Comparison of the two lines');
legend('Fitted Line','Original Line');
hold off;

MSE = sum((y-fitLine).^2)/length(y);
disp(['MSE: ',num2str(MSE)]);