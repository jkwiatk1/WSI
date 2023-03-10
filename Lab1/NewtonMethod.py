# Newton's Method
import numpy as np
import  math

# def f(x0):
#         x = x0[0]
#         y =  x0[1]
#         return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2
#
# def grad_f(x0):
#         x = x0[0]
#         y = x0[1]
#         df_dx = 2 * (x + 2 * y - 7) + 4 * (2 * x + y - 5)
#         df_dy = 4 * (x + 2 * y - 7) + 2 * (2 * x + y - 5)
#         return df_dx, df_dy

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

# def newtons_method(x0, max_iter=100, eps=1e-12):
#         x = x0
#         iter_num = 0
#         for i in range(max_iter):
#                 g = grad_f(x)
#                 H = hessian_f()
#                 H_inv = np.linalg.inv(H)
#                 p = -H_inv @ g
#                 x_new = x + p
#                 iter_num += 1
#                 norm = math.sqrt(sum([i ** 2 for i in g]))
#                 if norm < eps:
#                         return x_new,f(x),iter_num
#                 x = x_new
#         return x,f(x),iter_num


def newtons_method(x,y, max_iter=100, eps=1e-12):
        iter_num = 0
        for i in range(max_iter):
                df_dx, df_dy = grad_f(x,y)
                H = hessian_f()
                H_inv = np.linalg.inv(H)
                p = -H_inv @ [df_dx, df_dy]
                x_new, y_new = [x,y] + p
                iter_num += 1
                norm = math.sqrt(sum([i ** 2 for i in [df_dx, df_dy]]))
                if norm < eps:
                        return x_new, y_new,f(x_new, y_new),iter_num
                x = x_new
                y = y_new
        return x_new, y_new,f(x_new, y_new),iter_num


