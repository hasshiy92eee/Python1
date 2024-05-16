# hikisu_2.py

def countdown(start, end=0):
    print('1つめで受け取った値:', start)
    print('2つめで受け取った値:', end)
    print('カウントダウンをします')
    counter = start
    while counter >= end:
        print(counter)
        counter -= 1


countdown(10)
countdown(10, 4)
