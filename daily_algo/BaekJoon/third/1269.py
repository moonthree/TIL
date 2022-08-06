n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a^b))

# set 연산자 활용 : 합집합, 교집합, 차집합, 대칭차집함
# 합집합 : |
# 교집합 : &
# 차집합 : -
# 대칭차집합(합집합 - 교집합) : ^