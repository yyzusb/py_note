'''主进程会等所有子进程执行完毕后再结束，如果想让主进程结束的同时结束子进程，有两种办法
1、将子进程设置为守护进程，随着主进程的结束而结束
2、在主进程结束前结束所有子进程
'''
import time
import os
import multiprocessing

def process_sub():
    print('this is process_sub')
    time.sleep(5)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=process_sub)
    #第一种办法将子进程设置为守护进程
    p1.daemon=True
    p1.start();

    print('this is main process')
    #第二种办法是主进程结束前杀死所有子进程
    #p1.terminate()
    print('main process finished')

