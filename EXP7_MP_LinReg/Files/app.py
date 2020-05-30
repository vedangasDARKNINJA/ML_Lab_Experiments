from random import random, seed
import math
import numpy as np
import matplotlib.pyplot as plt


data_m = -2
data_c = 12
def err(r): return r*(- 1 + 2*random())


learningRate = 0.0001
Iterations = 3000
Points = 50
data = np.array([[x, data_m*x + data_c + err(3)] for x in range(1, Points+1)])
w = 0
b = 0

MSEgraph = []
MSE = 0
prevMSE = 0

for j in range(Iterations):
    prevMSE = round(MSE/Points, 1)
    MSE = 0
    for i in range(Points):
        predicted = w * data[i, 0] + b
        expected = data[i, 1]
        error = expected-predicted
        w += learningRate*error*data[i, 0]
        b += learningRate*error
        MSE += error**2
    if round(MSE/Points, 1) != prevMSE and j > 0:
        MSEgraph.append([len(MSEgraph), MSE/Points])
        print("iteration({0}): MSE = {1}".format(j, MSE))

MSEgraph = np.array(MSEgraph)
finalPoints = []
for i in range(Points):
    finalPoints.append(w*data[i, 0] + b)

print("FINAL VALUES:\nW:{0}\nB:{1}\nMSE:{2}".format(w, b, MSE))


plt.figure(1)
plt.plot(data[:, 0], data[:, 1])
plt.plot(data[:, 0], finalPoints)
plt.xlabel('X_data')
plt.ylabel('Y_data')
plt.title('Gradient Descent: Linear Regression')

plt.figure(2)
plt.plot(MSEgraph[:, 0], MSEgraph[:, 1])
plt.title('Error vs iterations plot')
plt.xlabel('Iterations')
plt.ylabel('Mean Sqaured Error')
plt.show()
