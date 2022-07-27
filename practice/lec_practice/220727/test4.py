# 데코레이팅 함수
def add_print(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper


@add_print #add_print를 사용해서 print_hello()함수를 꾸며주도록 하는 명령어
def print_hello():
    print('hi')

print_hello()
#함수 시작
#hi
#함수 끝