import random
com = random.randint(1, 99)
num = 0

while True:
    num = int(input('1～99を入力 (999:終了) > '))
    if num == 999:
        break
    if num == com:
        print('当たり')
        com = random.randint(1, 99)
    elif num > com:
        print('大きすぎます')
    else:
        print('小さすぎます')

print('お疲れ様でした')
