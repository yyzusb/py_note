'''
闭包条件
1、函数的嵌套
2、内部函数使用外部函数的参数或者变量
3、外部函数将内部函数作为返回值

闭包作用
保存外部函数的变量
'''

def func_out():
    num = 10
    num1 = 20
    def func_inner(par1):
        #如果此处想修改num1,需要声明一个globe num1
        #globe  num1
        return num + par1
    # 此处是返回内部函数保留的外部函数的变量，不是内部函数内存地址
    return func_inner

if __name__ == '__main__':
    #new_func就是创建的闭包对象
    new_func = func_out()
    #此处执行new_func其实是执行func_inner
    print('闭包结果展示',new_func(3))





