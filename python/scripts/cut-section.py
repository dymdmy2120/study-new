#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list = [0,6,88,188]

print(list[0:-1])
print(list[:1])
print(list[0:1])
print(list[-3:-1])
print(list[::2])

print('ABCDEFG'[-3::3])
print('ABCDEFG'[-1:])
print('ABCDEFG'[-1:0])

def trim(s) :
  
	fIndex = 1
	bIndex = -2 
	while(True) :
		
		if s[fIndex-1:fIndex] == ' ' :
			fIndex+=1
			
		else :
			if s[-1:] == ' ' :
				if s[bIndex:bIndex+1] == ' ' :
					bIndex-=1
					print(bIndex)
					
				else :
					break
			else :
				bIndex+=2
				break

				            

	print('fIndex = %s,bIndex = %s' % (fIndex,bIndex))
	print(len(s)+bIndex)
	return s[fIndex-1:len(s)+bIndex+1]

##另外一种实现方式
def trim1(s) :
	while(s[:1] == ' ') :
		s = s[1:]
	while(s[-1:] == ' ') :
		s = s[:-1]
	return s

s = trim1('')
print(s)

print(len(s))
