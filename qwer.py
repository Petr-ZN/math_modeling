from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
 
 
def circle_move(R, angle_vel, time):
    alpha = angle_vel * np.pi / 180 * time
    x = R * (alpha-np.sin(alpha))
    y = R * (1-np.cos(alpha))
    return x, y
 
x, y = [], []
def animate(i):
    ball.set_data(circle_move(R=1, angle_vel=1, time=i))
    
    coords = circle_move(R=1, angle_vel=1, time=i)
    x.append(coords[0])
    y.append(coords[1])
    line.set_data(x, y)
    
 
 
if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='Ball')
    line, = plt.plot([], [], '-', color='r', label='Ball')
 
    edge = 6
    plt.axis('equal')
    ax.set_xlim(0, 12)
    ax.set_ylim(-6, 6)
 
    ani = FuncAnimation(fig,
                        animate,
                        frames=720,
                        interval=30)
 
    plt.show()