# Stochastic Gradient Descent
import math

def f(x, y):
    return (x+2*y-7)**2 + (2*x+y-5)**2

def grad_f(x, y):
    df_dx = 2*(x+2*y-7) + 4*(2*x+y-5)
    df_dy = 4*(x+2*y-7) + 2*(2*x+y-5)
    return df_dx, df_dy

def stochastic_gradient_descent(x,y, learning_rate = 0.01, max_iter=1000, eps=1e-12):
    iter_num = 0
    for i in range(max_iter):
        df_dx, df_dy = grad_f(x, y)
        x = x - learning_rate * df_dx
        y = y - learning_rate * df_dy
        iter_num += 1
        gradient_norm = math.sqrt(df_dx ** 2 + df_dy ** 2)
        if gradient_norm < eps:
            return x, y, f(x, y), iter_num
    return x, y, f(x, y), iter_num


