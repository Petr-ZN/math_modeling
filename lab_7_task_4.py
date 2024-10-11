from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots() # Создание пространства и подпространства
 
anim_object, = plt.plot([], [], '-', lw=2) # Объект анимации
ax.set_xlim(-1, 1) # Пределы изменения переменной Х
ax.set_ylim(-1, 1) # Пределы изменения переменной У
x= []
y =[]
c = 0.3
d = 0.33
x.append(0.1)
y.append(0.1)
for n in range(1, 30):
        x.append(x[n-1]**2 - y[n-1]**2 + c)
        y.append(2*x[n-1] * y[n-1]+d)

def fractal (n):
    
    anim_object.set_data(x[:n], y[:n]) # Передача координат
    return anim_object,

ani = FuncAnimation(fig, # Стандартный вызов пространства
                    fractal, # Вызов функции подстановки координат
                    frames=len(x),
                    interval=100 # Интервал между кадрами,
                    )            # по умолчанию 200 милисекунд

plt.show() 