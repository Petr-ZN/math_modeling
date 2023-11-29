import numpy as np

g = 9.8
x0 = 0
y0 = 0
vx = 2
vy = 3

t = np.arange(0,5,0.1)

x = x0 + vx*t
y = y0 + vy*t + g*t**2/2

array = np.zeros ((len(t), 3))

for i in range (len(t)):
       
    array[i, 0] = t[i]

    array[i, 1] = x[i]
    
    array[i, 2] = y[i]

print(array)