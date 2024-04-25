#Pythonの比較演算子（===　厳密比較演算子はない)

x = "multiplication"
result = x == 30
print(result)

y = "division"
result = y == "plus"
print(result)

z = 20
result = z == 20
print(result)

a = ["a", "b", "c"]
result = a == ["a", "b", "c"]
print(a)

#包含（ほうがん）の条件式 x in y
#文字列の大文字、小文字を区別する。
f = 'A'
result = f in 'apple'
print(result)

c = 'peach'
result = c in ['pineapple', 'peach']
print(result)

e = 'orange'
result = e in ['pineapple', 'peach']
print(result)

#複数条件式の組み合わせ and:かつ　　or：または
age = 22
gender = 'woman'
result = (age >= 20) and (gender  == 'woman')
print(result)

year = 10
type = 'gundam'
result = (year >= 40 ) or (type == 'zaku')
print(result)

#否定 (not)条件式
age = 30
result = not (age >= 20)
print(result)
