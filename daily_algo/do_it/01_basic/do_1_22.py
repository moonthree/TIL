# 1_22 start

# 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

n = int(input('짧은 변의 길이를 입력하세요.: '))

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print()

'''
 i = 0, j = 0~1
 i = 1, j = 0~2
 ...
 i = n, j = 0~n+1
'''
# 1_22 end

# 1_23 start
print('-------------------')
# 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기
for i in range(n):
    for _ in range(n-i -1):    # 공백을 출력
        print(' ', end='')
    for _ in range(i + 1):      # *을 출력
        print('*', end ='')
    print()
print('-------------------')
# 피라미드 출력하기
for i in range(n):
    for _ in range(n-i -1):     # 공백을 출력
        print(' ', end='')
    for _ in range(i + 1):      # *을 출력
        print('*', end ='')
    for _ in range(1, i + 1):   # *을 출력
        print('*', end ='')
    print()
print('-------------------')
# 역피라미드 출력하기
for i in range(n):
    for _ in range(i):      
        print(' ', end ='')
    for _ in range(n-i -1):
        print('*', end='')
    for _ in range(n-i+1 -1):
        print('*', end='')
    print()
# 1_23 end
