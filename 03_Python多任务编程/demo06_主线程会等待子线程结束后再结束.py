'''主线程会等所有子线程执行完毕后再结束，如果想让主线程结束的同时结束子线程，1、将子线程设置为守护进程，随着主线程的结束而结束'''
import threading
import time

def thread_1():
    for i in range(5):
        print(f'thread_1...{i}')
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=thread_1);
    print('thread_1 info ',t1)
    t1.daemon=True

    t1.start()

