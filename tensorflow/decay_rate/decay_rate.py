import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np


learning_rate = 0.5
decay_rate = 0.9
y = []
y_ = []

fig = plt.figure()
ax = fig.add_subplot(111)


if __name__ == '__main__':
    for i in range(500):
        y.append(learning_rate * decay_rate ** (i/20))
        y_.append(learning_rate * decay_rate ** int(i/20))
    x = np.linspace(0, 500, 500)
    line1 = ax.plot(x, y, label='staircase=True', c='g')
    line2 = ax.plot(x, y_, label='staircase=False', c='r')
    ax.set_title('exponetial_decay')
    ax.set(xlabel='iterator_time', ylabel='learning_date')
    # handles, labels = ax.get_legend_handles_labels()
    # ax.legend(handles, labels, loc='upper right')
    ax.legend()
    plt.show()

