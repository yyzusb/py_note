dict1 = {"name":"tom","age":18,"gender":"man"}
print(dict1)

dict2 = {}
print(type(dict2))

dict3 = dict()
print(type(dict3))


#如果没有这个key，字典就新增加一个，如果存在就修改这个key的value
dict1['id'] = 110
print(dict1)
dict2 = dict1


dict1['name'] = 'Rose'
print(dict1)

del dict1['name']
print(dict1)
dict1.clear()
print(dict1)
del dict1                           #删除字典
print('dict2=',dict2)               #字典1清空后，字典2也被清空了

dict4 = {"name":"tom","age":18,"gender":"man"}
dict4['id'] = 110
print('dict4',dict4)
print(dict4.get('name'))
print(dict4.get('name','lili'))     #只返回有效key
print(dict4.keys())                 #返回一个可迭代的对象
print(dict4.values())
print(dict4.items())                #返回字典中所有的键值对，返回可迭代对象，里面的数据是元组，键值对改成一个元组里的两个数据



for key in dict4.keys():
    print(key)

for value in dict4.values():
    print('value=',value)

#遍历键值对
for item in dict4.items():
    print('item = ',item)


for key,value in dict4.items():
    print(f'{key} = {value}')

#创建集合两种方法，s1 = {}, s2 = set('b')，集合是天然去重复
s1 = {1,2,3}
s2 = set('abc')

print(type(s1),type(s2))

#add()只能增加单一数据s1.add(55)，如果增加序列会报错.s1.add([1,5,6,]),update()用来增加序列
s1.add(4)
print(s1)
s1.update([7,8,9])
print(s1)

s1.remove(1)  #remove（）删除指定数据，如果数据不存在，会报错，使用discard（）,数据不存在也不会报错
print(s1)

print(s1.pop())#随机删除一个数据
print(s1)

#判断数据是否在集合里面
print(10 in s1)
print(10 not in s1)



