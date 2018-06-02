import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

circle, = ax.plot([], [], 'bo', ms=20)
point = np.array([5000.,9000.]) 
speed = np.array([0.,0.]) 

# область анимации
def init():
    ax.set_xlim([0., 10000.])
    ax.set_ylim([0., 10000.])
    return circle, 

g = 9.8

def updatefig(frame):
    point[1] = point[1] + speed[1] - 0.5 * g # начальная координата плюс смещение на вектор скорости (без потери энергии)
    speed[1] = speed[1] - g # на каждый кадр будет ускорение вниз по у
    if point[1] <= 0.:
        speed[1] = -speed[1] # упругий удар
    circle.set_xdata(point[0])
    circle.set_ydata(point[1])
    return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=1000, init_func=init, interval=30, blit=True, repeat=False)
plt.show()
