import math

def myround(suji):
    suji = suji * 10
    suji = suji + 0.5
    suji = math.floor(suji)
    suji = suji / 10
    return suji

def circumference(radius):
    return ('円周', myround(radius * 2 * math.pi))

def area_of_circle(radius):
    return ('円の面積', myround(radius * radius * math.pi))

def get_circle(radius, func):
    text, val = func(radius)
    print(f'{text}は{val}')

