import numpy as np
from physical_constants import acceleration_of_free_fall as g

x = int(input('введите x '))
y = int(input('введите y '))
speed_x = int(input('введите скорость по оси x'))
speed_y = int(input('введите скорость по оси y'))

array = np.zeros((5,3))

for time in range (5):
       
    array [time,0] = time
    
    array [time,1] = x + speed_x*time
    
    array [time,2] = y + speed_y*time - (g*time**2)/2

print (array)