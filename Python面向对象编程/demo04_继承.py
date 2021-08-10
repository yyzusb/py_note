class A():
    def __init__(self):
        self.number_1 = 1
    def print_info(self):
        print(f'这是父类.{self.number_1}')

class B(A):
    def __init__(self):
        self.number_2 = 2

    def print_info(self):
        print(f'这是子类.{self.number_2}')


#如果一个类继承了多个类，那么他将按照继承的顺序，默认继承第一个类中的同名函数
res = B();

res.print_info()