# hikisu.py

def countdown(start):
    print('関数が受け取った値:', start)
    print('カウントダウンをします')
    counter = start
    while counter >= 0:
        print(counter)
        counter -= 1
    print('startは', start)


countdown(3)
countdown(10)
