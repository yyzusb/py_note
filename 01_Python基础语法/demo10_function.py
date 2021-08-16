import random

def fuction_01(name,age):
    print(f'function_1 : {name},{age}')

fuction_01('tom' ,19)


#函数说明文档
def fuction_02():
    '''返回一个烟
    最后返回
    '''
    return '烟'

goods = fuction_02()
print(goods)

help(fuction_02)

def function_3():
    print('function_3_start')
    print('function_3_end')

def function_4():
    print('function_4_start')
    function_3()
    print('function_4_end')

function_4()

def function_5():
    print('*' * 20)

function_5()

a = random.random()
print(a)

battle = 100
def func1():
    battle =  200;
    print(battle)

func1()
print(battle)



def user_info(name,age,gender):
    print(f'名字是{name}，年龄是{age}，性别是{gender}')

user_info('tom',18,'男人')
user_info('tom',gender='女',age=99)

#缺省参数
def user_info_2(name='bill',age=22,gender='man'):
    print(f'名字是{name}，年龄是{age}，性别是{gender}')

user_info_2()
user_info_2('kk')
user_info_2(age=18)

def user_info_3(*args):
    print(args)

user_info_3('peter')

user_info_3('peter',99,'man')

def user_info_4(**kwargs):
    print(kwargs)

user_info_4(name = 'jike',age=18)








