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
print (a)
b = a[::,0]
c = a[::,-1]

a[::,0] , a[::,-1] = c, b
print (a)


