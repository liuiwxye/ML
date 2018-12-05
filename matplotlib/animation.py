import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import seaborn as sns

sns.set_style("darkgrid")


def rand_point():
    x = np.random.randint(1, 100, 3)
    y = np.random.randint(1, 2, 3)
    return x, y


fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

x = np.arange(0, 2 * np.pi, 0.01)

line1, = ax1.plot(x, np.sin(x), label='line1', color='r')
x1, y1 = rand_point()
sca1 = ax1.scatter(x1, y1, label='sca1', color='y')

line2, = ax2.plot(x, np.cos(x), label='line2', color='g')  # 余弦波
x2, y2 = rand_point()
sca2 = ax2.scatter(x2, y2, label='sca2', color='c')  # 散点图
ax1.legend((line1, sca1), ('line1', 'sca1'), loc='center')
ax2.legend((line2, sca2), ('line2', 'sca2'), loc='center')


def init():
    line2.set_ydata(np.sin(x))
    line1.set_ydata(np.cos(x))
    x1, y1 = rand_point()
    x2, y2 = rand_point()
    data1 = [[x, y] for x, y in zip(x1, y1)]
    data2 = [[x, y] for x, y in zip(x1, y1)]
    sca1.set_offsets(data1)
    sca2.set_offsets(data2)
    label = 'timestep {0}'.format(0)
    ax2.set_xlabel(label)
    return line1, line2, sca1, sca2, ax2


def animate(i):
    line1.set_ydata(np.sin(x + i / 10.0))
    line2.set_ydata(np.cos(x + i / 10.0))
    x1, y1 = rand_point()
    x2, y2 = rand_point()
    data1 = [[x, y] for x, y in zip(x1, y1)]
    data2 = [[x, y] for x, y in zip(x2, y2)]
    sca1.set_offsets(data1)  # 散点图
    sca2.set_offsets(data2)  # 散点图
    label = 'timestep {0}'.format(i)
    ax2.set_xlabel(label)
    return line1, line2, sca1, sca2, ax2


ani = FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=2000, blit=True)

plt.show()
