# 테스트 케이스 만큼 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하라.ㄴ

def self_a():
    test_case = int(input('테스트 케이스를 입력하세요. : '))

    for i in range(test_case):
        globals()[f'list_{i}'] = list(map(int, input('0 이상 10000 이하의 정수를 10개 입력하세요.').split()))
        
    for j in range(test_case):
        sum = 0
        list_a = eval(f'list_{j}')
        len_a = len(eval(f'list_{j}'))
        for k in range(len_a):
            if list_a[k] % 2 != 0:
                sum += list_a[k]
        print(f'#{j+1}', sum)

def google():
    t = int(input('테스트 케이스를 입력하세요. : '))

    for i in range(1, t + 1) :
        data = list(map(int, input().split()))
        result = 0
        for j in range(len(data)) :
            if data[j] % 2 == 1 :
                result += data[j]

        #print('#%d %d' % (i, result))
        print(f'#{i} {result}')

# t = int(input())

# for i in range(1, t + 1) :
#     data = list(map(int, input().split()))
#     result = 0
#     for j in range(len(data)) :
#         if data[j] % 2 == 1 :
#             result += data[j]

#     print(f'#{i} {result}')
# self_a()