import matplotlib.pyplot as plt
import numpy as np
# INITIALE VALUE FOR THE EQUATION 'Y = aX +b'
a = 0.1
b = 100
my_data = np.genfromtxt('data.csv', delimiter= ',')
print(my_data)
x = my_data[:, 0].reshape(-1, 1) # set the size of the array
ones = np.ones([x.shape[0], 1]) # Create matrix(100, 1) continingg 1, X.shape --> (100,1) shape[0] == 100
x = np.concatenate([ones, x], axis=1 ) # CREATE MATRIX(100, 2) BY concatenate THE ONE and THE X
#print(x)
y = my_data[:, 1].reshape(-1,1) # create the y matrix
#print(y)
plt.scatter(my_data[:, 0].reshape(-1,1), y)
plt.show()
print(my_data[:, 0].reshape(-1,1))
print('-------------------------')
print(y)