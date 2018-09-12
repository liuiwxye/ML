# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 11:45:38 2018

@author: admin
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size,n_layer, activate_function=None):
    layer_name = "layer%s" % n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope("Weights"):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]),name="W")
            tf.summary.histogram("liu",Weights)
        with tf.name_scope("biases"):
            biases = tf.Variable(tf.zeros([1, out_size])+0.1)
            tf.summary.histogram(layer_name + "/biases", biases)
        with tf.name_scope("Wx_plus_b"):
            Wx_plus_b = tf.matmul(inputs, Weights)+biases
        if activate_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activate_function(Wx_plus_b,)
        tf.summary.histogram(layer_name + "/outputs", outputs)
        return outputs


x_data = np.linspace(-2, 2, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data)-0.5+noise

with tf.name_scope("inputs"):
    xs = tf.placeholder(tf.float32, [None, 1], name="x_input")
    ys = tf.placeholder(tf.float32, [None, 1], name="y_input")


l1=add_layer(xs, 1, 10, n_layer=1, activate_function=tf.nn.relu)
prediction=add_layer(l1, 10, 1, n_layer=2, activate_function=None)

with tf.name_scope("loss"):
    loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),
                   reduction_indices=[1]))
    tf.summary.scalar("loss", loss)

# loss = tf.losses.mean_squared_error(labels=y_data,predictions=prediction)

# 等价于
# loss=tf.reduce_sum(tf.reduce_sum(tf.square(ys-prediction),
#                    reduction_indices=[1]))/600
# 第一个reduce_sum做的是按列求和，其实这里只有一列，第二个是按行求和共300行
# 所以还可以将上述loss简化为loss=tf.reduce_mean((tf.square(ys-prediction)))

with tf.name_scope("train"):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)

plt.ion()
# plt.show()

merged = tf.summary.merge_all()
writer = tf.summary.FileWriter("./logs/", sess.graph)

for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i%50==0:
        result = sess.run(merged,feed_dict={xs:x_data,ys:y_data})
        writer.add_summary(result, i)
        # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value=sess.run(prediction,feed_dict={xs:x_data,ys:y_data})
        lines=ax.plot(x_data,prediction_value,'r-',lw=5)
        plt.pause(0.5)

