# encoding:utf-8
from math import log
import operator

def calcSHannonEnt(dataSet):   #计算数据的熵
    numEnteries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEnteries  #该分类的概率
        shannonEnt -= prob* log(prob, 2)  #香农求熵
    return shannonEnt

def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing' , 'flippers']
    return dataSet, labels


# 按照特征划分数据集
def splitDataSet(dataSet, axis, value): # 待划分数据集, 划分数据集的特征, 特征的返回值
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]    # 将符合特征的数据抽取出来,这里每个数据样本是有多个特征的
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

# 选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcSHannonEnt(dataSet) # 计算数据熵
    bestInfoGain = 0.0  # 信息增益
    bestFeature = -1    # 特征
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)  # 转化为集合,得到列表中唯一元素
        newEntropy = 0.0  # 熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)  # 计算每种划分方式结果
            prob = len(subDataSet)/float(len(dataSet))    # 求概率
            newEntropy += prob * calcSHannonEnt(subDataSet)  # 对所有唯一特征值进行熵求和
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCat(classList):
    classCount= {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key= operator.itemgetter(1), reversed= True)# 进行排序
    return sortedClassCount[0][0]

# 创建树
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):  # count统计字符出现的次数
        return classList[0]   # 类别完全相同则停止继续划分
    if len(dataSet[0]) == 1:    # 遍历完所有特征时还未完全相同返回出现最多的
        return majorityCat(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 找到最好的划分方式
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]  # 获得列表包含所有属性值
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

def classify(inputTree, featLabels, testVec):  # 使用决策树的分类函数
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)  # 将标签字符串转换为索引,即开始出现firstStr字符的索引
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel

# 使用pickle模块存储决策树
def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)

