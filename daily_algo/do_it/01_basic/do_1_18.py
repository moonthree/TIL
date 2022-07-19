# 10~99 사이의 난수 n개 생성하기(13이 나오면 중단)

import random

n = int(input('난수의 개수를 입력하세요. : '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end = ' ')
    if r == 13:
        print('\n 프로그램을 중단합니다.')
        break
else:
    print('\n 난수 생성을 종료합니다.')

'''
    for문을 사용하여 2자리 정수인 난수를 n개 생성하여 출력
    이 과정에서 13이 생성될 경우 break 문으로 반복문을 강제 종료
    만약 13이 생성되지 않으면 반복이 끝난 후 else문이 실행
'''