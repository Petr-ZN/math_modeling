acceleration_of_free_fall = 9.80665
import numpy as np

a = np.zeros((2,4))

a[0,0] = 0
a[0,1] = 1
a[0,2] = 2
a[0,3] = 3
a[1,0] = 4
a[1,1] = 5
a[1,2] = 6
a[1,3] = 7

b = a[::,0] # срез первого столбца [0. 4.]
c = a[::,2] # срез второго столбца [3. 7.]

print(a)
print(b)
print(c)


a[::, 2] = b
a[::, 0] = c
print (a)