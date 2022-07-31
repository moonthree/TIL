m, n = map(int, input().split())

for i in range(m, n+1):
    if i == 1 :                         # 1은 소수가 아니므로 제외
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j == 0 :
            break
    else:
        print(i)

# 에라토스네스의 체(소구 구하기)
# 반복문을 돌린다.
# 범위는 2부터 int(i**0.5)+1 까지이다. 

print(3**0.5)