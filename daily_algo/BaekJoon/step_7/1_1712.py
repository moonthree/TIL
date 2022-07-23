# 손익분기점
# 수학을 사용하면 더 빨리 풀 수 있음을 알려주는 문제
# 반복문 사용시 시간초과


A, B, C = map(int, input().split())

# B가 C보다 크거나 같다면 아무리 많이 팔아도 손익분기점을 넘길 수 없다.
if B >= C:
    print(-1)
else:
    # A+(B*n) < C*n
    # A < C*n - B*n
    # A < (C-B)n
    # A/(C-B) < n
    print(int(A/(C-B))+1)