import numpy as np
from lab_4_task_3_const import g

def Energy (mass, height, speed):
    Ek = mass*speed**2/2
    Ep = mass*g*height
    print (Ek+Ep)

mass = 10
height = 8
speed = 5

Energy (mass, height, speed)