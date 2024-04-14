o = 100
#Pythonはint型を""や''で括らなくても良い

fruits = "apple + grape + melon"
add_fruits = "strawberry + banana"
result = fruits + " + " + add_fruits
# result = (fruits + add_fruits)
print(result)
# 文字列同士の連結は result = fruits + " + " + add_fruits
# の方が文字列連結の間にスペースと+が入力されるので良い。


x = "Hello"
y = "World"
print(x + y)

str_int = ["Hello", "ander", "the", "world!", "100"]
str_int.append('true/false')  # 新しい要素を追加
print(str_int[0:3])  # インデックス0から3未満までの要素を取得

print(str_int[0])  # インデックス0の要素を取得
print(str_int[3])  # インデックス3の要素を取得

print(str_int[0:6])
str_int.remove("the")
print(str_int[0:6]) # Pythonは範囲外のインデックスに達しても　
#エラーを発生させず、可能な限りで処理するらしい。

#リストを増やしてリスト同士結合してみる
bool = ["true", "false"]
str_int.extend(bool)

#plus = str_int + bool でも似たような結果が得られる

#extendメソッドは、リストに別のリストを連結して拡張します。
#元のリストが変更され、返り値はありません。

#リストの連結演算子(+)は、新しいリストを作成し、
#元のリストと別のリストを連結します。元のリストは変更されず、
#連結された新しいリストが返されます。

#上でも同じこしてるけど、リスト内を分割
num = [1, 2, 3, 4, 5, 6]
print(num[0:3])
