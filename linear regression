# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 14:58:00 2017

@author: admin
"""
import numpy as np
import matplotlib.pyplot as plt
x=[45, 73, 89, 120, 140, 163]
y=[80, 150, 198, 230, 280, 360]
x=np.array(x)
y=np.array(y)
#散点图
plt.scatter(x,y,c='r')
plt.xlabel("space")
plt.ylabel("price")
plt.xlim(0,500)
plt.ylim(0,500)
# theta 初始值
theta=[0,0]
# 初始函数
a=np.arange(0,500)
b=theta[0]+theta[1]*a
plt.xlim(0,500)
plt.ylim(0,500)
plt.plot(a,b,linewidth='4',c="g")
plt.show()

loss=10
epsilon=0.0001
alpha=0.00005          #learn rate,如果learn选择不对，则 theta 参数更新结果会不对,过大导致
iter_count=0		   #counter
max_iters=10		   #iterator times
error=0
'''
while(loss>epsilon and iter_count<max_iters):
    loss=0
    for i in range(6):
        pred_y=theta[0]+theta[1]*x[i]
        theta[0]=theta[0]-alpha*(pred_y-y[i])
        theta[1]=theta[1]-alpha*(pred_y-y[i])*x[i]
        
    for i in range(len(x)):
        pred_y=theta[0]+theta[1]*x[i]
        error=0.5*(pred_y-y[i])**2
        loss+=error
    
    iter_count+=1
'''

#批梯度下降法
while(iter_count<max_iters and loss >epsilon):
    sum0=0
    sum1=0
	#loss function
    for i in range(len(x)):
		#假设函数
        pred_y=theta[0]+theta[1]*x[i]
        sum0+=alpha*(pred_y-y[i])
        sum1+=alpha*(pred_y-y[i])*x[i]
    theta[0]=theta[0]-sum0/len(x)
    theta[1]=theta[1]-sum1/len(x)
	
    for i in range(len(x)):
        pred_y=theta[0]+theta[1]*x[i]
		# 损失函数(calc loss)
        error=0.5*(pred_y-y[i])**2
        loss+=error
    loss=loss/len(x)
    iter_count+=1


print(theta)
plt.scatter(x,y,c="g")
a=np.arange(0,200)
b=theta[0]+theta[1]*a
plt.plot(a,b,linewidth='2',c="b")
plt.plot(x,theta[0]+theta[1]*x,c='r')
plt.show()
