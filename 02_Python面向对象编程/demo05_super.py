
class D():
    def __init__(self):
        self.number_1 = 1
    def print_info(self):
        print(f'这是父类D,{self.number_1}')

class E(D):
    def job(self):
        super().print_info()

e = E();
e.job()










