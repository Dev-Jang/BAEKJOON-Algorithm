#2920
asc = [1,2,3,4,5,6,7,8]
des = [8,7,6,5,4,3,2,1]
um = list(map(int,input().split()))
if um == asc:
    print("ascending")
elif um == des:
    print("descending")
else:
    print("mixed")