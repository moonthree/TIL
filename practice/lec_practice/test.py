# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업
num = [1, 2, 3]

# for 반복문 이용
result1 = []
for i in num:
    result1.append(i * 2)
print(f'result1 : {result1}')

def double(n):
    return 2*n
result2 = list(map(double, num))
print(f'result2 : {result2}')