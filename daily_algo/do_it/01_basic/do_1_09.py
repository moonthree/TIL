# a부터 b까지 정수의 합 구하기

print('a부터 b까지의 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요. : '))
b = int(input('정수 b를 입력하세요. : '))

if a > b:
    a, b = b, a     # a와 b를 오름차순으로 정렬
                    # a가 3, b가 8인 경우 : a < b 이므로 if문 동작 x
                    # a가 8, b가 3인 경우 : a > b 이므로 if문 동작 -> a, b에 b, a를 대입


sum = 0
for i in range(a, b+1):     #range(a, b) : a 이상 b 미만인 수를 차례로 나열하는 수열
    sum += i        # for문을 a 이상 b+1 미만까지 반복하며 sum에 i를 더함
                    # 3, 5라면?
                    # sum = 0
                    # sum += 3 -> sum = 3
                    # sum += 4 -> sum = 7
                    # sum += 5 -> sum = 12

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')