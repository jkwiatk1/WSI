import random

def f(x, y):
    return (x+2*y-7)**2 + (2*x+y-5)**2

def grad_f(x, y):
    df_dx = 2*(x+2*y-7) + 4*(2*x+y-5)
    df_dy = 4*(x+2*y-7) + 2*(2*x+y-5)
    return df_dx, df_dy

def stochastic_gradient_descent(learning_rate, num_iterations):
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    for i in range(num_iterations):
        df_dx, df_dy = grad_f(x, y)
        x = x - learning_rate * df_dx
        y = y - learning_rate * df_dy
    return x, y, f(x, y)

x_min, y_min, f_min = None, None, float('inf')
for i in range(10):
    x, y, f_val = stochastic_gradient_descent(0.01, 1000)
    if f_val < f_min:
        x_min, y_min, f_min = x, y, f_val

print("Minimum value of f(x,y) = (x+2*y-7)^2 + (2*x+y-5)^2 is {:.2f} at x = {:.2f} and y = {:.2f}".format(f_min, x_min, y_min))