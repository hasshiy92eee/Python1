print('a / bの計算をします')
try:

    a = input('aの値を入力してください:')
    b = input('bの値を入力してください:')
    c = float(a) / float(b)
    print('答えは', c)

except ValueError:
    print('入力が数字ではない/及び適切ではありません')
except ZeroDivisionError:
    print('ゼロで割れません')
else:
    print('いいぞ！その調子')
finally:
    print('我が人生に一片の悔いなし')

print('処理を終了します')
