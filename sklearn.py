import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn import linear_model
from sklearn import svm
from sklearn import neighbors


def f(x1, x2):
    y = 0.5 * np.sin(x1) + 0.5 * np.cos(x2) + 0.1 * x1 + 3
    return y


def load_data():
    x1_train = np.linspace(0, 50, 500)
    x2_train = np.linspace(-10, 10, 500)
    data_train = np.array([[x1, x2, f(x1, x2) + (np.random.random(1) - 0.5)] for x1, x2 in zip(x1_train, x2_train)])
    x1_test = np.linspace(0, 50, 100) + 0.5 * np.random.random(100)
    x2_test = np.linspace(-10, 10, 100) + 0.02 * np.random.random(100)
    data_test = np.array([[x1, x2, f(x1, x2)] for x1, x2 in zip(x1_test, x2_test)])
    return data_train, data_test


train_set, test_set = load_data()
x_train = train_set[:, 0:2]
y_train = train_set[:, 2]

x_test = test_set[:, 0:2]
y_test = test_set[:, 2]
clf = neighbors.KNeighborsRegressor()
clf.fit(x_train, y_train)
result = clf.predict(x_test)
score = clf.score(x_test, y_test)
print(score)

plt.figure()
plt.plot(np.arange(len(result)), y_test, 'go-', label='true value')
plt.plot(np.arange(len(result)), result, 'ro-', label='predict value')
plt.title('score: %f' % score)
plt.legend()
plt.show()
