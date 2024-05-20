lst = ['apple', 'banana', 'orange']
a = input('好きな整数を入力:')
try:
    index = int(a)
    if 0 <= index < len(lst):
        print(lst[index])
    else:
        print("指定された数字は範囲外です。")
except ValueError:
    print("整数を入力してください。")
except IndexError:
    print("指定された数字は無効だよ(;´･ω･)")
print("☆終了☆")
