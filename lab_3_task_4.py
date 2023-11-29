import numpy as np
 
#n = int(input())
#m = int(input())

n = 4
m = 5

array = np.ones((n, m))
for i in range (n):
    for j in range (m):
        array[i, j] = np.sin(n * i + m * j)
        if array[i, j] < 0:
            array[i, j] = 0
print (array)