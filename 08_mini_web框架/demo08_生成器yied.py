#根据程序员制定的算法规则生成数据，等条件不成立的时候取消生成，工作过程是生产一个对象，使用完毕后再生产一个对象
#使用yield关键字来生成


def my_generator():
    for i in range(5):
        print('开始生成数据')
        #只需执行到yield停止执行，并把数结果返回，下次再调用函数的时候，继续生成数据
        yield i
        print('数据使用完毕')

#调用函数，返回生成器对象
result = my_generator()
print(result)
value = next(result)
print(value)

value = next(result)
print(value)

value = next(result)
print(value)

value = next(result)
print(value)


value = next(result)
print(value)


value = next(result)
print(value)


value = next(result)
print(value)


value = next(result)
print(value)



