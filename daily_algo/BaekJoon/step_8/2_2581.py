m = int(input())
n = int(input())

list_prime_num = []                         # 소수 담을 리스트
for i in range(m, n+1):                     # m이상 n이하까지 반복
    count_prime_num = 0                     # 소수 판단 위한 카운트
    for j in range(2, i):                   # 2부터 i-1까지 반복
        if i % j == 0:                      # 나눠 떨어지면
            count_prime_num += 1            # 카운트 +1
            break                           
    if count_prime_num == 0 and i != 1:     # 소수면
        list_prime_num.append(i)            # 리스트에 추가

if list_prime_num:                          # 리스트에 뭐가 들어있으면 합계랑 최소 출력
    print(sum(list_prime_num))
    print(min(list_prime_num))
else:                                       # 리스트에 뭐가 없으면 -1 출력
    print(-1)