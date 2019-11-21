#4344
for i in range(int(input())):
    n = list(map(int, input().split()))
    avg = sum(n[1:])/n[0]
    print('%.3f%%' % round(sum(j > avg for j in n[1:])/n[0]*100,3))