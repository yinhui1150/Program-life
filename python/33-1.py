try:
    sum = 1 + '1'
    #typeerror就会调转到except，下面不会处理了
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错啦 reason = '+ str(reason))
except TypeError as reason:
    print('类型出错啦 reason = '+ str(reason))


try:
    sum = 1 + '1'
    #typeerror就会调转到except，下面不会处理了
except (OSError, TypeError):
    print('出错了')

finally:
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()