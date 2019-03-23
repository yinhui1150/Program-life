count = 5
def MyFun():
    global count 
    count = 10
    print(count)

MyFun()
print(count)

#内嵌函数
def func1():
    print('func1正在被调用')
    def fun2():
        print('func2正在被调用')
    fun2()

func1()
#闭包
def funx(x):
    def funy(y):
        return x * y
        #返回函数类型
    return funy
    
i = funx(8)
print(type(i))
print(i(5))

#非全局变量的局部变量x
def Fun1():
    x = 5
    def Fun2():
        nonlocal x
        x *= x
        return x
    #返回函数调用
    return Fun2()

print(Fun1())