import multiprocessing
import os
import time
#多进程开发要比多线程开发稳定性要强大


'''multiprocessing.Process()四个参数分别是（1、group目前为空，不用写，2、子进程要执行的函数3、以元组方式传递函数参数，4、以字典方式传递函数参数
'''
def dance():
    print('子进程dance编号 = ', os.getpid())
    print('子进程dance获取主进程编号 = ', os.getppid())
    for i in range(10):
        if (i == 4):
            print('开始杀死子进程 process_1');
            os.kill(os.getpid(), 9);
        print(f'process_1......{i}');
        time.sleep(4);


def sing():
    print('子进程sing编号 = ', os.getpid())
    print('子进程sing获取主进程编号 = ', os.getppid())
    for i in range(2):
        print(f'process_2......{i}')
        time.sleep(2)


def show_info(name, age, way):
    print(f'name = {name},age = {age},用{way}方式传递进程参数')
    time.sleep(5)


if __name__ == '__main__':
    print('主进程编号 = ', os.getpid())

    p1 = multiprocessing.Process(target=dance)
    p2 = multiprocessing.Process(target=sing)
    print(p1)
    print(p2)
 #   p3 = multiprocessing.Process(target=show_info, args=('procees_3', 18, '元组'))
 #   p4 = multiprocessing.Process(target=show_info, kwargs={'name':'process_4', 'age':18, 'way':'字典'})

    p1.start()
    p2.start()
 #   p3.start()
 #   p4.start()