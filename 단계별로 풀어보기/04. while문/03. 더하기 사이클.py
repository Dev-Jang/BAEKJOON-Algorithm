#1110
N = int(input())
temp, cnt = N, 0
while True:
    if temp < 10:
        a,b = 0,temp
    else:
        a,b = int(temp/10),(temp%10)
    if a+b < 10:
        temp = (b*10) + (a+b)
    else:
        temp = (b*10) + ((a+b)%10)
    cnt += 1
    if temp == N:
        print(cnt)
        break