import threading
import time

g_list = []


def  add_data():
    print(f'函数执行前的数据是{g_list}');
    for i in range(3):
        g_list.append(i)
    print(f'数据修改成成功,等于={g_list}')


def  load_data():
    print(f'读取到的data={g_list}')

if __name__ == '__main__':


    p1 = threading.Thread(target=add_data)
    p2 = threading.Thread(target=load_data)

    p1.start()

    #使用join（），主线程等待子线程p1接受后再继续
    p1.join()
    p2.start()

