T = int(input())
a,b = [],[]
for i in range(0,T):
    n1, n2 = map(int, input().split())
    a.append(n1)
    b.append(n2)
for i in range(0,T):
    print(a[i]+b[i])