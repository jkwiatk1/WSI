'''
WSI Laboratorium 1
@author Jan Kwiatkowski
'''

from unittest import TestCase
import autograd.numpy as np
from autograd import grad, hessian

# Validate the calculated gradient and hessian

# Define the function for numpy autograd library
def f(x):
    return (x[0]+2*x[1]-7)**2 + (2*x[0]+x[1]-5)**2


# Define the function for my program
def f_f(x0):
    x = x0[0]
    y = x0[1]
    return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2

def grad_f(x0):
    x = x0[0]
    y = x0[1]
    df_dx = 2 * (x + 2 * y - 7) + 4 * (2 * x + y - 5)
    df_dy = 4 * (x + 2 * y - 7) + 2 * (2 * x + y - 5)
    return [df_dx, df_dy]

def hessian_f():
    d2f_dx2 = 2 + 4 * 2
    d2f_dy2 = 4 * 2 + 2
    d2f_dxdy = 2 * 4
    return [[d2f_dx2, d2f_dxdy], [d2f_dxdy, d2f_dy2]]


# Define the test class
class TestGradientHessian(TestCase):
    def test_isGradientSetOk(self):
        # Compute the gradient and Hessian at a point
        test_values = [(1, 1), (2, 3), (0, 0), (-1, 2), (3, -1)]

        for x, y in test_values:
            x0 = np.array([x, y], dtype=float)
            gradient = grad(f)
            hessian_calc = hessian(f)

            self.assertEquals(f(x0), f_f(x0))
            self.assertEquals(gradient(x0).tolist(), grad_f(x0))
            self.assertEquals(hessian_calc(x0).tolist(), hessian_f())
