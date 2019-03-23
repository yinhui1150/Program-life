#关键字参数
def Saysome(name, words):
    print(name + '->' + words)

Saysome('小甲鱼', '让程序改变世界')

Saysome(words='让程序改变世界', name='小甲鱼')

#默认参数

def Saysome2(name='小甲鱼', words='让程序改变世界'):
    print(name + '->' + words)

Saysome2()

#收集参数
def test(*params, exp=8):
    print('参数的长度', len(params))
    print('第二个参数是', params[1])

test(1, 2, 3)

