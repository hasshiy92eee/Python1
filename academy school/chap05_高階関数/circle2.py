import math

def myround(suji):
    suji = suji * 10
    suji = suji + 0.5
    suji = math.floor(suji)
    suji = suji / 10
    return suji

def circumference(radius):
    val = myround(radius * 2 * math.pi)
    return f'円周は{val}'

def area_of_circle(radius):
    val = myround(radius * radius * math.pi)
    return f'円の面積は{val}'

def get_circle(radius, func):
    print(func(radius))

