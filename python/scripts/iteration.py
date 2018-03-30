#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable



list = [0,6,88,188]

print(isinstance(list,Iterable))
print(isinstance(2,Iterable))

#list 迭代

for val in list :
	print(val)	

#index iterate

for i,val in enumerate(list) :
		print(i,val)

#dict

m = {"1":8,"6":188,"8":1888}

#iterate keys
for keys in m :
	print(keys)

#iterate values
for value in m.values() :
	print(value)

#iterate key-value
for k,v in m.items() :
	print(k,v)

#iterate string
for str in 'ABGCCC' :
	print(str)

#multivariable
for x,y in [(1,5),(6,88),("A",88)] :
	print(x,y)

#find min max from list
def findMinAndMax(list) :
	if len(list) == 0:
		return (None,None)
	max = min = list[0]
	for i,x in enumerate(list) :
		if i == 0 :
			continue
		if x > max :
			max = x
		if x < min :
			min = x
	return (min,max)



if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')




