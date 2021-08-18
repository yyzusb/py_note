#当使用 from  ×× import * 的时候，可以使用all来控制可以引用的函数列表
#当引用此模块到其他程序时候，all可以在本模块控制其他程序可以引用该模块的哪些内容
__all__  = ['function_1','function_2']

def function_1():
    print('function_1');


def function_2():
    print('function_2');


def function_3():
    print('function_3');





