class WashingMachine():
    def __init__(self,width,heigh):
        self.width = width;
        self.heigh = heigh;

    def __str__(self):
        return '海尔洗衣机说明书\n'

    def __del__(self):
        print(f'{self}已经被删除');

#打印str函数的返回值
haier1 = WashingMachine(10,20);

