import random
secret = random.randint(1,10)
print(secret)
print('-----------------我爱鱼c工作室----------------------')
temp = input('猜一下数字\n')
guess = int(temp)
while guess != secret:
    if guess > secret:
        print('大了大了')
    else:
        print('小了小了')
    temp = input('猜错了 猜一下数字\n')
    guess = int(temp)
    
if guess == secret:
    print('你是小甲鱼心里的蛔虫吗')
    print('哼，猜中了，也没有奖励')

print('游戏结束')