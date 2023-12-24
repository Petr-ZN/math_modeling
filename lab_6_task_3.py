import matplotlib.pyplot as plt
import numpy as np
 
def elips (radius=10, a = 10, b = 5):
    
    x = np.arange(-2*radius, 2*radius, 0.1)
    y = np.arange(-2*radius, 2*radius, 0.1)
 
    # Переход к неявнозаданным координатам
    X, Y = np.meshgrid(x, y)
 
    fxy = X**2/a**2 + Y**2/b**2 - 1 # Уравнение окружности
 
    # Команда рисования
    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')
    
    plt.show()
    
if __name__ == '__main__':
	elips()