import matplotlib.pyplot as plt
import numpy as np


x = np.array([[3, 3], [4, 3], [1, 1]])
y = np.array([[1], [1], [-1]])

# w = np.array([1, 2])
w = np.array([0, 0])

b = np.array([0])

lr = 1
n = 0
loss = 10


def update(x_i, y_i):
    global loss, w, b
    w = w + lr*x_i*y_i
    b = b + lr*y_i
    loss = 1
    return loss


fig, ax = plt.subplots()
ax.scatter(x[:, 0], x[:, 1])


if __name__ == "__main__":
    while loss > 0 and n < 100:     # Perception 无法解决或门电路，loss一直大于0，当迭代超过100次就退出

        for i in range(len(x)):                    # 对于每一个input
            if (np.dot(w, x[i]) + b) * y[i] <= 0:  # 如果yi*(w*xi+b)<=0，即划分错误，这里我们不管修正后是否正确，
                loss = update(x[i], y[i])          # 更新参数后继续迭代，即修正x[0]后，去搜索后面的input，这里是x[2]
                                                   # 如果要管修正后是否正确，则只需完成修正后break，然后再从头开始遍历

            else:                                  # 如果对于所有的input都有yi*(w*xi+b)>0，则loss=0，退出
                loss = 0
        n += 1
        print(n, w, b)

    x_show = np.arange(0, 5)
    y_show = (-b - w[0]*x_show)/w[1]
    plt.plot(x_show, y_show, 'r')
    plt.show()
