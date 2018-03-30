# 一、基本语法
## Python简介

1、Python属于解释性语言，执行一句经过解释器转化成机器语言执行，PHP JS都是解释性语言，Java属于半编译半解释，C属于编译性语言。Python语言是解释性语言，所以命名变量时可以不用指定其类型，同时该变量可以代表任意类型，因此称为动态语言，在运行时就可以动态分配空间。而java必须先前指定(因为在编译时需要确定给变量分配多少个字节空间)

## 字符和字符编码问题

> 现在，捋一捋ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。
> 
> 字母A用ASCII编码是十进制的65，二进制的01000001；
> 
> 字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；
> 
> 汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。
> 
> 你可以猜测，如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码
新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。

所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间。

**总结：**

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：

str表示字符串类型 

x=b'\xe4\xb8\xad\xe6\x96\x87' 表示bytes类型，如果将字符存入到磁盘或放在网络传输就需要将其str根据某种编码方式转换成对应字节。

 ‘中文'.encode('utf-8') 返回的就是b'\xe4\xb8\xad\xe6\x96\x87'
 
 相反当计算机从网络读取数据，或从磁盘中加载数据时，需要将bytes转换成 str供给用户查看
 
 b'\xe4\xb8\xad\xe6\x96\x87‘.decode('utf-8',errors='ignore')假如含有部分解码不了的字节时，加上了errors依然能解出一部分字符来。
 如果解码的时候使用了gbk字符集，就会报错或者出现乱码，按什么字符集编的码就需要按对应字符集解码，否则会乱码。
 
 **len()**

 len('中文‘)函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
 
由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：

> \#!/usr/bin/env python3
> 
> \# -*- coding: utf-8 -*-
> 
>第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

>第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：

###格式化

在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略

> print('nihao %s cc %s' % (8,88))

有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：

> 'growth rate: %d %%' % 7
> 
'growth rate: 7 %'

**format()**

另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：

> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
> 
'Hello, 小明, 成绩提升了 17.1%'

## list和tuple

**list**

Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
其中等价于java的List 里面的元素可以时不同类型

array = ["1","hah","b"];
print("array = %s,size = %s" % (array,len(array)));
array1 = array[0] = array[-3] ##如果取倒数第一个则 array[len(array)-1] 等价于 array[-1]
print(array1)

array.append("c")##在后面追加
array.insert(2,"m")##在指定位置插入
array.pop()##删除最后一个元素
array.pop(2)##删除第三个元素 array.pop(i)删除第i个元素
array[1] = 2##修改指定元素

\##list中元素类型可以是任意类型，如果元素也为list则array是二维数组，还有散文、四维...
p = ["test",'cc']
array[2] = p
print(array[2][0])

**tupe**
其基本含义和list类似，但是该列表中的内容不可以改变的(其中如果元素为list时，可以修改list中的内容从而整体改变了tuple，但是tuple中的元素指向不变但是list本身可以改变)，所以也就没有像list的 append insert 和赋值等修改列表的方法，其中使用()来定义的 a = (1,2)


##条件判断	



	if <条件判断1>:
	    <执行1>
	elif <条件判断2>:
	    <执行2>
	elif <条件判断3>:
	    <执行3>
	else:
	    <执行4>
    

根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了。缩进是一个tab，4个空格键

if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else

	if x:
	    print('True')
	    
只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

##循环

**for x in ...**

所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：

	>>> list(range(5))
	[0, 1, 2, 3, 4]

range(101)就可以生成0-100的整数序列，计算如下：

	for x in range(101):
	    sum = sum + x
	print(sum)


**while**

第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：

	sum = 0
	n = 99
	while n > 0:
	    sum = sum + n
	    n = n - 2
	print(sum)
在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。

break:终止while循环

continue:

在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环

如果我们想只打印奇数，可以用continue语句跳过某些循环：

	n = 0
	while n < 10:
	    n = n + 1
	    if n % 2 == 0: # 如果n是偶数，执行continue语句
	        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
	    print(n)

## dict和set

dict全名为dictionary 字典数据结构，类似为map。 如果在O(1)快速找到某个key映射的值，可以使用dict。而如果使用list需要遍历整个列表找到符合条件的值，时间复杂度和列表的长度相关。但是会消耗更多的空间，使用空间换取时间。key为不变类型，字符串或整数，如果使用list就会报错，因为需要对key进行hash计算出hashcode，要保证每次一样，这才能 hashcode % length-1 定位到数组的同个位置，此位置中存放的就是value的内存地址。

dict中的顺序会插入的顺序无关

	d = {'dym':1,'dmy':'t'}
	
	print(d['dym'])#如果d['m'] key不存在则会报错 d.get('m')如果key不存在则返回None(类似null)
	
	key = 'dmy'
	if key in d:
		print(d[key])
	
	print(None == d.get('d')) #如果key不存在则可以指定某个值d.get('d'，1)
	
	d.pop('dmy')#删除key=dmy
	print(d)

set类似于java的Set,其内部实现也是用了dict原理，其中列表元素不能重复，和插入顺序无关

	s = set([1,8,6])
	s.add(3)
	s.remove(1)
	s1 = set([6,88])
	
	print(s & s1)
	print(s | s1)

# 二、函数


##函数的调用

Python内置很多函数，例如abs求绝对值的函数 可以通过 help(abs)进行查看详情。

https://docs.python.org/3/index.html

**类型转换函数**

int(‘123’) 转换成int类型123 
float() str(1.23) bool(1) 返回True bool('')返回false

函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

	>>> a = abs # 变量a指向abs函数
	>>> a(-1) # 所以也可以通过a调用abs函数
	1
	
##函数的定义

如果函数中引用其他模块中的函数数时需要使用import,可以认为以 function.py的文件为function模块，里面有好多定义的函数。 然后通过import function 下面就可以通过function.函数名(arg0..),也可以通过from function import my_abs,move 指定导入几个函数下面可以直接使用my_abs、move函数
function.py 函数定义模块

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

function-application.py 调用函数模块

	#!/usr/bin/env python3
	# -*- coding: utf-8 -*-
	import function#导入function模块，也就是以function命名的py文件，里面定义了多种函数 直接function.name(arg0...)引用
	
	print(function.my_abs(2))
	p = function.move(2,3,4,2)
	print(p[0],p[1])
	
	print(function.quadratic(4,9,0))

##函数的参数
###位置参数

def f1(a,b):

位置参数也是必传参数，就是定义普通函数时的参数是在调用时必须传入的

###默认参数

def f1(a,b,c=0,d=1):

定义默认参数时，调用函数时可以不用传,如果只知道参数d则可以 f1(1,2,d=8)这样调用

有个坑：如果默认参数定义了一个list类型，因为默认参数在函数定义的时候就开辟了空间，然后多次调用时,使用的默认参数都是同一个，所以默认参数必须指向不变对象。

	例如 def f1(a,b,c=0,d=[]):
	           d.append('Empty']

如果多次调用f1发现参数d的多次追加Empty，改进将默认参数指向不可变参数

		def f1(a,b,c=0,d=None):
		           if d is None:
		              d = []
		            d.append('Empty')



###可变参数

其实可以定义参数为a 调用时可以传入list或tuple类型参数 f1([1,2,3])，然后取的话直接循环取出。
但是也可以定义可变参数：*args args接收的是一个tuple；

def f1(a,b,c=0,*d): 那么参数d就是可变参数，调用方式 f1(1,3,7,8,9) 其中如果参数 l = [8,88,888]那么调用函数时方式可以是 f1(1,3,\*l)进行调用

###关键字参数

关键参数就是 dict类型，

def f1(a,b,**key): 调用时可以不传入关键字参数，如果传入可以 f1(1,2,city='dd',gender='M') 如果有个参数为dict类型 d={'city':'d','gender':'M'} 直接调用 f1(1,2,\*\*d)

###命名关键字参数

可以指定dict类型中的key name

def f1(a,b,*,city,gender) 只从dict字典类型中取出key为 city和gender的对应的值


###参数组合

参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


	def f1(a, b, c=0, *args, **kw):
	    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
	
	def f2(a, b, c=0, *, d, **kw):
	    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去

所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。但是args的值的个数要和函数参数对应，否则运行出错。

# 一、高级特性

## 切片

list tuple和字符串都可以使用切片方式，可以取出其中一部分，不用总是遍历。

l = [1,88,888]

复制整个list：l[:]

取出0至倒数第一个1之间的数： l[:-1]

取出前两个数： l[:2]等价于 l[0:2]

取出倒数第一个数： l[-1:] 但是并不等于l[-1:0]
取出倒数第二个数： l[-2:-1] 

取出序号为0、2的数 l[::2]

从前2个数中取出0、2序号的数 l[:2:2]

在python中没有substr函数只能通过切片进行对字符串操作 

‘ABCDEFG'[:2] 则返回为AB


## 迭代

在Python中 for不仅可以迭代list tuple还可以迭代dict 字符串，可以通过 collections模块中的Iterable进行判断是否可以迭代 isinstance('abc',Iterable) True可迭代，否则不可以。

**isinstance判断是否可以迭代**
   
	这里需要从collections模块中导入Iterable类型 from collections import Iterable
   
	print(isinstance(list,Iterable))
	print(isinstance(2,Iterable))


**list迭代**

	for val in list :
		print(val)	

**dict迭代**

对key 和 value 以及对同时迭代 key-value

	m = {"1":8,"6":188,"8":1888}
   
	for keys in m :
		print(keys)
		
	#iterate values
	for value in m.values() :
		print(value)
	
	#iterate key-value 
	for item in m.items() :
		print(item) 返回的item为tuple类型 ("1",8) ("6",188) ("8",1888)
			
	for k,v in m.items() :
		print(k,v) 这样直接获取key 和 value 把tuple第一个元素用变量k表示，第二个用v表示
**字符串迭代**

	#iterate string
	for str in 'ABGCCC' :
		print(str)
	
**需要获取循环的下标**

	for i,val in enumerate(list) :
			print(i,val)

**可以引用多个变量**

	#multivariable
	for x,y in [(1,5),(6,88),("A",88)] :
		print(x,y)