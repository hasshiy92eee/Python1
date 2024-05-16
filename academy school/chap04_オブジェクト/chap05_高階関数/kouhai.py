
def price_without_tax(price):
    return f'税込み{price}円'

def price_with_tax(price):
    return f'税込み{int(price*1.1)}円'

def price_2bai(price):
    return f'{price*2}円'

def print_price(price, func):
    print('価格は' + func(price))

print_price(800, price_without_tax)
# 価格は税込み800円
print_price(800, price_with_tax)
# 価格は税込み880円
print_price(800, price_2bai)
# 1600円
