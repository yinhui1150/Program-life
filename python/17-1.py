def MyFirstFun():
    print('这是我创建的第一个函数！')
    
def MySecondFun(name):
    print('hello ' + name)

def add(num1, num2):
    '测试__doc__'
    return (num1 + num2)


MyFirstFun()
MySecondFun('python')
print(add(5, 6))    
print(add.__doc__)        
