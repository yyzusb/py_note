#带有参数的装饰器，先用一个带参数的函数来返回一个装饰器，然后在执行

def return_decorator(flag):
    def decorator(func):
        def inner(a, b):
            if(flag == '-'):
                print('努力计算减法中')
                return a - b
            elif(flag == '+'):
                print('努力计算加法中')
                return a + b
        return inner
    return decorator


@return_decorator('+')
def add_num(a, b):
    return a + b
@return_decorator('-')
def sub_num(a,b):
    return a - b


print(add_num(6,6))
print(sub_num(5,5))

