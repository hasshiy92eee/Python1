scores = [65, 80, 40, 92, 76, 52]
count = 0
total = 0
for i in scores:
    if i > 60:
        count += 1
        total += i
print(count)  # 4
print(total)  # 313
