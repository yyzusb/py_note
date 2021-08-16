#互斥锁
#一直等待对方释放锁的情况叫做死锁

import threading

mutex = threading.Lock()
g_data = 0

def task_1():
    global g_data
    print(f'task_1: g_data现在是{g_data}')
    print('task_1: 开始加锁')
    mutex.acquire()
    print('task_1: 加锁成功')

    for i in range(1000000):
        g_data += 1

    print('task_1: 开始解锁')
    mutex.release()
    print('task_1: 解锁成功')

    print(f'task_1: g_data现在是{g_data}')

def task_2():
    global g_data
    print(f'task_2: g_data现在是{g_data}')
    print('task_2: 开始加锁')
    mutex.acquire()
    print('task_2: 加锁成功')

    for i in range(1000000):
        g_data += 1

    print('task_2: 开始解锁')
    mutex.release()
    print('task_2: 解锁成功')

    print(f'task_2: g_data现在是{g_data}')

if __name__ == '__main__':

    t1 = threading.Thread(target=task_1)
    t2 = threading.Thread(target=task_2)

    t1.start()
    t2.start()

