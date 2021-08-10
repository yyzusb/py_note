def print_hi(name):
    print(f'Hi, {name}')  


if __name__ == '__main__':
    print_hi('PyCharm')

#列表
c = [1,2,3,4]
print(type(c))
print(c)

#元组
d = (1,2,3,4)
print(type(d))
print(d)

#集合
e = {1,2,3,4}
print(type(e))
print(e)


#字典
f = {'abc':'1'}
print(type(f))
print(f)


age = 14
name = 'jean'
weight = 60.0
number = 7
print('我是%s,今年%d，体重%.2f，学号%03d'%(name,age,weight,number));
print(f'我是{name},今年{age}，体重%.2f，学号%03d'%(weight,number));

print('hello',end=',')
print('word')




