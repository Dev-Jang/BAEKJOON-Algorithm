hour, minute = map(int, input().split())
if minute >= 45:
    minute -= 45
elif hour == 0:
    hour = 23
    minute += 15
else:
    hour -= 1
    minute += 15
print(hour, minute)