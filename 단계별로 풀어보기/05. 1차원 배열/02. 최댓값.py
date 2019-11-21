#2562
a = []
for i in range(0,9):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)

#숏코딩
#print(max(f'{input()} {i+1}'for i in range(2)))