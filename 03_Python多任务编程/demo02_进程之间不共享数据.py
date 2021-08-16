import multiprocessing
import time

data_a = 0

def  add_data():
    data_a = 10
    print(f'data数据修改成成功,等于={data_a}')


def  load_data():
    time.sleep(3)
    print(f'读取到的data={data_a}')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=add_data)
    p2 = multiprocessing.Process(target=load_data)

    p1.start()
    time.sleep(2)
    print(f'此时data_a的数据是{data_a}');

    p2.start()

