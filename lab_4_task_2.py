import numpy as np

def product (a):
    p = 1
    for i in a:
        p *= i
    print (p)

array = np.arange(1,10)
product (array)