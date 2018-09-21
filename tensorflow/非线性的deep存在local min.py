# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 11:45:38 2018

@author: admin
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, activate_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size])+0.1)
    Wx_plus_b = tf.matmul(inputs, Weights)+biases
    if activate_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activate_function(Wx_plus_b)
    return outputs


data = np.array(([-1, 3], [1, -3], [3, 0], [4, 1], [5, 2]))
x_data = data[:,0].reshape(5,1)
y_data = data[:,1].reshape(5,1)


xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

#l1=add_layer(xs, 1, 10, activate_function=tf.nn.relu)
prediction=add_layer(xs, 1, 1, activate_function=tf.nn.relu)

loss = tf.losses.mean_squared_error(labels=ys,predictions=prediction)
# 等价于
# loss=tf.reduce_sum(tf.reduce_sum(tf.square(ys-prediction),
#                    reduction_indices=[1]))/600
# 第一个reduce_sum做的是按列求和，其实这里只有一列，第二个是按行求和共300行
# 所以还可以将上述loss简化为loss=tf.reduce_mean((tf.square(ys-prediction)))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)

plt.ion()
# plt.show()

writer = tf.summary.FileWriter("./tmp/tensorflow", sess.graph)

for i in range(10000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i%50==0:
        # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value=sess.run(prediction,feed_dict={xs:x_data,ys:y_data})
        lines=ax.plot(x_data,prediction_value,'r-',lw=5)
        plt.pause(1)

