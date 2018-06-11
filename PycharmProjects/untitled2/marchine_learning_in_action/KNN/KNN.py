# coding=utf-8
from numpy import *
import numpy as np
import operator
from os import listdir  # 用于列出给定目录的文件名

def createDataset():
    group = array([[1.0, 1.1], [1.0, 1.0],[0,0],[0, 0.1]])
    labels = ['a', 'a', 'b', 'b']
    return group, labels

def classify(inx, dataset, labels, k):# inx: 用于分类的输入向量   dataset: 训练样本集  labels: 标签向量  k : k值
    datasetsize = dataset.shape[0]   #: shape用于读取矩阵长度,[参数]为维数
    diffmat = tile(inx, (datasetsize , 1)) - dataset
    sqdiffmat = diffmat**2
    sqdistances = sqdiffmat.sum(axis= 1)
    distances = sqdistances**0.5   # 以上为求距离,即输入向量与样本的距离
    sorteddistindicies = distances.argsort()  # 将距离从小到大排序
    classcount = {}
    for i in range(k):
        voteiabel = labels[sorteddistindicies[i]]
        classcount[voteiabel] = classcount.get(voteiabel, 0) + 1  #统计离各标签最近K个的个数
    sortedclasscount = sorted(classcount.items(), key = operator.itemgetter(1), reverse = True)   # iteritems()返回一个迭代器
    # sorted()用于进行排序,items()将字典以列表的形式返回,key为用于比较的维度,reverse为排序方式,默认false从小到大
    return sortedclasscount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayolines = fr.readlines() #读取到文件行数
    numberoflines = len(arrayolines)  #得到文件行数
    returnmat = zeros((numberoflines, 3))  # 创建返回的numpy矩阵,以0填充
    classlabelvector = []
    index = 0
    for line in arrayolines:
        line = line.strip() # 去除回车自付
        listfromline = line.split('\t')  # 进行切片 ,切片中是\t,生成一个元素列表
        returnmat[index, : ]= listfromline[0:3]  # 选取3个元素存储到特征矩阵中
        classlabelvector.append(int(listfromline[-1])) # 将最后一列存贮到向量中
        index += 1
    return returnmat, classlabelvector

#归一化特征
def autonorm(dataset):
    minvals = dataset.min(0)  # min(0)和max(0)可从数据集中选出最小值和最大值
    maxvals = dataset.max(0)
    ranges = maxvals - minvals
    normdataset = zeros(shape(dataset))  #读取一个和数据集一样的0矩阵
    m = dataset.shape[0]
    normdataset = dataset - tile(minvals, (m, 1))   # 元数据集每行将去一个最小值
    normdataset = normdataset/tile(ranges, (m, 1))
    return normdataset, ranges, minvals

#测试代码

def datingclasstest():
    horatio = 0.10
    datingdatamat, datinglabels = file2matrix('datingTestSet2.txt')  # 获取数据
    normmat, ranges, minvals = autonorm(datingdatamat)  # 将数据的样本集进行归一化
    m = normmat.shape[0]    # 数据集0维维数
    numtestvecs = int(m*horatio)  # 采取10%做为测试集
    errorcount = 0.0
    for i in range(numtestvecs):
        classifierresult = classify(normmat[i, : ], normmat[numtestvecs:m, :],  # knn分类器
                                    datinglabels[numtestvecs:m], 5)
        print("the classifier came back with: %d, the real answer is : %d" %
              (classifierresult, datinglabels[i]))
        if (classifierresult != datinglabels[i]):
            errorcount += 1.0
    print("the total right rate is : %f" % (1-errorcount/float(numtestvecs)))

def classifyperson():
    resultlist = ['not at all', 'in small doses', 'in large deses']
    percenttats = float(input("percentage of time spent playing vider games?\n\t"))
    ffmiles = float(input("frequent flier miles earned per year?\n\t"))
    icecream = float(input("liters of ice cream consumed per year?\n\t"))
    datingdatamat, datinglabels = file2matrix('datingTestSet2.txt')
    normmat, ranges, minvals = autonorm(datingdatamat)
    inarr = np.array([ffmiles, percenttats, icecream])
    classifierresult = classify((inarr- minvals)/ranges, normmat, datinglabels, 3)
    print("you will probably like this person: ", resultlist[classifierresult -1])


#-------------------------------------------------------------------------
#以下为一个手写数字识别的程序

def img2vector(filename):  # 将图像转化为向量,用于使分类器可以识别
    returnvect = zeros((1,1024))   # 构造一个1*1024的矩阵
    fr = open(filename)  # 打开文件
    for i in range(32):   # 循环读取
        linestr = fr.readline() # 此为读取文件一行,而readlines()直接读取整个文件
        for j in range(32):
            returnvect[0, 32*i + j] = int(linestr[j])  #将32*32 转化为1*1024
    return returnvect

def handwritingclasstest(): # 手写数字识别系统的测试
    hwlabels = []
    trainingfilelist = listdir('trainingDigits')
    m = len(trainingfilelist)   #文件个数
    trainingmat = zeros((m, 1024))   # 获取所有文件构成矩阵
    for i in range(m):
        filenamestr = trainingfilelist[i]  # 获取文件
        filestr = filenamestr.split('.')[0]   # 截取.前半部分,即去除.txt
        classnumstr = int(filestr.split('_')[0])  #此为获取数字分类
        hwlabels.append(classnumstr)
        trainingmat[i, :] = img2vector('trainingDigits/%s' % filenamestr)
    testFileList = listdir('testDigits')  # 测试集
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileNameStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify(vectorUnderTest, trainingmat, hwlabels, 4)
        print("the classifier came back with: %d, the real answer is: %d" %
              (classifierResult, classNumStr))
        if(classifierResult != classNumStr):
            errorCount += 1.0
    print("the total number of errors is : %d" % errorCount)
    print("the total error rate is : %f\n" % (errorCount/float(mTest)))












'''
分析数据:
import KNN
a,b = KNN.file2matrix('datingTestSet.txt')
from numpy as np
c = np.array(b)   # 注意此处,应将list转化为numpy中的array,使用np.array()
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure
ax = fig.add_subplot(1111)
ax.scatter(a[:,1],a[:,2],a[:,0],15.0*c, 15.0*c,15.0*c)
plt.show()

'''