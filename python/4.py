print('-----------------我爱鱼c工作室----------------------')
temp = input('猜一下数字\n')
guess = int(temp)
if guess == 8:
    print('你是小甲鱼心里的蛔虫吗')
    print('哼，猜中了，也没有奖励')
else:
    if guess > 8:
        print('大了大了')
    else:
        print('小了小了')

print('游戏结束')