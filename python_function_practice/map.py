# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업
num = [1, 2, 3]

# for 반복문 이용
result1 = []
for i in num:
    result1.append(i * 2)
print(f'result1 : {result1}')

# map 함수 이용
def double(n):
    return 2*n
result2 = list(map(double, num))
print(f'result2 : {result2}')



# 숫자를 입력받아서 A, B, C에 넣는 작업
# 수작업
A = int(input())
B = int(input())
C = int(input())

# map 함수 이용
A, B, C = map(int, input().split())

list_num = list(map(int, input().split()))