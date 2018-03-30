#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#d= {(1,2,[3,4]):'3'}

d = {'dym':1,'dmy':'t'}

print(d['dym'])#如果d['m'] key不存在则会报错 d.get('m')如果key不存在则返回None(类似null)

key = 'dmy'
if key in d:
	print(d[key])

print(None == d.get('d')) #如果key不存在则可以指定某个值d.get('d'，1)

#d.pop('dmy')#删除key=dmy
print(d)

for map in d:
	print("map",d[map])


##set

s = set([1,8,6])
s.add(3)
#s.add((1,2,[3]))#tuple中增加了list类型元素属于可变的了
s.remove(1)
s1 = set([6,88])

print(s & s1)
print(s | s1)
