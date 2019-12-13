#4673
def d(n):
    result = n
    temp = n
    while True:
        if temp >= 10:
            result += (temp % 10)
            temp = int(temp / 10)
        else:
            result += temp
            return result

natural_num = []
for i in range(1,10001):
    natural_num.append(i)

for i in range(1,10001):
    if d(i) in natural_num:
        natural_num.remove(d(i))

for i in range(len(num)):
    print(num[i])