# 浅拷贝是对可变类型的第一层对象进行拷贝,不可变类型：数字，字符串，元组,如果拷贝的是列表，那么拷贝的时候，只拷贝第一层列表数据，列表中的列表将不拷贝
# 对拷贝的对象开辟新的内存空间进行存储 ，不会拷贝对象内部的子对象，本质就是拷贝了对象的一个地址存储到新开辟的内存空间

import copy

num1 = 1
#copy是一个浅拷贝,1是不可变类型 ，深浅拷贝都不会开辟新的内存空间来存储对象
num2 = copy.copy(1)
print('1是不可变类型,浅拷贝num1:',id(num1),'浅拷贝num2:',id(num2))
list1 = [1,2,3]
list2 = copy.deepcopy(list1)
print('浅拷贝:list1',id(list1),'浅拷贝:list2',id(list2))



#是对可变类型的对象内所有数据拷贝到另外一个地址内存，并且修改原来位置的数据不影响拷贝后的数据
num1 = 1
#1是不可变类型 ，深浅拷贝都不会开辟新的内存空间来存储对象
num2 = copy.deepcopy(1)
print('1是不可变类型,深拷贝num1:',id(num1),'深拷贝num2:',id(num2))
list1 = [1,2,3]
list2 = copy.deepcopy(list1)
print('深拷贝:list1',id(list1),'深拷贝:list2',id(list2))










