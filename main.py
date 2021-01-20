import matplotlib.pyplot as plt
import numpy as np
def average(arr):
	return int(sum(arr) / len(arr))
my_data = np.genfromtxt('data.csv', delimiter= ',')

#x = my_data[:, 0].reshape(-1,1)
#y = my_data[:, 1].reshape(-1, 1)
x = [1, 2, 3]
y= [3, 7, 8]
print(x)
print('----------------')
print(y)
print('---------------')
x_bar = (average(x))
y_bar = (average(y))
print(x_bar, y_bar)
plt.scatter(x, y)
plt.axline((0, 1), (2, 6))
plt.show()