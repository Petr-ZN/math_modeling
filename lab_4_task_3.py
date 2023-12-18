import numpy as np
from lab_4_task_3_const import g

def Energy (mass, height, speed):
    Ek = mass*speed**2/2
    Ep = mass*g*height
    print (Ek+Ep)

Energy (10, 8, 5)