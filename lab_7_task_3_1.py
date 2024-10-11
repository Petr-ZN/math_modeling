from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

	
fig, ax = plt.subplots() # Создание пространства и подпространства
 
anim_object, = plt.plot([], [], '-', lw=2) # Объект анимации
 
xdata, ydata = [], [] # Координаты объекта анимации
 
ax.set_xlim(-20, 20) # Пределы изменения переменной Х
ax.set_ylim(-20, 20) # Пределы изменения переменной У

def heart (t):
    xdata.append (16*np.sin(t)**3)
    ydata.append (13*np.cos(t) - 5*np.cos(2*t)- 2*np.cos(3*t)- np.cos(4*t))
    anim_object.set_data(xdata, ydata) # Передача координат
    return anim_object,

ani = FuncAnimation(fig, # Стандартный вызов пространства
                    heart, # Вызов функции подстановки координат
                    frames=np.arange(0, 2*np.pi, 0.05),
                    interval=30 # Интервал между кадрами,
                    )            # по умолчанию 200 милисекунд

plt.show() 
ani.save('animation_1.gif')





