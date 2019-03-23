import random as r
class Parent:
    def hello(self):
        print('正在调用父类的方法')
class Child(Parent):
    def hello(self):
        print('正在调用子类的方法')

p = Parent()
p.hello()
c = Child()
c.hello()

class Fish():
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    
    def move(self):
        self.x -= 1
        print('我的位置是:', self.x, self.y)
    
class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        #Fish.__init__(self)
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Shark is hungry')
            self.hungry = False
        else:
            print('shark is not hungry')

fish = Fish()
fish.move()
fish.move()

shark = Shark()
shark.move()
#会出错，因为shark重写了父类的init方法


