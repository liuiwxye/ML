import numpy as np
import matplotlib.pyplot as plt

# 输入数据
data = np.array([[1, 3, 3],
                 [1, 4, 3],
                 [1, 1, 1],
                 [1, 5, 5]])
# 标签
label = np.array([1, 1, -1, 1])
# 权值初始化一行三列，取值范围-1到1
# W = (np.random.random(3) - 0.5) * 2
w = np.array([0, 0, 0])
print("W is :", w)
# 学习率设置
# lr = 1
lr = 0.11
# 计算迭代次数
n = 0
# 神经网络输出
output = 0


def update():
    global data, label, w, lr, n, output
    n += 1
    output = np.sign(np.dot(data, w.T))  # w*x+b的符号
    print("Y - O.T", label - output.T)   # y*(w*x+b) 同号为0，异号不为0
    w_t = lr * (label - output.T).dot(data) / int(data.shape[0])  # 权值需要改变的值 批量y*(w*x+b)
    print("O", output, w_t)
    w = w + w_t  # 修正权值


def show():
    # 正样本
    x1 = [3, 4, 5]
    y1 = [3, 3, 5]

    # 负样本
    x2 = [1]
    y2 = [1]

    # 计算分界线的斜率及截距
    k = -w[1] / w[2]
    d = -w[0] / w[2]
    print("k:", k)
    print("d:", d)

    x_data = np.linspace(0, 5)

    plt.figure()

    plt.plot(x_data, x_data * k + d, "r")
    plt.plot(x1, y1, "bo")
    plt.plot(x2, y2, "yx")
    plt.show()


if __name__ == "__main__":

    for _ in range(100):
        update()  # 更新权值
        print("w:", w)  # 打印权值
        print("n", n)  # 打印迭代次数
        output = np.sign(np.dot(data, w.T))  # 计算当前输出
        if (output == label.T).all():  # 如果实际输出等领域期望输出，模型收敛，循环结束
            print("Finished")
            print("epoch:", n)
            break
    show()
