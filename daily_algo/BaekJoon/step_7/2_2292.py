# 벌집
# 1 - 6 - 12 - 18 - 24
#   5   6    6    6
# 7 19 37 61
#6 12 18 24
# 
# n = 1 n = n
# num = 1
# n = 0
# num = num+6n

n = int(input())

num = 1
cnt = 0
while True:
    if n <= num+6*cnt:
        print(cnt+1)
        break
    num = num+6*cnt
    cnt += 1