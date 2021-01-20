import matplotlib.pyplot as plt
import numpy as np
def average(arr):
	return int(sum(arr) / len(arr))
my_data = np.genfromtxt('data.csv', delimiter= ',')

#x = my_data[:, 0].reshape(-1,1)
#y = my_data[:, 1].reshape(-1, 1)
x = [100, 12, 13]
y= [30, 60, 19]
print(x)
print('----------------')
print(y)
print('---------------')
x_bar = (average(x))
y_bar = (average(y))
base = 0
base_2 = 0
for i in range(len(x)):
	s = (x[i] - x_bar) * (y[i] - y_bar)
	base += s
	base_2 += (x[i] - x_bar)**2
m = base / base_2
b = y_bar - (m * x_bar)

x_0 = 0
y_0 = m * x_0 + b
x_1 = 1
y_1 = m * x_1 + b
print(x_bar, y_bar)
plt.scatter(x, y)

plt.axline((x_0, y_0), (x_1, y_1))
plt.show()