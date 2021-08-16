class A():
    def  __init__(self):
        print('这是基类A')

class B():
    def __init__(self):
        print('这是基类B')

class C(A,B):
    def __init__(self):
        print('这是子类')
    def  use_baseA_init(self):
        A.__init__(self)
    def  use_baseB_init(self):
        B.__init__(self)
#如果一个类继承了多个类，那么他将按照继承的顺序，默认继承第一个类中的同名函数
c = C();

c.use_baseA_init();
c.use_baseB_init();


###################################################################################
print('#########################################################################')

class D():
    def __init__(self):
        self.number_1 = 1
    def print_info(self):
        print(f'这是父类D.{self.number_1}')

class E(D):
    def __init__(self):
        self.number_2 = 2

#子类重写父类方法
    def print_info(self):
        print(f'这是子类E.{self.number_2}')

res = D();
res.print_info()
#查看这个类继承了哪个类
print(D.mro())
print(D.__mro__)



