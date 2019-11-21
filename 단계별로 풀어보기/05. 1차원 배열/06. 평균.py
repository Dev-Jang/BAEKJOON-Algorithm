#1546
n = int(input())
score = list(map(int, input().split()))
sum = 0
for i in score:
    sum += i/max(score)*100
print(sum/len(score))