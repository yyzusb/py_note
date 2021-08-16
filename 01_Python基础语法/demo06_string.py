str1 = 'envirment'
print(str1[1])

str2 = '0123456789'
print(str2[2:9:1])

str3 = 'hello world and itcast and it and python and  apple'
print(str3.find('and'))#返回 下标
print(str3.find('and',15,40))
print(str3.find('qq'))#不存在返回-1


print(str3.index('and'))#返回 下标
print(str3.index('and',15,40))
#print(str3.index('qq'))#不存在返回-1

print(str3.rfind('and'))#从右边开始查找，返回下标

print(str3.replace('and','qq',2))

print(str3.split('and'))   #分割字符串,返回一个列表

print(str3.split('and',2))

list1 =  ['aa','bb','cc']
str4  =  '...'
print(str4.join(list1))#使用join后会把列表变成字符串
print(type(str4.join(list1)))


str5 = 'apple  and  pear'
print(str5.capitalize())
print(str5.title())
print(str5.upper())
print(str5.lower())

str6  =  '   apple   '
print(str6.lstrip())#删除字符串左或右边的空字符串
print(str6.strip())
print(str6.rstrip())


str7 = 'apple'
print(str7.ljust(10,'$'))
print(str7.rjust(10,'$'))
print(str7.center(10,'$'))
print(str7.center(10))

str3 = 'hello world and itcast and it and python and  apple'
print(str3.startswith('hello'))
print(str3.endswith('hello'))
print(str3.startswith('world',6,30))

str4 = 'hello'
print(str4.isalpha(),'abc')
print(str4.isdigit())


str5 = 'hello123 '
print(str4.isalnum())
print(str4.isspace())

str6 = ' '
print(str6.isspace())












