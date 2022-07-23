# 달팽이는 올라가고 싶다
# A = 올라가기
# B = 잠자면서 미끄러지기
# V = 정상
import math
A, B, V = map(int, input().split())

# V <= A*n - B(n-1)
# V <= A*n - Bn + B
# V <= (A-B)n + B
# V/(A-B) - B/(A-B) <= n

# n = 1
# while True:
#     if V <= A*n - B*(n-1) :
#         print(n)
#         break
#     else:
#         n += 1

a = math.ceil((V/(A-B) - B/(A-B)))
print(int(a))