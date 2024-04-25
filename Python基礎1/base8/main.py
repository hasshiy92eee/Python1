# 例外処理コード
x = 10
y = 1

try:
    result = x / y
except ZeroDivisionError as e:
    print('ゼロで割ることはできません。')
    print(e)
except NameError as ne:
    print('変数が定義されていません')
    print(ne)
else:
    print(result)
    print("正常に終了しました")
finally:
    print("割り算を終了します")


a = 5

try:
    result = a / y
except Exception as ee:
    print('例外が発生しました。')
    print(ee)
