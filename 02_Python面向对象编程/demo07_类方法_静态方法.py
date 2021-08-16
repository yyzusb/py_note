class Apple():
    __price  = 50
    #类方法
    @classmethod
    def get_price(cls):
        return cls.__price;

    @staticmethod
    def print_info():
        print('this is staticmethond')

a = Apple();
b = a.get_price();
print(b);
a.print_info();

print('*'*40);

#静态方法不用生成实例，直接使用
Apple.print_info()





