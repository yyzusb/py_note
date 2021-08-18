class  Student(object):
    def __init__(self):
        #私有属性以 __开头，只能在类中使用,若要使用，或者修改类属性，要使用类函数来修改
        self.__age = 18
    def get_age(self):
        return  self.__age
    def set_age(self,num):
        self.__age = num
    age = property(get_age,set_age)

student = Student()
age = student.age
print(age)

student.age = 22
age = student.age
print(age)

