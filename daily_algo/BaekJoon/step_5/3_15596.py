n = int(input())

hansu = 0
for i in range(1, n+1):
    if i < 100:
        hansu += 1                                  # 100보다 작으면 무조건 등차수열
    elif i < 1000:
        check = []
        for j in str(i):
            check.append(int(j))
        
        check1_10 = check[0] - check[1]             # 10-1
        check10_100 = check[1] - check[2]           # 100-10

        if check1_10 == check10_100:                # 10-1 == 100-10 -> 등차수열
            hansu += 1
    else:
        pass
print(hansu)