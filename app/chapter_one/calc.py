import random
secret = random.randint(1,10)
temp = input("请输入一个整数")
number = int(temp)
while number != 8:
    temp = input("请重新输入一个整数")
    number =int(temp)
    if number == secret:
        print("中奖了")
    else:
        if number > 5:
          print("猜大了")
        else:
          print("猜小了")
print("游戏结束")
 