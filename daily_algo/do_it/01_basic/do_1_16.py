# break

# 1부터 n까지 정수의 합 구하기(n값은 양수만 입력받음)

print('1부터 n까지 정수의 합을 구합니다.')

while True:                                         # while 문이 무한 반복되도록 만든 무한루프
    n = int(input('n값을 입력하세요. : '))
    if n > 0:                                       # 양수를 입력 받을 시
        break                                       # break 문을 활용하여 무한루프 탈출

sum = 0
i = 1

for i in range(1, n+1):
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
print(f'i의 값은 {i}입니다.')