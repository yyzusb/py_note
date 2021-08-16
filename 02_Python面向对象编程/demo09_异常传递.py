#异常传递就是在异常中套用异常
import time
try:
    f = open('test.txt','r')
    try:
        content = 0
        while(True):
            content = f.readline();
            if(len(content) == 0):
                break;
            time.sleep(2);
            print(content);
    except:
        print('读取文件异常终止')

except:
    print("文件不存在")

