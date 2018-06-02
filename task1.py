import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

circle, = ax.plot([], [], 'bo', ms=20)
ppoint = np.array([5000.,9000.]) 
speed = np.array([0.,0.]) 

def init():
    ax.set_xlim([0., 10000.])
    ax.set_ylim([0., 10000.])
    return circle, 

g = 9.8
def Euler(point,speed, g):           
    point[1] = point[1] + speed[1] * 0.5
    speed[1] = speed[1] - g
    return point

h = 0.5
def RungeKutta(point, speed, h, g):
    k1 = speed [1]
    k2 = speed [1] - g
    point[1] = point[1] + h * (k1 + k2) * 0.5
    speed[1] = speed[1] - 9.8
    return point

def updatefig(frame):
    #Euler(point,speed, g)
    RungeKutta(point, speed, h, g)
    circle.set_xdata(point[0])
    circle.set_ydata(point[1])
    return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=1000, init_func=init, interval=30, blit=True, repeat=False)
plt.show()
