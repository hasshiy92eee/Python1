#Hello, World!を使用して簡単なコードを作成する。
print("Hello, World!")


def choose_greeting(hour):
    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"


import datetime
current_hour = datetime.datetime.now().hour


greeting = choose_greeting(current_hour)
print(f"{greeting} Hello, World!")
