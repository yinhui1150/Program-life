#递归
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

number = int(input('请输入一个正整数'))
print('%d 的阶乘是 %d' %(number, factorial(number)))

def fact(n):
    if n == 1:
        return 1
    else: 
        return n * fact(n-1)

number2 = int(input('请输入一个正整数'))
print('%d 的阶乘是 %d' %(number2, fact(number2)))