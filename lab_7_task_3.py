from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

	
fig, ax = plt.subplots() # Создание пространства и подпространства
 
anim_object, = plt.plot([], [], '-', lw=2) # Объект анимации
 
xdata, ydata = [], [] # Координаты объекта анимации
 
ax.set_xlim(-5, 5) # Пределы изменения переменной Х
ax.set_ylim(-5, 5) # Пределы изменения переменной У

def babochka (t):
    xdata.append  (np.sin(t)* (np.e**np.cos(t) - 2*np.cos(4*t) + np.sin(t/12)**5))
    ydata.append (np.cos(t)* (np.e**np.cos(t) - 2*np.cos(4*t) + np.sin(t/12)**5))
    anim_object.set_data(xdata, ydata) # Передача координат
    return anim_object,

ani = FuncAnimation(fig, # Стандартный вызов пространства
                    babochka, # Вызов функции подстановки координат
                    frames=np.arange(0, 12*np.pi, 0.01),
                    interval=100 # Интервал между кадрами,
                    )            # по умолчанию 200 милисекунд

plt.show() 
ani.save('animation_1.gif')





