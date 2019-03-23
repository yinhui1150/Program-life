#组合
class Turtle:
    def __init__(self, x):
        self.num = x

class Fish:
    def __init__(self, x):
        self.num = x

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    
    def print_num(self):
        print("fish = %d Turtle = %d" %(self.turtle.num, self.fish.num))
#类，类对象(C)，实例化对象（a,b,c）
class C:
    count = 0

a = C()
b = C()
c = C()
print(C.count)
print(a.count)
print(b.count)
print(c.count)

C.count += 10
print(C.count)
print(a.count)
print(b.count)
print(c.count)
c.count += 10
C.count += 20
print(C.count)
print(a.count)
print(b.count) #30
print(c.count) #20

#Mix-in

#类的方法和属性名称相同时，属性会覆盖方法

class C2():
    count = 0
    def x(self):
        print('X-man')
c = C2()
c.x()
#c.x = 1
print(C2.count)

#到底什么是绑定
