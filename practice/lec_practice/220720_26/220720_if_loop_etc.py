def a():
    # 세로로 출력하기
    # 자연수 number 를 입력 받아, 1부터 number 까지의 수를 세로로 한 줄 씩 출력하시오.
    number = int(input('자연수를 입력하세용 : '))
    for i in range(1, number+1):
        print(i)

def b():
    # 가로로 출력하기
    # 자연수 number 를 입력 받아, 1부터 number 까지의 수를 가로로 한 줄 씩 출력하시오.
    number = int(input('자연수를 입력하세용 : '))
    for i in range(1, number+1):
        print(i, end=' ')

def c():
    # 거꾸로 세로로 출력하기
    # 자연수 number 를 입력 받아, number 부터 0 까지의 수를 거꾸로 세로로 한 줄 씩 출력하시오.
    number = int(input('자연수를 입력하세용 : '))
    for i in range(number, -1, -1):
        print(i)

def d():
    # 거꾸로 가로로 출력하기
    # 자연수 number 를 입력 받아, number 부터 0 까지의 수를 거꾸로 가로로 한 줄 씩 출력하시오.
    number = int(input('자연수를 입력하세용 : '))
    for i in range(number, -1, -1):
        print(i, end='')

def e():
    # n줄 덧셈
    # 자연수 number가 주어질 때, 1부터 자연수 number 까지를 모두 더한 값을 출력하세요.
    number = 10
    sum_number = 0
    for i in range(1, number+1):
        sum_number += i
    print(sum_number)

def f():
    # n줄 덧셈 홀수만
    # 자연수 number가 주어질 때, 1부터 자연수 number 까지중 홀수만 모두 더한 값을 출력하세요.
    number = 10
    sum_number = 0
    for i in range(1, number+1, 2):
        #if i % 2 != 0:
        sum_number += i
    print(sum_number)

#result = 0
def sum_number(x):
    result = 0
    for i in range(x):
        result += i
    return(result)

#print(sum_number(10))

def func():
    def fun(n):
        if(n < 2):
            return 1
        else:
            return n + fun(n-1)
    n = int(input("입력 : "))
    print(fun(n))
func()