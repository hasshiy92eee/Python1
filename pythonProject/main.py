import random


# リストから最大値を見つける関数プログラムを作成する。
def find_max(numbers):

    max_number = numbers[0]


    for num in numbers:
        if num > max_number:
            max_number = num


    return max_number


# メインプログラム
def main():

    random_numbers = [random.randint(1, 100) for _ in range(10)]

    # 最大値を見つける関数を呼び出して結果を取得
    max_number = find_max(random_numbers)


    print("ランダムな数値のリスト:", random_numbers)
    print("最大値:", max_number)



if __name__ == "__main__":
    main()
