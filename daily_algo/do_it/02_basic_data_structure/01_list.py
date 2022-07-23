# 빈 배열 판단하기
def array_judge():
    x = []
    if x:
        print('x가 비어있지 않으면(True) 실행')
    else:
        print('x가 비어있으면(False) 실행')
#array_judge()

# 내포 표기 생성
def inside():
    numbers = [1, 2, 3, 4, 5]
    twise = [i*2 for i in numbers if i % 2 == 1]
    print(twise)
#inside()

# meter = [3, 5, 8, 10]
# centi_meter = [100*i for i in meter]
# print(centi_meter)

N = int(input())
for i in range(1, 10):
    print(f'{N} * {i} = {N*i}')