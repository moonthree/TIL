def self():
    n = int(input('가로의 길이 n을 입력하세요. : '))
    m = int(input('세로의 길이 m을 입력하세요. : '))

    for _ in range(m):
        for _ in range(n):
            print('*', end='')
        print()

def fun1_tuple():
    n = int(input('가로의 길이 n을 입력하세요. : '))
    m = int(input('세로의 길이 m을 입력하세요. : '))

    tup = (n, m)

    for _ in range(tup[1]):
        print('*' * tup[0])


def square():
    n = 5
    m = 9

    print(('*' * n + '\n')*m)

square()