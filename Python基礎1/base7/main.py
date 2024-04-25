print('あいうえお' + 'かきくけこ')

fruits = "grape" + "strawberry"
print(fruits)

x = [1000, 4000,  3000]
y = 700
result = x[1]
calc = y + x[2]
print(calc)

z = 10000
plus = x[0] + z
print(plus)

a = ['a', 'b']
b = ['A', 'B']
result1 = a + b
print(result1)

d = {"orange":100, "banana":190, "strawberry":180}
d["grape"] = 1000

Math = 100
super_power = 10000
if Math == 100000:
    print('凡人です')
elif super_power >= 10000:
    print('超人です')
else:
    print('ゴミでした')

for r in range(10):
    print(r)

order_list = [3, 12, 43, 1, -9]
for g in order_list:
    v_double = g * 4
    print(v_double)

z_dictionary = {"book1":100, "book2":200, "book3":300}
for k, v in z_dictionary.items():
    print(k + '|' + str(v))

def division_Math(t, u):
    print("２つの数を割り算する処理です。")
    divi = t / u
    return divi

result5 = division_Math(50, 5)
print(result5)

# ------------class-------------------------

import random

class Object:
    def __init__(self):
        pass

    def rand(self, rock, paper, scissors):
        pass

person = {
    "personname": "toshiki",
    "gender": "man",
    "wigth": 56,
    "height": 170
}

janken = ["rock", "paper", "scissors"]
toshiki_choice = random.choice(janken)
winner = random.choice(["person", "opponent"])

if winner == "person":
    print("俊樹がじゃんけんに勝ちました！ 1000円を獲得しました。")
else:
    print("俊樹がじゃんけんに負けました。ランダムに1つの情報を晒します...")
    expose_info = random.choice(["gender", "wigth", "height"])
    print(f"俊樹の{expose_info}は{person[expose_info]}です。")

# ----------class2-----------

class Student:
    def __init__(self, arg_name):
        self.name = arg_name
    def print_name(self):
        print(self.name)

student_1 = Student("斉藤")
student_1.print_name()

student_2 = Student("田中")
student_2.print_name()

student_3 = Student("鈴木")
student_3.print_name()


# ---------class3----------

import random

class RockPaperScissors:
    def __init__(self, name):
        self.name = name

    def rand(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)

# プレイヤーの情報を辞書として定義する
class Player1:
    def __init__(self, name, sword, shield, armor):
        self.name = name
        self.sword = sword
        self.shield = shield
        self.armor = armor

    def __str__(self):
        return f"{self.name}(Sword:{self.sword}, Shield:{self.shield}, Armor:{self.armor})"

# プレイヤーと対戦相手の情報を作成
player = Player1("You", sword=10000, shield=7000, armor=12000)
enemy = Player1("Opponent", sword=8000, shield=8000, armor=10000)

# じゃんけん結果を判定する
rps = RockPaperScissors(player.name)
player_choice = rps.rand()
enemy_choice = rps.rand()

print(f"{player.name}の選択: {player_choice}")
print(f"{enemy.name}の選択: {enemy_choice}")

#勝敗を判定し、薔薇を奪う
if player_choice == enemy_choice:
    print("引き分け!")

elif(player_choice == "rock" and enemy_choice == "scissors") or \
    (player_choice == "paper" and enemy_choice == "rock") or \
    (player_choice == "scissors" and enemy_choice == "paper"):
    print(f"{player.name}が勝利しました！")

else:
    print(f"{enemy.name}が勝利しました！")
    # 負けた場合はランダムに装備を奪われる
    equipment = random.choice(["sword", "shield", "armor"])
    print(f"{enemy.name}が{player.name}の{equipment}を奪いました！")
    setattr(player, equipment, 0)
    print(player)  # プレイヤーの状態を表示
