# encoding:utf-8
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle= "sawtooth", fc = '0.8')
leafNode= dict(boxstyle= 'round4', fc= '0.8')
array_args = dict(arrowstyle= "<-")      # 定义文本框和箭头格式

def plotNode(nodeTxt, centerPt, parentPt, nodeType):  # 绘制带箭头的注解
    createPlot.axl.annotate(nodeTxt, xy= parentPt, xycoords= 'axes fraction', xytext= centerPt,
                            textcoords= 'axes fraction',va= 'center', ha= 'center', bbox= nodeType,
                            arrowprops= array_args)

def createPlot():
    fig= plt.figure(1, facecolor= 'white')
    fig.clf()
    createPlot.axl = plt.subplot(111, frameon= False)
    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('a leaf node', (0.8, 0.1),(0.3, 0.8), leafNode)
    plt.show()

def getNumLeafs(myTree):  # 获取叶节点数
    numLeafs = 0
    firstStr = list(myTree.keys())[0]  # 获取第一个键
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':  # 测试节点的数据类型是否为字典
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs

def getTreeDepth(myTree):  # 获得数层数
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth

def retrieveTree(i):
    listOfTrees = [{'no surfacing' : {0: 'no', 1: {'flippers' : {0: 'no', 1: 'yes'}}}},
                   {'no surfacing' : {0: 'no', 1: {'flippers' : {0: {'head': {0: 'no', 1: 'yes'}}}}}}]
    return listOfTrees[i]

def plotMidText(cntrPt, parentPt, txtString):  # 在父子节点之间填充文本信息
    xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1]- cntrPt[1])/2.0 + cntrPt[1]
    createPlot.axl.text(xMid, yMid, txtString)

def plotTree(myTree, parentPt, nodeText):  # 对这个画图问题真的头大
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]   # plotTree.totalW 存储树宽度, totalD 存储树深度
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeText)   # 标记子节点属性值
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff= plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():                           #减少y偏移
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

def createPlot(inTree):   # 绘图
    fig = plt.figure()
    fig.clf()
    axprops = dict(xticks= [], yticks = [])
    createPlot.axl = plt.subplot(111, frameon = False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()