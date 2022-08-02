n = int(input())

def factorial_recursive(n):
    if n <= 1:          # n이 1이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)! 를 그래도 코드로 작성하기
    return n * factorial_recursive(n-1)

print(factorial_recursive(n))