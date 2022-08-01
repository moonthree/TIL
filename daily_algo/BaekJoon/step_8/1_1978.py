count_nums = int(input())

list_nums = list(map(int, input().split()))

count_prime_num = 0
for num in list_nums:                   # 리스트 반복
    count_divisor = 0                   # divisor = 약수, 소수는 1 또는 자기 자신만을 약수로 가지는 수, 즉 1과 자기 자신 외에는 나눌 수 없어야 함, 1은 소수가 아님
    for i in range(1, num):             # 1부터 본인-1 까지 반복하여 나눔
        if num % i == 0:                # 나눠지면
            count_divisor += 1          # 약수 카운트 +
    if count_divisor == 1 and num != 1: # 1부터 본인-1 까지 했으니 약수 카운트가 1이어야 소수임
        count_prime_num += 1
print(count_prime_num)