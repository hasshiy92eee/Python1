with open('new_file.txt', 'w', encoding='UTF-8') as f:
    for i in range(0, 100):
        f.write(str(i) + '\n')
