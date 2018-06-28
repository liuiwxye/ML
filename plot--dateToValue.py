# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:23:10 2018

@author: admin
"""
import pylab
## 从.txt文件中读取数据
def loadData(flieName):
    inFile = open(flieName, 'r')#以只读方式打开某fileName文件
 
    #定义两个空list，用来存放文件中的数据
    X = []
    y = []
 
    for line in inFile:
        trainingSet = line.split(' ') #对于每一行，按' '把数据分开，这里是分成两部分
        X.append(trainingSet[0]) #第一部分，即文件中的第一列数据逐一添加到list X 中
        y.append(trainingSet[1]) #第二部分，即文件中的第二列数据逐一添加到list y 中
    return (X, y)    # X,y组成一个元组，这样可以通过函数一次性返回

## 绘制该文件中的数据
## 需要引入pylab库，里面用到的函数和MATLAB里的非常类似
def plotData(X, y):
    length = len(y)
    pylab.figure(1)
 
    pylab.plot(X, y, 'r*')
    pylab.xlabel('date')
    pylab.ylabel('The value of corresponding date')
 
    pylab.show()#让绘制的图像在屏幕上显示出来


(value,date)=loadData('C:\\Users\\admin\\桌面\\hello.txt')
plotData(date,value)
