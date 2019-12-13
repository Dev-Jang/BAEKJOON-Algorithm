#1065
def solve(n):
    cnt = 0
    for i in range(1, n+1):
        if i < 100:
            cnt += 1
        else:
            num, difference = [], set()
            for j in str(i):
                num.append(int(j))
            for j in range(len(num)-1):
                difference.add(num[j] - num[j+1])
            if len(difference) == 1:
                cnt += 1
    print(cnt)

n = int(input())
solve(n)