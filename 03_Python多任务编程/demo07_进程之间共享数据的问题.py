import threading
import time

g_list = 0

def  add_data():
    global g_list
    print(f'函数执行前的数据是{g_list}')

    g_list = 3
    print(f'修改成成功,等于={g_list}')


def  load_data():
    print(f'读取到的数据={g_list}')

if __name__ == '__main__':

    p1 = threading.Thread(target=add_data)
    p2 = threading.Thread(target=load_data)

    p1.start()

    #使用join（），主线程等待子线程p1接受后再继续
    p1.join()
    p2.start()



