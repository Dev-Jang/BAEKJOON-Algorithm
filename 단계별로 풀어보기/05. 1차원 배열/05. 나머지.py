#3052
n = []
for i in range(10):
    n.append((int(input()))%42)
n = set(list(n))
print(len(n))