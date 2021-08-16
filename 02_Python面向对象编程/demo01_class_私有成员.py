class WashingMachine():
    #在函数或者变量前面加两个下划线，会变成私有成员
    __tall = 600
    def __init__(self):
        self.width = 400;
        self.heigh = 500;
    def Washing(self):
        print('已经洗衣服了')
    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.heigh}')
    def get_tall(self):
        return self.__tall
    def set_tall(self):
        self.__tall = 900;
        return self.__tall
    def __private_test(self):
        print('这是私有方法')

haier = WashingMachine();
print(haier.get_tall())
print(haier.set_tall())




