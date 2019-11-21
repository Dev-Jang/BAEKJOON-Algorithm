#8958
n = int(input())
score,cnt = 0,1
for i in range(n):
    case = list(input())
    for j in case:
        if j == "O":
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)
    score,cnt = 0,1