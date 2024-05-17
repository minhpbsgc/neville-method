#Neville's Method
import math
import numpy as np
def neville_method(data_x: list, data_y: list, x0: int) -> list:
    n = len(data_x)
    Q = np.zeros((n, n))
    Q[:, 0] = data_y
    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i, j] = ((x0 - data_x[i - j]) * Q[i, j - 1] - (x0 - data_x[i]) * Q[i - 1, j - 1]) / (data_x[i] - data_x[i - j])
    return Q#[n-1,n-1]

#Data approximation
#print(neville_method([8.1,8.3,8.6,8.7], [16.94410,17.56492,18.50515,18.82091], 8.4))
#print(neville_method([-0.75, -0.5, -0.25, 0], [-0.07181250, -0.02475000, 0.33493750, 1.10100000], -0.3333333333333))
#print(neville_method([0.1, 0.2, 0.3, 0.4], [0.62049958, -0.28398668, 0.00660095, 0.24842440], 0.25))
#print(neville_method([0.6, 0.7, 0.8, 1.0], [-0.17694460, 0.01375227, 0.22363362, 0.65809197], 0.9))
#print(" ")
#print(neville_method([0,0.25,0.5,0.75], [1,1.64872,2.71828,4.48169], 0.43))
#print(neville_method([-0.5,-0.25,0.25,0.5],[1.93750,1.33203,0.800781,0.687500],0))  
#print(neville_method([0.1,0.2,0.3,0.4],[-0.29004986,-0.56079734,-0.81401972,-1.0526302],0.18)) 
#print(neville_method([-1,-0.5,0,0.5],[0.86199480,0.95802009,1.0986123,1.2943767],0.25)) 

#data_x = [-2, -1, 0, 1, 2]
data_x = [0,1,2,3]
data_y = [1,6,3.5,4]
x0 = 2.5
print(neville_method(data_x, data_y, x0))

