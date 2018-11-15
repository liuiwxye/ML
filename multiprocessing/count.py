# -*- encoding: utf-8 -*-

import multiprocessing as mp
import os
import time


# 并行处理某个目录下文件中的字符个数和行数
# 获取需要统计的文件
def getFile(path):
    fileList = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if i.endswith('.py'):
                fileList.append(os.path.join(os.path.abspath(root), i))
                # fileList.append(os.path.join(root), i) 需要配合path，即path是绝对路径可用
    return fileList


# 对得到的文件进行统计
def operFile(path):
    print(mp.current_process().name, path)
    filepath = path
    fp = open(filepath, encoding='utf-8')
    content = fp.readlines()
    fp.close()
    lines = len(content)
    alphaNum = 0
    for i in content:
        alphaNum += len(i.strip('\n'))
    return lines, alphaNum, filepath


# 将统计结果存入文件
def out(list1, writerfilepath):
    filelines = 0
    charNum = 0
    fp = open(writerfilepath, 'a')
    for i in list1:
        fp.write(i[2] + " 行数："+ str(i[0]) + " 字符数："+str(i[1]) + "\n")
        filelines += i[0]
        charNum += i[1]
    fp.close()
    # print(filelines, charNum)


if __name__ == '__main__':
    t = time.time()
    filelist = getFile('.')
    # print(filelist)
    pool = mp.Pool(processes=5)
    resultlist = pool.map(operFile, filelist)
    pool.close()
    pool.join()
    writefilepath = './count.txt'
    # print(resultlist)
    out(resultlist, writefilepath)
    print(time.time()-t)
