#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import function#导入function模块，也就是以function命名的py文件，里面定义了多种函数 直接function.name(arg0...)引用

print(function.my_abs(2))
p = function.move(2,3,4,2)
print(p[0],p[1])

print(function.quadratic(4,9,0))

function.f1(1,2,8)

l = [8,88]
function.f2(*l)
#function.f2(1,2,*l)

d={'city':'B','gender':'M','address':'C'}
function.f3(1,2,**d) #传入参数时只是对d的一份拷贝，函数中对dict类型修改不影响d
#function.f3(1,2,city='Beijing')
function.f4(1,2,city='d',gender='M')
function.f5(1,2,**d) #当传入**d然后从中取出 city gender对应的值，剩下的在给d
function.f5(*l,**d) #对于任意函数，都可以通过类似func(*args, **kw)的形式调用它

print(function.product(8))

print(function.fact(100))

print(function.moveH(3, 'A', 'B', 'C'))