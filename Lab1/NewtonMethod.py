# Newton's Method
import numpy as np
import  math


def f(x, y):
    return (x+2*y-7)**2 + (2*x+y-5)**2

def grad_f(x, y):
    df_dx = 2*(x+2*y-7) + 4*(2*x+y-5)
    df_dy = 4*(x+2*y-7) + 2*(2*x+y-5)
    return df_dx, df_dy

def hessian_f():
        d2f_dx2 = 2 + 4 * 2
        d2f_dy2 = 4 * 2 + 2
        d2f_dxdy = 2 * 4
        return [[d2f_dx2, d2f_dxdy], [d2f_dxdy, d2f_dy2]]


def newtons_method(x, y, learning_rate = 0.01, max_iter=1000, eps=1e-12):
        iter_num = 0
        for i in range(max_iter):
                df_dx, df_dy = grad_f(x,y)
                Hessian_inv = np.linalg.inv(hessian_f())
                p = -Hessian_inv @ [df_dx, df_dy]
                x, y = [x,y] + learning_rate * p
                iter_num += 1
                gradient_norm = math.sqrt(sum([i ** 2 for i in [df_dx, df_dy]]))
                if gradient_norm < eps:
                        return x, y, f(x, y), iter_num
        return x, y, f(x, y), iter_num


