#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['dynamo','elsewhere','Lucky']
for name in names:
	print('name: %s' % name)

sum = 0
for i in range(102):
	sum += i
print("sum = %s" % sum)

##while
sum = 0
n = 99
while n > 0 :
	sum += n
	n= n - 2
print('sum = %s' % sum)

list = ['A','B','C']
for name in list:
	print('hello,%s' % name)

##break
n = 1
while n <= 100 :
	if n > 10:
		break#结素当前循环
	print(n)
	n = n+1 

#continue

n = 0
while n < 10:
	    n = n + 1
	    if n % 2 == 0: # 如果n是偶数，执行continue语句
	        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
	    print(n)

