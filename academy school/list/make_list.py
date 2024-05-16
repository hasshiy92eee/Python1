import random

list01 = []
for i in range(10):
    n = random.randint(1, 99)
    list01.append(n)
print(list01)

list02 = []
for i in list01:
    if i % 3 == 0:   # 3の倍数
        list02.append(i)
print(list02)

list03 = [n for n in list01 if n%3==0]
print(list03)
