#!/usr/bin/env python
#-*- coding: utf-8 -*-

from math import log
from operator import itemgetter 

#步骤
'''
---- 创建决策树 ----
假设有n个特征，依次根据数据增益情况求出最优特征，然后根据特征求出对应的分支
1. 根据数据集选取出最佳特征
2. 计算该特征对应的值分别对应的结果标签--- 可能是结果标签，也可能是其他特征的决策树

'''



'''
计算数据集无序程度的方法： 
香农熵：熵被定义为信息的期望值,熵越高，则不确定性越大
'''
def calShannotEvent(dataSet) :
	currentLabels = {}
	for val in dataSet :
		if val[-1] not in currentLabels.keys() : currentLabels[val[-1]] = 0
		currentLabels[val[-1]]+=1
	
	shannotEvent = 0.0
	
	for key in currentLabels:
		#当前标签，也就是最后一列标签的值相同的个数除以标签总数
		prob = float(currentLabels[key])/len(dataSet)
		#墒农计算公式 以2为底求对数
		shannotEvent += -prob*log(prob,2)		

	return shannotEvent

'''
@description：根据给定特定划分数据集
@param dataSet 数据集
@param axis    列
@param value   指定特征值
'''
def splitDataSet(dataSet,axis,value) :

	retSplitData = []

	for list in dataSet :
		
		if list[axis] == value :

			#根据某列、某值进行分割数据集，取出为value的值组成新的行
			#原数据集为[0,2,3],[1,2,8] 如果 axis=1 value=2 则分割后的数据集为[0,3],[1,8]
			recordList = list[:axis]
			recordList.extend(list[axis+1:])
			retSplitData.append(recordList)

	return retSplitData
			
'''
数据格式为：n(feature) + 1(label)
二元模型熵,条件越多,数据越多,不确定性越小
选择出和当前标签相关性最大的特征列
'''

def chooseBestFeature(dataSet) :
	#除最后一列标签列
	numFeatures = len(dataSet[0])-1
    #数据集的熵
	baseShannot = calShannotEvent(dataSet)
	bestFeature = -1
	bestInfoGain = 0.0    

	for i in range(numFeatures) :
 		#获取i列的值
		featureValue = [feature[i] for feature in dataSet]
		#去重
		featureValue = set(featureValue)
		#某特征列条件墒 有个联合概率和条件概率概念
		conditionShannot = 0.0
		for val in featureValue :
			subDataSet = splitDataSet(dataSet,i,val)
			unionProb = len(subDataSet)/float(len(dataSet))
			conditionShannot += unionProb*calShannotEvent(subDataSet)
               
		infoGain = baseShannot - conditionShannot
	        
		if (infoGain > bestInfoGain) :

			bestInfoGain = infoGain
			bestFeature = i
	
	return bestFeature		


#当构建决策树,最后只剩下最后一个当前标签时，然后按照该标签的出现概率来选取值,概率大的则返回

def majorityCnt(classList) :

	classCounts = {}
	
	for vote in classList :

		if(vote not in classCounts.keys()) : classCounts[vote] = 0

		classCounts[vote]+=1

	#按照value 进行排序
	sortedLabelCount = sorted(classCounts.iteritems(),key=itemgetter(1),reverse=True)
	return sortedLabelCount[0][0]
	

'''
构建决策树
@param dataSet 数据集
@param labels 特征名

'''
def createTree(dataSet,labels) :

	#获取当前标签类别列表
	classList = [example[-1] for example in dataSet]

	#如果类别表值都相同 也就是同个类别时则停止划分
	if(classList.count(classList[0]) == len(classList)) : 
		return classList[0]

	#如果当前数据集只剩下最后一列，则通过概率选择出现次数最多的类别
	if(len(dataSet[0]) == 1) :
		return majorityCnt(classList)

     #最优划分
	bestFeature = chooseBestFeature(dataSet)
	featureName = labels[bestFeature]
	myTree = {featureName:{}}
     #删除当前最优标签
	del(labels[bestFeature])
	#求出该最优特证的各种取值
	featVals = [example[bestFeature] for example in dataSet]
	#去重
	uniqueVals = set(featVals)

	#具体值继续做为决策树节点
	for val in uniqueVals :
		#cop label
		subLabels = labels[:]
		subDataSet = splitDataSet(dataSet,bestFeature,val)
		myTree[featureName][val] = createTree(subDataSet,subLabels)

	return myTree

'''
输入测试的数据，根据决策树进行分类，得到最终的一个决策结果
@param decisionTree 已经构建好的决策树
@param featLabels   特征标签
@param testVec 		待分类的特征
'''

def classify(decisionTree,featLabels,testVector) :
	rootLabel = list(decisionTree.keys())[0]
	secondIndex = decisionTree[rootLabel]
	index = featLabels.index(rootLabel)
	classLabel = None
	for key in secondIndex :
		if(testVector[index] == key) :
			if(type(secondIndex[key]).__name__ == 'dict') :
				classLabel = classify(secondIndex[key],featLabels,testVector)
			else :
				classLabel = secondIndex[key]

	return classLabel




#print(calShannotEvent([[1, 1], [2, 1], [8, 1]]))
#print(splitDataSet([[1,8,8]],0,1))
#print(chooseBestFeature([[1,4,1],[2,4,1],[8,4,1],[3,2,0]]))

#print(majorityCnt([1,4,4,8]))

dataSet = [
['Rainy','Hot','High','FALSE','NO'],
['Rainy','Hot','High','TURE','NO'],
['Overcast','Hot','High','FALSE','YES'],
['Sunny','Mid','High','FALSE','YES'],
['Sunny','Cool','Normal','FALSE','YES'],
['Sunny','Cool','Normal','TRUE','NO'],
['Overcast','Cool','Normal','TRUE','YES'],
['Rainy','Mid','High','FALSE','NO'],
['Rainy','Cool','Normal','FALSE','YES'],
['Sunny','Mid','Normal','FALSE','YES'],
['Rainy','Mid','Normal','TRUE','YES'],
['Overcast','Mid','High','TRUE','YES'],
['Overcast','Hot','Normal','FALSE','YES'],
['Sunny','Mid','High','TRUE','NO']
]
labels = ['Outlook','Temp','Humidity','Wind','Play Golf']
featLabels = labels[:]
print(classify(createTree(dataSet,labels),featLabels,['Overcast','Hot','High','TRUE']))

