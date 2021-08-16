#+合并，字典和集合不支持合并
str1 = 'abc'
str2 = 'def'

print(str1+str2)

print(str1 * 3)

#计算长度
dict1 = {"name":"tom","age":18}
print(len(dict1))

#元素中最大元素，最小元素
str3 = 'abcdefg'
print('max = ',max(str3))
list1 = [5,6,7,8,4]
print('min = ',min(list1))

for i in range(1,10,1):
    print('i = ',i)

for j in range(1,10,2):
    print('j = ',j)

for k in range(10):
    print('k = ',k)

#enumerate（）返回结果是元组，元组内容是迭代对象的下标和数据
list2 = ['a','b','c','d','e','f']
for i in enumerate(list2):
    print('enumerate =',i)


dict2 = {i:i**2 for i in range(1,5)}
print(dict2)







