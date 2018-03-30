

array = ["1","hah","b"];
print("array = %s,size = %s" % (array,len(array)));
array1 = array[0] = array[-3] ##如果取倒数第一个则 array[len(array)-1] 等价于 array[-1]
print(array1)

array.append("c")##在后面追加
array.insert(2,"m")##在指定位置插入
array.pop()##删除最后一个元素
array.pop(2)##删除第三个元素 array.pop(i)删除第i个元素
array[1] = 2##修改指定元素

##list中元素类型可以是任意类型，如果元素也为list则array是二维数组，还有散文、四维...
p = ["test",'cc']
array[2] = p
print(array[2][1])

##tuple
p = (1,3,'r',['a','b'])
p[3][1] = 'm'
print(p)