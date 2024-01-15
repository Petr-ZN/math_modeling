import matplotlib.pyplot as plt
import numpy as np
def giperbola(x_min, x_max, n):
    
    x = np.linspace(x_min, 0.0001, n/2) + np.linspace( 0.0001, x_max, n/2)

    y = 1/x
    
    plt.plot(x, y, label='my giperbola')
    plt.xlabel ('X')
    plt.ylabel ('Y')
    
    plt.show()

if __name__ == '__main__':
    giperbola(-10, 10, 100)