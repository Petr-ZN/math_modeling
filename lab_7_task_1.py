import matplotlib.pyplot as plt
import numpy as np
import math

def cicloida (r = 1):
    t = np.arange (0, 10, 0.1)
    x = r * (t - np.sin(t)**3)
    y = r * (1 - np.cos(t)**3)
    
    plt.plot(x, y)
    plt.show()
    
if __name__ == '__main__':
    cicloida(2)