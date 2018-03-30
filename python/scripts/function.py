#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def my_abs(x):
	if not isinstance(x,(int,float)): #参数检查
		raise TypeError('bad operand type')
	if x >= 0 :
		return x
	else :
		return -x

def nop():#define empty function
	pass;

##return many value

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

##一元二次方程的解

def quadratic(a,b,c):
	dt = math.pow(b,2)-4*a*c
	return (-b-math.sqrt(abs(dt)))/(2*a),(-b+math.sqrt(abs(dt)))/(2*a)


##函数的参数

def f1(a,b,c=0,d=[]): #默认参数
	d.append('Empty')
	print('a=',a,'b=',b,'c=',c,'d=',d)

def f2(a,b,c=8,*d):  #可变参数
	print('a=',a,'b=',b,'c=',c,'d=',d)

def f3(a,b,c=8,**d): #关键字参数
	print('a=',a,'b=',b,'c=',c,'d=',d)

def f4(a,b,c=8,*,city,gender): #命名关键字参数
	print('a=',a,'b=',b,'c=',c,'city=',city,'gender=',gender)

##多个参数组合 参数顺序 位置参数(必传参数) -> 默认参数 -> 可变参数 -> 命名关键字参数 -> 关键字参数

def f5(a,b,c=8,*,city,gender,**d): #组合关键字参数 
	print('a=',a,'b=',b,'c=',c,'city=',city,'gender=',gender,'d=',d)

def product(x,*args):
	if args == []:
		return x
	multiple = x
	for a in args :
	    multiple = multiple*a
	return multiple

##递归函数

def fact(n):
	if n == 1 :
		return 1
	return n*fact(n-1)
# 利用递归函数移动汉诺塔:
def moveH(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        moveH(n-1, a, c, b)
        moveH(1, a, b, c)
        moveH(n-1, b, a, c)



