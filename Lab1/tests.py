import numpy as np
from SteepestGradientDescent import stochastic_gradient_descent
from NewtonMethod import newtons_method

x_min, y_min, f_min ,iter_num= None, None, float('inf'), 0

for i in range(10):
    x, y, f_val, iter_num = stochastic_gradient_descent(0.01, 1000)
    if f_val < f_min:
        x_min, y_min, f_min = x, y, f_val

print("Minimum value of f(x,y) = (x+2*y-7)^2 + (2*x+y-5)^2 is {:.2f} at x = {:.2f} and y = {:.2f}".format(f_min, x_min, y_min))
print(iter_num)




iter_num = 0
f_minNewton = 0
x0 = np.array([-4.1221, 3.2131412], dtype=float)
xmin,ymin, f_minNewton, iter_num = newtons_method(x0[0],x0[1])
print(iter_num)
print("Minimum at x =", xmin)
print("Minimum at y =", ymin)
print("Minimum value =", f_minNewton)
