from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def circle_move(R):

    alpha = np.arange(0, 2*np.pi+10, 0.01) 
    x = R*np.cos(alpha)
    y = R*np.sin(alpha)
    return x, y


def animate(i):
    ball.set_data(circle_move(R=i))


if __name__ == '__main__':

    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='b', label='Ball')

    edge = 100
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    
    ani = FuncAnimation(fig,
                        animate,
                        frames=100,
                        interval=100
                       )

    ani.save('animation_3.gif')
    plt.show()