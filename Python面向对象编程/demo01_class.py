class WashingMachine():
    def __init__(self):
        self.width = 400;
        self.heigh = 500;
    def Washing(self):
        print('已经洗衣服了')
    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.heigh}')

haier = WashingMachine();
haier.print_info()





