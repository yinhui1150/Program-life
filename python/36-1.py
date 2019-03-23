#类和对象 封装
#类是以大写字母开头
class Turtle:
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'
    
    def climb(self):
        print('climb')
    def run(self):
        print('run')
    def bite(self):
        print('bite')
    def eat(self):
        print('eat')
    def sleep(self):
        print('sleep')

tt = Turtle()
tt.bite()

class MyTurtle(Turtle):
    pass

tt2 = MyTurtle()
tt2.climb()