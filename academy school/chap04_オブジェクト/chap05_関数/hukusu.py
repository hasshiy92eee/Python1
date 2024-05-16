# hukusu.py

def get_two_numbers():
    return (2, 3)

a, b = get_two_numbers()
# print(a, b)

import random
SIZE = 5

def get_rand():
    return random.randint(0, SIZE-1)

def get_pos():
    return (get_rand(), get_rand())

y, x = get_pos()
print(f'モンスター (Y:{y} X:{x})')
