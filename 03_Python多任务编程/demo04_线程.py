'''threading.Thread()五个参数分别是（1、group目前为空，不用写，2、子进程要执行的函数3、以元组方式传递函数参数，4、以字典方式传递函数参数
5、name，线程名字，一般可以忽略'''
import time
import threading

def foo(par):
    current_thread = threading.current_thread()
    print('foo thread info = ',current_thread,f'  参数{par}测试')
    for i in range(5):
        print('this is foo  ......')
        time.sleep(3)

def bar(par):
    current_thread = threading.current_thread()
    print('bar thread info = ',current_thread,f'  参数{par}测试')
    for i in range(5):
        print('this is bar  ......')
        time.sleep(3)


if  __name__ == '__main__':
    t1 = threading.Thread(target=foo,args={'par':'foo'})
    t2 = threading.Thread(target=bar,args={"par":"bar"})

    current_thread = threading.current_thread()
    print('main thread info = ',current_thread)

    t1.start()
    t2.start()








