clc 
clear all

n = input('Enter number of samples: ');
d = input('Enter interval spacing: ');
x = 0:d:(n-1)*d;
y = sin(0.5*x)+0.5*(-1+2*rand(1,n));
figure(1);
scatter(x,y,'filled');hold on;
plot(x,sin(0.5*x));
legend('data set','original function');
hold off;
newMSE = zeros(1,10);
figure(2);
for i=1:1:10
    p=polyfit(x,y,i);
    newY = polyval(p,x);
    newMSE(i) = sum((y - polyval(p,x)).^2)/length(y);
    subplot(2,5,i);
    scatter(x,y,'filled');hold on;
    plot(x,newY);
    xlabel('x');
    ylabel('y');
    title(['Degree: ',num2str(i),', ','MSE: ',num2str(newMSE(i))]);
end
