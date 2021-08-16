#通用装饰器的作用，可以装饰任意类型的函数

def decorater(fn):
    def inner(*args,**kwargs):
        print('正在努力执行\n')
        num = fn(*args,**kwargs)
        return num
    return inner

@decorater
def add_num(*args,**kwargs):
    result = 0
    for value in args:
        result += value

    for value in kwargs.keys():
        result += value

    print('结果为:',result)

add_num(66,22)






