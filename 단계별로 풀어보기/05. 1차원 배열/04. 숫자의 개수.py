#2577
multi = 1
exec(3*'multi*=int(input());')
for i in range(10):
    print(str(multi).count(str(i)))