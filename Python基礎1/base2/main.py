# 辞書型の結合　※Python3.9.0以降はのコードの書き方もある
x = {"apple": 190, "banana":150, "strawberry":310}
y = {"tomato":100, "melon":340, "peach":210}
# x.update(y)
z = x | y
print(z)


#条件分岐(if, else, elif)の練習
x = 122
if x >= 100:
    print("限界突破しました")
elif x >= 50:
    print("限界値です")
elif x >= 10:
    print("10以上")
else:
    print("10未満")

#for文
a_list = [100,190,530000]
for a in a_list:
    a_yen = str(a) + "円"
    print(a_yen)
#for文をdictionaryに変更
r_dictionary = {'orange':100, 'pineapple':160}
for key, value in r_dictionary.items():
    text = key + 'は' +  str(value) + '円です'
    print(text)

for c in range(50):
    print(c)
