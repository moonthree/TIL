#세 정수의 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요. : '))
b = int(input('정수 b의 값을 입력하세요. : '))
c = int(input('정수 c의 값을 입력하세요. : '))

maximum = a             # maximum에 a의 값을 대입
if b > maximum:         # b의 값이 maximum보다 크면, maximum에 b의 값을 대입
    maximum = b
if c > maximum:         # c의 값이 maximum보다 크면, maximum에 c의 값을 대입
    maximum = c

print(f'최댓값은 {maximum}입니다.')


'''
08~12 행은 순차적으로 실행된다.
이렇게 한 문장씩 순서대로 처리되는 구조를 순차 구조라고 한다.
08행은 단순한 대입문이지만, 09~12행은 if문으로 복합문이다.
또한, if와 콜론 사이에 있는 식을 조건식이라고 한다.
조건식으로 평가한 결과에 따라 프로그램의 실행 흐름이 변경되는데 이러한 구조를 선택 구조라고 한다.
'''