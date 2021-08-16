list1 =['aa','bb','cc','dd','aa','bb']
print(list1)
print(list1.index('bb'))

print(list1.count('bb'))

print(len(list1))

print('aa' in list1)
print('aa' not in list1)

list1.append('xx')
list1.append([1,2])
print(list1)

list1.extend('yy')#extend会拆开，一个一个加入
list1.extend(['tom','bill'])
print(list1)
list1.insert(1,'hh')
print(list1)

#del(list1)#删除整个列表
del(list1[1])#删除指定元素
print(list1.pop())#默认删除最后一个，返回被删除的数据
print(list1)

list1.clear()#清空列表

list2 =['aa','bb','cc','aa']
list2.remove('aa')
print(list2)


list3  =  [2,4,8,3]
list3.sort()
print(list3)
list3.reverse()
print(list3)

list4 = list3.copy()
print(list4)

i = 0
while i < len(list4):
    print(list4[i])
    i += 1;

list5 = [['a1','a2'],['b1','b2'],['c1','c2']]
print(list5[1][1])


#元组里面如果只有一个数据，必须以，结尾
tupletmp = (1,)

tuplea = ('a','b','c')#元组不支持修改

print(tuplea.index('c'))
print(tuplea.count('c'))
print(len(tuplea))

tupleb = (1,2,3,['a','b'])#元组里面有列表，支持修改元组里面的列表
tupleb[3][0] = 'c'
print(tupleb)
print(type(tupleb))
print(type(tupleb[0]))
print(type(tupleb[3]))



