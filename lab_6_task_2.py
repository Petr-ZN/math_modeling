import matplotlib.pyplot as plt
import numpy as np
def giperbola(x_min, x_max, n):
    
    x = np.linspace(x_min, x_max, n/2)

    y = 1/x
    
    plt.plot(x, y, label='my giperbola')
    plt.xlabel ('X')
    plt.ylabel ('Y')
    plt.show('lab_6_task_2')
    plt.show()

if __name__ == '__main__':
    giperbola(-10, 10, 100)