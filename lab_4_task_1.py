import numpy as np

def arithmetic_mean (a):
    sum = 0
    for i in a:
        sum += i
    n = len(a)
    print (sum/n)

array = np.arange(10)
print (array)
arithmetic_mean(array)