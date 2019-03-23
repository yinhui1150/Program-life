#函数与过程
def hello():
    print('hello fishc')
    return

#temp = hello()

#返回多个值
def back():
    return [1, '小甲鱼']
back()

def back2():
    return 1, '小甲鱼'
back2()

#全局变量局部变量
#局部不要修改全局变量，那样会在局部创建一个局部对象
def discount(price=100, rate=0.8):
    fina_price = price * rate
    old_price = 50
    print('修改后的old_price 1', old_price)
    return fina_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discount(old_price, rate)
print('修改后的old_price 2是' ,old_price)
print('打折后价格是:' ,new_price)