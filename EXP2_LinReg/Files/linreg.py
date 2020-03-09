import random
import numpy as np
import matplotlib.pyplot as plt

iterations = 10000
learningRate = 0.001
mse = []
def gradient_descent(x,y):
    m_curr = b_curr = 0    
    n= len(x)
    prev_mse = 0
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        #printing line progress
        if not i%2000:
            plt.plot(x,y_predicted)
        
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        curr_mse = (1/n)*sum((y-y_predicted)**2)
        
        if(round(curr_mse)!= round(prev_mse)):
            print("itr: {} => appending to mse: {}".format(i,curr_mse))
            mse.append(curr_mse)
        m_curr = m_curr - learningRate * md
        b_curr = b_curr - learningRate * bd
        prev_mse = curr_mse
        if i==0 or i==iterations-1:
            print("itr:{} \n m: {}, b: {}".format(i,m_curr,b_curr))

    newY = []
    for i in range(n):
        newY.append(m_curr*i + b_curr)

    newY = np.array(newY)
    return newY

random.seed(1)
dataSet = 50
dataLine_m = 3
dataLine_b = 4
weight = 2

x = []
y = []
for c in range(dataSet):
    x.append(c)
    y.append(dataLine_m*c+dataLine_b + weight*random.random()*(- 1 + 2*random.random()))

x = np.array(x)
y = np.array(y)

fitLine = gradient_descent(x,y)

plt.scatter(x,y)
plt.plot(x,fitLine,'-r')
plt.xlabel('X_data')
plt.ylabel('Y_data')
plt.title('Gradient Descent: Linear Regression')
plt.show()

err_x = np.linspace(0,len(mse),len(mse))
plt.figure(2)
plt.plot(err_x,mse);
plt.title('Error vs iterations plot')
plt.xlabel('Iterations')
plt.ylabel('Mean Sqaured Error')
plt.show()