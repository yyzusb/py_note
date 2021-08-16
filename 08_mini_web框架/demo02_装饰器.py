'''
装饰器作用：对已有函数进行额外的功能扩展,原理就是闭包

要求：
1、不修改已有函数代码；
2、不修改已有函数调用方式；
3、给已有函数进行功能扩充
'''

#创建修饰器
def decorator(func):
    def inner():
        #在内部函数对已有函数进行验证，
        print('开始验证')
        func()
    return inner

@decorator#装饰器的糖果写法。可以注释commit = decorator(commit) 这行代码
def commit():
    print('登录成功')

#decorator参数是填写要装饰的函数
#commit = decorator(commit)

#原来函数的执行方法不变
commit()
