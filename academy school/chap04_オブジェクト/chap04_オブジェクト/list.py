data = [2**n for n in range(1, 11)]
print(data)

data = [n*2 for n in range(1, 11)]
print(data)

data = [n**2 for n in range(1, 11)]
print(data)

data = [str(n)+'月' for n in range(1, 11)]
print(data)

data = ['apple', 'orange', 'banana', 'avocado']
data = [n.upper() for n in data]
print(data)

data = ['apple', 'orange', 'banana', 'avocado']
data = [n for n in data if n[0] == 'a']
print(data)