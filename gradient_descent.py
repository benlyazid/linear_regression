import matplotlib.pyplot as plt
import numpy

def clc_sum_of_err(y, x):
    y_square = 0
    a_square = 0
    b_square = 0
    a = 0
    b = 0
    a_b = 0

# we are calculing the sum of  errors using (y' - y)**2 where y' = ax + b
    
    for i in range(len(y)):

# The final formule is y^2 + b^2 + a^2*x^2 + ma + nb + k*a*b where (k, m, n) are reals numbers

        y_square += y[i]**2
        b_square += 1
        a_square += x[i]**2
        a += 2 * x[i] * y[i]
        b += 2 * y[i]
        a_b += 2 * x[i]
    print(y_square, a_square, b_square, a, b, a_b)

    
# 1- find the equation of b: b_square * B^2 + (b + a_b) * B + *(y_square + a_square + a)
        #solution : x = -b / 2a ==> (b + a_b) / 2 * b_square

# 2- find the equation of a: a_square * a^2 + (a + a_b) * a + *(y_square + b_square + b)
        #solution : x = -b / 2a ==> (a + a_b) / 2 * a_square

# 3- from 2 and 1
    a_res = (a  - (a_b * b / (2 * b_square)) / (2 * a_square + ()))




#x = [80, 60, 95, 77, 56, 75, 65, 90, 65, 76]
x = [3, 5, 7]
y = [1, 6, 8]
#f(x) = 4.5x + 4
#y = [180, 160, 190, 178, 150, 177, 168, 220, 159, 179]

# start with g(x) = 1x + 0
print(y)
g_error = []
g_x = []
clc_sum_of_err(y, x)
#plt.scatter(x, g)
#plt.figure(1)
#plt.plot(x, y, 'go')
#plt.show()
