#丰富的else语句
'''
def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('%d 最大的约数是%d' % (num, count))
            break
        count -= 1
    else:
        print('%d 是素数' % num)

showMaxFactor(int(input('请输入一个数')))
'''
try:
    int('abc')
except ValueError as reason:
    print("出错了")
else:
    print('没有异常了')