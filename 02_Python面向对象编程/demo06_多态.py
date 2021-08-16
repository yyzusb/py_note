#子类从新父类的方法，实现不同功能，叫做多态
class Dog(object):
    def do_work(self):
        print('旺旺叫')

class ArmyDog(Dog):
    def do_work(self):
        print('打仗')

class PoliceDog(Dog):
    def do_work(self):
        print('抓贼')

class Person(object):
    def go_to_work(self,dog2):
        dog2.do_work();


police = Person();
police_dog = PoliceDog();
police.go_to_work(police_dog);

soldier = Person();
army_dog = ArmyDog();
soldier.go_to_work(army_dog)



