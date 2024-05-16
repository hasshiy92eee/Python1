total = 0
for i in range(10):  # [0, 1, ..., 9]
    total += i
    if total > 20:
        break

print(i, total)
