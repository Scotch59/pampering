import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import math
import random

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

def animate(f):
    ax.clear()
    k = 300

    x_tree = [math.cos(i / 5 + f / 10) * (k - i) for i in range(k)]
    y_tree = [math.sin(i / 5 + f / 10) * (k - i) for i in range(k)]
    z_tree = [i for i in range(k)]
    ax.scatter(x_tree, y_tree, z_tree, c="green", marker="^")

    step = 3


    z_garland = [i for i in range(1, k, step)]
    x_garland = [math.cos(i / 5 + 2 + f / 10) * (k - i + 10) for i in range(1, k, step)]
    y_garland = [math.sin(i / 5 + 2 + f / 10) * (k - i + 10) for i in range(1, k, step)]
    colors = ["#" +  ''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) for _ in range(len(z_garland))]

    ax.scatter([0], [0], [k], c="gold", marker="*", s=200)

    ax.set_xlim(-500, 500)
    ax.set_ylim(-500, 500)
    ax.set_zlim(0, k)

    ax.set_box_aspect([1, 1, 1])

    return  fig,


ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
ani.save("Ёлочка.gif")