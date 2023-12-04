import numpy as np

def func (a, b, n):
    x = np.linspace(a, b, n)
    y = x**2
    print (y)

a = 0
b = 10
n = 11
func (a, b, n)