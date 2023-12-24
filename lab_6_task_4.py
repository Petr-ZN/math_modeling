import matplotlib.pyplot as plt
import numpy as np
import math


def fun_1 (b):
    fi = np.arange(0, math.pi*100, 0.01)
    r = math.e**(b * fi)
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    plt.plot (x, y)
    plt.axis('equal')
    plt.show()


def fun_2 (k):
    fi = np.arange(0, math.pi*8, 0.01)
    r = fi * k
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    plt.plot (x, y)
    plt.axis('equal')
    plt.show()
    

def fun_3 (k):
    fi = np.arange(0.01, math.pi*8, 0.01)
    r = k / fi**0.5
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    plt.plot (x, y)
    plt.axis('equal')
    plt.show()
    
    
def fun_4 (k):
    fi = np.arange(0.001, math.pi*24, 0.01)
    r = np.cos(k * fi)
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    plt.plot (x, y)
    plt.axis('equal')
    plt.show()
 
    
if __name__ == '__main__':
#    fun_1(0.1)
#    fun_2(1)
#    fun_3(1)
    fun_4(0.3)